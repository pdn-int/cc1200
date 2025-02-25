########################################################################
# CC1200 
# This file contains various pre-set register values for the CC1200 Chip
#
# These Presets extracted from SmartRF Studio 7
#
# SEE CC1200 USER MANUAL FOR MORE INFORMATION
#
# Last modified: Feb 25 2025
#
########################################################################

from register import Register


### "Name":      Register(address, value)

### Register Reset - Default values
REGISTER_RESET ={
    "IOCFG3":           Register(0x0000,0x06),    #GPIO3 IO Pin Configuration
    "IOCFG2":           Register(0x0001,0x07),    #GPIO2 IO Pin Configuration
    "IOCFG1":           Register(0x0002,0x30),    #GPIO1 IO Pin Configuration
    "IOCFG0":           Register(0x0003,0x3C),    #GPIO0 IO Pin Configuration
    "SYNC3":            Register(0x0004,0x93),    #Sync Word Configuration [31:24]
    "SYNC2":            Register(0x0005,0x0B),    #Sync Word Configuration [23:16]
    "SYNC1":            Register(0x0006,0x51),    #Sync Word Configuration [15:8]
    "SYNC0":            Register(0x0007,0xDE),    #Sync Word Configuration [7:0]
    "SYNC_CFG1":        Register(0x0008,0xAA),    #Sync Word Detection Configuration Reg. 1
    "SYNC_CFG0":        Register(0x0009,0x03),    #Sync Word Detection Configuration Reg. 0
    "DEVIATION_M":      Register(0x000A,0x06),    #Frequency Deviation Configuration
    "MODCFG_DEV_E":     Register(0x000B,0x03),    #Modulation Format and Frequency Deviation Configur..
    "DCFILT_CFG":       Register(0x000C,0x4C),    #Digital DC Removal Configuration
    "PREAMBLE_CFG1":    Register(0x000D,0x14),    #Preamble Length Configuration Reg. 1
    "PREAMBLE_CFG0":    Register(0x000E,0xDA),    #Preamble Detection Configuration Reg. 0
    "IQIC":             Register(0x000F,0xC4),    #Digital Image Channel Compensation Configuration
    "CHAN_BW":          Register(0x0010,0x94),    #Channel Filter Configuration
    "MDMCFG1":          Register(0x0011,0x46),    #General Modem Parameter Configuration Reg. 1
    "MDMCFG0":          Register(0x0012,0x0D),    #General Modem Parameter Configuration Reg. 0
    "SYMBOL_RATE2":     Register(0x0013,0x43),    #Symbol Rate Configuration Exponent and Mantissa [1..
    "SYMBOL_RATE1":     Register(0x0014,0xA9),    #Symbol Rate Configuration Mantissa [15:8]
    "SYMBOL_RATE0":     Register(0x0015,0x2A),    #Symbol Rate Configuration Mantissa [7:0]
    "AGC_REF":          Register(0x0016,0x36),    #AGC Reference Level Configuration
    "AGC_CS_THR":       Register(0x0017,0x00),    #Carrier Sense Threshold Configuration
    "AGC_GAIN_ADJUST":  Register(0x0018,0x00),    #RSSI Offset Configuration
    "AGC_CFG3":         Register(0x0019,0xB1),    #Automatic Gain Control Configuration Reg. 3
    "AGC_CFG2":         Register(0x001A,0x20),    #Automatic Gain Control Configuration Reg. 2
    "AGC_CFG1":         Register(0x001B,0x52),    #Automatic Gain Control Configuration Reg. 1
    "AGC_CFG0":         Register(0x001C,0xC3),    #Automatic Gain Control Configuration Reg. 0
    "FIFO_CFG":         Register(0x001D,0x80),    #FIFO Configuration
    "DEV_ADDR":         Register(0x001E,0x00),    #Device Address Configuration
    "SETTLING_CFG":     Register(0x001F,0x0B),    #Frequency Synthesizer Calibration and Settling Con..
    "FS_CFG":           Register(0x0020,0x02),    #Frequency Synthesizer Configuration
    "WOR_CFG1":         Register(0x0021,0x08),    #eWOR Configuration Reg. 1
    "WOR_CFG0":         Register(0x0022,0x21),    #eWOR Configuration Reg. 0
    "WOR_EVENT0_MSB":   Register(0x0023,0x00),    #Event 0 Configuration MSB
    "WOR_EVENT0_LSB":   Register(0x0024,0x00),    #Event 0 Configuration LSB
    "RXDCM_TIME":       Register(0x0025,0x00),    #RX Duty Cycle Mode Configuration
    "PKT_CFG2":         Register(0x0026,0x04),    #Packet Configuration Reg. 2
    "PKT_CFG1":         Register(0x0027,0x03),    #Packet Configuration Reg. 1
    "PKT_CFG0":         Register(0x0028,0x00),    #Packet Configuration Reg. 0
    "RFEND_CFG1":       Register(0x0029,0x0F),    #RFEND Configuration Reg. 1
    "RFEND_CFG0":       Register(0x002A,0x00),    #RFEND Configuration Reg. 0
    "PA_CFG1":          Register(0x002B,0x7F),    #Power Amplifier Configuration Reg. 1
    "PA_CFG0":          Register(0x002C,0x56),    #Power Amplifier Configuration Reg. 0
    "ASK_CFG":          Register(0x002D,0x0F),    #ASK Configuration
    "PKT_LEN":          Register(0x002E,0x03),    #Packet Length Configuration
    "IF_MIX_CFG":       Register(0x2F00,0x00),    #IF Mix Configuration
    "FREQOFF_CFG":      Register(0x2F01,0x20),    #Frequency Offset Correction Configuration
    "TOC_CFG":          Register(0x2F02,0x0B),    #Timing Offset Correction Configuration
    "MARC_SPARE":       Register(0x2F03,0x00),    #MARC Spare
    "ECG_CFG":          Register(0x2F04,0x00),    #External Clock Frequency Configuration
    "MDMCFG2":          Register(0x2F05,0x08),    #General Modem Parameter Configuration Reg. 2
    "EXT_CTRL":         Register(0x2F06,0x01),    #External Control Configuration
    "RCCAL_FINE":       Register(0x2F07,0x00),    #RC Oscillator Calibration Fine
    "RCCAL_COARSE":     Register(0x2F08,0x00),    #RC Oscillator Calibration Coarse
    "RCCAL_OFFSET":     Register(0x2F09,0x00),    #RC Oscillator Calibration Clock Offset
    "FREQOFF1":         Register(0x2F0A,0x00),    #Frequency Offset MSB
    "FREQOFF0":         Register(0x2F0B,0x00),    #Frequency Offset LSB
    "FREQ2":            Register(0x2F0C,0x00),    #Frequency Configuration [23:16]
    "FREQ1":            Register(0x2F0D,0x00),    #Frequency Configuration [15:8]
    "FREQ0":            Register(0x2F0E,0x00),    #Frequency Configuration [7:0]
    "IF_ADC2":          Register(0x2F0F,0x02),    #Analog to Digital Converter Configuration Reg. 2
    "IF_ADC1":          Register(0x2F10,0x5A),    #Analog to Digital Converter Configuration Reg. 1
    "IF_ADC0":          Register(0x2F11,0x1A),    #Analog to Digital Converter Configuration Reg. 0
    "FS_DIG1":          Register(0x2F12,0x08),    #Frequency Synthesizer Digital Reg. 1
    "FS_DIG0":          Register(0x2F13,0x5A),    #Frequency Synthesizer Digital Reg. 0
    "FS_CAL3":          Register(0x2F14,0x00),    #Frequency Synthesizer Calibration Reg. 3
    "FS_CAL2":          Register(0x2F15,0x20),    #Frequency Synthesizer Calibration Reg. 2
    "FS_CAL1":          Register(0x2F16,0x00),    #Frequency Synthesizer Calibration Reg. 1
    "FS_CAL0":          Register(0x2F17,0x00),    #Frequency Synthesizer Calibration Reg. 0
    "FS_CHP":           Register(0x2F18,0x28),    #Frequency Synthesizer Charge Pump Configuration
    "FS_DIVTWO":        Register(0x2F19,0x01),    #Frequency Synthesizer Divide by 2
    "FS_DSM1":          Register(0x2F1A,0x00),    #FS Digital Synthesizer Module Configuration Reg. 1
    "FS_DSM0":          Register(0x2F1B,0x03),    #FS Digital Synthesizer Module Configuration Reg. 0
    "FS_DVC1":          Register(0x2F1C,0xFF),    #Frequency Synthesizer Divider Chain Configuration ..
    "FS_DVC0":          Register(0x2F1D,0x1F),    #Frequency Synthesizer Divider Chain Configuration ..
    "FS_LBI":           Register(0x2F1E,0x00),    #Frequency Synthesizer Local Bias Configuration
    "FS_PFD":           Register(0x2F1F,0x51),    #Frequency Synthesizer Phase Frequency Detector Con..
    "FS_PRE":           Register(0x2F20,0x2C),    #Frequency Synthesizer Prescaler Configuration
    "FS_REG_DIV_CML":   Register(0x2F21,0x11),    #Frequency Synthesizer Divider Regulator Configurat..
    "FS_SPARE":         Register(0x2F22,0x00),    #Frequency Synthesizer Spare
    "FS_VCO4":          Register(0x2F23,0x14),    #FS Voltage Controlled Oscillator Configuration Reg..
    "FS_VCO3":          Register(0x2F24,0x00),    #FS Voltage Controlled Oscillator Configuration Reg..
    "FS_VCO2":          Register(0x2F25,0x00),    #FS Voltage Controlled Oscillator Configuration Reg..
    "FS_VCO1":          Register(0x2F26,0x00),    #FS Voltage Controlled Oscillator Configuration Reg..
    "FS_VCO0":          Register(0x2F27,0x81),    #FS Voltage Controlled Oscillator Configuration Reg..
    "GBIAS6":           Register(0x2F28,0x00),    #Global Bias Configuration Reg. 6
    "GBIAS5":           Register(0x2F29,0x02),    #Global Bias Configuration Reg. 5
    "GBIAS4":           Register(0x2F2A,0x00),    #Global Bias Configuration Reg. 4
    "GBIAS3":           Register(0x2F2B,0x00),    #Global Bias Configuration Reg. 3
    "GBIAS2":           Register(0x2F2C,0x10),    #Global Bias Configuration Reg. 2
    "GBIAS1":           Register(0x2F2D,0x00),    #Global Bias Configuration Reg. 1
    "GBIAS0":           Register(0x2F2E,0x00),    #Global Bias Configuration Reg. 0
    "IFAMP":            Register(0x2F2F,0x01),    #Intermediate Frequency Amplifier Configuration
    "LNA":              Register(0x2F30,0x01),    #Low Noise Amplifier Configuration
    "RXMIX":            Register(0x2F31,0x01),    #RX Mixer Configuration
    "XOSC5":            Register(0x2F32,0x0C),    #Crystal Oscillator Configuration Reg. 5
    "XOSC4":            Register(0x2F33,0xA0),    #Crystal Oscillator Configuration Reg. 4
    "XOSC3":            Register(0x2F34,0x03),    #Crystal Oscillator Configuration Reg. 3
    "XOSC2":            Register(0x2F35,0x04),    #Crystal Oscillator Configuration Reg. 2
    "XOSC1":            Register(0x2F36,0x01),    #Crystal Oscillator Configuration Reg. 1
    "XOSC0":            Register(0x2F37,0x00),    #Crystal Oscillator Configuration Reg. 0
    "ANALOG_SPARE":     Register(0x2F38,0x00),    #Analog Spare
    "PA_CFG3":          Register(0x2F39,0x00),    #Power Amplifier Configuration Reg. 3
    "WOR_TIME1":        Register(0x2F64,0x00),    #eWOR Timer Counter Value MSB
    "WOR_TIME0":        Register(0x2F65,0x00),    #eWOR Timer Counter Value LSB
    "WOR_CAPTURE1":     Register(0x2F66,0x00),    #eWOR Timer Capture Value MSB
    "WOR_CAPTURE0":     Register(0x2F67,0x00),    #eWOR Timer Capture Value LSB
    "BIST":             Register(0x2F68,0x00),    #MARC Built-In Self-Test
    "DCFILTOFFSET_I1":  Register(0x2F69,0x00),    #DC Filter Offset I MSB
    "DCFILTOFFSET_I0":  Register(0x2F6A,0x00),    #DC Filter Offset I LSB
    "DCFILTOFFSET_Q1":  Register(0x2F6B,0x00),    #DC Filter Offset Q MSB
    "DCFILTOFFSET_Q0":  Register(0x2F6C,0x00),    #DC Filter Offset Q LSB
    "IQIE_I1":          Register(0x2F6D,0x00),    #IQ Imbalance Value I MSB
    "IQIE_I0":          Register(0x2F6E,0x00),    #IQ Imbalance Value I LSB
    "IQIE_Q1":          Register(0x2F6F,0x00),    #IQ Imbalance Value Q MSB
    "IQIE_Q0":          Register(0x2F70,0x00),    #IQ Imbalance Value Q LSB
    "RSSI1":            Register(0x2F71,0x80),    #Received Signal Strength Indicator Reg. 1
    "RSSI0":            Register(0x2F72,0x00),    #Received Signal Strength Indicator Reg.0
    "MARCSTATE":        Register(0x2F73,0x41),    #MARC State
    "LQI_VAL":          Register(0x2F74,0x00),    #Link Quality Indicator Value
    "PQT_SYNC_ERR":     Register(0x2F75,0xFF),    #Preamble and Sync Word Error
    "DEM_STATUS":       Register(0x2F76,0x00),    #Demodulator Status
    "FREQOFF_EST1":     Register(0x2F77,0x00),    #Frequency Offset Estimate MSB
    "FREQOFF_EST0":     Register(0x2F78,0x00),    #Frequency Offset Estimate LSB
    "AGC_GAIN3":        Register(0x2F79,0x00),    #Automatic Gain Control Reg. 3
    "AGC_GAIN2":        Register(0x2F7A,0xD1),    #Automatic Gain Control Reg. 2
    "AGC_GAIN1":        Register(0x2F7B,0x00),    #Automatic Gain Control Reg. 1
    "AGC_GAIN0":        Register(0x2F7C,0x3F),    #Automatic Gain Control Reg. 0
    "CFM_RX_DATA_OUT":  Register(0x2F7D,0x00),    #Custom Frequency Modulation RX Data
    "CFM_TX_DATA_IN":   Register(0x2F7E,0x00),    #Custom Frequency Modulation TX Data
    "ASK_SOFT_RX_DATA": Register(0x2F7F,0x30),    #ASK Soft Decision Output
    "RNDGEN":           Register(0x2F80,0x7F),    #Random Number Generator Value
    "MAGN2":            Register(0x2F81,0x00),    #Signal Magnitude after CORDIC [16]
    "MAGN1":            Register(0x2F82,0x00),    #Signal Magnitude after CORDIC [15:8]
    "MAGN0":            Register(0x2F83,0x00),    #Signal Magnitude after CORDIC [7:0]
    "ANG1":             Register(0x2F84,0x00),    #Signal Angular after CORDIC [9:8]
    "ANG0":             Register(0x2F85,0x00),    #Signal Angular after CORDIC [7:0]
    "CHFILT_I2":        Register(0x2F86,0x02),    #Channel Filter Data Real Part [16]
    "CHFILT_I1":        Register(0x2F87,0x00),    #Channel Filter Data Real Part [15:8]
    "CHFILT_I0":        Register(0x2F88,0x00),    #Channel Filter Data Real Part [7:0]
    "CHFILT_Q2":        Register(0x2F89,0x00),    #Channel Filter Data Imaginary Part [16]
    "CHFILT_Q1":        Register(0x2F8A,0x00),    #Channel Filter Data Imaginary Part [15:8]
    "CHFILT_Q0":        Register(0x2F8B,0x00),    #Channel Filter Data Imaginary Part [7:0]
    "GPIO_STATUS":      Register(0x2F8C,0x00),    #General Purpose Input/Output Status
    "FSCAL_CTRL":       Register(0x2F8D,0x01),    #Frequency Synthesizer Calibration Control
    "PHASE_ADJUST":     Register(0x2F8E,0x00),    #Frequency Synthesizer Phase Adjust
    "PARTNUMBER":       Register(0x2F8F,0x00),    #Part Number
    "PARTVERSION":      Register(0x2F90,0x00),    #Part Revision
    "SERIAL_STATUS":    Register(0x2F91,0x00),    #Serial Status
    "MODEM_STATUS1":    Register(0x2F92,0x01),    #Modem Status Reg. 1
    "MODEM_STATUS0":    Register(0x2F93,0x00),    #Modem Status Reg. 0
    "MARC_STATUS1":     Register(0x2F94,0x00),    #MARC Status Reg. 1
    "MARC_STATUS0":     Register(0x2F95,0x00),    #MARC Status Reg. 0
    "PA_IFAMP_TEST":    Register(0x2F96,0x00),    #Power Amplifier Intermediate Frequency Amplifier T..
    "FSRF_TEST":        Register(0x2F97,0x00),    #Frequency Synthesizer Test
    "PRE_TEST":         Register(0x2F98,0x00),    #Frequency Synthesizer Prescaler Test
    "PRE_OVR":          Register(0x2F99,0x00),    #Frequency Synthesizer Prescaler Override
    "ADC_TEST":         Register(0x2F9A,0x00),    #Analog to Digital Converter Test
    "DVC_TEST":         Register(0x2F9B,0x0B),    #Digital Divider Chain Test
    "ATEST":            Register(0x2F9C,0x40),    #Analog Test
    "ATEST_LVDS":       Register(0x2F9D,0x00),    #Analog Test LVDS
    "ATEST_MODE":       Register(0x2F9E,0x00),    #Analog Test Mode
    "XOSC_TEST1":       Register(0x2F9F,0x3C),    #Crystal Oscillator Test Reg. 1
    "XOSC_TEST0":       Register(0x2FA0,0x00),    #Crystal Oscillator Test Reg. 0
    "AES":              Register(0x2FA1,0x00),    #AES
    "MDM_TEST":         Register(0x2FA2,0x00),    #MODEM Test
    "RXFIRST":          Register(0x2FD2,0x00),    #RX FIFO Pointer First Entry
    "TXFIRST":          Register(0x2FD3,0x00),    #TX FIFO Pointer First Entry
    "RXLAST":           Register(0x2FD4,0x00),    #RX FIFO Pointer Last Entry
    "TXLAST":           Register(0x2FD5,0x00),    #TX FIFO Pointer Last Entry
    "NUM_TXBYTES":      Register(0x2FD6,0x00),    #TX FIFO Status
    "NUM_RXBYTES":      Register(0x2FD7,0x00),    #RX FIFO Status
    "FIFO_NUM_TXBYTES": Register(0x2FD8,0x0F),    #TX FIFO Status
    "FIFO_NUM_RXBYTES": Register(0x2FD9,0x00),    #RX FIFO Status
    "RXFIFO_PRE_BUF":   Register(0x2FDA,0x00),    #RX FIFO Status
    "AES_KEY15":        Register(0x2FE0,0x00),    #Advanced Encryption Standard Key [127:120]
    "AES_KEY14":        Register(0x2FE1,0x00),    #Advanced Encryption Standard Key [119:112]
    "AES_KEY13":        Register(0x2FE2,0x00),    #Advanced Encryption Standard Key [111:104]
    "AES_KEY12":        Register(0x2FE3,0x00),    #Advanced Encryption Standard Key [103:96]
    "AES_KEY11":        Register(0x2FE4,0x00),    #Advanced Encryption Standard Key [95:88]
    "AES_KEY10":        Register(0x2FE5,0x00),    #Advanced Encryption Standard Key [87:80]
    "AES_KEY9":         Register(0x2FE6,0x00),    #Advanced Encryption Standard Key [79:72]
    "AES_KEY8":         Register(0x2FE7,0x00),    #Advanced Encryption Standard Key [71:64]
    "AES_KEY7":         Register(0x2FE8,0x00),    #Advanced Encryption Standard Key [63:56]
    "AES_KEY6":         Register(0x2FE9,0x00),    #Advanced Encryption Standard Key [55:48]
    "AES_KEY5":         Register(0x2FEA,0x00),    #Advanced Encryption Standard Key [47:40]
    "AES_KEY4":         Register(0x2FEB,0x00),    #Advanced Encryption Standard Key [39:32]
    "AES_KEY3":         Register(0x2FEC,0x00),    #Advanced Encryption Standard Key [31:24]
    "AES_KEY2":         Register(0x2FED,0x00),    #Advanced Encryption Standard Key [23:16]
    "AES_KEY1":         Register(0x2FEE,0x00),    #Advanced Encryption Standard Key [15:8]
    "AES_KEY0":         Register(0x2FEF,0x00),    #Advanced Encryption Standard Key [7:0]
    "AES_BUFFER15":     Register(0x2FF0,0x00),    #Advanced Encryption Standard Buffer [127:120]
    "AES_BUFFER14":     Register(0x2FF1,0x00),    #Advanced Encryption Standard Buffer [119:112]
    "AES_BUFFER13":     Register(0x2FF2,0x00),    #Advanced Encryption Standard Buffer [111:104]
    "AES_BUFFER12":     Register(0x2FF3,0x00),    #Advanced Encryption Standard Buffer [103:93]
    "AES_BUFFER11":     Register(0x2FF4,0x00),    #Advanced Encryption Standard Buffer [95:88]
    "AES_BUFFER10":     Register(0x2FF5,0x00),    #Advanced Encryption Standard Buffer [87:80]
    "AES_BUFFER9":      Register(0x2FF6,0x00),    #Advanced Encryption Standard Buffer [79:72]
    "AES_BUFFER8":      Register(0x2FF7,0x00),    #Advanced Encryption Standard Buffer [71:64]
    "AES_BUFFER7":      Register(0x2FF8,0x00),    #Advanced Encryption Standard Buffer [63:56]
    "AES_BUFFER6":      Register(0x2FF9,0x00),    #Advanced Encryption Standard Buffer [55:48]
    "AES_BUFFER5":      Register(0x2FFA,0x00),    #Advanced Encryption Standard Buffer [47:40]
    "AES_BUFFER4":      Register(0x2FFB,0x00),    #Advanced Encryption Standard Buffer [39:32]
    "AES_BUFFER3":      Register(0x2FFC,0x00),    #Advanced Encryption Standard Buffer [31:24]
    "AES_BUFFER2":      Register(0x2FFD,0x00),    #Advanced Encryption Standard Buffer [23:16]
    "AES_BUFFER1":      Register(0x2FFE,0x00),    #Advanced Encryption Standard Buffer [15:8]
    "AES_BUFFER0":      Register(0x2FFF,0x00),    #Advanced Encryption Standard Buffer [7:0]
}


# Bit Rate = 50 
# Carrier Frequency = 867.999878 
# Deviation = 24.948120 
# Modulation Format = 2-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 104.166667 
# Symbol rate = 50 
EASY_MODE ={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC3":          Register(0x0004,0x55),    
"SYNC2":          Register(0x0005,0x55),    
"SYNC1":          Register(0x0006,0x7A),    
"SYNC0":          Register(0x0007,0x0E),    
"SYNC_CFG1":      Register(0x0008,0x48),    
"SYNC_CFG0":      Register(0x0009,0x23),    
"DEVIATION_M":    Register(0x000A,0x47),    
"MODCFG_DEV_E":   Register(0x000B,0x0B),    
"DCFILT_CFG":     Register(0x000C,0x56),    
"PREAMBLE_CFG0":  Register(0x000E,0xBA),    
"IQIC":           Register(0x000F,0xC8),    
"CHAN_BW":        Register(0x0010,0x84),    
"MDMCFG1":        Register(0x0011,0x40),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0x94),    
"SYMBOL_RATE1":   Register(0x0014,0x7A),    
"SYMBOL_RATE0":   Register(0x0015,0xE1),    
"AGC_REF":        Register(0x0016,0x3E),    
"AGC_CS_THR":     Register(0x0017,0xF1),    
"AGC_CFG1":       Register(0x001B,0x11),    
"AGC_CFG0":       Register(0x001C,0x90),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x18),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x02),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x07),    
"FS_DIG0":        Register(0x2F13,0xAA),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC0":        Register(0x2F1D,0x17),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x05),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 1.2 
# Carrier Frequency = 867.999878 
# Deviation = 3.986359 
# Modulation Format = 2-FSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 10.964912 
# Symbol rate = 1.2
EXPERT_HIGH_1={
"IOCFG2":         Register(0x0001,0x06),    
"DEVIATION_M":    Register(0x000A,0xD1),    
"MODCFG_DEV_E":   Register(0x000B,0x00),    
"DCFILT_CFG":     Register(0x000C,0x5D),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0xCB),    
"CHAN_BW":        Register(0x0010,0xA6),    
"MDMCFG1":        Register(0x0011,0x40),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0x3F),    
"SYMBOL_RATE1":   Register(0x0014,0x75),    
"SYMBOL_RATE0":   Register(0x0015,0x10),    
"AGC_REF":        Register(0x0016,0x20),    
"AGC_CS_THR":     Register(0x0017,0xEC),    
"AGC_CFG1":       Register(0x001B,0x51),    
"AGC_CFG0":       Register(0x001C,0x87),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"FREQOFF_CFG":    Register(0x2F01,0x22),    
"MDMCFG2":        Register(0x2F05,0x0C),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x07),    
"FS_DIG0":        Register(0x2F13,0xAF),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC0":        Register(0x2F1D,0x17),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 4.8 
# Carrier Frequency = 867.999878 
# Deviation = 17.967224 
# Modulation Format = ASK/OOK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 128.205128 
# Symbol rate = 4.8
EXPERT_HIGH_2={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC_CFG1":      Register(0x0008,0xAC),    
"DEVIATION_M":    Register(0x000A,0xD7),    
"MODCFG_DEV_E":   Register(0x000B,0x1A),    
"DCFILT_CFG":     Register(0x000C,0x13),    
"PREAMBLE_CFG0":  Register(0x000E,0xE3),    
"IQIC":           Register(0x000F,0x00),    
"CHAN_BW":        Register(0x0010,0x0D),    
"MDMCFG0":        Register(0x0012,0x02),    
"SYMBOL_RATE2":   Register(0x0013,0x5F),    
"SYMBOL_RATE1":   Register(0x0014,0x75),    
"SYMBOL_RATE0":   Register(0x0015,0x10),    
"AGC_REF":        Register(0x0016,0x35),    
"AGC_CS_THR":     Register(0x0017,0xEC),    
"AGC_CFG3":       Register(0x0019,0x31),    
"AGC_CFG1":       Register(0x001B,0x24),    
"AGC_CFG0":       Register(0x001C,0x9F),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"ASK_CFG":        Register(0x002D,0xBF),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"FREQOFF_CFG":    Register(0x2F01,0x00),    
"MDMCFG2":        Register(0x2F05,0xFC),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x07),    
"FS_DIG0":        Register(0x2F13,0xA0),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC0":        Register(0x2F1D,0x17),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x09),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 38.4 
# Carrier Frequency = 867.999878 
# Deviation = 19.989014 
# Modulation Format = 2-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 104.166667 
# Symbol rate = 38.4
EXPERT_HIGH_3={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC_CFG1":      Register(0x0008,0xA9),    
"MODCFG_DEV_E":   Register(0x000B,0x0B),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0xC8),    
"CHAN_BW":        Register(0x0010,0x10),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0x8F),    
"SYMBOL_RATE1":   Register(0x0014,0x75),    
"SYMBOL_RATE0":   Register(0x0015,0x10),    
"AGC_REF":        Register(0x0016,0x27),    
"AGC_CS_THR":     Register(0x0017,0xEE),    
"AGC_CFG1":       Register(0x001B,0x11),    
"AGC_CFG0":       Register(0x001C,0x94),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x02),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x50),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC1":        Register(0x2F1C,0xF7),    
"FS_DVC0":        Register(0x2F1D,0x0F),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x09),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 38.4 
# Carrier Frequency = 920.599976 
# Deviation = 19.989014
# Modulation Format = 2-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 104.166667 
# Symbol rate = 38.4 
EXPERT_HIGH_4={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC_CFG1":      Register(0x0008,0xA9),    
"MODCFG_DEV_E":   Register(0x000B,0x0B),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0xC8),    
"CHAN_BW":        Register(0x0010,0x10),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0x8F),    
"SYMBOL_RATE1":   Register(0x0014,0x75),    
"SYMBOL_RATE0":   Register(0x0015,0x10),    
"AGC_REF":        Register(0x0016,0x27),    
"AGC_CS_THR":     Register(0x0017,0x01),    
"AGC_CFG1":       Register(0x001B,0x11),    
"AGC_CFG0":       Register(0x001C,0x94),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x02),    
"FREQ2":          Register(0x2F0C,0x5C),    
"FREQ1":          Register(0x2F0D,0x0F),    
"FREQ0":          Register(0x2F0E,0x5C),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x55),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC0":        Register(0x2F1D,0x17),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x09),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 50 
# Carrier Frequency = 867.999878 
# Deviation = 24.948120 
# Modulation Format = 2-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 104.166667 
# Symbol rate = 50
EXPERT_HIGH_5={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC3":          Register(0x0004,0x6F),    
"SYNC2":          Register(0x0005,0x4E),    
"SYNC1":          Register(0x0006,0x90),    
"SYNC0":          Register(0x0007,0x4E),    
"SYNC_CFG1":      Register(0x0008,0xE5),    
"SYNC_CFG0":      Register(0x0009,0x23),    
"DEVIATION_M":    Register(0x000A,0x47),    
"MODCFG_DEV_E":   Register(0x000B,0x0B),    
"DCFILT_CFG":     Register(0x000C,0x56),    
"PREAMBLE_CFG0":  Register(0x000E,0xBA),    
"IQIC":           Register(0x000F,0xC8),    
"CHAN_BW":        Register(0x0010,0x84),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0x94),    
"SYMBOL_RATE1":   Register(0x0014,0x7A),    
"SYMBOL_RATE0":   Register(0x0015,0xE1),    
"AGC_REF":        Register(0x0016,0x27),    
"AGC_CS_THR":     Register(0x0017,0xF1),    
"AGC_CFG1":       Register(0x001B,0x11),    
"AGC_CFG0":       Register(0x001C,0x90),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x24),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x18),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x02),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x50),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC1":        Register(0x2F1C,0xF7),    
"FS_DVC0":        Register(0x2F1D,0x0F),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x05),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Address Config = No address check 
# Bit Rate = 50 
# Carrier Frequency = 920.599976 
# Deviation = 24.948120 
# Device Address = 0 
# Manchester Enable = false 
# Modulation Format = 2-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 104.166667 
# Symbol rate = 50 
# Whitening = false 
EXPERT_HIGH_6={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC3":          Register(0x0004,0x6F),    
"SYNC2":          Register(0x0005,0x4E),    
"SYNC1":          Register(0x0006,0x90),    
"SYNC0":          Register(0x0007,0x4E),    
"SYNC_CFG1":      Register(0x0008,0xE5),    
"SYNC_CFG0":      Register(0x0009,0x23),    
"DEVIATION_M":    Register(0x000A,0x47),    
"MODCFG_DEV_E":   Register(0x000B,0x0B),    
"DCFILT_CFG":     Register(0x000C,0x56),    
"PREAMBLE_CFG0":  Register(0x000E,0xBA),    
"IQIC":           Register(0x000F,0xC8),    
"CHAN_BW":        Register(0x0010,0x84),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0x94),    
"SYMBOL_RATE1":   Register(0x0014,0x7A),    
"SYMBOL_RATE0":   Register(0x0015,0xE1),    
"AGC_REF":        Register(0x0016,0x27),    
"AGC_CS_THR":     Register(0x0017,0x01),    
"AGC_CFG1":       Register(0x001B,0x11),    
"AGC_CFG0":       Register(0x001C,0x90),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x24),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x18),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x02),    
"FREQ2":          Register(0x2F0C,0x5C),    
"FREQ1":          Register(0x2F0D,0x0F),    
"FREQ0":          Register(0x2F0E,0x5C),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x55),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC0":        Register(0x2F1D,0x17),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x05),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 100 
# Carrier Frequency = 867.999878 
# Deviation = 49.896240
# Modulation Format = 2-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 208.333333 
# Symbol rate = 100
EXPERT_HIGH_7={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC_CFG1":      Register(0x0008,0xA8),    
"SYNC_CFG0":      Register(0x0009,0x23),    
"DEVIATION_M":    Register(0x000A,0x47),    
"MODCFG_DEV_E":   Register(0x000B,0x0C),    
"DCFILT_CFG":     Register(0x000C,0x4B),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0xD8),    
"CHAN_BW":        Register(0x0010,0x08),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0xA4),    
"SYMBOL_RATE1":   Register(0x0014,0x7A),    
"SYMBOL_RATE0":   Register(0x0015,0xE1),    
"AGC_REF":        Register(0x0016,0x2A),    
"AGC_CS_THR":     Register(0x0017,0xF6),    
"AGC_CFG1":       Register(0x001B,0x12),    
"AGC_CFG0":       Register(0x001C,0x80),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x02),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x50),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC1":        Register(0x2F1C,0xF7),    
"FS_DVC0":        Register(0x2F1D,0x0F),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x09),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 100 
# Carrier Frequency = 920.599976 
# Deviation = 49.896240
# Modulation Format = 2-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 208.333333 
# Symbol rate = 100
EXPERT_HIGH_8={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC_CFG1":      Register(0x0008,0xA8),    
"SYNC_CFG0":      Register(0x0009,0x23),    
"DEVIATION_M":    Register(0x000A,0x47),    
"MODCFG_DEV_E":   Register(0x000B,0x0C),    
"DCFILT_CFG":     Register(0x000C,0x4B),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0xD8),    
"CHAN_BW":        Register(0x0010,0x08),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0xA4),    
"SYMBOL_RATE1":   Register(0x0014,0x7A),    
"SYMBOL_RATE0":   Register(0x0015,0xE1),    
"AGC_REF":        Register(0x0016,0x2A),    
"AGC_CS_THR":     Register(0x0017,0x01),    
"AGC_CFG1":       Register(0x001B,0x12),    
"AGC_CFG0":       Register(0x001C,0x80),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x02),    
"FREQ2":          Register(0x2F0C,0x5C),    
"FREQ1":          Register(0x2F0D,0x0F),    
"FREQ0":          Register(0x2F0E,0x5C),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x55),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC0":        Register(0x2F1D,0x17),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x09),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 1000 
# Carrier Frequency = 867.999878 
# Deviation = 399.169922
# Modulation Format = 4-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 1666.666667 
# Symbol rate = 500
EXPERT_HIGH_9={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC_CFG1":      Register(0x0008,0xA8),    
"DEVIATION_M":    Register(0x000A,0x47),    
"MODCFG_DEV_E":   Register(0x000B,0x2F),    
"DCFILT_CFG":     Register(0x000C,0x1E),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0x00),    
"CHAN_BW":        Register(0x0010,0x01),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0xC9),    
"SYMBOL_RATE1":   Register(0x0014,0x99),    
"SYMBOL_RATE0":   Register(0x0015,0x99),    
"AGC_REF":        Register(0x0016,0x2F),    
"AGC_CS_THR":     Register(0x0017,0xF8),    
"AGC_CFG2":       Register(0x001A,0x60),    
"AGC_CFG1":       Register(0x001B,0x12),    
"AGC_CFG0":       Register(0x001C,0x84),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"FREQOFF_CFG":    Register(0x2F01,0x23),    
"MDMCFG2":        Register(0x2F05,0x00),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0xA3),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC1":        Register(0x2F1C,0xF7),    
"FS_DVC0":        Register(0x2F1D,0x0F),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x0D),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 1000 
# Carrier Frequency = 920.599976 
# Deviation = 399.169922
# Modulation Format = 4-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 1666.666667 
# Symbol rate = 500
EXPERT_HIGH_10={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC_CFG1":      Register(0x0008,0xA8),    
"DEVIATION_M":    Register(0x000A,0x47),    
"MODCFG_DEV_E":   Register(0x000B,0x2F),    
"DCFILT_CFG":     Register(0x000C,0x1E),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0x00),    
"CHAN_BW":        Register(0x0010,0x01),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0xC9),    
"SYMBOL_RATE1":   Register(0x0014,0x99),    
"SYMBOL_RATE0":   Register(0x0015,0x99),    
"AGC_REF":        Register(0x0016,0x2F),    
"AGC_CS_THR":     Register(0x0017,0x01),    
"AGC_CFG2":       Register(0x001A,0x60),    
"AGC_CFG1":       Register(0x001B,0x12),    
"AGC_CFG0":       Register(0x001C,0x84),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"FREQOFF_CFG":    Register(0x2F01,0x23),    
"MDMCFG2":        Register(0x2F05,0x00),    
"FREQ2":          Register(0x2F0C,0x5C),    
"FREQ1":          Register(0x2F0D,0x0F),    
"FREQ0":          Register(0x2F0E,0x5C),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0xA3),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC0":        Register(0x2F1D,0x17),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x0D),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 500 
# Carrier Frequency = 867.999878 
# Deviation = 124.816895
# Modulation Format = 2-FSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 833.333333 
# Symbol rate = 500
EXPERT_HIGH_11={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC_CFG1":      Register(0x0008,0xA8),    
"SYNC_CFG0":      Register(0x0009,0x13),    
"DEVIATION_M":    Register(0x000A,0x99),    
"MODCFG_DEV_E":   Register(0x000B,0x05),    
"DCFILT_CFG":     Register(0x000C,0x26),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0x00),    
"CHAN_BW":        Register(0x0010,0x02),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0xC9),    
"SYMBOL_RATE1":   Register(0x0014,0x99),    
"SYMBOL_RATE0":   Register(0x0015,0x99),    
"AGC_REF":        Register(0x0016,0x2F),    
"AGC_CS_THR":     Register(0x0017,0xEC),    
"AGC_CFG1":       Register(0x001B,0x16),    
"AGC_CFG0":       Register(0x001C,0x84),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x18),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x00),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x50),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC1":        Register(0x2F1C,0xF7),    
"FS_DVC0":        Register(0x2F1D,0x0F),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x0D),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 500 
# Carrier Frequency = 920.599976 
# Deviation = 124.816895
# Modulation Format = 2-FSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 833.333333 
# Symbol rate = 500
EXPERT_HIGH_12={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC_CFG1":      Register(0x0008,0xA8),    
"SYNC_CFG0":      Register(0x0009,0x13),    
"DEVIATION_M":    Register(0x000A,0x99),    
"MODCFG_DEV_E":   Register(0x000B,0x05),    
"DCFILT_CFG":     Register(0x000C,0x26),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0x00),    
"CHAN_BW":        Register(0x0010,0x02),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0xC9),    
"SYMBOL_RATE1":   Register(0x0014,0x99),    
"SYMBOL_RATE0":   Register(0x0015,0x99),    
"AGC_REF":        Register(0x0016,0x2F),    
"AGC_CS_THR":     Register(0x0017,0x01),    
"AGC_CFG1":       Register(0x001B,0x16),    
"AGC_CFG0":       Register(0x001C,0x84),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x18),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x00),    
"FREQ2":          Register(0x2F0C,0x5C),    
"FREQ1":          Register(0x2F0D,0x0F),    
"FREQ0":          Register(0x2F0E,0x5C),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x55),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC0":        Register(0x2F1D,0x17),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x0D),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 130 
# Carrier Frequency = 867.999878 
# Deviation = 54.931641
# Modulation Format = 4-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 185.185185 
# Symbol rate = 65
EXPERT_HIGH_13={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC3":          Register(0x0004,0x00),    
"SYNC2":          Register(0x0005,0x00),    
"SYNC1":          Register(0x0006,0xD9),    
"SYNC0":          Register(0x0007,0xCC),    
"SYNC_CFG1":      Register(0x0008,0x47),    
"SYNC_CFG0":      Register(0x0009,0x00),    
"DEVIATION_M":    Register(0x000A,0x68),    
"MODCFG_DEV_E":   Register(0x000B,0x2C),    
"DCFILT_CFG":     Register(0x000C,0x4B),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0xEC),    
"CHAN_BW":        Register(0x0010,0x09),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0x9A),    
"SYMBOL_RATE1":   Register(0x0014,0x9F),    
"SYMBOL_RATE0":   Register(0x0015,0xBE),    
"AGC_REF":        Register(0x0016,0x2F),    
"AGC_CS_THR":     Register(0x0017,0xF6),    
"AGC_CFG1":       Register(0x001B,0x12),    
"AGC_CFG0":       Register(0x001C,0x84),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x02),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x50),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC1":        Register(0x2F1C,0xF7),    
"FS_DVC0":        Register(0x2F1D,0x0F),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x09),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}



# Bit Rate = 150 
# Carrier Frequency = 867.999878 
# Deviation = 54.931641
# Modulation Format = 4-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 185.185185 
# Symbol rate = 75
EXPERT_HIGH_14={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC3":          Register(0x0004,0x00),    
"SYNC2":          Register(0x0005,0x00),    
"SYNC1":          Register(0x0006,0xD9),    
"SYNC0":          Register(0x0007,0xCC),    
"SYNC_CFG1":      Register(0x0008,0x47),    
"SYNC_CFG0":      Register(0x0009,0x00),    
"DEVIATION_M":    Register(0x000A,0x68),    
"MODCFG_DEV_E":   Register(0x000B,0x2C),    
"DCFILT_CFG":     Register(0x000C,0x4B),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0xEC),    
"CHAN_BW":        Register(0x0010,0x09),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0x9E),    
"SYMBOL_RATE1":   Register(0x0014,0xB8),    
"SYMBOL_RATE0":   Register(0x0015,0x52),    
"AGC_REF":        Register(0x0016,0x2F),    
"AGC_CS_THR":     Register(0x0017,0xF6),    
"AGC_CFG1":       Register(0x001B,0x12),    
"AGC_CFG0":       Register(0x001C,0x84),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x12),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x02),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x50),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC1":        Register(0x2F1C,0xF7),    
"FS_DVC0":        Register(0x2F1D,0x0F),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x09),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 1.2 
# Carrier Frequency = 433.999939 
# Deviation = 3.986359
# Modulation Format = 2-FSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 10.964912 
# Symbol rate = 1.2
EXPERT_MED_1={
"IOCFG2":         Register(0x0001,0x06),    
"DEVIATION_M":    Register(0x000A,0xD1),    
"MODCFG_DEV_E":   Register(0x000B,0x00),    
"DCFILT_CFG":     Register(0x000C,0x5D),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0xCB),    
"CHAN_BW":        Register(0x0010,0xA6),    
"MDMCFG1":        Register(0x0011,0x40),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0x3F),    
"SYMBOL_RATE1":   Register(0x0014,0x75),    
"SYMBOL_RATE0":   Register(0x0015,0x10),    
"AGC_REF":        Register(0x0016,0x20),    
"AGC_CS_THR":     Register(0x0017,0xEC),    
"AGC_CFG1":       Register(0x001B,0x51),    
"AGC_CFG0":       Register(0x001C,0x87),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x14),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"FREQOFF_CFG":    Register(0x2F01,0x22),    
"MDMCFG2":        Register(0x2F05,0x0C),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x07),    
"FS_DIG0":        Register(0x2F13,0xAF),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC0":        Register(0x2F1D,0x17),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 4.8 
# Carrier Frequency = 433.999939 
# Deviation = 17.967224
# Modulation Format = ASK/OOK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 128.205128 
# Symbol rate = 4.8
EXPERT_MED_2={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC_CFG1":      Register(0x0008,0xAC),    
"DEVIATION_M":    Register(0x000A,0xD7),    
"MODCFG_DEV_E":   Register(0x000B,0x1A),    
"DCFILT_CFG":     Register(0x000C,0x13),    
"PREAMBLE_CFG0":  Register(0x000E,0xE3),    
"IQIC":           Register(0x000F,0x00),    
"CHAN_BW":        Register(0x0010,0x0D),    
"MDMCFG0":        Register(0x0012,0x02),    
"SYMBOL_RATE2":   Register(0x0013,0x5F),    
"SYMBOL_RATE1":   Register(0x0014,0x75),    
"SYMBOL_RATE0":   Register(0x0015,0x10),    
"AGC_REF":        Register(0x0016,0x35),    
"AGC_CS_THR":     Register(0x0017,0xEC),    
"AGC_CFG3":       Register(0x0019,0x31),    
"AGC_CFG1":       Register(0x001B,0x24),    
"AGC_CFG0":       Register(0x001C,0x9F),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x14),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"ASK_CFG":        Register(0x002D,0xBF),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"FREQOFF_CFG":    Register(0x2F01,0x00),    
"MDMCFG2":        Register(0x2F05,0xFC),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x07),    
"FS_DIG0":        Register(0x2F13,0xA0),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC0":        Register(0x2F1D,0x17),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x09),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 38.4 
# Carrier Frequency = 433.999939 
# Deviation = 19.989014
# Modulation Format = 2-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 104.166667 
# Symbol rate = 38.4
EXPERT_MED_3={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC_CFG1":      Register(0x0008,0xA9),    
"MODCFG_DEV_E":   Register(0x000B,0x0B),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0xC8),    
"CHAN_BW":        Register(0x0010,0x10),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0x8F),    
"SYMBOL_RATE1":   Register(0x0014,0x75),    
"SYMBOL_RATE0":   Register(0x0015,0x10),    
"AGC_REF":        Register(0x0016,0x27),    
"AGC_CS_THR":     Register(0x0017,0xEE),    
"AGC_CFG1":       Register(0x001B,0x11),    
"AGC_CFG0":       Register(0x001C,0x94),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x14),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x02),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x50),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC1":        Register(0x2F1C,0xF7),    
"FS_DVC0":        Register(0x2F1D,0x0F),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x09),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 50 
# Carrier Frequency = 433.999939 
# Deviation = 24.948120
# Modulation Format = 2-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 104.166667 
# Symbol rate = 50
EXPERT_MED_4={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC3":          Register(0x0004,0x6F),    
"SYNC2":          Register(0x0005,0x4E),    
"SYNC1":          Register(0x0006,0x90),    
"SYNC0":          Register(0x0007,0x4E),    
"SYNC_CFG1":      Register(0x0008,0xE5),    
"SYNC_CFG0":      Register(0x0009,0x23),    
"DEVIATION_M":    Register(0x000A,0x47),    
"MODCFG_DEV_E":   Register(0x000B,0x0B),    
"DCFILT_CFG":     Register(0x000C,0x56),    
"PREAMBLE_CFG0":  Register(0x000E,0xBA),    
"IQIC":           Register(0x000F,0xC8),    
"CHAN_BW":        Register(0x0010,0x84),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0x94),    
"SYMBOL_RATE1":   Register(0x0014,0x7A),    
"SYMBOL_RATE0":   Register(0x0015,0xE1),    
"AGC_REF":        Register(0x0016,0x27),    
"AGC_CS_THR":     Register(0x0017,0xF1),    
"AGC_CFG1":       Register(0x001B,0x11),    
"AGC_CFG0":       Register(0x001C,0x90),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x14),    
"PKT_CFG2":       Register(0x0026,0x24),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x18),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x02),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x50),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC1":        Register(0x2F1C,0xF7),    
"FS_DVC0":        Register(0x2F1D,0x0F),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x05),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 100 
# Carrier Frequency = 433.999939 
# Deviation = 49.896240 
# Modulation Format = 2-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 208.333333 
# Symbol rate = 100 
EXPERT_MED_5={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC_CFG1":      Register(0x0008,0xA8),    
"SYNC_CFG0":      Register(0x0009,0x23),    
"DEVIATION_M":    Register(0x000A,0x47),    
"MODCFG_DEV_E":   Register(0x000B,0x0C),    
"DCFILT_CFG":     Register(0x000C,0x4B),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0xD8),    
"CHAN_BW":        Register(0x0010,0x08),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0xA4),    
"SYMBOL_RATE1":   Register(0x0014,0x7A),    
"SYMBOL_RATE0":   Register(0x0015,0xE1),    
"AGC_REF":        Register(0x0016,0x2A),    
"AGC_CS_THR":     Register(0x0017,0xF6),    
"AGC_CFG1":       Register(0x001B,0x12),    
"AGC_CFG0":       Register(0x001C,0x80),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x14),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x02),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x50),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC1":        Register(0x2F1C,0xF7),    
"FS_DVC0":        Register(0x2F1D,0x0F),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x09),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 1000 
# Carrier Frequency = 433.999939 
# Deviation = 399.169922 
# Modulation Format = 4-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 1666.666667 
# Symbol rate = 500 
EXPERT_MED_6={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC_CFG1":      Register(0x0008,0xA8),    
"DEVIATION_M":    Register(0x000A,0x47),    
"MODCFG_DEV_E":   Register(0x000B,0x2F),    
"DCFILT_CFG":     Register(0x000C,0x1E),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0x00),    
"CHAN_BW":        Register(0x0010,0x01),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0xC9),    
"SYMBOL_RATE1":   Register(0x0014,0x99),    
"SYMBOL_RATE0":   Register(0x0015,0x99),    
"AGC_REF":        Register(0x0016,0x2F),    
"AGC_CS_THR":     Register(0x0017,0xF8),    
"AGC_CFG2":       Register(0x001A,0x60),    
"AGC_CFG1":       Register(0x001B,0x12),    
"AGC_CFG0":       Register(0x001C,0x84),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x14),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"FREQOFF_CFG":    Register(0x2F01,0x23),    
"MDMCFG2":        Register(0x2F05,0x00),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0xA3),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC1":        Register(0x2F1C,0xF7),    
"FS_DVC0":        Register(0x2F1D,0x0F),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x0D),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 500 
# Carrier Frequency = 433.999939 
# Deviation = 124.816895 
# Modulation Format = 2-FSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 833.333333 
# Symbol rate = 500 
EXPERT_MED_7={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC_CFG1":      Register(0x0008,0xA8),    
"SYNC_CFG0":      Register(0x0009,0x13),    
"DEVIATION_M":    Register(0x000A,0x99),    
"MODCFG_DEV_E":   Register(0x000B,0x05),    
"DCFILT_CFG":     Register(0x000C,0x26),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0x00),    
"CHAN_BW":        Register(0x0010,0x02),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0xC9),    
"SYMBOL_RATE1":   Register(0x0014,0x99),    
"SYMBOL_RATE0":   Register(0x0015,0x99),    
"AGC_REF":        Register(0x0016,0x2F),    
"AGC_CS_THR":     Register(0x0017,0xEC),    
"AGC_CFG1":       Register(0x001B,0x16),    
"AGC_CFG0":       Register(0x001C,0x84),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x14),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x18),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x00),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x50),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC1":        Register(0x2F1C,0xF7),    
"FS_DVC0":        Register(0x2F1D,0x0F),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x0D),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 130 
# Carrier Frequency = 433.999939 
# Deviation = 54.931641 
# Modulation Format = 4-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 185.185185 
# Symbol rate = 65 
EXPERT_MED_8={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC3":          Register(0x0004,0x00),    
"SYNC2":          Register(0x0005,0x00),    
"SYNC1":          Register(0x0006,0xD9),    
"SYNC0":          Register(0x0007,0xCC),    
"SYNC_CFG1":      Register(0x0008,0x47),    
"SYNC_CFG0":      Register(0x0009,0x00),    
"DEVIATION_M":    Register(0x000A,0x68),    
"MODCFG_DEV_E":   Register(0x000B,0x2C),    
"DCFILT_CFG":     Register(0x000C,0x4B),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0xEC),    
"CHAN_BW":        Register(0x0010,0x09),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0x9A),    
"SYMBOL_RATE1":   Register(0x0014,0x9F),    
"SYMBOL_RATE0":   Register(0x0015,0xBE),    
"AGC_REF":        Register(0x0016,0x2F),    
"AGC_CS_THR":     Register(0x0017,0xF6),    
"AGC_CFG1":       Register(0x001B,0x12),    
"AGC_CFG0":       Register(0x001C,0x84),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x14),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x02),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x50),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC1":        Register(0x2F1C,0xF7),    
"FS_DVC0":        Register(0x2F1D,0x0F),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x09),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 150 
# Carrier Frequency = 433.999939 
# Deviation = 54.931641 
# Modulation Format = 4-GFSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 185.185185 
# Symbol rate = 75 
EXPERT_MED_9={
"IOCFG2":         Register(0x0001,0x06),    
"SYNC3":          Register(0x0004,0x00),    
"SYNC2":          Register(0x0005,0x00),    
"SYNC1":          Register(0x0006,0xD9),    
"SYNC0":          Register(0x0007,0xCC),    
"SYNC_CFG1":      Register(0x0008,0x47),    
"SYNC_CFG0":      Register(0x0009,0x00),    
"DEVIATION_M":    Register(0x000A,0x68),    
"MODCFG_DEV_E":   Register(0x000B,0x2C),    
"DCFILT_CFG":     Register(0x000C,0x4B),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0xEC),    
"CHAN_BW":        Register(0x0010,0x09),    
"MDMCFG1":        Register(0x0011,0x42),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0x9E),    
"SYMBOL_RATE1":   Register(0x0014,0xB8),    
"SYMBOL_RATE0":   Register(0x0015,0x52),    
"AGC_REF":        Register(0x0016,0x2F),    
"AGC_CS_THR":     Register(0x0017,0xF6),    
"AGC_CFG1":       Register(0x001B,0x12),    
"AGC_CFG0":       Register(0x001C,0x84),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x14),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"TOC_CFG":        Register(0x2F02,0x03),    
"MDMCFG2":        Register(0x2F05,0x02),    
"FREQ2":          Register(0x2F0C,0x56),    
"FREQ1":          Register(0x2F0D,0xCC),    
"FREQ0":          Register(0x2F0E,0xCC),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x04),    
"FS_DIG0":        Register(0x2F13,0x50),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC1":        Register(0x2F1C,0xF7),    
"FS_DVC0":        Register(0x2F1D,0x0F),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"IFAMP":          Register(0x2F2F,0x09),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}


# Bit Rate = 1.2 
# Carrier Frequency = 169.000000 
# Deviation = 3.986359 
# Modulation Format = 2-FSK 
# Packet Bit Length = 0 
# Packet Length = 255 
# Packet Length Mode = Variable 
# RX Filter BW = 10.964912 
# Symbol rate = 1.2
EXPERT_LOW_1={
"IOCFG2":         Register(0x0001,0x06),    
"DEVIATION_M":    Register(0x000A,0xD1),    
"MODCFG_DEV_E":   Register(0x000B,0x00),    
"DCFILT_CFG":     Register(0x000C,0x5D),    
"PREAMBLE_CFG0":  Register(0x000E,0x8A),    
"IQIC":           Register(0x000F,0xCB),    
"CHAN_BW":        Register(0x0010,0xA6),    
"MDMCFG1":        Register(0x0011,0x40),    
"MDMCFG0":        Register(0x0012,0x05),    
"SYMBOL_RATE2":   Register(0x0013,0x3F),    
"SYMBOL_RATE1":   Register(0x0014,0x75),    
"SYMBOL_RATE0":   Register(0x0015,0x10),    
"AGC_REF":        Register(0x0016,0x20),    
"AGC_CS_THR":     Register(0x0017,0xEC),    
"AGC_CFG1":       Register(0x001B,0x51),    
"AGC_CFG0":       Register(0x001C,0x87),    
"FIFO_CFG":       Register(0x001D,0x00),    
"FS_CFG":         Register(0x0020,0x1A),    
"PKT_CFG2":       Register(0x0026,0x00),    
"PKT_CFG0":       Register(0x0028,0x20),    
"PKT_LEN":        Register(0x002E,0xFF),    
"IF_MIX_CFG":     Register(0x2F00,0x1C),    
"FREQOFF_CFG":    Register(0x2F01,0x22),    
"MDMCFG2":        Register(0x2F05,0x0C),    
"FREQ2":          Register(0x2F0C,0x54),    
"FREQ1":          Register(0x2F0D,0x80),    
"IF_ADC1":        Register(0x2F10,0xEE),    
"IF_ADC0":        Register(0x2F11,0x10),    
"FS_DIG1":        Register(0x2F12,0x07),    
"FS_DIG0":        Register(0x2F13,0xAF),    
"FS_CAL1":        Register(0x2F16,0x40),    
"FS_CAL0":        Register(0x2F17,0x0E),    
"FS_DIVTWO":      Register(0x2F19,0x03),    
"FS_DSM0":        Register(0x2F1B,0x33),    
"FS_DVC0":        Register(0x2F1D,0x17),    
"FS_PFD":         Register(0x2F1F,0x00),    
"FS_PRE":         Register(0x2F20,0x6E),    
"FS_REG_DIV_CML": Register(0x2F21,0x1C),    
"FS_SPARE":       Register(0x2F22,0xAC),    
"FS_VCO0":        Register(0x2F27,0xB5),    
"XOSC5":          Register(0x2F32,0x0E),    
"XOSC1":          Register(0x2F36,0x03),    
}

