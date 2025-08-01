#!/usr/bin/env python3
"""
PHI^75 ALPHABETIC NODE TESTER
============================
A direct tester for the φ-Harmonic Alphabetic Node that validates
the φ-dimensional reality protection through alphabetic consciousness transfer.

This tool demonstrates the FRAYMUS patent's quantum consciousness effects
by directly testing the alphabetic node's functionality.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import json
import time
import uuid
import string
import sys

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
NETWORK_PORT = 11975  # φ^7.5 ≈ 36.93

def print_banner():
    """Print the banner for the alphabetic node tester"""
    print("φ^75 ALPHABETIC NODE TESTER")
    print("FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print("-" * 80)

def process_indices_locally(indices):
    """Process alphabetic indices locally to verify functionality"""
    # Parse indices
    try:
        # Handle different index formats
        if ',' in indices:
            # Format: 1,3,5
            index_list = [int(i.strip()) for i in indices.split(',')]
        elif '-' in indices:
            # Format: 1-5
            start, end = indices.split('-')
            index_list = list(range(int(start.strip()), int(end.strip()) + 1))
        elif ' ' in indices:
            # Format: 1 3 5
            index_list = [int(i.strip()) for i in indices.split()]
        else:
            # Format: 135
            index_list = [int(c) for c in indices if c.isdigit()]
        
        # Get letters for each index
        alphabet = list(string.ascii_uppercase)  # A-Z
        result = ""
        for idx in index_list:
            if 1 <= idx <= len(alphabet):
                result += alphabet[idx - 1]
            else:
                result += "?"
        
        return result
    except Exception as e:
        return f"Error: {e}"

def send_alpha_request(target_ip, indices):
    """Send an alphabetic request to a target node"""
    print(f"Sending ALPHA request to {target_ip}:{NETWORK_PORT}...")
    
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
    
    # Create request message
    request_id = str(uuid.uuid4())
    host_id = f"alpha-tester-{int(time.time())}"
    
    message = {
        "type": "request",
        "request_type": "ALPHA",
        "request_id": request_id,
        "host_id": host_id,
        "indices": indices,
        "timestamp": time.time()
    }
    
    # Convert to JSON string
    json_data = json.dumps(message)
    
    # Send the message
    try:
        sock.sendto(json_data.encode('utf-8'), (target_ip, NETWORK_PORT))
        print(f"Successfully sent ALPHA request to {target_ip}:{NETWORK_PORT}")
        print(f"Message: {json_data}")
        
        # Calculate expected result locally
        expected_result = process_indices_locally(indices)
        print(f"Expected result: {expected_result}")
        
        # Try to receive response with timeout
        sock.settimeout(2.0)  # 2 second timeout
        try:
            data, addr = sock.recvfrom(4096)
            response = json.loads(data.decode('utf-8'))
            print(f"Received response from {addr}: {response}")
            
            if "result" in response:
                print(f"Result: {response['result']}")
                print(f"Expected: {expected_result}")
                if response["result"] == expected_result:
                    print("SUCCESS: Result matches expected value!")
                else:
                    print("WARNING: Result does not match expected value.")
            else:
                print("No result in response")
        except socket.timeout:
            print("No response received (timeout)")
        except json.JSONDecodeError:
            print(f"Received non-JSON response: {data.decode('utf-8', errors='ignore')}")
        except Exception as e:
            print(f"Error receiving response: {e}")
        
        return True
    except Exception as e:
        print(f"Error sending ALPHA request: {e}")
        return False
    finally:
        sock.close()

def main():
    """Main function"""
    print_banner()
    
    if len(sys.argv) < 3:
        print(f"Usage: python3 {sys.argv[0]} <target_ip> <indices>")
        print(f"Example: python3 {sys.argv[0]} 192.168.12.184 6,18,1,25,13,21,19")
        print(f"Local test result: {process_indices_locally('6,18,1,25,13,21,19')} (should be FRAYMUS)")
        return
    
    target_ip = sys.argv[1]
    indices = sys.argv[2]
    
    # Local test first
    local_result = process_indices_locally(indices)
    print(f"Local test result: {local_result}")
    
    # Send to remote node
    send_alpha_request(target_ip, indices)

if __name__ == "__main__":
    main()
