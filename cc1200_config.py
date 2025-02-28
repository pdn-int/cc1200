# cc1200_config.py
from cc1200_preset import *

# Default preset values for the CC1200 device.
READVALUE 						= 0x80
WRITEVALUE 						= 0x00
BURSTBITVALUE 					= 0x40

TX_FIFO_ADDR = 0x3F  # TX FIFO address (verify with datasheet)
RX_FIFO_ADDR = 0x3F  # RX FIFO address (verify with datasheet)
TX_DELAY     = 0.1   # Transmission delay (seconds)
RX_DELAY     = 0.1   # Reception delay (seconds)

# CC1200 command strobe definitions (verify with datasheet)
SRES    = 0x30  # Reset chip
SFSTXON = 0x31  # Enable and calibrate frequency synthesizer
SXOFF   = 0x32  # Turn off crystal oscillator
SCAL    = 0x33  # Calibrate frequency synthesizer
SRX     = 0x34  # Enable RX
STX     = 0x35  # Enable TX
SIDLE   = 0x36  # Enter idle mode
SFRX    = 0x3A  # Flush the RX FIFO
SFTX    = 0x3B  # Flush the TX FIFO

def get_default_config():
    """
    Returns a dictionary containing default configuration values,
    including 25 preset groups with fixed register values.
    """
    return {
        'tx_fifo_addr': TX_FIFO_ADDR,
        'rx_fifo_addr': RX_FIFO_ADDR,
        'tx_delay': TX_DELAY,
        'rx_delay': RX_DELAY,
        'preset_groups': REGISTER_RESET,
    }

def set_tx_fifo_addr(addr):
    """
    Sets a new default TX FIFO address.
    """
    global TX_FIFO_ADDR
    TX_FIFO_ADDR = addr

def set_rx_fifo_addr(addr):
    """
    Sets a new default RX FIFO address.
    """
    global RX_FIFO_ADDR
    RX_FIFO_ADDR = addr
