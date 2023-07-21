import socket
import subprocess
from datetime import datetime

# Clear the terminal screen
subprocess.call('clear', shell=True)

# Prompt the user to enter the target IP address or hostname
target = input("Enter the target IP address or hostname: ")

# Function to perform the port scanning
def port_scan(target):
    try:
        # Get the IP address of the target
        ip = socket.gethostbyname(target)

        # Print scanning information
        print("-" * 50)
        print("Scanning target:", ip)
        print("Time started:", datetime.now())
        print("-" * 50)

        # Iterate over a range of port numbers and attempt to connect
        for port in range(1, 65635):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a timeout for the connection attempt
            result = sock.connect_ex((ip, port))
            if result == 0:
                # If the connection was successful (port is open), print the port number
                print("Port {}: Open".format(port))
            sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")

    except socket.error:
        print("Could not connect to the server.")

# Call the port_scan function with the specified target
port_scan(target)
