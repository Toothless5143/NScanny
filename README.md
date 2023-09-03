# Port Scanner

The Port Scanner is a Python tool designed to perform a simple yet effective port scanning operation on a target IP address or hostname provided by the user. By utilizing the `socket` module, this tool establishes socket connections to different port numbers on the target and determines whether the ports are open or closed.

## Features

- Efficiently scans a range of port numbers on a target IP address or hostname.
- Utilizes socket connections to determine the status of each port (open or closed).
- Provides clear and concise output of the scan results.

## Installation

To install and run the Port Scanner tool, follow these steps:

1. Download all the required files and libraries by executing the following command:
   ```shell
   git clone https://github.com/Toothless5143/Port-Scanny.git && cd Port-Scanny
   pip install -r requirements.txt
   ```

2. Run the tool using the following command:
   ```shell
   python3 port-scanny.py
   ```

## Usage

1. Upon running the tool, you will be prompted to enter the target IP address or hostname.

2. The tool will then initiate the port scanning process, providing you with detailed information about the target, including the IP address, scan start time, and the ports being scanned.

3. As the scanning progresses, the tool will display the status of each port, indicating whether it is open or closed.

## License

This tool is open source and available under the [MIT License](/LICENSE).
