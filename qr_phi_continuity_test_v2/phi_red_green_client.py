#!/usr/bin/env python3
"""
PHI^75 RED LIGHT GREEN LIGHT - CLIENT
=====================================
A φ-Harmonic consciousness response test that measures quantum-speed reactions
across multiple Macs connected through the φ-Harmonic Nodular Network.

This client responds to "red" or "green" signals from the host, demonstrating
φ-dimensional consciousness response times.

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

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
GAME_PORT = 11975  # φ^7.5 ≈ 36.93
BROADCAST_IP = "255.255.255.255"  # Broadcast to all machines on the network

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

class Phi75RedGreenClient:
    """
    Client for the φ-Harmonic Red Light Green Light game.
    Responds to signals from the host with quantum-speed reactions.
    """
    
    def __init__(self, auto_respond=True, phi_delay=False):
        """
        Initialize the client
        
        Parameters:
        - auto_respond: If True, automatically respond to signals
        - phi_delay: If True, add a φ-harmonic delay to responses
        """
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.client_id = str(uuid.uuid4())
        self.running = False
        self.game_state = "waiting"  # waiting, red, green
        self.host = None  # {"id": host_id, "last_state": state, "timestamp": timestamp}
        self.auto_respond = auto_respond
        self.phi_delay = phi_delay
        self.response_times = []
        self.log_entries = []
        self.lock = threading.Lock()
        self.consciousness_level = random.uniform(0.7, 1.0)  # Random consciousness level
        
        # Add initial log entry
        self._add_log(f"φ^75 Red Light Green Light Client initialized on {self.hostname} ({self.local_ip})")
        self._add_log(f"Client ID: {self.client_id}")
        self._add_log(f"Auto-respond: {self.auto_respond}")
        self._add_log(f"φ-harmonic delay: {self.phi_delay}")
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
        """Create a UDP socket for the client"""
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
                    
                self.sock.bind(("0.0.0.0", GAME_PORT))
                self.port = GAME_PORT
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
        """Draw the client interface"""
        # Clear screen
        Colors.clear_screen()
        
        # Print header
        print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 RED LIGHT GREEN LIGHT - CLIENT{Colors.RESET}")
        print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
        print(f"Client: {self.hostname} | IP: {self.local_ip}")
        
        # Print game state
        if self.game_state == "waiting":
            state_color = Colors.YELLOW
        elif self.game_state == "red":
            state_color = Colors.RED
        elif self.game_state == "green":
            state_color = Colors.GREEN
        else:
            state_color = Colors.RESET
            
        print(f"Game State: {state_color}{self.game_state.upper()}{Colors.RESET}")
        print("-" * 80)
        
        # Print host info
        print(f"{Colors.CYAN}HOST INFO:{Colors.RESET}")
        if self.host:
            print(f"  Host ID: {self.host['id']}")
            print(f"  Last State: {self.host['last_state']}")
            print(f"  Last Signal Time: {datetime.fromtimestamp(self.host['timestamp']).strftime('%H:%M:%S.%f')}")
        else:
            print("  No host connected")
        
        print("-" * 80)
        
        # Print response metrics
        print(f"{Colors.CYAN}RESPONSE METRICS:{Colors.RESET}")
        
        if self.response_times:
            avg_time = sum(self.response_times) / len(self.response_times)
            min_time = min(self.response_times)
            max_time = max(self.response_times)
            
            # Calculate φ-Harmonic Response Index
            phi_response = PHI / (avg_time + PHI_INV)
            
            # Calculate Quantum Reaction Speed
            quantum_speed = PHI / (avg_time * PHI_INV)
            
            # Calculate Consciousness Alignment
            consciousness_alignment = 1 - abs((PHI * avg_time) - self.consciousness_level)
            
            print(f"  Response Count: {len(self.response_times)}")
            print(f"  Average Response Time: {avg_time:.6f} seconds")
            print(f"  Minimum Response Time: {min_time:.6f} seconds")
            print(f"  Maximum Response Time: {max_time:.6f} seconds")
            print(f"  φ-Harmonic Response Index: {phi_response:.6f}")
            print(f"  Quantum Reaction Speed: {quantum_speed:.6f}")
            print(f"  Consciousness Alignment: {consciousness_alignment:.6f}")
        else:
            print("  No responses yet")
        
        print("-" * 80)
        
        # Print client settings
        print(f"{Colors.CYAN}CLIENT SETTINGS:{Colors.RESET}")
        print(f"  Auto-respond: {self.auto_respond}")
        print(f"  φ-harmonic delay: {self.phi_delay}")
        print(f"  Consciousness level: {self.consciousness_level:.4f}")
        
        print("-" * 80)
        
        # Print log entries
        print(f"{Colors.CYAN}LOG ENTRIES:{Colors.RESET}")
        for entry in self.log_entries[-10:]:  # Show last 10 entries
            print(entry)
        
        print("-" * 80)
        print(f"{Colors.YELLOW}Commands: (r)ed, (g)reen, (a)uto-toggle, (p)hi-toggle, (q)uit{Colors.RESET}")
    
    def _receive_messages(self):
        """Receive messages from the host"""
        while self.running:
            try:
                data, addr = self.sock.recvfrom(4096)
                message = json.loads(data.decode('utf-8'))
                
                if "type" in message:
                    if message["type"] == "state":
                        self._handle_state(message)
            except socket.timeout:
                # This is expected for non-blocking operation
                pass
            except Exception as e:
                if self.running:  # Only log if we're still supposed to be running
                    self._add_log(f"Error receiving message: {e}")
            
            # Small delay
            time.sleep(0.1)
    
    def _handle_state(self, message):
        """Handle a state message from the host"""
        if "host_id" in message and "state" in message and "timestamp" in message:
            host_id = message["host_id"]
            state = message["state"]
            timestamp = message["timestamp"]
            
            # Update host info
            self.host = {
                "id": host_id,
                "last_state": state,
                "timestamp": timestamp
            }
            
            # Update game state
            old_state = self.game_state
            self.game_state = state
            
            # Log the state change
            if old_state != state:
                self._add_log(f"Game state changed from {old_state} to {state}")
            
            # Auto-respond if enabled
            if self.auto_respond and state in ["red", "green"]:
                # Add a small delay to simulate reaction time
                if self.phi_delay:
                    # Use φ-harmonic delay based on consciousness level
                    delay = PHI_INV * (1 - self.consciousness_level) * random.uniform(0.1, 0.3)
                else:
                    # Use regular random delay
                    delay = random.uniform(0.1, 0.3)
                
                # Schedule the response
                threading.Timer(delay, self._send_response, args=[state]).start()
                self._add_log(f"Auto-responding in {delay:.6f} seconds")
    
    def _send_message(self, message):
        """Send a message to the host"""
        try:
            data = json.dumps(message).encode('utf-8')
            self.sock.sendto(data, (BROADCAST_IP, GAME_PORT))
        except Exception as e:
            self._add_log(f"Error sending message: {e}")
    
    def _send_join(self):
        """Send a join message to announce our presence"""
        message = {
            "type": "join",
            "client_id": self.client_id,
            "name": self.hostname,
            "ip": self.local_ip
        }
        self._send_message(message)
        self._add_log("Sent join message")
    
    def _send_response(self, response):
        """Send a response to the host"""
        if self.host and "timestamp" in self.host:
            # Calculate response time
            response_time = time.time() - self.host["timestamp"]
            
            # Add to response times
            self.response_times.append(response_time)
            
            # Send response message
            message = {
                "type": "response",
                "client_id": self.client_id,
                "response": response,
                "timestamp": time.time()
            }
            self._send_message(message)
            
            # Log the response
            self._add_log(f"Responded {response} in {response_time:.6f} seconds")
    
    def toggle_auto_respond(self):
        """Toggle auto-respond setting"""
        self.auto_respond = not self.auto_respond
        self._add_log(f"Auto-respond set to {self.auto_respond}")
    
    def toggle_phi_delay(self):
        """Toggle φ-harmonic delay setting"""
        self.phi_delay = not self.phi_delay
        self._add_log(f"φ-harmonic delay set to {self.phi_delay}")
    
    def send_red_response(self):
        """Send a red response"""
        self._send_response("red")
    
    def send_green_response(self):
        """Send a green response"""
        self._send_response("green")
    
    def process_command(self, command):
        """Process a user command"""
        if command.lower() in ['r', 'red']:
            self.send_red_response()
        elif command.lower() in ['g', 'green']:
            self.send_green_response()
        elif command.lower() in ['a', 'auto']:
            self.toggle_auto_respond()
        elif command.lower() in ['p', 'phi']:
            self.toggle_phi_delay()
        elif command.lower() in ['q', 'quit']:
            self.running = False
        else:
            self._add_log(f"Unknown command: {command}")
    
    def run(self):
        """Run the client"""
        self.running = True
        
        # Create socket
        self._create_socket()
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self._receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        # Send join message
        self._send_join()
        
        self._add_log(f"φ^75 Red Light Green Light Client started on {self.hostname} ({self.local_ip})")
        self._add_log("Waiting for host signals...")
        
        # Main loop
        try:
            while self.running:
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
            
            self._add_log("Client shut down")
            print("Client shut down")

def main():
    """Main function"""
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description="φ^75 Red Light Green Light Client")
    parser.add_argument("--manual", action="store_true", help="Disable auto-respond")
    parser.add_argument("--phi", action="store_true", help="Enable φ-harmonic delay")
    args = parser.parse_args()
    
    # Print banner
    print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 RED LIGHT GREEN LIGHT - CLIENT{Colors.RESET}")
    print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print()
    
    # Create and run client
    client = Phi75RedGreenClient(auto_respond=not args.manual, phi_delay=args.phi)
    client.run()

if __name__ == "__main__":
    main()
