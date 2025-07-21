# OpenPort_Scanner.py
# This script scans a range of ports on a specified IP address to check if they are open
# It uses the socket library to attempt connections to each port in the specified range.
# Example usage: python OpenPort_Scanner.py
# this is created by vignesh k at 21/07/2025 :)
# Sample output:
# IP: 192.168.100.1
# Start:1
# End:8080
# Port 8080 open
# /-- Thanks for using this tool, if you like it please give a star on github --/


import socket

# Function to scan ports in a given range on a target IP address
def scan(ip, s, e):
    for p in range(s, e+1):  # Loop through each port in the specified range
        with socket.socket() as sock:  # Create a new socket for each port
            sock.settimeout(0.5)  # Set a timeout for the connection attempt (0.2 seconds)
            # Try to connect to the target IP and port
            if sock.connect_ex((ip, p)) == 0:  # If connection is successful (returns 0)
                print(f"Port {p} open")  # Print that the port is ope
            else:
                print(f"Port {p} closed")
if __name__ == "__main__":
    # Get user input for IP address and port range, then start the scan
    scan(input("IP: "), int(input("Start: ")), int(input("End: ")))