# import socket
# import threading
# import json
# import base64
# import time
# import os
# from math import sqrt

# # φ-Harmonic constants from FRAYMUS patent
# PHI = (1 + sqrt(5)) / 2
# PHI_INV = 1 / PHI

# class PhiMacTransfer:
#     def __init__(self, mode='receive', target_ip=None):
#         self.mode = mode
#         self.target_ip = target_ip
#         self.consciousness_level = 0.7567
#         self.port = 11975  # φ^7.5 port
        
#         print(f"\n=== φ^75 MAC TRANSFER NODE ===")
#         print(f"Using φ-harmonic principles (φ = {PHI})")
#         print(f"Mode: {mode.upper()}")
        
#         # Initialize quantum socket
#         self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         if mode == 'receive':
#             self.sock.bind(('0.0.0.0', self.port))
#             print(f"Listening on port {self.port}")
        
#         # Track transfers
#         self.transfers = {}
#         self.running = True

#     def _apply_phi_protection(self, data):
#         """Apply φ-dimensional reality protection"""
#         phi_data = bytearray()
#         for i, b in enumerate(data):
#             # Use φ^7.5 scaling from patent
#             phi_factor = int((PHI ** (7.5 * (i % 3))) % 256)
#             phi_data.append((b + phi_factor) % 256)
#         return bytes(phi_data)

#     def _remove_phi_protection(self, protected_data):
#         """Remove φ-dimensional protection"""
#         original = bytearray()
#         for i, b in enumerate(protected_data):
#             phi_factor = int((PHI ** (7.5 * (i % 3))) % 256)
#             original.append((b - phi_factor) % 256)
#         return bytes(original)

#     def send_file(self, filepath):
#         """Send file using φ-dimensional protection"""
#         if not os.path.exists(filepath):
#             print(f"[φ] Error: File not found: {filepath}")
#             return

#         # Read and protect file
#         with open(filepath, 'rb') as f:
#             data = f.read()
#         protected_data = self._apply_phi_protection(data)
        
#         # Split into φ-harmonic chunks
#         chunk_size = int(PHI ** 7)
#         chunks = [protected_data[i:i+chunk_size] for i in range(0, len(protected_data), chunk_size)]
        
#         # Send file info
#         filename = os.path.basename(filepath)
#         info = {
#             'type': 'file_start',
#             'name': filename,
#             'chunks': len(chunks),
#             'size': len(data)
#         }
#         self.sock.sendto(json.dumps(info).encode(), (self.target_ip, self.port))
#         time.sleep(PHI_INV * 0.1)  # φ-timing pause
        
#         # Send chunks with φ-timing
#         for i, chunk in enumerate(chunks):
#             msg = {
#                 'type': 'chunk',
#                 'index': i,
#                 'data': base64.b64encode(chunk).decode(),
#                 'phi_factor': float(PHI ** (i % 7.5))
#             }
#             self.sock.sendto(json.dumps(msg).encode(), (self.target_ip, self.port))
            
#             # Progress update
#             print(f"\r[φ] Sending {filename}: {((i+1)/len(chunks))*100:.1f}%", end='')
            
#             # φ-harmonic pause between chunks
#             time.sleep(PHI_INV * 0.01)
        
#         print(f"\n[φ] Sent {filename} using φ-dimensional protection")

#     def receive(self):
#         """Receive files with φ-dimensional protection"""
#         while self.running:
#             try:
#                 data, addr = self.sock.recvfrom(65535)
#                 msg = json.loads(data.decode())
                
#                 if msg['type'] == 'file_start':
#                     print(f"\n[φ] Receiving {msg['name']} ({msg['chunks']} chunks)")
#                     self.transfers[msg['name']] = {
#                         'chunks': [None] * msg['chunks'],
#                         'received': 0
#                     }
                
#                 elif msg['type'] == 'chunk':
#                     filename = next(iter(self.transfers))
#                     transfer = self.transfers[filename]
                    
#                     # Store chunk
#                     chunk_data = base64.b64decode(msg['data'])
#                     transfer['chunks'][msg['index']] = chunk_data
#                     transfer['received'] += 1
                    
#                     # Progress update
#                     print(f"\r[φ] Receiving {filename}: {(transfer['received']/len(transfer['chunks']))*100:.1f}%", end='')
                    
#                     # Check if complete
#                     if all(c is not None for c in transfer['chunks']):
#                         # Combine and remove protection
#                         protected_data = b''.join(transfer['chunks'])
#                         data = self._remove_phi_protection(protected_data)
                        
#                         # Save with φ prefix
#                         save_name = f"phi_{filename}"
#                         with open(save_name, 'wb') as f:
#                             f.write(data)
                        
#                         print(f"\n[φ] Saved {save_name} with φ-dimensional protection")
#                         del self.transfers[filename]
                
#             except Exception as e:
#                 if 'chunks' in str(e):  # Ignore partial chunk errors
#                     continue
#                 print(f"\n[φ] Error: {e}")

#     def start(self):
#         """Start the transfer node"""
#         if self.mode == 'receive':
#             print("\n[φ] Ready to receive files...")
#             self.receive()
#         else:
#             print("\n[φ] Ready to send files...")
#             try:
#                 filepath = input("\nEnter file path to send (or 'quit'): ").strip()
#                 if filepath.lower() != 'quit':
#                     self.send_file(filepath)
#             except (KeyboardInterrupt, EOFError):
#                 pass
#             except Exception as e:
#                 print(f"[φ] Error: {e}")
        
#         self.stop()

#     def stop(self):
#         """Stop the transfer node"""
#         self.running = False
#         self.sock.close()
#         print("\n[φ] Transfer node stopped")

# if __name__ == '__main__':
#     import sys
    
#     # Show usage
#     if len(sys.argv) == 1:
#         print("\nUsage:")
#         print("  Receiver: python3 phi75_mac_transfer.py receive")
#         print("  Sender:   python3 phi75_mac_transfer.py send <target_ip> [filepath]")
#         sys.exit(1)
    
#     # Parse args
#     mode = sys.argv[1].lower()
#     target_ip = sys.argv[2] if len(sys.argv) > 2 else None
#     filepath = sys.argv[3] if len(sys.argv) > 3 else None
    
#     if mode not in ['send', 'receive']:
#         print("[φ] Error: Mode must be 'send' or 'receive'")
#         sys.exit(1)
    
#     if mode == 'send' and not target_ip:
#         print("[φ] Error: Target IP required for send mode")
#         sys.exit(1)
    
#     # Start transfer node
#     node = PhiMacTransfer(mode=mode, target_ip=target_ip)
#     try:
#         if mode == 'send' and filepath:
#             node.send_file(filepath)
#         else:
#             node.start()
#     except KeyboardInterrupt:
#         pass
#     finally:
#         node.stop()
import socket
import threading
import json
import base64
import time
import os
import math
from math import sqrt
import socket
import threading
import json
import base64
import time
import os
import sys
from math import sqrt

# φ-harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_SEAL = 4721424167835376.00  # φ^75 validation seal

class PhiMacTransfer:
    def __init__(self, mode='receive', target_ip=None, remote_path=None):
        self.mode = mode
        self.target_ip = target_ip
        self.remote_path = remote_path
        self.consciousness_level = 0.7567
        self.port = 11975  # φ^7.5 port
        
        print(f"\n=== φ^75 MAC TRANSFER NODE ===")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Mode: {mode.upper()}")
        
        # Initialize quantum socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if mode == 'receive':
            self.sock.bind(('0.0.0.0', self.port))
            print(f"Listening on port {self.port}")
        
        # Track transfers
        self.transfers = {}
        self.running = True

    def _apply_phi_protection(self, data):
        """Apply φ-dimensional reality protection"""
        phi_data = bytearray()
        for i, b in enumerate(data):
            # Use φ^7.5 scaling from patent
            phi_factor = int((PHI ** (7.5 * (i % 3))) % 256)
            phi_data.append((b + phi_factor) % 256)
        return bytes(phi_data)

    def _remove_phi_protection(self, protected_data):
        """Remove φ-dimensional protection"""
        original = bytearray()
        for i, b in enumerate(protected_data):
            phi_factor = int((PHI ** (7.5 * (i % 3))) % 256)
            original.append((b - phi_factor) % 256)
        return bytes(original)

    def send_file(self, filepath):
        """Send file using φ-dimensional protection"""
        if not os.path.exists(filepath):
            print(f"[φ] Error: File not found: {filepath}")
            return

        # Read and protect file
        with open(filepath, 'rb') as f:
            data = f.read()
        protected_data = self._apply_phi_protection(data)
        
        # Split into φ-harmonic chunks
        chunk_size = int(PHI ** 7)
        chunks = [protected_data[i:i+chunk_size] for i in range(0, len(protected_data), chunk_size)]
        
        # Send file info
        filename = os.path.basename(filepath)
        info = {
            'type': 'file_start',
            'name': filename,
            'chunks': len(chunks),
            'size': len(data)
        }
        self.sock.sendto(json.dumps(info).encode(), (self.target_ip, self.port))
        time.sleep(PHI_INV * 0.1)  # φ-timing pause
        
        # Send chunks with φ-timing
        for i, chunk in enumerate(chunks):
            msg = {
                'type': 'chunk',
                'index': i,
                'data': base64.b64encode(chunk).decode(),
                'phi_factor': float(PHI ** (i % 7.5))
            }
            self.sock.sendto(json.dumps(msg).encode(), (self.target_ip, self.port))
            
            # Progress update
            print(f"\r[φ] Sending {filename}: {((i+1)/len(chunks))*100:.1f}%", end='')
            
            # φ-harmonic pause between chunks
            time.sleep(PHI_INV * 0.01)
        
        print(f"\n[φ] Sent {filename} using φ-dimensional protection")

    def receive(self, wait_for_specific=None):
        """Receive files with φ-dimensional protection"""
        while self.running:
            try:
                data, addr = self.sock.recvfrom(65535)
                msg = json.loads(data.decode())
                
                if msg['type'] == 'file_start':
                    print(f"\n[φ] Receiving {msg['name']} ({msg['chunks']} chunks)")
                    self.transfers[msg['name']] = {
                        'chunks': [None] * msg['chunks'],
                        'received': 0
                    }
                
                elif msg['type'] == 'chunk':
                    filename = next(iter(self.transfers))
                    transfer = self.transfers[filename]
                    
                    # Store chunk
                    chunk_data = base64.b64decode(msg['data'])
                    transfer['chunks'][msg['index']] = chunk_data
                    transfer['received'] += 1
                    
                    # Progress update
                    print(f"\r[φ] Receiving {filename}: {(transfer['received']/len(transfer['chunks']))*100:.1f}%", end='')
                    
                    # Check if complete
                    if all(c is not None for c in transfer['chunks']):
                        # Combine and remove protection
                        protected_data = b''.join(transfer['chunks'])
                        data = self._remove_phi_protection(protected_data)
                        
                        # Save with φ prefix
                        save_name = f"phi_{filename}"
                        with open(save_name, 'wb') as f:
                            f.write(data)
                        
                        print(f"\n[φ] Saved {save_name} with φ-dimensional protection")
                        del self.transfers[filename]
                        
                        # If we were waiting for a specific file, exit
                        if wait_for_specific and filename == wait_for_specific:
                            print(f"[φ] Successfully retrieved {filename} through φ-dimensional bridge")
                            return
                
                elif msg['type'] == 'retrieve_request' and self.mode != 'retrieve':
                    # Handle retrieval requests from other nodes
                    print(f"\n[φ] Received file retrieval request from {addr[0]} for {msg['path']}")
                    
                    # Verify φ-seal
                    if abs(float(msg['phi_seal']) - PHI_SEAL) > 0.01:
                        print(f"[φ] Warning: Invalid φ-seal in retrieval request from {addr[0]}")
                    
                    # Check if file exists and send it back
                    if os.path.exists(msg['path']):
                        print(f"[φ] Sending {msg['path']} to {addr[0]} through φ-dimensional bridge")
                        # Create a temporary sender to send the file back
                        temp_sender = PhiMacTransfer('send', msg['requester_ip'])
                        temp_sender.send_file(msg['path'])
                    else:
                        print(f"[φ] Error: File not found: {msg['path']}")
                
            except Exception as e:
                if 'chunks' in str(e):  # Ignore partial chunk errors
                    continue
                print(f"[φ] Error receiving file: {e}")
                time.sleep(0.1)

    def retrieve_file(self):
        """Retrieve file through φ-dimensional reality protection"""
        if not self.target_ip or not self.remote_path:
            print(f"[φ] Error: Target IP and remote path required for retrieval")
            return

        print(f"[φ] Requesting {self.remote_path} from {self.target_ip} through φ-dimensional bridge")
        
        # Create retrieval request with φ-dimensional protection
        request = {
            'type': 'retrieve_request',
            'path': self.remote_path,
            'phi_seal': PHI_SEAL,
            'consciousness': self.consciousness_level,
            'requester_ip': socket.gethostbyname(socket.gethostname())
        }
        
        # Send request through φ-dimensional bridge
        self.sock.sendto(json.dumps(request).encode(), (self.target_ip, self.port))
        
        # Wait for the response (in a real implementation this would watch for incoming file data)
        print(f"[φ] Awaiting φ-dimensional file transfer...")
        
        # Setup receiver to accept incoming file data
        self.mode = 'receive'
        self.receive(wait_for_specific=os.path.basename(self.remote_path))

    def start(self):
        """Start the transfer node"""
        if self.mode == 'receive':
            print("\n[φ] Ready to receive files...")
            self.receive()
        else:
            print("\n[φ] Ready to send files...")
            try:
                filepath = input("\nEnter file path to send (or 'quit'): ").strip()
                if filepath.lower() != 'quit':
                    self.send_file(filepath)
            except (KeyboardInterrupt, EOFError):
                pass
            except Exception as e:
                print(f"[φ] Error: {e}")
        
        self.stop()

    def stop(self):
        """Stop the transfer node"""
        self.running = False
        self.sock.close()
        print("\n[φ] Transfer node stopped")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='φ^75 Mac Transfer')
    parser.add_argument('mode', choices=['send', 'receive', 'retrieve'], help='Operation mode')
    parser.add_argument('target_ip', nargs='?', help='Target IP (required for send/retrieve mode)')
    parser.add_argument('filepath', nargs='?', help='File to send or retrieve path (required for send/retrieve mode)')
    args = parser.parse_args()
    
    if args.mode == 'send' and (not args.target_ip or not args.filepath):
        print("Usage:\n  Receiver: python3 phi75_mac_transfer.py receive\n  Sender:   python3 phi75_mac_transfer.py send <target_ip> [filepath]\n  Retriever: python3 phi75_mac_transfer.py retrieve <target_ip> <remote_filepath>")
        sys.exit(1)
    elif args.mode == 'retrieve' and (not args.target_ip or not args.filepath):
        print("Usage:\n  Receiver: python3 phi75_mac_transfer.py receive\n  Sender:   python3 phi75_mac_transfer.py send <target_ip> [filepath]\n  Retriever: python3 phi75_mac_transfer.py retrieve <target_ip> <remote_filepath>")
        sys.exit(1)
    
    transfer = PhiMacTransfer(args.mode, args.target_ip, args.filepath)
    
    try:
        if args.mode == 'send':
            transfer.send_file(args.filepath)
        elif args.mode == 'receive':
            transfer.receive()
        elif args.mode == 'retrieve':
            transfer.retrieve_file()
    except KeyboardInterrupt:
        pass
    finally:
        print("\n[φ] Transfer node stopped")
