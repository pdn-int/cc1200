#!/usr/bin/env python3
import logging
import spidev
import time
from cc1200_config import *

_LOGGER = logging.getLogger(__name__)

class CC1200:
    """
    CC1200 class encapsulates SPI communication, configuration,
    and data transmission/reception routines for the CC1200 evaluation board.
    """
    def __init__(self, bus=0, device=0, config=None):
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)
        self.spi.max_speed_hz = 5000000  # Adjust based on board requirements
        self.spi.mode = 0
        # Load configuration from provided config or use defaults from cc1200_config.
        self.config = config if config is not None else get_default_config()

    def send_strobe(self, strobe):
        """
        Sends a command strobe to the CC1200 and returns the status byte.
        """
        status = self.spi.xfer3([strobe])
        return status[0]

    def write_register(self, addr, value):
        """
        Writes a single byte to a specified register.
        """
        self.spi.xfer3([addr, value])

    def read_register(self, addr):
        """
        Reads a single byte from a specified register.
        """
        result = self.spi.xfer3([addr | 0x80, 0x00])
        return result[1]

    def write_burst(self, addr, data):
        """
        Writes multiple bytes (burst mode) starting at the given register address.
        """
        burst_addr = addr | 0x40  # Set burst bit for multi-byte write
        self.spi.xfer3([burst_addr] + data)

    def read_burst(self, addr, length):
        """
        Reads multiple bytes (burst mode) starting at the given register address.
        """
        burst_addr = addr | 0xC0  # Set read and burst bits for multi-byte read
        result = self.spi.xfer3([burst_addr] + [0x00] * length)
        return result[1:]  # First byte is the status byte

    # def configure(self):
        """
        Configures the CC1200 with required register settings.

        For efficiency, contiguous register addresses are grouped and
        written via burst write operations.
        """
        config = self.config['preset_groups']
        if not config:
            return

        # Sort registers by address.
        sorted_regs = sorted(config.items(), key=lambda x: x[0])
        contiguous_groups = []
        current_group = [sorted_regs[0]]

        # Group contiguous registers.
        for reg, val in sorted_regs[1:]:
            last_reg, _ = current_group[-1]
            if reg == last_reg + 1:
                current_group.append((reg, val))
            else:
                contiguous_groups.append(current_group)
                current_group = [(reg, val)]
        contiguous_groups.append(current_group)

        # Write groups: single register writes or burst writes for contiguous blocks.
        for group in contiguous_groups:
            if len(group) == 1:
                reg, val = group[0]
                self.write_register(reg, val)
            else:
                start_addr = group[0][0]
                data = [val for (_, val) in group]
                self.write_burst(start_addr, data)
            time.sleep(0.005)  # Optional delay between groups for register settling

    def configure(self):
        """
        Configures the CC1200 with required register settings.
        """
        for reg, value in self.config['preset_groups'].items():
            self.write_register(reg, value)
            time.sleep(0.01)  # Allow time for register settling
    
    def tx(self, data):
        """
        Transmits a payload.
        """
        self.send_strobe(SFTX)  # Flush TX FIFO
        time.sleep(0.01)
        
        self.write_burst(self.config['tx_fifo_addr'], data)
        
        self.send_strobe(STX)  # Start transmission
        time.sleep(self.config['tx_delay'])
        
        self.send_strobe(SIDLE)  # Return to idle mode

    def rx(self, length):
        """
        Receives a payload.
        """
        self.send_strobe(SFRX)  # Flush RX FIFO
        time.sleep(0.01)
        
        self.send_strobe(SRX)   # Enable RX mode
        time.sleep(self.config['rx_delay'])
        
        data = self.read_burst(self.config['rx_fifo_addr'], length)
        
        self.send_strobe(SIDLE)  # Return to idle mode
        return data
