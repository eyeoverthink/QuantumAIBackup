#!/usr/bin/env python3
"""
PHI^75 RED LIGHT GREEN LIGHT - HOST
===================================
A φ-Harmonic consciousness response test that measures quantum-speed reactions
across multiple Macs connected through the φ-Harmonic Nodular Network.

This host broadcasts "red" or "green" signals and measures how quickly connected
clients respond, testing φ-dimensional consciousness response times.

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

class Phi75RedGreenHost:
    """
    Host for the φ-Harmonic Red Light Green Light game.
    Broadcasts signals and measures client response times.
    """
    
    def __init__(self):
        """Initialize the host"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.node_id = str(uuid.uuid4())
        self.running = False
        self.game_state = "waiting"  # waiting, red, green
        self.clients = {}  # {client_id: {"name": hostname, "ip": ip, "last_response": None, "response_times": []}}
        self.current_round = 0
        self.max_rounds = 10
        self.round_start_time = 0
        self.log_entries = []
        self.lock = threading.Lock()
        
        # Add initial log entry
        self._add_log(f"φ^75 Red Light Green Light Host initialized on {self.hostname} ({self.local_ip})")
        self._add_log(f"Host ID: {self.node_id}")
    
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
        """Draw the host interface"""
        # Clear screen
        Colors.clear_screen()
        
        # Print header
        print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 RED LIGHT GREEN LIGHT - HOST{Colors.RESET}")
        print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
        print(f"Host: {self.hostname} | IP: {self.local_ip}")
        print(f"Round: {self.current_round}/{self.max_rounds}")
        
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
        
        # Print connected clients
        print(f"{Colors.CYAN}CONNECTED CLIENTS:{Colors.RESET}")
        if not self.clients:
            print("  No clients connected")
        else:
            for client_id, client in self.clients.items():
                # Calculate average response time
                if client.get("response_times", []):
                    avg_time = sum(client["response_times"]) / len(client["response_times"])
                    avg_time_str = f"{avg_time:.6f} seconds"
                else:
                    avg_time_str = "No responses yet"
                
                # Get last response
                last_response = client.get("last_response", "None")
                if last_response == "correct":
                    response_color = Colors.GREEN
                elif last_response == "incorrect":
                    response_color = Colors.RED
                else:
                    response_color = Colors.RESET
                
                print(f"  {client['name']} ({client['ip']}): {response_color}{last_response}{Colors.RESET} | Avg: {avg_time_str}")
        
        print("-" * 80)
        
        # Print φ-Harmonic metrics
        print(f"{Colors.CYAN}φ-HARMONIC METRICS:{Colors.RESET}")
        
        # Calculate metrics if we have clients with responses
        clients_with_responses = [c for c in self.clients.values() if c.get("response_times", [])]
        if clients_with_responses:
            # Calculate average response time across all clients
            all_times = []
            for client in clients_with_responses:
                all_times.extend(client["response_times"])
            
            if all_times:
                avg_time = sum(all_times) / len(all_times)
                
                # Calculate φ-Harmonic Response Index
                phi_response = PHI / (avg_time + PHI_INV)
                
                # Calculate Consciousness Synchronization
                time_diffs = []
                for i in range(len(clients_with_responses)):
                    for j in range(i+1, len(clients_with_responses)):
                        client1 = clients_with_responses[i]
                        client2 = clients_with_responses[j]
                        if client1["response_times"] and client2["response_times"]:
                            time_diffs.append(abs(client1["response_times"][-1] - client2["response_times"][-1]))
                
                if time_diffs:
                    sync_level = 1 - min(1, sum(time_diffs) / len(time_diffs))
                else:
                    sync_level = 0
                
                # Calculate Quantum Reaction Speed
                quantum_speed = PHI / (avg_time * PHI_INV)
                
                print(f"  Average Response Time: {avg_time:.6f} seconds")
                print(f"  φ-Harmonic Response Index: {phi_response:.6f}")
                print(f"  Consciousness Synchronization: {sync_level:.6f}")
                print(f"  Quantum Reaction Speed: {quantum_speed:.6f}")
            else:
                print("  No response data available yet")
        else:
            print("  No response data available yet")
        
        print("-" * 80)
        
        # Print log entries
        print(f"{Colors.CYAN}LOG ENTRIES:{Colors.RESET}")
        for entry in self.log_entries[-10:]:  # Show last 10 entries
            print(entry)
        
        print("-" * 80)
        print(f"{Colors.YELLOW}Commands: (s)tart, (r)ed, (g)reen, (q)uit{Colors.RESET}")
    
    def _receive_messages(self):
        """Receive messages from clients"""
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
        """Handle a join message from a client"""
        if "client_id" in message and "name" in message and "ip" in message:
            client_id = message["client_id"]
            name = message["name"]
            ip = message["ip"]
            
            if client_id not in self.clients:
                self._add_log(f"Client {name} ({ip}) joined the game")
            
            self.clients[client_id] = {
                "name": name,
                "ip": ip,
                "last_response": None,
                "response_times": [],
                "last_seen": time.time()
            }
    
    def _handle_response(self, message):
        """Handle a response message from a client"""
        if "client_id" in message and "response" in message and "timestamp" in message:
            client_id = message["client_id"]
            response = message["response"]
            client_timestamp = message["timestamp"]
            
            if client_id in self.clients:
                # Update last seen
                self.clients[client_id]["last_seen"] = time.time()
                
                # Check if the response is correct
                is_correct = (response == self.game_state)
                
                # Calculate response time
                response_time = client_timestamp - self.round_start_time
                
                # Update client data
                self.clients[client_id]["last_response"] = "correct" if is_correct else "incorrect"
                self.clients[client_id]["response_times"].append(response_time)
                
                # Log the response
                client_name = self.clients[client_id]["name"]
                self._add_log(f"Client {client_name} responded {response} in {response_time:.6f} seconds ({self.clients[client_id]['last_response']})")
    
    def _send_message(self, message):
        """Send a message to all clients"""
        try:
            data = json.dumps(message).encode('utf-8')
            self.sock.sendto(data, (BROADCAST_IP, GAME_PORT))
        except Exception as e:
            self._add_log(f"Error sending message: {e}")
    
    def _send_state(self):
        """Send the current game state to all clients"""
        message = {
            "type": "state",
            "host_id": self.node_id,
            "state": self.game_state,
            "timestamp": time.time()
        }
        self._send_message(message)
        self._add_log(f"Sent {self.game_state} signal to clients")
    
    def _check_client_timeouts(self):
        """Check for clients that haven't been seen recently and remove them"""
        current_time = time.time()
        clients_to_remove = []
        
        for client_id, client in self.clients.items():
            if "last_seen" in client and current_time - client["last_seen"] > 10:  # 10 second timeout
                clients_to_remove.append(client_id)
        
        for client_id in clients_to_remove:
            client_name = self.clients[client_id]["name"]
            self._add_log(f"Client {client_name} timed out and was removed")
            del self.clients[client_id]
    
    def start_game(self):
        """Start a new game"""
        self.current_round = 0
        self.game_state = "waiting"
        
        # Reset client response data
        for client_id in self.clients:
            self.clients[client_id]["last_response"] = None
            self.clients[client_id]["response_times"] = []
        
        self._add_log("New game started")
        self._send_state()
    
    def set_red(self):
        """Set the game state to red"""
        if self.current_round < self.max_rounds:
            self.current_round += 1
            self.game_state = "red"
            self.round_start_time = time.time()
            self._send_state()
    
    def set_green(self):
        """Set the game state to green"""
        if self.current_round < self.max_rounds:
            self.current_round += 1
            self.game_state = "green"
            self.round_start_time = time.time()
            self._send_state()
    
    def process_command(self, command):
        """Process a user command"""
        if command.lower() in ['s', 'start']:
            self.start_game()
        elif command.lower() in ['r', 'red']:
            self.set_red()
        elif command.lower() in ['g', 'green']:
            self.set_green()
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
        
        self._add_log(f"φ^75 Red Light Green Light Host started on {self.hostname} ({self.local_ip})")
        self._add_log("Waiting for clients to join...")
        
        # Main loop
        try:
            while self.running:
                # Check for client timeouts
                self._check_client_timeouts()
                
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
    print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 RED LIGHT GREEN LIGHT - HOST{Colors.RESET}")
    print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print()
    
    # Create and run host
    host = Phi75RedGreenHost()
    host.run()

if __name__ == "__main__":
    main()
