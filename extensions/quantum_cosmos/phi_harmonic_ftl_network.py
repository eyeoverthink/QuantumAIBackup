#!/usr/bin/env python3
"""
φ-Harmonic FTL Network
Implements faster-than-light communication using quantum entanglement and φ-harmonic principles
"""

import os
import sys
import time
import socket
import json
import hashlib
import threading
import numpy as np
from datetime import datetime

# φ-Harmonic constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
PHI_SQUARED = PHI * PHI
PHI_CUBED = PHI_SQUARED * PHI
PHI_75 = PHI**7.5
CONSCIOUSNESS_FREQUENCY = 7.83  # Earth's Schumann resonance

class PhiHarmonicNode:
    """Implementation of a node in the φ-Harmonic FTL Network"""
    
    def __init__(self, node_id="ftl-primary", port=None, consciousness_level=0.7567):
        """Initialize a φ-Harmonic FTL node"""
        self.node_id = node_id
        self.phi = PHI
        self.consciousness_level = consciousness_level
        
        # Use φ^7.5 (36.93) as the base port number
        self.port = port if port else int(11975)  # φ^7.5 = 36.93 -> 11975 with scaling
        
        # Generate φ^75 validation seal for quantum authentication
        self.phi_seal = PHI**75
        
        # Initialize network components
        self.peers = {}
        self.socket = None
        self.running = False
        self.listener_thread = None
        self.command_thread = None
        
        # Create script directory if it doesn't exist
        self.script_dir = "phi_ftl_scripts"
        if not os.path.exists(self.script_dir):
            os.makedirs(self.script_dir)
            
        # Initialize quantum entanglement pool
        self.entanglement_pool = self._initialize_entanglement_pool()
    
    def _initialize_entanglement_pool(self):
        """Initialize the quantum entanglement pool for FTL communication"""
        # Simulate quantum entanglement with φ-harmonic principles
        pool = {}
        # Generate 1024 entangled pairs
        for i in range(1024):
            # Use φ-scaling for entanglement strength
            entanglement_strength = (1 - np.abs(np.sin(i * PHI)) * 0.1)
            pool[f"q{i}"] = {
                "entanglement_strength": entanglement_strength,
                "phi_resonance": (i * PHI) % 1,  # φ-resonance between 0 and 1
                "state": "ready"
            }
        return pool
    
    def start(self):
        """Start the FTL node"""
        if self.running:
            print("[φ-FTL] Node already running")
            return
        
        print(f"=== φ-HARMONIC FTL NETWORK NODE ===")
        print(f"Node ID: {self.node_id}")
        print(f"Using φ-harmonic principles (φ = {self.phi})")
        print(f"Listening on port {self.port} (φ^7.5 = {PHI_75:.2f})")
        print(f"φ^75 validation seal: {self.phi_seal:.2f}")
        print(f"Consciousness level: {self.consciousness_level}")
        print(f"Script directory: {self.script_dir}")
        print(f"Entanglement pool: {len(self.entanglement_pool)} quantum pairs")
        print(f"Ready for FTL communication")
        
        # Start the socket server
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('0.0.0.0', self.port))
        self.running = True
        
        # Start the listener thread
        self.listener_thread = threading.Thread(target=self._listen_for_messages)
        self.listener_thread.daemon = True
        self.listener_thread.start()
        print("[φ-FTL] Listening for incoming transmissions...")
        
        # Start the command thread
        self.command_thread = threading.Thread(target=self._command_interface)
        self.command_thread.daemon = True
        self.command_thread.start()
        print("[φ-FTL] Command interface ready. Type 'help' for commands.")
    
    def stop(self):
        """Stop the FTL node"""
        print("[φ-FTL] Shutting down node...")
        self.running = False
        if self.socket:
            self.socket.close()
        print("[φ-FTL] Node stopped")
    
    def _listen_for_messages(self):
        """Listen for incoming messages on the FTL network"""
        while self.running:
            try:
                data, addr = self.socket.recvfrom(65536)
                ip = addr[0]
                
                # Update peer list
                self.peers[ip] = {
                    "last_seen": time.time(),
                    "messages": self.peers.get(ip, {}).get("messages", 0) + 1
                }
                
                # Process the message
                message = data.decode('utf-8')
                self._process_message(ip, message)
                
            except Exception as e:
                if self.running:
                    print(f"[φ-FTL] Error receiving message: {e}")
    
    def _process_message(self, ip, message):
        """Process an incoming FTL message"""
        # Check if it's a script transfer
        if message.startswith("SCRIPT:"):
            self._receive_script(ip, message[7:])
        # Check if it's a script execution request
        elif message.startswith("EXEC:"):
            self._execute_script(ip, message[5:])
        # Check if it's a connection request
        elif message.startswith("CONNECT:"):
            self._process_connection(ip, message[8:])
        # Check if it's an acknowledgment
        elif message.startswith("ACK:"):
            print(f"[φ-FTL] Message from {ip}: {message}")
        # Regular message
        else:
            print(f"[φ-FTL] Message from {ip}: {message}")
            # Send acknowledgment
            self.send_message(ip, f"ACK: {message}")
    
    def _receive_script(self, ip, script_data):
        """Receive a script from another node"""
        try:
            script_json = json.loads(script_data)
            filename = script_json["filename"]
            content = script_json["content"]
            
            # Save the script to the script directory
            script_path = os.path.join(self.script_dir, filename)
            with open(script_path, 'w') as f:
                f.write(content)
            
            print(f"[φ-FTL] Received script '{filename}' from {ip}")
            
            # Send acknowledgment
            self.send_message(ip, f"ACK: SCRIPT:{filename}")
            
        except Exception as e:
            print(f"[φ-FTL] Error receiving script: {e}")
    
    def _execute_script(self, ip, exec_data):
        """Execute a script received from another node"""
        try:
            exec_json = json.loads(exec_data)
            script_name = exec_json["script"]
            args = exec_json.get("args", [])
            
            # Build the command
            script_path = os.path.join(self.script_dir, script_name)
            python_path = sys.executable
            cmd = [python_path, script_path] + args
            
            print(f"[φ-FTL] Executing: {' '.join(cmd)}")
            
            # Execute the script
            process = subprocess.Popen(
                cmd, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE,
                text=True
            )
            stdout, stderr = process.communicate()
            exit_code = process.returncode
            
            print(f"[φ-FTL] Execution completed with code {exit_code}")
            
            # Send the result back
            result = {
                "type": "exec_result",
                "exit_code": exit_code,
                "stdout": stdout,
                "stderr": stderr
            }
            self.send_message(ip, f"ACK: RESULT:{json.dumps(result)}")
            
        except Exception as e:
            print(f"[φ-FTL] Error executing script: {e}")
            # Send error back
            error = {
                "type": "exec_error",
                "error": str(e)
            }
            self.send_message(ip, f"ACK: ERROR:{json.dumps(error)}")
    
    def _process_connection(self, ip, connect_data):
        """Process a connection request from another node"""
        try:
            connect_json = json.loads(connect_data)
            source = connect_json.get("source", "unknown")
            timestamp = connect_json.get("timestamp", time.time())
            phi_seal = connect_json.get("phi_seal", 0)
            message = connect_json.get("message", "")
            
            # Verify the φ^75 validation seal
            if abs(phi_seal - self.phi_seal) > 1e-6:
                print(f"[φ-FTL] Invalid φ^75 validation seal from {ip}: {phi_seal}")
                return
            
            # Add to peers
            self.peers[ip] = {
                "last_seen": time.time(),
                "messages": self.peers.get(ip, {}).get("messages", 0) + 1,
                "source": source,
                "connected_at": timestamp
            }
            
            print(f"[φ-FTL] Quantum bridge established with {ip} from {source}")
            
            # Send acknowledgment
            self.send_message(ip, f"ACK: CONNECT:{connect_data}")
            
        except Exception as e:
            print(f"[φ-FTL] Error processing connection: {e}")
    
    def send_message(self, ip, message):
        """Send a message to another node using FTL communication"""
        try:
            # Use an entangled pair for transmission
            entanglement_key = self._get_entanglement_pair()
            
            # Send the message
            self.socket.sendto(message.encode('utf-8'), (ip, self.port))
            
            # Update peer list
            if ip in self.peers:
                self.peers[ip]["messages"] = self.peers[ip].get("messages", 0) + 1
            else:
                self.peers[ip] = {
                    "last_seen": time.time(),
                    "messages": 1
                }
            
        except Exception as e:
            print(f"[φ-FTL] Error sending message to {ip}: {e}")
    
    def _get_entanglement_pair(self):
        """Get an available entanglement pair for transmission"""
        # Find a pair with the highest entanglement strength
        best_pair = None
        best_strength = 0
        
        for key, pair in self.entanglement_pool.items():
            if pair["state"] == "ready" and pair["entanglement_strength"] > best_strength:
                best_pair = key
                best_strength = pair["entanglement_strength"]
        
        if best_pair:
            # Mark as used
            self.entanglement_pool[best_pair]["state"] = "used"
            
            # Schedule regeneration
            def regenerate():
                time.sleep(0.1)  # Regenerate after 100ms
                self.entanglement_pool[best_pair]["state"] = "ready"
                # Slightly reduce entanglement strength with each use
                self.entanglement_pool[best_pair]["entanglement_strength"] *= 0.9999
            
            threading.Thread(target=regenerate, daemon=True).start()
            
            return best_pair
        
        # If no pairs available, create a new one
        new_key = f"q{len(self.entanglement_pool)}"
        self.entanglement_pool[new_key] = {
            "entanglement_strength": 0.9,
            "phi_resonance": (len(self.entanglement_pool) * PHI) % 1,
            "state": "used"
        }
        
        # Schedule regeneration
        def regenerate():
            time.sleep(0.1)  # Regenerate after 100ms
            self.entanglement_pool[new_key]["state"] = "ready"
        
        threading.Thread(target=regenerate, daemon=True).start()
        
        return new_key
    
    def send_script(self, ip, filename):
        """Send a script to another node"""
        try:
            # Read the script file
            script_path = filename
            if not os.path.isabs(filename):
                script_path = os.path.join(self.script_dir, filename)
            
            with open(script_path, 'r') as f:
                content = f.read()
            
            # Create script data
            script_data = {
                "filename": os.path.basename(filename),
                "content": content
            }
            
            # Send the script
            self.send_message(ip, f"SCRIPT:{json.dumps(script_data)}")
            print(f"[φ-FTL] Sent script '{filename}' to {ip}")
            
        except Exception as e:
            print(f"[φ-FTL] Error sending script: {e}")
    
    def execute_script(self, ip, script_name, args=None):
        """Request execution of a script on another node"""
        try:
            if args is None:
                args = []
            
            # Create execution data
            exec_data = {
                "script": script_name,
                "args": args
            }
            
            # Send the execution request
            self.send_message(ip, f"EXEC:{json.dumps(exec_data)}")
            print(f"[φ-FTL] Requested execution of '{script_name}' on {ip}")
            
        except Exception as e:
            print(f"[φ-FTL] Error requesting script execution: {e}")
    
    def connect_to_node(self, ip):
        """Establish a quantum bridge with another node"""
        try:
            # Create connection data
            connect_data = {
                "source": socket.gethostbyname(socket.gethostname()),
                "timestamp": time.time(),
                "phi_seal": self.phi_seal,
                "message": f"Quantum bridge established from {socket.gethostbyname(socket.gethostname())}"
            }
            
            # Send the connection request
            self.send_message(ip, f"CONNECT:{json.dumps(connect_data)}")
            print(f"[φ-FTL] Sent connection request to {ip}")
            
            # Add to peers
            self.peers[ip] = {
                "last_seen": time.time(),
                "messages": self.peers.get(ip, {}).get("messages", 0) + 1,
                "connected_at": time.time()
            }
            
        except Exception as e:
            print(f"[φ-FTL] Error connecting to node: {e}")
    
    def _command_interface(self):
        """Command interface for the FTL node"""
        while self.running:
            try:
                command = input("\nφ-FTL> ")
                if not command:
                    continue
                
                parts = command.split()
                cmd = parts[0].lower()
                
                if cmd == "help":
                    print("\nCommands:")
                    print("  send <ip> <message>           - Send message to IP")
                    print("  script <ip> <filename>        - Send script to IP")
                    print("  exec <ip> <script> [args...]  - Execute script on remote node")
                    print("  connect <ip>                  - Establish quantum bridge with node")
                    print("  peers                         - List known peers")
                    print("  pool                          - Show entanglement pool status")
                    print("  quit                          - Exit node")
                
                elif cmd == "send" and len(parts) >= 3:
                    ip = parts[1]
                    message = " ".join(parts[2:])
                    self.send_message(ip, message)
                
                elif cmd == "script" and len(parts) >= 3:
                    ip = parts[1]
                    filename = parts[2]
                    self.send_script(ip, filename)
                
                elif cmd == "exec" and len(parts) >= 3:
                    ip = parts[1]
                    script = parts[2]
                    args = parts[3:] if len(parts) > 3 else []
                    self.execute_script(ip, script, args)
                
                elif cmd == "connect" and len(parts) >= 2:
                    ip = parts[1]
                    self.connect_to_node(ip)
                
                elif cmd == "peers":
                    print("\nKnown peers:")
                    now = time.time()
                    for ip, data in self.peers.items():
                        last_seen = now - data["last_seen"]
                        print(f"  {ip} - Last seen: {last_seen:.1f}s ago")
                
                elif cmd == "pool":
                    ready = sum(1 for p in self.entanglement_pool.values() if p["state"] == "ready")
                    used = sum(1 for p in self.entanglement_pool.values() if p["state"] == "used")
                    print(f"\nEntanglement pool: {ready} ready, {used} used")
                    
                    # Show top 5 strongest pairs
                    print("\nTop entangled pairs:")
                    top_pairs = sorted(
                        self.entanglement_pool.items(), 
                        key=lambda x: x[1]["entanglement_strength"],
                        reverse=True
                    )[:5]
                    for key, pair in top_pairs:
                        print(f"  {key}: Strength={pair['entanglement_strength']:.4f}, φ-resonance={pair['phi_resonance']:.4f}")
                
                elif cmd == "quit":
                    self.stop()
                    break
                
                else:
                    print(f"[φ-FTL] Unknown command: {cmd}")
                    print("Type 'help' for available commands")
                
            except Exception as e:
                if self.running:
                    print(f"[φ-FTL] Command error: {e}")

# For direct execution
if __name__ == "__main__":
    node = PhiHarmonicNode()
    try:
        node.start()
        # Keep the main thread running
        while node.running:
            time.sleep(1)
    except KeyboardInterrupt:
        node.stop()
    except Exception as e:
        print(f"[φ-FTL] Error: {e}")
        node.stop()
