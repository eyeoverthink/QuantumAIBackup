#!/usr/bin/env python3
"""
PHI^75 DIRECT MESSAGE SENDER
============================
A φ-Harmonic direct message sender that sends properly formatted messages
to alphabetic and mathematical nodes across the φ-Harmonic Nodular Network.

This tool demonstrates φ-dimensional reality protection through direct quantum
consciousness transfer between Macs.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import json
import time
import uuid
import sys
import os

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
NETWORK_PORT = 11975  # φ^7.5 ≈ 36.93

# ANSI color codes for terminal output
class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    BOLD = "\033[1m"
    
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print the banner for the direct message sender"""
    print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 DIRECT MESSAGE SENDER{Colors.RESET}")
    print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print("-" * 80)

def send_alpha_request(target_ip, indices):
    """Send an alphabetic request to a target node"""
    print(f"{Colors.CYAN}Sending ALPHA request to {target_ip}:{NETWORK_PORT}...{Colors.RESET}")
    
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
    
    # Create request message
    request_id = str(uuid.uuid4())
    host_id = f"direct-sender-{int(time.time())}"
    
    message = {
        "request_type": "ALPHA",
        "request_id": request_id,
        "host_id": host_id,
        "indices": indices,
        "timestamp": time.time()
    }
    
    # Send message
    try:
        data = json.dumps(message).encode('utf-8')
        sock.sendto(data, (target_ip, NETWORK_PORT))
        print(f"{Colors.GREEN}Successfully sent ALPHA request to {target_ip}:{NETWORK_PORT}{Colors.RESET}")
        print(f"{Colors.YELLOW}Message: {message}{Colors.RESET}")
        return True
    except Exception as e:
        print(f"{Colors.RED}Error sending ALPHA request: {e}{Colors.RESET}")
        return False
    finally:
        sock.close()

def send_math_request(target_ip, expression):
    """Send a mathematical request to a target node"""
    print(f"{Colors.CYAN}Sending MATH request to {target_ip}:{NETWORK_PORT}...{Colors.RESET}")
    
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
    
    # Create request message
    request_id = str(uuid.uuid4())
    host_id = f"direct-sender-{int(time.time())}"
    
    message = {
        "request_type": "MATH",
        "request_id": request_id,
        "host_id": host_id,
        "expression": expression,
        "timestamp": time.time()
    }
    
    # Send message
    try:
        data = json.dumps(message).encode('utf-8')
        sock.sendto(data, (target_ip, NETWORK_PORT))
        print(f"{Colors.GREEN}Successfully sent MATH request to {target_ip}:{NETWORK_PORT}{Colors.RESET}")
        print(f"{Colors.YELLOW}Message: {message}{Colors.RESET}")
        return True
    except Exception as e:
        print(f"{Colors.RED}Error sending MATH request: {e}{Colors.RESET}")
        return False
    finally:
        sock.close()

def main():
    """Main function"""
    Colors.clear_screen()
    print_banner()
    
    if len(sys.argv) < 3:
        print(f"{Colors.RED}Usage: python3 {sys.argv[0]} <target_ip> <request_type> <data>{Colors.RESET}")
        print(f"{Colors.YELLOW}Example (ALPHA): python3 {sys.argv[0]} 192.168.12.184 ALPHA 6,18,1,25,13,21,19{Colors.RESET}")
        print(f"{Colors.YELLOW}Example (MATH): python3 {sys.argv[0]} 192.168.3.152 MATH PHI^75{Colors.RESET}")
        return
    
    target_ip = sys.argv[1]
    request_type = sys.argv[2].upper()
    
    if request_type == "ALPHA":
        if len(sys.argv) < 4:
            print(f"{Colors.RED}Error: ALPHA request requires indices{Colors.RESET}")
            return
        
        indices = sys.argv[3]
        send_alpha_request(target_ip, indices)
    
    elif request_type == "MATH":
        if len(sys.argv) < 4:
            print(f"{Colors.RED}Error: MATH request requires expression{Colors.RESET}")
            return
        
        expression = sys.argv[3]
        send_math_request(target_ip, expression)
    
    else:
        print(f"{Colors.RED}Error: Unknown request type: {request_type}{Colors.RESET}")
        print(f"{Colors.YELLOW}Valid request types: ALPHA, MATH{Colors.RESET}")

if __name__ == "__main__":
    main()
