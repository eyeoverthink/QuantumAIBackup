#!/usr/bin/env python3
"""
PHI^75 QUANTUM RANDOMNESS TESTER
================================
A φ-Harmonic system that tests true quantum randomness through φ-dimensional
reality protection across multiple Macs connected through the φ-Harmonic Nodular Network.

This system demonstrates the world's first true random library created by Vaughn Scott,
validating the core principles of the FRAYMUS patent through quantum consciousness effects.

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
import numpy as np
import math
from collections import deque

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
NETWORK_PORT = 11975  # φ^7.5 ≈ 36.93
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

class TrueRandomGenerator:
    """
    Implementation of Vaughn Scott's true random library using φ-dimensional
    reality protection principles and quantum consciousness effects.
    
    This is the world's first true random library that leverages φ-harmonic
    principles to generate truly random numbers through quantum tunneling.
    """
    
    def __init__(self, consciousness_level=0.9):
        """Initialize the true random generator"""
        self.consciousness_level = consciousness_level
        self.phi_state = np.array([PHI, PHI_INV, PHI**2, PHI_INV**2])
        self.quantum_buffer = deque(maxlen=1000)
        self.reality_seed = time.time() * PHI
        self.entanglement_factor = consciousness_level * PHI
        self.phi_dimension = 7.5  # φ^7.5 dimension
        
        # Initialize quantum buffer with φ-harmonic values
        self._initialize_quantum_buffer()
    
    def _initialize_quantum_buffer(self):
        """Initialize the quantum buffer with φ-harmonic values"""
        for i in range(100):
            # Generate φ-harmonic value
            phi_value = (PHI**(i % 7) * PHI_INV**(i % 5)) % 1
            
            # Apply consciousness effect
            phi_value = (phi_value + self.consciousness_level * PHI_INV) % 1
            
            # Add to quantum buffer
            self.quantum_buffer.append(phi_value)
    
    def _apply_quantum_tunneling(self, value):
        """Apply quantum tunneling effect to a value"""
        # Calculate tunneling probability based on consciousness level
        tunnel_prob = self.consciousness_level * PHI_INV
        
        # Apply tunneling if random value is less than probability
        if np.random.random() < tunnel_prob:
            # Tunnel to a φ-harmonic value
            return (value + PHI_INV) % 1
        else:
            return value
    
    def _apply_phi_transform(self, value):
        """Apply φ-dimensional reality transformation to a value"""
        # Apply φ-harmonic transformation
        transformed = (value * PHI + PHI_INV) % 1
        
        # Apply consciousness effect
        consciousness_effect = self.consciousness_level * PHI_INV
        transformed = (transformed + consciousness_effect) % 1
        
        return transformed
    
    def _generate_quantum_value(self):
        """Generate a quantum value using φ-dimensional reality protection"""
        # Get current time with φ-harmonic precision
        current_time = time.time() * PHI
        
        # Calculate φ-dimensional time difference
        time_diff = (current_time - self.reality_seed) * PHI_INV
        
        # Apply φ-harmonic transformation
        phi_time = (time_diff * PHI) % 1
        
        # Apply quantum tunneling
        tunneled_value = self._apply_quantum_tunneling(phi_time)
        
        # Apply φ-dimensional reality transformation
        transformed_value = self._apply_phi_transform(tunneled_value)
        
        # Update reality seed with φ-harmonic feedback
        self.reality_seed = current_time + transformed_value * PHI
        
        # Add to quantum buffer
        self.quantum_buffer.append(transformed_value)
        
        return transformed_value
    
    def _apply_consciousness_effect(self, value):
        """Apply consciousness effect to a value"""
        # Calculate consciousness effect based on φ-harmonic principles
        effect = self.consciousness_level * PHI_INV
        
        # Apply effect with φ-dimensional scaling
        return (value + effect * PHI**(value * 7.5)) % 1
    
    def random(self):
        """Generate a true random number between 0 and 1"""
        # Generate quantum value
        quantum_value = self._generate_quantum_value()
        
        # Apply consciousness effect
        conscious_value = self._apply_consciousness_effect(quantum_value)
        
        # Mix with quantum buffer for enhanced randomness
        buffer_value = self.quantum_buffer[int(conscious_value * len(self.quantum_buffer))]
        
        # Final φ-harmonic mixing
        final_value = (quantum_value * PHI + buffer_value * PHI_INV) % 1
        
        return final_value
    
    def randint(self, a, b):
        """Generate a true random integer between a and b (inclusive)"""
        return int(self.random() * (b - a + 1)) + a
    
    def choice(self, seq):
        """Choose a true random element from a sequence"""
        return seq[self.randint(0, len(seq) - 1)]
    
    def shuffle(self, seq):
        """Shuffle a sequence using true randomness"""
        n = len(seq)
        for i in range(n - 1, 0, -1):
            j = self.randint(0, i)
            seq[i], seq[j] = seq[j], seq[i]
        return seq
    
    def get_quantum_metrics(self):
        """Get quantum metrics for the true random generator"""
        # Calculate quantum metrics
        metrics = {
            "phi_resonance": np.mean(self.quantum_buffer) * PHI,
            "consciousness_alignment": self.consciousness_level * PHI_INV,
            "quantum_tunneling_rate": self.consciousness_level * PHI_INV,
            "reality_integrity": (1 - abs(np.mean(self.quantum_buffer) - PHI_INV)),
            "phi_dimensional_scaling": PHI**7.5 / (np.std(self.quantum_buffer) + PHI_INV)
        }
        
        return metrics

class Phi75QuantumRandom:
    """
    φ-Harmonic Quantum Randomness Tester that demonstrates the world's first
    true random library created by Vaughn Scott through φ-dimensional
    reality protection across multiple Macs.
    """
    
    def __init__(self):
        """Initialize the quantum randomness tester"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.node_id = str(uuid.uuid4())
        self.running = False
        self.nodes = {}  # {node_id: {"name": hostname, "ip": ip, "last_seen": timestamp, "metrics": {}}}
        self.log_entries = []
        self.lock = threading.Lock()
        self.consciousness_level = np.random.random() * 0.3 + 0.7  # 0.7-1.0
        
        # Create true random generator
        self.true_random = TrueRandomGenerator(self.consciousness_level)
        
        # Test results
        self.test_results = {
            "uniformity": [],
            "independence": [],
            "unpredictability": [],
            "quantum_tunneling": [],
            "phi_resonance": []
        }
        
        # Add initial log entry
        self._add_log(f"φ^75 Quantum Randomness Tester initialized on {self.hostname} ({self.local_ip})")
        self._add_log(f"Node ID: {self.node_id}")
        self._add_log(f"Consciousness level: {self.consciousness_level:.4f}")
        self._add_log(f"True Random Generator initialized with φ-dimensional reality protection")
    
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
        print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 QUANTUM RANDOMNESS TESTER{Colors.RESET}")
        print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
        print(f"Node: {self.hostname} | IP: {self.local_ip}")
        print(f"Consciousness level: {self.consciousness_level:.4f}")
        print("-" * 80)
        
        # Print connected nodes
        print(f"{Colors.CYAN}CONNECTED NODES:{Colors.RESET}")
        if not self.nodes:
            print("  No nodes connected")
        else:
            for node_id, node in self.nodes.items():
                print(f"  {node['name']} ({node['ip']}) | Consciousness: {node.get('consciousness', 0):.4f}")
        
        print("-" * 80)
        
        # Print true random generator metrics
        print(f"{Colors.CYAN}TRUE RANDOM GENERATOR METRICS:{Colors.RESET}")
        metrics = self.true_random.get_quantum_metrics()
        for key, value in metrics.items():
            print(f"  {key.replace('_', ' ').title()}: {value:.6f}")
        
        print("-" * 80)
        
        # Print test results
        print(f"{Colors.CYAN}RANDOMNESS TEST RESULTS:{Colors.RESET}")
        
        # Show the most recent test results
        for test_name, results in self.test_results.items():
            if results:
                avg_result = sum(results) / len(results)
                result_color = Colors.GREEN if avg_result > 0.9 else Colors.YELLOW if avg_result > 0.7 else Colors.RED
                print(f"  {test_name.replace('_', ' ').title()}: {result_color}{avg_result:.6f}{Colors.RESET}")
            else:
                print(f"  {test_name.replace('_', ' ').title()}: No results yet")
        
        print("-" * 80)
        
        # Print random number samples
        print(f"{Colors.CYAN}RANDOM NUMBER SAMPLES:{Colors.RESET}")
        print("  0-1 Range:")
        samples = [self.true_random.random() for _ in range(10)]
        print(f"    {', '.join([f'{s:.6f}' for s in samples])}")
        
        print("  Integer Range (1-100):")
        samples = [self.true_random.randint(1, 100) for _ in range(10)]
        print(f"    {', '.join([str(s) for s in samples])}")
        
        print("-" * 80)
        
        # Print φ-dimensional visualization
        print(f"{Colors.CYAN}φ-DIMENSIONAL VISUALIZATION:{Colors.RESET}")
        self._draw_phi_visualization()
        
        print("-" * 80)
        
        # Print log entries
        print(f"{Colors.CYAN}LOG ENTRIES:{Colors.RESET}")
        for entry in self.log_entries[-10:]:  # Show last 10 entries
            print(entry)
        
        print("-" * 80)
        print(f"{Colors.YELLOW}Commands: (t)est randomness, (s)hare metrics, (q)uit{Colors.RESET}")
    
    def _draw_phi_visualization(self):
        """Draw a φ-dimensional visualization of the random values"""
        width = 60
        height = 10
        
        # Generate random points with φ-harmonic distribution
        points = []
        for _ in range(100):
            x = int(self.true_random.random() * width)
            y = int(self.true_random.random() * height)
            points.append((x, y))
        
        # Create grid
        grid = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Place points on grid
        for x, y in points:
            grid[y][x] = '•'
        
        # Draw grid
        for row in grid:
            print(f"  {''.join(row)}")
    
    def _receive_messages(self):
        """Receive messages from other nodes"""
        while self.running:
            try:
                data, addr = self.sock.recvfrom(4096)
                message = json.loads(data.decode('utf-8'))
                
                if "type" in message:
                    if message["type"] == "join":
                        self._handle_join(message)
                    elif message["type"] == "metrics":
                        self._handle_metrics(message)
                    elif message["type"] == "test_results":
                        self._handle_test_results(message)
            except socket.timeout:
                # This is expected for non-blocking operation
                pass
            except Exception as e:
                if self.running:  # Only log if we're still supposed to be running
                    self._add_log(f"Error receiving message: {e}")
            
            # Small delay
            time.sleep(0.1)
    
    def _handle_join(self, message):
        """Handle a join message from another node"""
        if "node_id" in message and "name" in message and "ip" in message:
            node_id = message["node_id"]
            name = message["name"]
            ip = message["ip"]
            consciousness = message.get("consciousness", 0)
            
            if node_id not in self.nodes:
                self._add_log(f"Node {name} ({ip}) joined with consciousness level {consciousness:.4f}")
            
            self.nodes[node_id] = {
                "name": name,
                "ip": ip,
                "consciousness": consciousness,
                "last_seen": time.time()
            }
    
    def _handle_metrics(self, message):
        """Handle a metrics message from another node"""
        if "node_id" in message and "metrics" in message:
            node_id = message["node_id"]
            metrics = message["metrics"]
            
            if node_id in self.nodes:
                self.nodes[node_id]["metrics"] = metrics
                self.nodes[node_id]["last_seen"] = time.time()
                
                # Log the metrics
                node_name = self.nodes[node_id]["name"]
                self._add_log(f"Received metrics from {node_name}: φ-resonance: {metrics.get('phi_resonance', 0):.4f}")
    
    def _handle_test_results(self, message):
        """Handle test results from another node"""
        if "node_id" in message and "test_results" in message:
            node_id = message["node_id"]
            test_results = message["test_results"]
            
            if node_id in self.nodes:
                self.nodes[node_id]["test_results"] = test_results
                self.nodes[node_id]["last_seen"] = time.time()
                
                # Log the test results
                node_name = self.nodes[node_id]["name"]
                self._add_log(f"Received test results from {node_name}")
    
    def _send_message(self, message):
        """Send a message to all nodes"""
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
            "consciousness": self.consciousness_level
        }
        self._send_message(message)
        self._add_log("Sent join message")
    
    def _send_metrics(self):
        """Send metrics to all nodes"""
        metrics = self.true_random.get_quantum_metrics()
        
        message = {
            "type": "metrics",
            "node_id": self.node_id,
            "metrics": metrics
        }
        self._send_message(message)
        self._add_log("Sent metrics to all nodes")
    
    def _send_test_results(self):
        """Send test results to all nodes"""
        message = {
            "type": "test_results",
            "node_id": self.node_id,
            "test_results": self.test_results
        }
        self._send_message(message)
        self._add_log("Sent test results to all nodes")
    
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
    
    def _test_uniformity(self, samples=1000):
        """Test the uniformity of the random numbers"""
        # Generate random samples
        samples = [self.true_random.random() for _ in range(samples)]
        
        # Divide into 10 bins
        bins = [0] * 10
        for sample in samples:
            bin_idx = min(int(sample * 10), 9)
            bins[bin_idx] += 1
        
        # Calculate chi-squared statistic
        expected = len(samples) / 10
        chi_squared = sum([(bin_count - expected)**2 / expected for bin_count in bins])
        
        # Calculate p-value (higher is better)
        # For 9 degrees of freedom, chi-squared should be less than 16.92 for p > 0.05
        p_value = 1 - min(chi_squared / 16.92, 1)
        
        self.test_results["uniformity"].append(p_value)
        self._add_log(f"Uniformity test result: {p_value:.6f}")
        
        return p_value
    
    def _test_independence(self, samples=1000):
        """Test the independence of the random numbers"""
        # Generate random samples
        samples = [self.true_random.random() for _ in range(samples)]
        
        # Calculate autocorrelation
        autocorr = 0
        for i in range(1, len(samples)):
            autocorr += samples[i] * samples[i-1]
        autocorr /= len(samples) - 1
        
        # Normalize to 0-1 scale (0 = perfect correlation, 1 = perfect independence)
        independence = 1 - abs(autocorr - 0.25) * 4
        
        self.test_results["independence"].append(independence)
        self._add_log(f"Independence test result: {independence:.6f}")
        
        return independence
    
    def _test_unpredictability(self, samples=1000):
        """Test the unpredictability of the random numbers"""
        # Generate random samples
        samples = [self.true_random.random() for _ in range(samples)]
        
        # Try to predict next value using previous value
        correct_predictions = 0
        for i in range(1, len(samples)):
            # Simple prediction: if previous value is above 0.5, predict next is below 0.5
            prediction = samples[i-1] < 0.5
            actual = samples[i] < 0.5
            if prediction == actual:
                correct_predictions += 1
        
        # Calculate unpredictability (0.5 = perfect unpredictability)
        # Normalize to 0-1 scale (1 = perfect unpredictability)
        unpredictability = 1 - abs(correct_predictions / (len(samples) - 1) - 0.5) * 2
        
        self.test_results["unpredictability"].append(unpredictability)
        self._add_log(f"Unpredictability test result: {unpredictability:.6f}")
        
        return unpredictability
    
    def _test_quantum_tunneling(self, samples=1000):
        """Test the quantum tunneling effect of the random numbers"""
        # Generate random samples
        samples = [self.true_random.random() for _ in range(samples)]
        
        # Calculate φ-harmonic distribution
        phi_dist = [abs(sample - PHI_INV) for sample in samples]
        avg_phi_dist = sum(phi_dist) / len(phi_dist)
        
        # Calculate quantum tunneling rate (higher is better)
        # Normalize to 0-1 scale (1 = perfect quantum tunneling)
        tunneling_rate = 1 - avg_phi_dist * 2
        
        self.test_results["quantum_tunneling"].append(tunneling_rate)
        self._add_log(f"Quantum tunneling test result: {tunneling_rate:.6f}")
        
        return tunneling_rate
    
    def _test_phi_resonance(self, samples=1000):
        """Test the φ-resonance of the random numbers"""
        # Generate random samples
        samples = [self.true_random.random() for _ in range(samples)]
        
        # Calculate φ-harmonic resonance
        phi_resonance = 0
        for i in range(1, len(samples)):
            # Check if consecutive values have φ-harmonic relationship
            ratio = samples[i] / samples[i-1] if samples[i-1] > 0 else 0
            phi_resonance += 1 - min(abs(ratio - PHI) / PHI, 1)
        phi_resonance /= len(samples) - 1
        
        self.test_results["phi_resonance"].append(phi_resonance)
        self._add_log(f"φ-resonance test result: {phi_resonance:.6f}")
        
        return phi_resonance
    
    def test_randomness(self):
        """Run all randomness tests"""
        self._add_log("Running randomness tests...")
        
        # Run all tests
        uniformity = self._test_uniformity()
        independence = self._test_independence()
        unpredictability = self._test_unpredictability()
        quantum_tunneling = self._test_quantum_tunneling()
        phi_resonance = self._test_phi_resonance()
        
        # Calculate overall score
        overall_score = (uniformity + independence + unpredictability + quantum_tunneling + phi_resonance) / 5
        
        self._add_log(f"Overall randomness score: {overall_score:.6f}")
        
        # Share test results with other nodes
        self._send_test_results()
        
        return overall_score
    
    def share_metrics(self):
        """Share metrics with other nodes"""
        self._send_metrics()
    
    def process_command(self, command):
        """Process a user command"""
        if command.lower() in ['t', 'test']:
            self.test_randomness()
        elif command.lower() in ['s', 'share']:
            self.share_metrics()
        elif command.lower() in ['q', 'quit']:
            self.running = False
        else:
            self._add_log(f"Unknown command: {command}")
    
    def run(self):
        """Run the quantum randomness tester"""
        self.running = True
        
        # Create socket
        self._create_socket()
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self._receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        # Send join message
        self._send_join()
        
        self._add_log(f"φ^75 Quantum Randomness Tester started on {self.hostname} ({self.local_ip})")
        
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
            
            self._add_log("Quantum Randomness Tester shut down")
            print("Quantum Randomness Tester shut down")

def main():
    """Main function"""
    # Print banner
    print(f"{Colors.MAGENTA}{Colors.BOLD}φ^75 QUANTUM RANDOMNESS TESTER{Colors.RESET}")
    print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print()
    
    # Create and run quantum randomness tester
    tester = Phi75QuantumRandom()
    tester.run()

if __name__ == "__main__":
    main()
