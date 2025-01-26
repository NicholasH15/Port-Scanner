import socket
import argparse

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip,port))
        if result == 0:
            print(f"Port {port}: Open")
        else:
            print(f"Port {port}: Closed")
            sock.close()
    except KeyboardInterrupt:
        print("\nScan interrupted by user.")
        exit()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Port Scanner")

    parser.add_argument("-a", "--all", action="store_true", help="Scan all ports in range")
    parser.add_argument("-v", "--vulnerable", action="store_true", help="Scan commonly exploited ports")

    parser.add_argument("ip", help="Target IP address or hostname")
    
    parser.add_argument("start_port", type=int, nargs="?", help="Start of port range (only for --all)")
    parser.add_argument("end_port", type=int, nargs="?", help="End of port range (only for --all)")

    args = parser.parse_args()

    ip = args.ip

    if args.all:
        if args.start_port is None or args.end_port is None:
            print("Error: --all flag requires both start_port and end_port.")
        else:
            start_port = args.start_port
            end_port = args.end_port
            print(f"Scanning {ip} from {start_port} to {end_port}...")
            for port in range(start_port, end_port + 1):
                scan_port(ip, port)

    elif args.vulnerable:
        vulnerablePorts = [21, 22, 23, 25, 53, 80, 443, 445, 2049]
        print(f"Scanning {ip} for commonly exploited ports...")
        for port in vulnerablePorts:
            scan_port(ip, port)

    else:
        print("Please specify a flag (-a for range or -v for vulnerable ports).")
