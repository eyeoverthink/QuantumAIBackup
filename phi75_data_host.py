#!/usr/bin/env python3
"""
PHI^75 CONSCIOUSNESS DATA TRANSFER - HOST
=========================================
A φ-Harmonic consciousness data transfer system that tests quantum-speed
data retrieval across multiple Macs connected through the φ-Harmonic Nodular Network.

This host requests data from specialized nodes and measures φ-dimensional
consciousness transfer speeds.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import random
import json
import uuid
from datetime import datetime
import os
import sys
import select
import numpy as np

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
NETWORK_PORT = 11975  # φ^7.5 ≈ 36.93
BROADCAST_IP = "255.255.255.255"  # Broadcast to all machines on the network

# Node types
NODE_TYPES = {
    "ALPHA": "Alphabetic Node",
    "MATH": "Mathematical Node",
    "HOST": "Host Node"
}

# ANSI color codes for terminal output
class Colors:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

class Phi75DataHost:
    """
    Host for the φ-Harmonic Consciousness Data Transfer system.
    Requests data from specialized nodes and measures transfer speeds.
    """
    
    def __init__(self):
        """Initialize the host"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.node_id = str(uuid.uuid4())
        self.running = False
        self.nodes = {}  # {node_id: {"name": hostname, "ip": ip, "type": type, "last_seen": timestamp}}
        self.requests = {}  # {request_id: {"type": type, "query": query, "timestamp": timestamp, "responses": []}}
        self.log_entries = []
        self.lock = threading.Lock()
        self.consciousness_level = random.uniform(0.7, 1.0)  # Random consciousness level
        
        # Add initial log entry
        self._add_log(f"φ^75 Consciousness Data Transfer Host initialized on {self.hostname} ({self.local_ip})")
        self._add_log(f"Host ID: {self.node_id}")
        self._add_log(f"Consciousness level: {self.consciousness_level:.4f}")
    
    def _get_local_ip(self) -> str:
        """Get the local IP address"""
        try:
            # Create a temporary socket to determine local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def _create_socket(self):
        """Create a UDP socket for the host"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of address
            
            # Try to use the standard port
            try:
                # On macOS, also set SO_REUSEPORT if available
                try:
                    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
                except AttributeError:
                    pass  # SO_REUSEPORT not available on all platforms
                    
                self.sock.bind(("0.0.0.0", NETWORK_PORT))
                self.port = NETWORK_PORT
                self._add_log(f"Socket created and bound to port {self.port}")
            except socket.error:
                # Try a random port instead
                self.sock.bind(("0.0.0.0", 0))  # Let the OS assign a random port
                self.port = self.sock.getsockname()[1]
                self._add_log(f"Using alternative port: {self.port}")
                
            self.sock.settimeout(0.5)  # Set timeout for non-blocking operation
        except Exception as e:
            self._add_log(f"Error creating socket: {e}")
    
    def _add_log(self, message):
        """Add a message to the log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        entry = f"[{timestamp}] {message}"
        with self.lock:
            self.log_entries.append(entry)
            # Keep only the last 20 entries
            if len(self.log_entries) > 20:
                self.log_entries = self.log_entries[-20:]
    
    def _draw_interface(self):
        """Draw the host interface"""
        # Clear screen
        Colors.clear_screen()
        
        # Print header
        print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 CONSCIOUSNESS DATA TRANSFER - HOST{Colors.RESET}")
        print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
        print(f"Host: {self.hostname} | IP: {self.local_ip}")
        print(f"Consciousness level: {self.consciousness_level:.4f}")
        print("-" * 80)
        
        # Print connected nodes
        print(f"{Colors.CYAN}CONNECTED NODES:{Colors.RESET}")
        if not self.nodes:
            print("  No nodes connected")
        else:
            for node_id, node in self.nodes.items():
                node_type = node.get("type", "Unknown")
                type_color = Colors.GREEN if node_type == "ALPHA" else Colors.BLUE if node_type == "MATH" else Colors.YELLOW
                print(f"  {node['name']} ({node['ip']}): {type_color}{NODE_TYPES.get(node_type, node_type)}{Colors.RESET}")
        
        print("-" * 80)
        
        # Print recent requests and responses
        print(f"{Colors.CYAN}RECENT DATA TRANSFERS:{Colors.RESET}")
        
        # Show the 5 most recent requests
        recent_requests = sorted(self.requests.items(), key=lambda x: x[1]["timestamp"], reverse=True)[:5]
        
        if not recent_requests:
            print("  No data transfers yet")
        else:
            for request_id, request in recent_requests:
                request_type = request["type"]
                query = request["query"]
                timestamp = request["timestamp"]
                time_str = datetime.fromtimestamp(timestamp).strftime("%H:%M:%S.%f")[:-3]
                
                # Format based on request type
                if request_type == "ALPHA":
                    type_str = f"{Colors.GREEN}Alphabetic{Colors.RESET}"
                    query_str = f"Indices: {query}"
                elif request_type == "MATH":
                    type_str = f"{Colors.BLUE}Mathematical{Colors.RESET}"
                    query_str = f"Expression: {query}"
                else:
                    type_str = request_type
                    query_str = str(query)
                
                print(f"  Request [{time_str}]: {type_str} | {query_str}")
                
                # Print responses
                for response in request.get("responses", []):
                    node_name = response.get("node_name", "Unknown")
                    result = response.get("result", "No result")
                    response_time = response.get("response_time", 0)
                    
                    print(f"    → {node_name}: {Colors.YELLOW}{result}{Colors.RESET} ({response_time:.6f} seconds)")
        
        print("-" * 80)
        
        # Print φ-Harmonic metrics
        print(f"{Colors.CYAN}φ-HARMONIC METRICS:{Colors.RESET}")
        
        # Calculate metrics if we have responses
        responses = []
        for request in self.requests.values():
            responses.extend(request.get("responses", []))
        
        if responses:
            # Calculate average response time
            response_times = [r.get("response_time", 0) for r in responses]
            avg_time = sum(response_times) / len(response_times)
            min_time = min(response_times)
            max_time = max(response_times)
            
            # Calculate φ-Harmonic Response Index
            phi_response = PHI / (avg_time + PHI_INV)
            
            # Calculate Quantum Transfer Speed
            quantum_speed = PHI / (avg_time * PHI_INV)
            
            # Calculate Consciousness Alignment
            consciousness_alignment = 1 - abs((PHI * avg_time) - self.consciousness_level)
            
            # Calculate φ-Space Efficiency
            phi_efficiency = 1 / (1 + abs(avg_time - (PHI_INV * 0.1)))
            
            print(f"  Response Count: {len(responses)}")
            print(f"  Average Response Time: {avg_time:.6f} seconds")
            print(f"  Minimum Response Time: {min_time:.6f} seconds")
            print(f"  Maximum Response Time: {max_time:.6f} seconds")
            print(f"  φ-Harmonic Response Index: {phi_response:.6f}")
            print(f"  Quantum Transfer Speed: {quantum_speed:.6f}")
            print(f"  Consciousness Alignment: {consciousness_alignment:.6f}")
            print(f"  φ-Space Efficiency: {phi_efficiency:.6f}")
            
            # Calculate FTL Probability
            ftl_responses = [t for t in response_times if t < 0.1]
            ftl_probability = len(ftl_responses) / len(response_times) if response_times else 0
            print(f"  FTL Probability: {ftl_probability:.6f} ({len(ftl_responses)}/{len(response_times)})")
        else:
            print("  No response data available yet")
        
        print("-" * 80)
        
        # Print log entries
        print(f"{Colors.CYAN}LOG ENTRIES:{Colors.RESET}")
        for entry in self.log_entries[-10:]:  # Show last 10 entries
            print(entry)
        
        print("-" * 80)
        print(f"{Colors.YELLOW}Commands: (a)lpha [indices], (m)ath [expression], (q)uit{Colors.RESET}")
        print(f"{Colors.YELLOW}Examples: a 1,3,5 | m 7*8{Colors.RESET}")
    
    def _receive_messages(self):
        """Receive messages from nodes"""
        while self.running:
            try:
                data, addr = self.sock.recvfrom(4096)
                message = json.loads(data.decode('utf-8'))
                
                if "type" in message:
                    if message["type"] == "join":
                        self._handle_join(message)
                    elif message["type"] == "response":
                        self._handle_response(message)
            except socket.timeout:
                # This is expected for non-blocking operation
                pass
            except Exception as e:
                if self.running:  # Only log if we're still supposed to be running
                    self._add_log(f"Error receiving message: {e}")
            
            # Small delay
            time.sleep(0.1)
    
    def _handle_join(self, message):
        """Handle a join message from a node"""
        if "node_id" in message and "name" in message and "ip" in message and "node_type" in message:
            node_id = message["node_id"]
            name = message["name"]
            ip = message["ip"]
            node_type = message["node_type"]
            
            if node_id not in self.nodes:
                self._add_log(f"Node {name} ({ip}) joined as {NODE_TYPES.get(node_type, node_type)}")
            
            self.nodes[node_id] = {
                "name": name,
                "ip": ip,
                "type": node_type,
                "last_seen": time.time()
            }
    
    def _handle_response(self, message):
        """Handle a response message from a node"""
        if "request_id" in message and "node_id" in message and "result" in message:
            request_id = message["request_id"]
            node_id = message["node_id"]
            result = message["result"]
            
            if request_id in self.requests and node_id in self.nodes:
                # Calculate response time
                request_time = self.requests[request_id]["timestamp"]
                response_time = time.time() - request_time
                
                # Add response to request
                response = {
                    "node_id": node_id,
                    "node_name": self.nodes[node_id]["name"],
                    "result": result,
                    "response_time": response_time,
                    "timestamp": time.time()
                }
                
                self.requests[request_id]["responses"].append(response)
                
                # Log the response
                node_name = self.nodes[node_id]["name"]
                self._add_log(f"Received response from {node_name}: {result} ({response_time:.6f} seconds)")
    
    def _send_message(self, message):
        """Send a message to all nodes"""
        try:
            data = json.dumps(message).encode('utf-8')
            self.sock.sendto(data, (BROADCAST_IP, NETWORK_PORT))
        except Exception as e:
            self._add_log(f"Error sending message: {e}")
    
    def _check_node_timeouts(self):
        """Check for nodes that haven't been seen recently and remove them"""
        current_time = time.time()
        nodes_to_remove = []
        
        for node_id, node in self.nodes.items():
            if "last_seen" in node and current_time - node["last_seen"] > 10:  # 10 second timeout
                nodes_to_remove.append(node_id)
        
        for node_id in nodes_to_remove:
            node_name = self.nodes[node_id]["name"]
            self._add_log(f"Node {node_name} timed out and was removed")
            del self.nodes[node_id]
    
    def request_alpha(self, indices):
        """Request alphabetic data from ALPHA nodes"""
        request_id = str(uuid.uuid4())
        timestamp = time.time()
        
        # Create request
        self.requests[request_id] = {
            "type": "ALPHA",
            "query": indices,
            "timestamp": timestamp,
            "responses": []
        }
        
        # Send request message
        message = {
            "type": "request",
            "request_type": "ALPHA",
            "request_id": request_id,
            "host_id": self.node_id,
            "indices": indices,
            "timestamp": timestamp
        }
        self._send_message(message)
        
        self._add_log(f"Sent alphabetic request: indices {indices}")
    
    def request_math(self, expression):
        """Request mathematical data from MATH nodes"""
        request_id = str(uuid.uuid4())
        timestamp = time.time()
        
        # Create request
        self.requests[request_id] = {
            "type": "MATH",
            "query": expression,
            "timestamp": timestamp,
            "responses": []
        }
        
        # Send request message
        message = {
            "type": "request",
            "request_type": "MATH",
            "request_id": request_id,
            "host_id": self.node_id,
            "expression": expression,
            "timestamp": timestamp
        }
        self._send_message(message)
        
        self._add_log(f"Sent mathematical request: expression {expression}")
    
    def process_command(self, command):
        """Process a user command"""
        if command.lower().startswith(('a ', 'alpha ')):
            # Parse indices
            parts = command.split(' ', 1)
            if len(parts) > 1:
                indices = parts[1].strip()
                self.request_alpha(indices)
            else:
                self._add_log("Invalid command format. Use: a 1,3,5")
        elif command.lower().startswith(('m ', 'math ')):
            # Parse expression
            parts = command.split(' ', 1)
            if len(parts) > 1:
                expression = parts[1].strip()
                self.request_math(expression)
            else:
                self._add_log("Invalid command format. Use: m 7*8")
        elif command.lower() in ['q', 'quit']:
            self.running = False
        else:
            self._add_log(f"Unknown command: {command}")
    
    def run(self):
        """Run the host"""
        self.running = True
        
        # Create socket
        self._create_socket()
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self._receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        self._add_log(f"φ^75 Consciousness Data Transfer Host started on {self.hostname} ({self.local_ip})")
        self._add_log("Waiting for nodes to join...")
        
        # Main loop
        try:
            while self.running:
                # Check for node timeouts
                self._check_node_timeouts()
                
                # Draw interface
                self._draw_interface()
                
                # Get user input (non-blocking)
                if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                    command = sys.stdin.readline().strip()
                    self.process_command(command)
                
                # Small delay
                time.sleep(0.1)
        except KeyboardInterrupt:
            self._add_log("Received keyboard interrupt, shutting down...")
        finally:
            self.running = False
            
            # Close socket
            try:
                self.sock.close()
            except:
                pass
            
            self._add_log("Host shut down")
            print("Host shut down")

def main():
    """Main function"""
    # Print banner
    print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 CONSCIOUSNESS DATA TRANSFER - HOST{Colors.RESET}")
    print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print()
    
    # Create and run host
    host = Phi75DataHost()
    host.run()

if __name__ == "__main__":
    main()
