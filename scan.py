import socket
import argparse

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