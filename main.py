#!/usr/bin/env python3
from cc1200 import CC1200
import time
import argparse

# def main(mode):
def main():
    radio = CC1200(bus=0, device=0)
    radio.configure()

    # if mode == "TX":
    #     # Transmit mode
    #     payload = [0x01, 0x02, 0x03, 0x04]
    #     radio.tx(payload)
    #     print("Transmission complete.")
    
    # elif mode == "RX":
    #     # Receive mode
    #     received_data = radio.rx(4)
    #     print("Received data:", received_data)
    
    # else:
    #     print("Invalid mode. Please choose either 'TX' or 'RX'.")
    #     return
    
    time.sleep(1)

if __name__ == "__main__":
    # # Set up argument parsing
    # parser = argparse.ArgumentParser(description="Choose TX or RX mode.")
    # parser.add_argument("mode", choices=["TX", "RX"], help="Select the mode: 'TX' for transmit, 'RX' for receive.")
    
    # # Parse the arguments
    # args = parser.parse_args()
    
    # # Run the main function with the selected mode
    # main(args.mode)

    main()