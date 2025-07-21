import os  # Import the os module to run system commands

openHost = []   # List to store IPs that respond to ping (online hosts)
closedHost = [] # List to store IPs that do not respond to ping (offline hosts)

def ping_sweep(network_prefix, start, end):
    """
    Ping a range of IP addresses and show which hosts are online.
    Shows progress percentage while scanning.
    """
    total = end - start + 1  # Calculate total number of IPs to scan
    print(f"Pinging hosts from {network_prefix}.{start} to {network_prefix}.{end} ...")
    # Loop through each host number in the given range
    for idx, i in enumerate(range(start, end + 1), 1):
        ip = f"{network_prefix}.{i}"  # Build the full IP address
        # Run the ping command (Windows: -n 1 = 1 ping, -w 500 = 500ms timeout, > nul hides output)
        response = os.system(f"ping -n 1 -w 500 {ip} > nul")
        if response == 0:
            openHost.append(ip)    # If ping is successful, add to openHost
        else:
            closedHost.append(ip)  # If ping fails, add to closedHost
        # Calculate and print progress percentage on the same line
        percent = int((idx / total) * 100)
        print(f"\rScanning... {percent}% complete", end="")
    # After scanning, print the list of online hosts
    print("\nOpen Hosts:", openHost)
    # Uncomment the next line to also print offline hosts
    # print("Closed Hosts:", closedHost)

if __name__ == "__main__":
    # Get user input for network prefix and host range
    prefix = input("Enter network prefix (e.g., 192.168.1): ")
    start = int(input("Start host number: "))
    end = int(input("End host number: "))
    # Start the ping sweep
    ping_sweep(prefix, start, end)