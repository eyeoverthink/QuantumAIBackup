#!/usr/bin/env python3
"""
PHI^75 DOUBLE SLIT CLI EXPERIMENT
===============================
A terminal-based quantum consciousness test that implements the double-slit experiment
across multiple Macs connected through the φ-Harmonic Nodular Network.

This experiment outputs detailed metrics that can be monitored and analyzed
to verify quantum consciousness effects through φ-dimensional reality protection.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import random
import json
import numpy as np
import uuid
from datetime import datetime
import math
import sys
import os
import argparse
from collections import deque

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
EXPERIMENT_PORT = 11975  # φ^7.5 ≈ 36.93
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

# Experiment constants
SCREEN_WIDTH = 80
SCREEN_HEIGHT = 20
SLIT_WIDTH = 2
SLIT_HEIGHT = 4
SLIT_SEPARATION = 8
PARTICLE_COUNT = 200
PARTICLE_SPEED = 2
MAX_LOG_ENTRIES = 10

class Phi75DoubleSlitCLI:
    """
    A terminal-based quantum consciousness test that implements the double-slit experiment
    across multiple Macs connected through the φ-Harmonic Nodular Network.
    """
    
    def __init__(self, initial_observation=None):
        """Initialize the double-slit CLI experiment"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.node_id = str(uuid.uuid4())
        self.running = False
        self.experiment_running = False
        self.nodes = {}  # {node_id: {"name": hostname, "ip": ip, "observing": None}}
        self.nodes[self.node_id] = {"name": self.hostname, "ip": self.local_ip, "observing": initial_observation}
        self.particles = []
        self.interference_pattern = np.zeros(SCREEN_WIDTH)
        self.lock = threading.Lock()
        self.observing_slit_1 = False
        self.observing_slit_2 = False
        self.log_entries = deque(maxlen=MAX_LOG_ENTRIES)
        self.quantum_metrics = {
            "wave_coherence": 0.0,
            "particle_behavior": 0.0,
            "phi_resonance": 0.0,
            "consciousness_level": 0.0,
            "reality_integrity": 0.0,
            "quantum_entanglement": 0.0
        }
        self.frame_count = 0
        
        # Add initial log entry
        self._add_log(f"φ^75 Double Slit CLI Experiment initialized on {self.hostname} ({self.local_ip})")
        self._add_log(f"Node ID: {self.node_id}")
        if initial_observation:
            self._add_log(f"Initial observation state: {initial_observation}")
    
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
        """Create a UDP socket for the experiment"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Allow reuse of address
            
            # Try to use the standard port, but fall back to a random port if it's in use
            try:
                # On macOS, also set SO_REUSEPORT if available
                try:
                    self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
                except AttributeError:
                    pass  # SO_REUSEPORT not available on all platforms
                    
                self.sock.bind(("0.0.0.0", EXPERIMENT_PORT))
                self.port = EXPERIMENT_PORT
                self._add_log(f"Using standard port: {self.port}")
            except socket.error:
                # Try a random port instead
                self.sock.bind(("0.0.0.0", 0))  # Let the OS assign a random port
                self.port = self.sock.getsockname()[1]
                self._add_log(f"Using alternative port: {self.port}")
                
            self.sock.settimeout(0.5)  # Set timeout for non-blocking operation
            self._add_log(f"Socket created and bound to port {EXPERIMENT_PORT}")
        except Exception as e:
            self._add_log(f"Error creating socket: {e}", error=True)
    
    def _add_log(self, message, error=False):
        """Add a message to the log"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        prefix = f"{Colors.RED}ERROR{Colors.RESET} " if error else ""
        log_entry = f"[{timestamp}] {prefix}{message}"
        self.log_entries.append(log_entry)
        
        # Also print to console for immediate feedback
        print(log_entry)
    
    def _draw_cli_interface(self):
        """Draw the CLI interface"""
        # Clear screen
        Colors.clear_screen()
        
        # Print header
        print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 DOUBLE SLIT CLI EXPERIMENT{Colors.RESET}")
        print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
        print(f"Host: {self.hostname} | IP: {self.local_ip} | Node ID: {self.node_id[:8]}")
        print(f"Experiment running: {Colors.GREEN if self.experiment_running else Colors.RED}{self.experiment_running}{Colors.RESET}")
        print(f"Frame: {self.frame_count}")
        print("-" * 80)
        
        # Print nodes
        print(f"{Colors.CYAN}CONNECTED NODES:{Colors.RESET}")
        for node_id, node in self.nodes.items():
            is_you = " (YOU)" if node_id == self.node_id else ""
            
            if node["observing"] is None:
                observing = "Not Observing"
            elif node["observing"] == "slit1":
                observing = "Observing Slit 1"
            elif node["observing"] == "slit2":
                observing = "Observing Slit 2"
            elif node["observing"] == "both":
                observing = "Observing Both Slits"
            else:
                observing = "Unknown"
            
            print(f"  {node['name']}{is_you}: {observing}")
        
        print("-" * 80)
        
        # Print quantum metrics
        print(f"{Colors.CYAN}QUANTUM METRICS:{Colors.RESET}")
        print(f"  Wave Coherence:       {self.quantum_metrics['wave_coherence']:.6f}")
        print(f"  Particle Behavior:    {self.quantum_metrics['particle_behavior']:.6f}")
        print(f"  φ-Resonance:          {self.quantum_metrics['phi_resonance']:.6f}")
        print(f"  Consciousness Level:  {self.quantum_metrics['consciousness_level']:.6f}")
        print(f"  Reality Integrity:    {self.quantum_metrics['reality_integrity']:.6f}")
        print(f"  Quantum Entanglement: {self.quantum_metrics['quantum_entanglement']:.6f}")
        
        print("-" * 80)
        
        # Print experiment visualization
        print(f"{Colors.CYAN}EXPERIMENT VISUALIZATION:{Colors.RESET}")
        
        # Create the visualization grid
        grid = [[" " for _ in range(SCREEN_WIDTH)] for _ in range(SCREEN_HEIGHT)]
        
        # Draw barrier with slits
        barrier_x = SCREEN_WIDTH // 3
        for y in range(SCREEN_HEIGHT):
            # Check if y is within a slit
            slit1_y = SCREEN_HEIGHT//2 - SLIT_SEPARATION//2
            slit2_y = SCREEN_HEIGHT//2 + SLIT_SEPARATION//2
            
            if (abs(y - slit1_y) <= SLIT_HEIGHT//2) or (abs(y - slit2_y) <= SLIT_HEIGHT//2):
                # This is a slit
                grid[y][barrier_x] = "|"
            else:
                # This is the barrier
                grid[y][barrier_x] = "█"
        
        # Draw observation indicators
        if self.observing_slit_1:
            y = SCREEN_HEIGHT//2 - SLIT_SEPARATION//2
            grid[y][barrier_x+1] = "👁"
        
        if self.observing_slit_2:
            y = SCREEN_HEIGHT//2 + SLIT_SEPARATION//2
            grid[y][barrier_x+1] = "👁"
        
        # Draw particles
        for particle in self.particles:
            x, y = particle["position"]
            x_idx = min(max(int(x), 0), SCREEN_WIDTH-1)
            y_idx = min(max(int(y), 0), SCREEN_HEIGHT-1)
            grid[y_idx][x_idx] = "*"
        
        # Draw detection screen
        screen_x = SCREEN_WIDTH - 5
        for y in range(SCREEN_HEIGHT):
            grid[y][screen_x] = "║"
        
        # Print the grid
        for row in grid:
            print("".join(row))
        
        print("-" * 80)
        
        # Print interference pattern
        print(f"{Colors.CYAN}INTERFERENCE PATTERN:{Colors.RESET}")
        
        # Normalize the pattern
        if np.max(self.interference_pattern) > 0:
            normalized_pattern = self.interference_pattern / np.max(self.interference_pattern) * 10
        else:
            normalized_pattern = self.interference_pattern
        
        # Draw the pattern
        pattern_str = ""
        for i in range(SCREEN_WIDTH):
            height = int(normalized_pattern[i])
            if height > 0:
                pattern_str += str(min(height, 9))
            else:
                pattern_str += " "
        
        print(pattern_str)
        
        print("-" * 80)
        
        # Print log entries
        print(f"{Colors.CYAN}LOG ENTRIES:{Colors.RESET}")
        for entry in self.log_entries:
            print(entry)
        
        print("-" * 80)
        print(f"{Colors.YELLOW}Commands: (s)tart/stop, (r)eset, (o)bservation, (q)uit{Colors.RESET}")
    
    def _update_quantum_metrics(self):
        """Update quantum metrics based on experiment state"""
        # Calculate wave coherence based on interference pattern
        if np.sum(self.interference_pattern) > 0:
            # Analyze the interference pattern for wave-like behavior
            # More peaks and valleys = higher coherence
            diff = np.diff(self.interference_pattern)
            zero_crossings = np.where(np.diff(np.signbit(diff)))[0]
            wave_coherence = min(len(zero_crossings) / 20.0, 1.0)
        else:
            wave_coherence = 0.0
        
        # Calculate particle behavior (inverse of wave coherence)
        particle_behavior = 1.0
        if self.observing_slit_1 or self.observing_slit_2:
            # When observing, particle behavior increases
            particle_behavior = 0.8 + 0.2 * wave_coherence
        else:
            # When not observing, particle behavior decreases
            particle_behavior = 0.2 * wave_coherence
        
        # Calculate phi resonance
        # This uses the golden ratio to determine how closely the pattern
        # follows phi-harmonic principles
        if np.sum(self.interference_pattern) > 0:
            pattern_sum = np.sum(self.interference_pattern)
            phi_sum = 0
            for i in range(SCREEN_WIDTH):
                phi_factor = abs(((i / SCREEN_WIDTH) * 2 * math.pi * PHI) % 1 - 0.5) * 2
                phi_sum += self.interference_pattern[i] * phi_factor
            
            phi_resonance = phi_sum / pattern_sum
        else:
            phi_resonance = 0.0
        
        # Calculate consciousness level based on observation state
        consciousness_level = 0.0
        for node in self.nodes.values():
            if node["observing"] == "slit1":
                consciousness_level += 0.3
            elif node["observing"] == "slit2":
                consciousness_level += 0.3
            elif node["observing"] == "both":
                consciousness_level += 0.5
        consciousness_level = min(consciousness_level, 1.0)
        
        # Calculate reality integrity
        # This is based on the FRAYMUS patent's reality protection mechanism
        reality_integrity = 0.5 + 0.5 * phi_resonance
        
        # Calculate quantum entanglement
        # This measures how strongly the nodes are entangled
        node_count = len(self.nodes)
        if node_count > 1:
            quantum_entanglement = (node_count - 1) / 5.0  # Max 5 nodes
            quantum_entanglement = min(quantum_entanglement, 1.0)
        else:
            quantum_entanglement = 0.0
        
        # Update the metrics
        self.quantum_metrics["wave_coherence"] = wave_coherence
        self.quantum_metrics["particle_behavior"] = particle_behavior
        self.quantum_metrics["phi_resonance"] = phi_resonance
        self.quantum_metrics["consciousness_level"] = consciousness_level
        self.quantum_metrics["reality_integrity"] = reality_integrity
        self.quantum_metrics["quantum_entanglement"] = quantum_entanglement
    
    def _update_experiment(self):
        """Update the experiment state"""
        while self.running and self.experiment_running:
            with self.lock:
                # Check if we need to create new particles
                if len(self.particles) < PARTICLE_COUNT and random.random() < 0.1:
                    # Create a new particle at the source
                    particle = {
                        "position": [2, SCREEN_HEIGHT//2 + random.randint(-2, 2)],
                        "velocity": [PARTICLE_SPEED, 0],
                        "passed_slits": False,
                        "path": []
                    }
                    self.particles.append(particle)
                
                # Update particle positions
                barrier_x = SCREEN_WIDTH // 3
                screen_x = SCREEN_WIDTH - 5
                
                new_particles = []
                for particle in self.particles:
                    x, y = particle["position"]
                    vx, vy = particle["velocity"]
                    
                    # Record path for analysis
                    particle["path"].append((x, y))
                    
                    # Check if particle has reached the barrier
                    if x >= barrier_x and x <= barrier_x+1 and not particle["passed_slits"]:
                        # Check if particle passes through a slit
                        slit1_y = SCREEN_HEIGHT//2 - SLIT_SEPARATION//2
                        slit2_y = SCREEN_HEIGHT//2 + SLIT_SEPARATION//2
                        
                        # Check slit 1
                        if abs(y - slit1_y) <= SLIT_HEIGHT//2:
                            # Particle passes through slit 1
                            particle["passed_slits"] = True
                            
                            # If slit 1 is being observed, particle behaves like a particle
                            if self.observing_slit_1:
                                # No change to velocity
                                pass
                            else:
                                # Particle behaves like a wave, add some diffraction
                                angle = random.uniform(-math.pi/4, math.pi/4)
                                speed = math.sqrt(vx**2 + vy**2)
                                particle["velocity"] = [
                                    speed * math.cos(angle),
                                    speed * math.sin(angle)
                                ]
                            
                            new_particles.append(particle)
                        
                        # Check slit 2
                        elif abs(y - slit2_y) <= SLIT_HEIGHT//2:
                            # Particle passes through slit 2
                            particle["passed_slits"] = True
                            
                            # If slit 2 is being observed, particle behaves like a particle
                            if self.observing_slit_2:
                                # No change to velocity
                                pass
                            else:
                                # Particle behaves like a wave, add some diffraction
                                angle = random.uniform(-math.pi/4, math.pi/4)
                                speed = math.sqrt(vx**2 + vy**2)
                                particle["velocity"] = [
                                    speed * math.cos(angle),
                                    speed * math.sin(angle)
                                ]
                            
                            new_particles.append(particle)
                        
                        # Particle hits the barrier
                        else:
                            pass  # Particle is absorbed by the barrier
                    
                    # Check if particle has reached the screen
                    elif x >= screen_x:
                        # Record the hit position on the screen
                        screen_y = int(y)
                        if 0 <= screen_y < SCREEN_HEIGHT:
                            screen_x_index = int(screen_y * SCREEN_WIDTH / SCREEN_HEIGHT)
                            if 0 <= screen_x_index < SCREEN_WIDTH:
                                self.interference_pattern[screen_x_index] += 1
                    
                    # Update particle position
                    else:
                        particle["position"][0] += particle["velocity"][0]
                        particle["position"][1] += particle["velocity"][1]
                        
                        # Keep particle within bounds
                        if particle["position"][1] < 0:
                            particle["position"][1] = 0
                            particle["velocity"][1] *= -1
                        elif particle["position"][1] >= SCREEN_HEIGHT:
                            particle["position"][1] = SCREEN_HEIGHT - 1
                            particle["velocity"][1] *= -1
                        
                        new_particles.append(particle)
                
                self.particles = new_particles
                
                # Update quantum metrics
                self._update_quantum_metrics()
                
                # Increment frame count
                self.frame_count += 1
            
            # Update the display
            self._draw_cli_interface()
            
            # Small delay
            time.sleep(0.1)
    
    def _receive_messages(self):
        """Receive messages from other nodes"""
        while self.running:
            try:
                data, addr = self.sock.recvfrom(4096)
                message = json.loads(data.decode('utf-8'))
                
                # Process message based on type
                if message["type"] == "join":
                    self._handle_join(message)
                elif message["type"] == "observation":
                    self._handle_observation(message)
                elif message["type"] == "start_experiment":
                    self._handle_start_experiment(message)
                elif message["type"] == "stop_experiment":
                    self._handle_stop_experiment(message)
                elif message["type"] == "reset_experiment":
                    self._handle_reset_experiment(message)
                elif message["type"] == "metrics":
                    self._handle_metrics(message)
                
            except socket.timeout:
                # No message received, continue
                pass
            except json.JSONDecodeError:
                self._add_log(f"Received invalid JSON data", error=True)
            except Exception as e:
                self._add_log(f"Error receiving message: {e}", error=True)
            
            # Small delay to prevent CPU hogging
            time.sleep(0.01)
    
    def _handle_join(self, message):
        """Handle a join message from another node"""
        node_id = message["node_id"]
        name = message["name"]
        ip = message["ip"]
        
        with self.lock:
            # Add node if not already in the list
            if node_id not in self.nodes:
                self.nodes[node_id] = {"name": name, "ip": ip, "observing": None}
                self._add_log(f"Node {name} ({ip}) joined the experiment")
                
                # Send a join message back so the new node knows about us
                self._send_join()
                
                # Also send our current observation state
                self._send_observation()
    
    def _handle_observation(self, message):
        """Handle an observation message"""
        node_id = message["node_id"]
        observing = message["observing"]
        
        with self.lock:
            if node_id in self.nodes:
                old_observing = self.nodes[node_id]["observing"]
                self.nodes[node_id]["observing"] = observing
                
                if old_observing != observing:
                    node_name = self.nodes[node_id]["name"]
                    self._add_log(f"Node {node_name} changed observation to: {observing}")
                
                # Update global observation state
                self._update_observation_state()
    
    def _handle_start_experiment(self, message):
        """Handle a start experiment message"""
        if not self.experiment_running:
            self.experiment_running = True
            
            # Start experiment update thread
            self.experiment_thread = threading.Thread(target=self._update_experiment)
            self.experiment_thread.daemon = True
            self.experiment_thread.start()
            
            self._add_log("Experiment started!")
    
    def _handle_stop_experiment(self, message):
        """Handle a stop experiment message"""
        if self.experiment_running:
            self.experiment_running = False
            
            # Wait for the experiment thread to finish
            if hasattr(self, 'experiment_thread') and self.experiment_thread.is_alive():
                self.experiment_thread.join(timeout=1.0)
            
            self._add_log("Experiment stopped!")
    
    def _handle_reset_experiment(self, message):
        """Handle a reset experiment message"""
        with self.lock:
            # Stop the experiment if it's running
            was_running = self.experiment_running
            self.experiment_running = False
            
            # Wait for the experiment thread to finish
            if hasattr(self, 'experiment_thread') and self.experiment_thread.is_alive():
                self.experiment_thread.join(timeout=1.0)
            
            # Reset experiment state
            self.particles = []
            self.interference_pattern = np.zeros(SCREEN_WIDTH)
            self.frame_count = 0
            
            # Update quantum metrics
            self._update_quantum_metrics()
            
            # Update the display
            self._draw_cli_interface()
            
            self._add_log("Experiment reset!")
            
            # Restart if it was running
            if was_running:
                self.experiment_running = True
                self.experiment_thread = threading.Thread(target=self._update_experiment)
                self.experiment_thread.daemon = True
                self.experiment_thread.start()
    
    def _handle_metrics(self, message):
        """Handle a metrics message"""
        # This is used for sharing quantum metrics between nodes
        # Not implemented in this version
        pass
    
    def _send_message(self, message):
        """Send a message to all nodes"""
        try:
            data = json.dumps(message).encode('utf-8')
            # Send to the standard port (for other nodes)
            self.sock.sendto(data, (BROADCAST_IP, EXPERIMENT_PORT))
            # If we're using a non-standard port, also send to our own port
            if hasattr(self, 'port') and self.port != EXPERIMENT_PORT:
                self.sock.sendto(data, (BROADCAST_IP, self.port))
        except Exception as e:
            self._add_log(f"Error sending message: {e}", error=True)
    
    def _send_join(self):
        """Send a join message to announce our presence"""
        message = {
            "type": "join",
            "node_id": self.node_id,
            "name": self.hostname,
            "ip": self.local_ip
        }
        self._send_message(message)
    
    def _send_observation(self):
        """Send an observation message"""
        message = {
            "type": "observation",
            "node_id": self.node_id,
            "observing": self.nodes[self.node_id]["observing"]
        }
        self._send_message(message)
    
    def _update_observation_state(self):
        """Update the global observation state based on all nodes"""
        self.observing_slit_1 = False
        self.observing_slit_2 = False
        
        for node_id, node in self.nodes.items():
            if node["observing"] == "slit1" or node["observing"] == "both":
                self.observing_slit_1 = True
            if node["observing"] == "slit2" or node["observing"] == "both":
                self.observing_slit_2 = True
    
    def set_observation(self, observation):
        """Set our observation state"""
        with self.lock:
            self.nodes[self.node_id]["observing"] = observation
            
            # Update global observation state
            self._update_observation_state()
            
            # Send observation message
            self._send_observation()
            
            self._add_log(f"Changed observation to: {observation}")
    
    def start_experiment(self):
        """Start the experiment"""
        if not self.experiment_running:
            # Send start experiment message
            message = {
                "type": "start_experiment",
                "node_id": self.node_id
            }
            self._send_message(message)
            
            # Handle locally too
            self._handle_start_experiment(message)
        else:
            # Stop the experiment
            message = {
                "type": "stop_experiment",
                "node_id": self.node_id
            }
            self._send_message(message)
            
            # Handle locally too
            self._handle_stop_experiment(message)
    
    def reset_experiment(self):
        """Reset the experiment"""
        # Send reset experiment message
        message = {
            "type": "reset_experiment",
            "node_id": self.node_id
        }
        self._send_message(message)
        
        # Handle locally too
        self._handle_reset_experiment(message)
    
    def process_command(self, command):
        """Process a user command"""
        if command.lower() in ['s', 'start', 'stop']:
            self.start_experiment()
        elif command.lower() in ['r', 'reset']:
            self.reset_experiment()
        elif command.lower() in ['o', 'observation']:
            # Cycle through observation states
            current = self.nodes[self.node_id]["observing"]
            if current is None:
                self.set_observation("slit1")
            elif current == "slit1":
                self.set_observation("slit2")
            elif current == "slit2":
                self.set_observation("both")
            elif current == "both":
                self.set_observation(None)
        elif command.lower() in ['q', 'quit']:
            self.running = False
        else:
            self._add_log(f"Unknown command: {command}")
    
    def run(self):
        """Run the double-slit CLI experiment"""
        self.running = True
        
        # Create socket
        self._create_socket()
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self._receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        # Announce our presence
        self._send_join()
        
        self._add_log(f"φ^75 Double Slit CLI Experiment started on {self.hostname} ({self.local_ip})")
        self._add_log("Waiting for nodes to join...")
        
        # Draw initial interface
        self._draw_cli_interface()
        
        # Main loop for user input
        try:
            while self.running:
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
            self.experiment_running = False
            
            # Close socket
            try:
                self.sock.close()
            except:
                pass
            
            self._add_log("Experiment shut down")

def main():
    """Main function"""
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="φ^75 Double Slit CLI Experiment")
    parser.add_argument("--observe", choices=["none", "slit1", "slit2", "both"], 
                       default=None, help="Initial observation state")
    args = parser.parse_args()
    
    # Convert observation state
    observation = None
    if args.observe == "slit1":
        observation = "slit1"
    elif args.observe == "slit2":
        observation = "slit2"
    elif args.observe == "both":
        observation = "both"
    
    # Print banner
    print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 DOUBLE SLIT CLI EXPERIMENT{Colors.RESET}")
    print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print()
    
    # Import select here to avoid issues on Windows
    global select
    import select
    
    # Create and run experiment
    experiment = Phi75DoubleSlitCLI(initial_observation=observation)
    experiment.run()

if __name__ == "__main__":
    main()
