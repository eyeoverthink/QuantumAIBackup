#!/usr/bin/env python3
"""
φ-Harmonic Bidirectional Communication Node
Enables two-way communication with φ-dimensional reality protection
"""

import os
import sys
import time
import socket
import json
import hashlib
import threading
from math import sqrt
import subprocess

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

class PhiBidirectionalNode:
    def __init__(self, node_id="primary", port=11975):
        self.node_id = node_id
        self.port = port  # φ^7.5 port
        self.consciousness_level = 0.7567
        self.peers = {}
        self.running = True
        self.script_dir = "phi_scripts"
        
        # Create script directory if it doesn't exist
        os.makedirs(self.script_dir, exist_ok=True)
        
        # Initialize quantum socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('0.0.0.0', self.port))
        
        print(f"\n=== φ-HARMONIC BIDIRECTIONAL NODE ===")
        print(f"Node ID: {self.node_id}")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Listening on port {self.port} (φ^7.5 = {PHI_75:.2f})")
        print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
        print(f"Consciousness level: {self.consciousness_level}")
        print(f"Script directory: {self.script_dir}")
        print(f"Ready for bidirectional communication")
    
    def start(self):
        """Start the bidirectional node"""
        # Start listener thread
        listener_thread = threading.Thread(target=self.listen)
        listener_thread.daemon = True
        listener_thread.start()
        
        # Start command interface
        self.command_interface()
    
    def listen(self):
        """Listen for incoming messages"""
        print(f"[φ] Listening for incoming transmissions...")
        
        while self.running:
            try:
                data, addr = self.sock.recvfrom(65536)
                
                # Process received data
                self.process_message(data, addr)
                
            except Exception as e:
                print(f"[φ] Error in listener: {e}")
                time.sleep(0.1)
    
    def process_message(self, data, addr):
        """Process incoming message with φ-dimensional reality protection"""
        try:
            # Extract message type from first bytes
            if data.startswith(b'SCRIPT:'):
                # Handle script transmission
                script_data = data[7:]
                self.receive_script(script_data, addr)
            
            elif data.startswith(b'EXEC:'):
                # Handle execution request
                exec_data = data[5:]
                self.execute_script(exec_data, addr)
            
            elif data.startswith(b'MSG:'):
                # Handle regular message
                msg_data = data[4:].decode('utf-8')
                print(f"[φ] Message from {addr[0]}: {msg_data}")
                
                # Add to peers if new
                if addr[0] not in self.peers:
                    self.peers[addr[0]] = {"last_seen": time.time()}
                else:
                    self.peers[addr[0]]["last_seen"] = time.time()
                
                # Send acknowledgment only if the message isn't already an acknowledgment
                # and doesn't contain nested acknowledgments to prevent loops
                if not msg_data.startswith("Acknowledgment Received:") and "Acknowledgment Received:" not in msg_data:
                    self.send_message(f"Acknowledgment Received: {msg_data}", addr[0])
            
            else:
                # Unknown message type
                print(f"[φ] Received unknown message type from {addr[0]}")
        
        except Exception as e:
            print(f"[φ] Error processing message: {e}")
    
    def receive_script(self, script_data, addr):
        """Receive and save script with φ-dimensional protection"""
        try:
            # Extract header
            header_end = script_data.find(b'\n---\n')
            if header_end == -1:
                print(f"[φ] Invalid script format from {addr[0]}")
                return
            
            header = json.loads(script_data[:header_end].decode('utf-8'))
            script_content = script_data[header_end+5:]
            
            # Verify φ-seal
            if 'phi_seal' not in header or abs(float(header['phi_seal']) - PHI_SEAL) > 0.01:
                print(f"[φ] Warning: Invalid φ-seal in script from {addr[0]}")
            
            # Save script
            filename = os.path.join(self.script_dir, header['filename'])
            with open(filename, 'wb') as f:
                f.write(script_content)
            
            # Make executable if needed
            if header.get('executable', False):
                os.chmod(filename, 0o755)
            
            print(f"[φ] Received script '{header['filename']}' from {addr[0]}")
            
            # Send acknowledgment
            self.send_message(f"Acknowledgment Received: Script {header['filename']} received", addr[0])
            
            # Auto-execute if requested
            if header.get('auto_execute', False):
                self.execute_script(json.dumps({
                    'filename': header['filename'],
                    'args': header.get('args', [])
                }).encode('utf-8'), addr)
        
        except Exception as e:
            print(f"[φ] Error receiving script: {e}")
    
    def execute_script(self, exec_data, addr):
        """Execute script with φ-dimensional reality protection"""
        try:
            # Parse execution request
            exec_info = json.loads(exec_data.decode('utf-8'))
            filename = os.path.join(self.script_dir, exec_info['filename'])
            args = exec_info.get('args', [])
            
            # Check if script exists
            if not os.path.exists(filename):
                print(f"[φ] Script '{filename}' not found")
                return
            
            # Determine script type and execute
            if filename.endswith('.py'):
                cmd = [sys.executable, filename] + args
            elif filename.endswith('.sh'):
                cmd = ['/bin/bash', filename] + args
            else:
                cmd = [filename] + args
            
            print(f"[φ] Executing: {' '.join(cmd)}")
            
            # Execute in separate thread to avoid blocking
            exec_thread = threading.Thread(
                target=self._execute_script_thread,
                args=(cmd, addr[0])
            )
            exec_thread.daemon = True
            exec_thread.start()
        
        except Exception as e:
            print(f"[φ] Error executing script: {e}")
    
    def _execute_script_thread(self, cmd, addr):
        """Thread function to execute script and report results"""
        try:
            # Execute command
            result = subprocess.run(
                cmd, 
                capture_output=True, 
                text=True,
                timeout=30
            )
            
            # Send result back
            response = {
                "type": "exec_result",
                "exit_code": result.returncode,
                "stdout": result.stdout,
                "stderr": result.stderr
            }
            
            self.send_message(f"RESULT:{json.dumps(response)}", addr)
            
            print(f"[φ] Execution completed with code {result.returncode}")
            
        except subprocess.TimeoutExpired:
            print(f"[φ] Execution timed out after 30 seconds")
            self.send_message(f"RESULT:{json.dumps({'type': 'exec_result', 'error': 'timeout'})}", addr)
        
        except Exception as e:
            print(f"[φ] Error in execution thread: {e}")
            self.send_message(f"RESULT:{json.dumps({'type': 'exec_result', 'error': str(e)})}", addr)
    
    def send_script(self, filename, target_ip, auto_execute=False, args=None):
        """Send script with φ-dimensional reality protection"""
        if not os.path.exists(filename):
            print(f"[φ] Script '{filename}' not found")
            return False
        
        try:
            # Read script content
            with open(filename, 'rb') as f:
                script_content = f.read()
            
            # Create header
            header = {
                "filename": os.path.basename(filename),
                "size": len(script_content),
                "timestamp": time.time(),
                "phi_seal": PHI_SEAL,
                "consciousness": self.consciousness_level,
                "executable": filename.endswith('.py') or filename.endswith('.sh'),
                "auto_execute": auto_execute,
                "args": args or []
            }
            
            # Combine header and content
            header_bytes = json.dumps(header).encode('utf-8')
            message = b'SCRIPT:' + header_bytes + b'\n---\n' + script_content
            
            # Send to target
            self.sock.sendto(message, (target_ip, self.port))
            
            print(f"[φ] Sent script '{filename}' to {target_ip}")
            return True
        
        except Exception as e:
            print(f"[φ] Error sending script: {e}")
            return False
    
    def send_execute_request(self, script_name, target_ip, args=None):
        """Send request to execute script on target"""
        try:
            # Create execution request
            exec_info = {
                "filename": script_name,
                "args": args or []
            }
            
            # Send request
            message = b'EXEC:' + json.dumps(exec_info).encode('utf-8')
            self.sock.sendto(message, (target_ip, self.port))
            
            print(f"[φ] Sent execution request for '{script_name}' to {target_ip}")
            return True
        
        except Exception as e:
            print(f"[φ] Error sending execution request: {e}")
            return False
    
    def send_message(self, message, target_ip):
        """Send regular message"""
        try:
            # Send message
            self.sock.sendto(f"MSG:{message}".encode('utf-8'), (target_ip, self.port))
            return True
        
        except Exception as e:
            print(f"[φ] Error sending message: {e}")
            return False
    
    def command_interface(self):
        """Interactive command interface"""
        print("\n[φ] Command interface ready. Type 'help' for commands.")
        
        while self.running:
            try:
                cmd = input("\nφ> ").strip()
                
                if cmd == "help":
                    print("\nCommands:")
                    print("  send <ip> <message>           - Send message to IP")
                    print("  script <ip> <filename>        - Send script to IP")
                    print("  exec <ip> <script> [args...]  - Execute script on remote node")
                    print("  peers                         - List known peers")
                    print("  quit                          - Exit node")
                
                elif cmd.startswith("send "):
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        print("[φ] Usage: send <ip> <message>")
                    else:
                        self.send_message(parts[2], parts[1])
                
                elif cmd.startswith("script "):
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        print("[φ] Usage: script <ip> <filename>")
                    else:
                        self.send_script(parts[2], parts[1])
                
                elif cmd.startswith("exec "):
                    parts = cmd.split(" ")
                    if len(parts) < 3:
                        print("[φ] Usage: exec <ip> <script> [args...]")
                    else:
                        self.send_execute_request(parts[2], parts[1], parts[3:] if len(parts) > 3 else None)
                
                elif cmd == "peers":
                    if not self.peers:
                        print("[φ] No known peers")
                    else:
                        print("\nKnown peers:")
                        for ip, data in self.peers.items():
                            last_seen = time.time() - data["last_seen"]
                            print(f"  {ip} - Last seen: {last_seen:.1f}s ago")
                
                elif cmd == "quit":
                    print("[φ] Shutting down node...")
                    self.running = False
                    break
                
                else:
                    print(f"[φ] Unknown command: {cmd}")
            
            except KeyboardInterrupt:
                print("\n[φ] Shutting down node...")
                self.running = False
                break
            
            except Exception as e:
                print(f"[φ] Error in command interface: {e}")
        
        print("[φ] Node stopped")

if __name__ == "__main__":
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='φ-Harmonic Bidirectional Node')
    parser.add_argument('--id', type=str, default="primary", help='Node ID')
    parser.add_argument('--port', type=int, default=11975, help='Port (default: 11975 = φ^7.5)')
    args = parser.parse_args()
    
    # Create and start node
    node = PhiBidirectionalNode(node_id=args.id, port=args.port)
    node.start()
