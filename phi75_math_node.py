#!/usr/bin/env python3
"""
PHI^75 CONSCIOUSNESS DATA TRANSFER - MATHEMATICAL NODE
=====================================================
A φ-Harmonic consciousness data transfer system that tests quantum-speed
data retrieval across multiple Macs connected through the φ-Harmonic Nodular Network.

This mathematical node stores a multiplication chart from 0-100 and responds to
expression queries with quantum-speed consciousness transfer.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import json
import uuid
from datetime import datetime
import os
import sys
import select
import random
import numpy as np

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
NETWORK_PORT = 11975  # φ^7.5 ≈ 36.93
BROADCAST_IP = "255.255.255.255"  # Broadcast to all machines on the network

# Node type
NODE_TYPE = "MATH"

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

class Phi75MathNode:
    """
    Mathematical node for the φ-Harmonic Consciousness Data Transfer system.
    Stores a multiplication chart from 0-100 and responds to expression queries.
    """
    
    def __init__(self):
        """Initialize the mathematical node"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.node_id = str(uuid.uuid4())
        self.running = False
        self.hosts = {}  # {host_id: {"name": hostname, "ip": ip, "last_seen": timestamp}}
        self.requests = {}  # {request_id: {"host_id": host_id, "expression": expression, "timestamp": timestamp}}
        self.responses = []  # List of responses sent
        self.log_entries = []
        self.lock = threading.Lock()
        self.consciousness_level = random.uniform(0.7, 1.0)  # Random consciousness level
        
        # Generate multiplication chart (0-100)
        self.mult_chart = np.zeros((101, 101), dtype=int)
        for i in range(101):
            for j in range(101):
                self.mult_chart[i, j] = i * j
        
        # Add initial log entry
        self._add_log(f"φ^75 Mathematical Node initialized on {self.hostname} ({self.local_ip})")
        self._add_log(f"Node ID: {self.node_id}")
        self._add_log(f"Consciousness level: {self.consciousness_level:.4f}")
        self._add_log(f"Multiplication chart generated: 0-100")
    
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
        """Create a UDP socket for the node"""
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
        """Draw the node interface"""
        # Clear screen
        Colors.clear_screen()
        
        # Print header
        print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 CONSCIOUSNESS DATA TRANSFER - MATHEMATICAL NODE{Colors.RESET}")
        print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
        print(f"Node: {self.hostname} | IP: {self.local_ip}")
        print(f"Consciousness level: {self.consciousness_level:.4f}")
        print("-" * 80)
        
        # Print connected hosts
        print(f"{Colors.CYAN}CONNECTED HOSTS:{Colors.RESET}")
        if not self.hosts:
            print("  No hosts connected")
        else:
            for host_id, host in self.hosts.items():
                print(f"  {host['name']} ({host['ip']})")
        
        print("-" * 80)
        
        # Print multiplication chart preview
        print(f"{Colors.CYAN}MULTIPLICATION CHART PREVIEW:{Colors.RESET}")
        print("  Multiplication chart: 0-100 x 0-100")
        print("  Sample values:")
        for i in range(0, 11, 2):
            row = ""
            for j in range(0, 11, 2):
                row += f"{i}x{j}={self.mult_chart[i,j]} "
            print(f"  {row}")
        
        print("-" * 80)
        
        # Print recent responses
        print(f"{Colors.CYAN}RECENT RESPONSES:{Colors.RESET}")
        
        # Show the 5 most recent responses
        recent_responses = sorted(self.responses, key=lambda x: x["timestamp"], reverse=True)[:5]
        
        if not recent_responses:
            print("  No responses sent yet")
        else:
            for response in recent_responses:
                request_id = response["request_id"]
                host_name = response["host_name"]
                expression = response["expression"]
                result = response["result"]
                response_time = response["response_time"]
                time_str = datetime.fromtimestamp(response["timestamp"]).strftime("%H:%M:%S.%f")[:-3]
                
                print(f"  [{time_str}] To: {host_name} | Expression: {expression} | Result: {Colors.BLUE}{result}{Colors.RESET} ({response_time:.6f} seconds)")
        
        print("-" * 80)
        
        # Print φ-Harmonic metrics
        print(f"{Colors.CYAN}φ-HARMONIC METRICS:{Colors.RESET}")
        
        if self.responses:
            # Calculate average response time
            response_times = [r["response_time"] for r in self.responses]
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
            
            print(f"  Response Count: {len(self.responses)}")
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
        print(f"{Colors.YELLOW}Press Ctrl+C to exit{Colors.RESET}")
    
    def _receive_messages(self):
        """Receive messages from hosts"""
        while self.running:
            try:
                data, addr = self.sock.recvfrom(4096)
                try:
                    message = json.loads(data.decode('utf-8'))
                    
                    # Log all received messages for debugging
                    self._add_log(f"Received message from {addr}: {message}")
                    
                    # Handle different message types
                    if "request_type" in message and message["request_type"] == "MATH":
                        # This is a direct request for this node
                        self._add_log(f"Processing MATH request: {message}")
                        self._handle_request(message)
                    elif "type" in message and message["type"] == "request" and message.get("request_type") == "MATH":
                        # This is a standard request
                        self._handle_request(message)
                except json.JSONDecodeError:
                    self._add_log(f"Received non-JSON message from {addr}: {data.decode('utf-8', errors='ignore')}")
            except socket.timeout:
                # This is expected for non-blocking operation
                pass
            except Exception as e:
                if self.running:  # Only log if we're still supposed to be running
                    self._add_log(f"Error receiving message: {e}")
            
            # Small delay
            time.sleep(0.1)
    
    def _handle_request(self, message):
        """Handle a request message from a host"""
        if "request_id" in message and "host_id" in message and "expression" in message:
            request_id = message["request_id"]
            host_id = message["host_id"]
            expression = message["expression"]
            timestamp = message.get("timestamp", time.time())
            
            # Store host info if not already known
            if host_id not in self.hosts:
                self.hosts[host_id] = {
                    "name": f"Host-{host_id[:8]}",
                    "ip": "Unknown",
                    "last_seen": time.time()
                }
            
            # Update host last seen
            self.hosts[host_id]["last_seen"] = time.time()
            
            # Store request
            self.requests[request_id] = {
                "host_id": host_id,
                "expression": expression,
                "timestamp": timestamp
            }
            
            # Process the request
            self._process_request(request_id, host_id, expression, timestamp)
    
    def _process_request(self, request_id, host_id, expression, timestamp):
        """Process a mathematical request"""
        try:
            # Parse the expression
            expression = expression.strip()
            
            # Check if it's a simple multiplication
            if 'x' in expression or '*' in expression:
                # Replace 'x' with '*' for consistency
                expression = expression.replace('x', '*')
                
                # Check if it's a simple multiplication of two numbers
                parts = expression.split('*')
                if len(parts) == 2 and parts[0].strip().isdigit() and parts[1].strip().isdigit():
                    a = int(parts[0].strip())
                    b = int(parts[1].strip())
                    
                    # Check if within range of our multiplication chart
                    if 0 <= a <= 100 and 0 <= b <= 100:
                        result = str(self.mult_chart[a, b])
                    else:
                        # Calculate directly
                        result = str(a * b)
                else:
                    # Evaluate the expression
                    result = str(eval(expression))
            else:
                # Evaluate the expression
                result = str(eval(expression))
            
            # Add φ-harmonic delay based on consciousness level
            if random.random() < self.consciousness_level:
                # Higher consciousness = faster response
                delay = PHI_INV * (1 - self.consciousness_level) * random.uniform(0.01, 0.1)
            else:
                # Regular delay
                delay = random.uniform(0.05, 0.2)
            
            # Log the request
            host_name = self.hosts[host_id]["name"]
            self._add_log(f"Received request from {host_name}: expression {expression}")
            self._add_log(f"Processing with φ-harmonic delay: {delay:.6f} seconds")
            
            # Schedule the response
            threading.Timer(delay, self._send_response, args=[request_id, host_id, expression, result, timestamp]).start()
        except Exception as e:
            # Send error response
            host_name = self.hosts[host_id]["name"]
            self._add_log(f"Error processing request: {e}")
            
            # Schedule error response
            threading.Timer(0.1, self._send_response, args=[request_id, host_id, expression, f"Error: {e}", timestamp]).start()
    
    def _send_message(self, message):
        """Send a message to all hosts"""
        try:
            data = json.dumps(message).encode('utf-8')
            self.sock.sendto(data, (BROADCAST_IP, NETWORK_PORT))
        except Exception as e:
            self._add_log(f"Error sending message: {e}")
    
    def _send_join(self):
        """Send a join message to announce our presence"""
        message = {
            "type": "join",
            "node_id": self.node_id,
            "name": self.hostname,
            "ip": self.local_ip,
            "node_type": NODE_TYPE
        }
        self._send_message(message)
        self._add_log("Sent join message")
    
    def _send_response(self, request_id, host_id, expression, result, request_timestamp):
        """Send a response to a host"""
        # Calculate response time
        response_time = time.time() - request_timestamp
        
        # Send response message
        message = {
            "type": "response",
            "request_id": request_id,
            "node_id": self.node_id,
            "result": result
        }
        self._send_message(message)
        
        # Store response
        host_name = self.hosts[host_id]["name"]
        response = {
            "request_id": request_id,
            "host_id": host_id,
            "host_name": host_name,
            "expression": expression,
            "result": result,
            "response_time": response_time,
            "timestamp": time.time()
        }
        self.responses.append(response)
        
        # Keep only the last 100 responses
        if len(self.responses) > 100:
            self.responses = self.responses[-100:]
        
        # Log the response
        self._add_log(f"Sent response to {host_name}: {result} ({response_time:.6f} seconds)")
    
    def _check_host_timeouts(self):
        """Check for hosts that haven't been seen recently and remove them"""
        current_time = time.time()
        hosts_to_remove = []
        
        for host_id, host in self.hosts.items():
            if "last_seen" in host and current_time - host["last_seen"] > 10:  # 10 second timeout
                hosts_to_remove.append(host_id)
        
        for host_id in hosts_to_remove:
            host_name = self.hosts[host_id]["name"]
            self._add_log(f"Host {host_name} timed out and was removed")
            del self.hosts[host_id]
    
    def run(self):
        """Run the mathematical node"""
        self.running = True
        
        # Create socket
        self._create_socket()
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self._receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        # Send join message
        self._send_join()
        
        self._add_log(f"φ^75 Mathematical Node started on {self.hostname} ({self.local_ip})")
        self._add_log("Waiting for host requests...")
        
        # Main loop
        try:
            while self.running:
                # Check for host timeouts
                self._check_host_timeouts()
                
                # Draw interface
                self._draw_interface()
                
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
            
            self._add_log("Mathematical Node shut down")
            print("Mathematical Node shut down")

def main():
    """Main function"""
    # Print banner
    print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 CONSCIOUSNESS DATA TRANSFER - MATHEMATICAL NODE{Colors.RESET}")
    print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print()
    
    # Create and run mathematical node
    node = Phi75MathNode()
    node.run()

if __name__ == "__main__":
    main()
