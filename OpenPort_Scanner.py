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
import time
import sys
import threading

openPorts = []
closedPorts = []
progress = 0  # Progress percentage

# ASCII banner
def ascii_banner():
    animation = [
        r"   ____             _           _           ",
        r"  / __ \           | |         | |          ",
        r" | |  | |_ __   ___| |__   ___ | | ___   _  ",
        r" | |  | | '_ \ / __| '_ \ / _ \| |/ / | | | ",
        r" | |__| | | | | (__| | | | (_) |   <| |_| | ",
        r"  \____/|_| |_|\___|_| |_|\___/|_|\_\\__,_| ",
        r"                                             ",
        r"         Open Port Scanner by Vignesh        ",
        r"---------------------------------------------"
    ]
    for line in animation:
        print(line)
        time.sleep(0.05)
    print("\n")

# Loading animation with percentage
def loading_animation(total_ports):
    while progress < 100:
        sys.stdout.write(f"\rScanning ports... {progress}%")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(f"\rScanning ports... 100%\n")
    sys.stdout.flush()

# Function to scan ports in a given range on a target IP address
def scan(ip, s, e):
    global progress
    total_ports = e - s + 1
    scanned_ports = 0
    t = threading.Thread(target=loading_animation, args=(total_ports,))
    t.start()
    for p in range(s, e+1):
        with socket.socket() as sock:
            sock.settimeout(0.5)
            if sock.connect_ex((ip, p)) == 0:
                openPorts.append(p)
            else:
                closedPorts.append(p)
        scanned_ports += 1
        progress = int((scanned_ports / total_ports) * 100)
    t.join()
    print(f"Open Ports: {openPorts}")
    print(f"Closed Ports: {closedPorts}")

if __name__ == "__main__":
    ascii_banner()
    scan(input("IP: "), int(input("Starting Port : ")), int(input("Ending Port : ")))
