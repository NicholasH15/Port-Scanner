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
    parser = argparse.ArgumentParser(description = "Simple Port Scanner")
    parser.add_argument("ip", help = "Target IP address or hostname")
    parser.add_argument("start_port", type = int, help = "Start of port range")
    parser.add_argument("end_port", type = int, help = "End of port range" )
    args = parser.parse_args()

    ip = args.ip
    start_port = args.start_port
    end_port = args.end_port

    print(f"Scanning {ip} from {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        scan_port(ip, port)