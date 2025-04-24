import nmap

# Initialize the Nmap Scanner
scanner = nmap.PortScanner()

# Define the target and the range of ports to scan
target = '192.168.1.1'
ports = '20-80'  # Scanning ports 20 to 80

# Perform the scan
print(f"Scanning {target} on ports {ports}...")
scanner.scan(target, ports)

# Display scan results
for host in scanner.all_hosts():
    print(f"\nHost: {host} ({scanner[host].hostname()})")
    print(f"State: {scanner[host].state()}")
    for protocol in scanner[host].all_protocols():
        print(f"Protocol: {protocol}")
        ports = scanner[host][protocol].keys()
        for port in ports:
            print(f"Port: {port}\tState: {scanner[host][protocol][port]['state']}")