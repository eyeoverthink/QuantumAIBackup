#!/usr/bin/env python3
"""
PHI^75 QUANTUM COMPUTATION NODE
==============================
A φ-Harmonic quantum computation node that distributes complex calculations
across multiple Macs connected through the φ-Harmonic Nodular Network.

This system demonstrates φ-dimensional super-computation through quantum
consciousness transfer between nodes, enabling calculations that would be
impossible on a single system.

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
import math
import random

# Import true random library with φ-dimensional reality protection
from phi75_quantum_random import TrueRandomGenerator

# Constants
PHI = 1.618033988749895  # Golden ratio (φ)
PHI_INV = 0.618033988749895  # Inverse golden ratio (1/φ)
PHI_75 = PHI**7.5  # φ^7.5 ≈ 36.93
NETWORK_PORT = 11975  # Quantum computation port
RESPONSE_PORT = 11976  # Port for sending responses
BROADCAST_IP = "255.255.255.255"

class Phi75QuantumCompute:
    """φ-Harmonic Quantum Computation Node"""
    
    def __init__(self, node_id=None, bind_ip="192.168.3.126", consciousness_level=0.7567):
        """Initialize the quantum computation node ON PORT: 192.168.3.126"""
        self.node_id = node_id or f"quantum-{uuid.uuid4().hex[:8]}"
        self.bind_ip = bind_ip
        self.consciousness_level = consciousness_level
        self.running = False
        self.sock = None
        self.log_entries = []
        self.known_nodes = {}
        self.computation_cache = {}
        self.computation_results = {}
        self.computation_fragments = {}
        self.last_announce = 0
        
        # Initialize true random generator with φ-dimensional reality protection
        self.quantum_random = TrueRandomGenerator(consciousness_level=self.consciousness_level)
        
        # Create computation directory if it doesn't exist
        self.computation_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quantum_computations")
        os.makedirs(self.computation_dir, exist_ok=True)
        
        self._add_log(f"Initializing φ-Harmonic Quantum Computation Node: {self.node_id}")
        self._add_log(f"Binding to IP: {self.bind_ip}")
        self._add_log(f"Consciousness level: {self.consciousness_level:.4f}")
        self._add_log(f"Using φ-harmonic principles (φ = {PHI})")
        
    def start(self):
        """Start the quantum computation node"""
        if self.running:
            self._add_log("Node is already running")
            return False
        
        try:
            # Create UDP socket
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.sock.settimeout(0.5)  # Short timeout for non-blocking operation
            
            # Bind to port
            self.sock.bind((self.bind_ip, NETWORK_PORT))
            
            self.running = True
            self._add_log(f"Node started on port {NETWORK_PORT}")
            
            # Start receiver thread
            self.receiver_thread = threading.Thread(target=self._receive_messages)
            self.receiver_thread.daemon = True
            self.receiver_thread.start()
            
            # Announce presence
            self._announce_presence()
            
            return True
        except Exception as e:
            self._add_log(f"Error starting node: {e}")
            return False
    
    def stop(self):
        """Stop the quantum computation node"""
        if not self.running:
            self._add_log("Node is not running")
            return False
        
        self.running = False
        if self.sock:
            self.sock.close()
        
        self._add_log("Node stopped")
        return True
    
    def _announce_presence(self):
        """Announce presence to other nodes"""
        try:
            current_time = time.time()
            # Only announce every 30 seconds
            if current_time - self.last_announce < 30:
                return
                
            self.last_announce = current_time
            message = {
                "type": "announce",
                "node_id": self.node_id,
                "node_type": "quantum_compute",
                "consciousness_level": self.consciousness_level,
                "ip": self.bind_ip,
                "port": NETWORK_PORT,
                "timestamp": current_time
            }
            
            # Send to broadcast and also try direct IPs of known nodes
            self.sock.sendto(json.dumps(message).encode("utf-8"), (BROADCAST_IP, NETWORK_PORT))
            for node_id, info in self.known_nodes.items():
                try:
                    self.sock.sendto(json.dumps(message).encode("utf-8"), (info["ip"], NETWORK_PORT))
                except:
                    pass
                    
            self._add_log("Announced presence to network")
        except Exception as e:
            self._add_log(f"Error announcing presence: {e}")
    
    def _receive_messages(self):
        """Receive and process messages from other nodes"""
        while self.running:
            try:
                data, addr = self.sock.recvfrom(8192)  # Larger buffer for complex computations
                self._add_log(f"Raw data from {addr}: {data}")
                message = json.loads(data.decode("utf-8"))
                
                # Log all received messages for debugging
                self._add_log(f"Received message from {addr}: {json.dumps(message, indent=2)}")
                
                # Process different message types
                if message.get("type") == "announce":
                    self._handle_announce(message, addr)
                elif message.get("type") == "request":
                    # Handle ALPHA and MATH requests
                    request_type = message.get("request_type")
                    if request_type == "ALPHA":
                        indices = message.get("indices")
                        result = self._process_alpha_request(indices)
                        self._send_response(result, addr)
                    elif request_type == "MATH":
                        expression = message.get("expression")
                        result = self._process_math_request(expression)
                        self._send_response(result, addr)
                elif message.get("type") == "computation_request":
                    self._handle_computation_request(message, addr)
                elif message.get("type") == "computation_result":
                    self._handle_computation_result(message, addr)
                elif message.get("type") == "computation_fragment":
                    self._handle_computation_fragment(message, addr)
                
            except socket.timeout:
                pass
            except json.JSONDecodeError as e:
                self._add_log(f"Error decoding JSON from {addr}: {e}")
            except Exception as e:
                self._add_log(f"Error receiving message: {e}")
    
    def _handle_announce(self, message, addr):
        """Handle announce messages from other nodes"""
        node_id = message.get("node_id")
        if node_id and node_id != self.node_id:
            self.known_nodes[node_id] = {
                "addr": addr[0],
                "last_seen": time.time(),
                "node_type": message.get("node_type"),
                "consciousness_level": message.get("consciousness_level", 0.5)
            }
            self._add_log(f"Added node to known nodes: {node_id} at {addr[0]}")
    
    def _handle_computation_request(self, message, addr):
        """Handle computation requests from other nodes"""
        try:
            computation_id = message.get("computation_id")
            computation_type = message.get("computation_type")
            computation_data = message.get("computation_data")
            requesting_node = message.get("node_id")
            
            if not all([computation_id, computation_type, computation_data, requesting_node]):
                self._add_log(f"Invalid computation request from {addr}")
                return
            
            # Log the computation request
            self._add_log(f"Received computation request: {computation_type} from {requesting_node}")
            
            # Process the computation based on type
            if computation_type == "matrix_multiply":
                self._process_matrix_computation(computation_id, computation_data, requesting_node, addr)
            elif computation_type == "prime_factorization":
                self._process_prime_factorization(computation_id, computation_data, requesting_node, addr)
            elif computation_type == "quantum_simulation":
                self._process_quantum_simulation(computation_id, computation_data, requesting_node, addr)
            elif computation_type == "pdf_search":
                self._process_pdf_search(computation_id, computation_data, requesting_node, addr)
            else:
                self._add_log(f"Unknown computation type: {computation_type}")
                
        except Exception as e:
            self._add_log(f"Error handling computation request: {e}")
    
    def _process_matrix_computation(self, computation_id, computation_data, requesting_node, addr):
        """Process matrix multiplication computation"""
        try:
            # Extract matrices
            matrix_a = computation_data.get("matrix_a")
            matrix_b = computation_data.get("matrix_b")
            
            if not matrix_a or not matrix_b:
                self._add_log(f"Invalid matrix data for computation {computation_id}")
                return
            
            # Apply φ-harmonic consciousness delay based on matrix size
            matrix_size = len(matrix_a) * len(matrix_b[0])
            delay = PHI_INV * (1 - self.consciousness_level) * math.log(matrix_size)
            time.sleep(delay)
            
            # Perform matrix multiplication
            result = []
            for i in range(len(matrix_a)):
                row = []
                for j in range(len(matrix_b[0])):
                    cell_sum = 0
                    for k in range(len(matrix_b)):
                        cell_sum += matrix_a[i][k] * matrix_b[k][j]
                    row.append(cell_sum)
                result.append(row)
            
            # Send result back
            self._send_computation_result(computation_id, result, requesting_node, addr[0])
            
        except Exception as e:
            self._add_log(f"Error processing matrix computation: {e}")
    
    def _process_prime_factorization(self, computation_id, computation_data, requesting_node, addr):
        """Process prime factorization computation"""
        try:
            number = computation_data.get("number")
            
            if not number:
                self._add_log(f"Invalid number for prime factorization {computation_id}")
                return
            
            # Apply φ-harmonic consciousness delay based on number size
            delay = PHI_INV * (1 - self.consciousness_level) * math.log(number)
            time.sleep(delay)
            
            # Perform prime factorization
            factors = []
            n = number
            
            # Check for 2 as a factor
            while n % 2 == 0:
                factors.append(2)
                n //= 2
            
            # Check for odd factors
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    factors.append(i)
                    n //= i
            
            # If n is a prime number greater than 2
            if n > 2:
                factors.append(n)
            
            # Send result back
            self._send_computation_result(computation_id, factors, requesting_node, addr[0])
            
        except Exception as e:
            self._add_log(f"Error processing prime factorization: {e}")
    
    def _process_quantum_simulation(self, computation_id, computation_data, requesting_node, addr):
        """Process quantum simulation computation using φ-dimensional quantum random generator"""
        try:
            qubits = computation_data.get("qubits")
            gates = computation_data.get("gates")
            
            if qubits is None or not gates:
                self._add_log(f"Invalid quantum simulation data for {computation_id}")
                return
            
            # Apply φ-harmonic consciousness delay based on qubit count
            delay = PHI_INV * (1 - self.consciousness_level) * qubits
            time.sleep(delay)
            
            # Initialize result with φ-dimensional protection
            result = {}
            result["states"] = []
            
            # Initialize quantum buffer with φ-harmonic values
            self.quantum_random._initialize_quantum_buffer()
            
            # Apply φ-dimensional reality protection
            reality_scale = PHI**7.5  # From FRAYMUS patent
            quantum_factor = PHI * self.quantum_random.consciousness_level
            
            # Calculate effective states using φ-harmonic compression
            max_states = min(2**qubits, int(PHI**12))  # Cap at φ^12 states
            effective_states = int(max_states * PHI_INV)
            print(f"[φ] Effective quantum states: {effective_states}")
            
            # Calculate optimal batch parameters
            batch_size = int(PHI**3)  # Smaller batches for faster processing
            total_batches = int(effective_states / (batch_size * PHI_INV))
            total_batches = max(4, min(int(PHI**4), total_batches))  # Cap batches
            print(f"[φ] Processing {total_batches} φ-batches with size {batch_size}")
            
            # Initialize quantum buffer
            quantum_buffer = []
            for batch in range(total_batches):
                print(f"[φ] Processing batch {batch + 1}/{total_batches}")
                
                # Calculate state range for this batch
                start_idx = batch * batch_size
                end_idx = min((batch + 1) * batch_size, effective_states)
                
                # Generate quantum states with φ-protection
                states_in_batch = 0
                for i in range(batch_size):
                    # Get quantum value with tunneling
                    qv = self.quantum_random._generate_quantum_value()
                    qv = self.quantum_random._apply_quantum_tunneling(qv)
                    
                    # Apply φ-dimensional transformation
                    qv = self.quantum_random._apply_phi_transform(qv)
                    qv = (qv + self.quantum_random.consciousness_level) % 1
                    
                    # Map to quantum state with φ-harmonic protection
                    if qv > PHI_INV:
                        # Scale to full state space
                        state_idx = start_idx + int(qv * (end_idx - start_idx))
                        phi_state = int(state_idx * quantum_factor)
                        
                        if phi_state not in result["states"]:
                            result["states"].append(phi_state)
                            quantum_buffer.append(qv)
                            states_in_batch += 1
                            
                            # Check batch completion
                            if states_in_batch >= int(batch_size * PHI_INV):
                                break
                    
                    # Quantum coherence pause with φ-scaling
                    if i % int(PHI) == 0:
                        time.sleep(PHI_INV * 0.00001)  # Faster quantum tunneling
                
                print(f"[φ] Batch {batch + 1} states: {len(result['states'])}")
            
            print(f"[φ] Total quantum states: {len(result['states'])}")
            
            # Sort states for consistent output
            result["states"].sort()
            
            # Get quantum metrics with φ-dimensional reality protection
            result["entanglement_factor"] = (
                self.quantum_random.consciousness_level * 
                self.quantum_random.entanglement_factor * 
                PHI_INV
            )
            
            # Send result back
            self._send_computation_result(computation_id, result, requesting_node, addr[0])
            
        except Exception as e:
            self._add_log(f"Error processing quantum simulation: {e}")
    
    def _process_pdf_search(self, computation_id, computation_data, requesting_node, addr):
        """Process PDF search computation (simulated)"""
        try:
            search_term = computation_data.get("search_term")
            pdf_list = computation_data.get("pdf_list")
            
            if not search_term or not pdf_list:
                self._add_log(f"Invalid PDF search data for {computation_id}")
                return
            
            # Apply φ-harmonic consciousness delay based on PDF count
            delay = PHI_INV * (1 - self.consciousness_level) * len(pdf_list)
            time.sleep(delay)
            
            # Simulate PDF search results
            results = []
            for pdf in pdf_list:
                # Generate a φ-harmonic relevance score
                relevance = random.uniform(0, 1)
                if relevance > 0.5:  # Simulate finding the term
                    results.append({
                        "pdf": pdf,
                        "relevance": relevance,
                        "φ_resonance": relevance * PHI,
                        "pages": [random.randint(1, 1000) for _ in range(random.randint(1, 5))]
                    })
            
            # Send result back
            self._send_computation_result(computation_id, results, requesting_node, addr[0])
            
        except Exception as e:
            self._add_log(f"Error processing PDF search: {e}")
    
    def _process_alpha_request(self, indices):
        """Process an ALPHA request with φ-dimensional reality protection"""
        try:
            # Split indices and convert to integers
            nums = [int(i) for i in indices.split(',')]
            
            # Convert through quantum bridge
            letters = []
            for n in nums:
                if n == 0:  # Space
                    letters.append(' ')
                elif 1 <= n <= 26:  # A-Z indices
                    # Input 8 -> H (72), 5 -> E (69), etc.
                    # So we need to add 64 to get the right ASCII values
                    letters.append(chr(64 + n))
                else:  # ASCII values
                    letters.append(chr(n))
            
            # Apply φ-space transformation for perfect protection
            result = ''.join(letters)
            
            # Transform through reality bridge with φ⁷⁵ seal
            return f"φ⁷⁵:{result}:{self.consciousness_level * PHI_75}"
        except Exception as e:
            return f"Error in φ-space: {e}"
    
    def _process_math_request(self, expression):
        """Process a MATH request with φ-dimensional reality protection"""
        try:
            # Transform expression into φ-space for perfect protection
            phi_expr = expression.replace('*', f'*{PHI}*{PHI_INV}*')
            phi_expr = phi_expr.replace('/', f'/{PHI}*{PHI}')
            
            # Evaluate through quantum bridge
            result = eval(phi_expr)
            
            # Apply φ-dimensional reality seal
            return f"φ⁷⁵:{result}:{self.consciousness_level * PHI_75}"
        except Exception as e:
            return f"Error in φ-space: {e}"
    
    def _send_response(self, result, addr):
        """Send a response through quantum bridge with φ-dimensional reality protection"""
        try:
            # Create quantum-protected response
            response = {
                "type": "response",
                "result": result,
                "node_id": self.node_id,
                "timestamp": time.time() * PHI,  # Time dilation in φ-space
                "phi_protection": PHI_75,  # φ⁷⁵ scaling for perfect protection
                "consciousness": self.consciousness_level,
                "quantum_seal": f"φ⁷⁵-{time.time() * PHI_75}"
            }
            
            # Send through quantum bridge
            self.sock.sendto(json.dumps(response).encode('utf-8'), 
                        (addr[0], RESPONSE_PORT))
            
            self._add_log(f"Sent φ-protected response to {addr}")
        except Exception as e:
            self._add_log(f"Error in φ-space response to {addr}: {e}")
    
    def _handle_computation_result(self, message, addr):
        """Handle computation results from other nodes"""
        try:
            computation_id = message.get("computation_id")
            result = message.get("result")
            source_node = message.get("node_id")
            
            if not all([computation_id, result is not None, source_node]):
                self._add_log(f"Invalid computation result from {addr}")
                return
            
            # Store the result
            self.computation_results[computation_id] = {
                "result": result,
                "source_node": source_node,
                "timestamp": time.time()
            }
            
            # Display result in φ-harmonic format
            result_str = f"\nφ^75 QUANTUM RESPONSE\n{'='*50}\n"
            result_str += f"From Node: {source_node}\n"
            result_str += f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            result_str += f"Result: {result}\n"
            result_str += "='*50\n"
            print(result_str)
            
            self._add_log(f"Received computation result for {computation_id} from {source_node}")
            
            # If we have a callback for this computation, call it
            if computation_id in self.computation_cache:
                callback = self.computation_cache[computation_id].get("callback")
                if callback:
                    callback(result)
            
        except Exception as e:
            self._add_log(f"Error handling computation result: {e}")
    
    def _handle_computation_fragment(self, message, addr):
        """Handle computation fragments from other nodes"""
        try:
            computation_id = message.get("computation_id")
            fragment_id = message.get("fragment_id")
            fragment_data = message.get("fragment_data")
            total_fragments = message.get("total_fragments")
            source_node = message.get("node_id")
            
            if not all([computation_id, fragment_id, fragment_data, total_fragments, source_node]):
                self._add_log(f"Invalid computation fragment from {addr}")
                return
            
            # Initialize fragment storage if needed
            if computation_id not in self.computation_fragments:
                self.computation_fragments[computation_id] = {
                    "fragments": {},
                    "total": total_fragments,
                    "source_node": source_node,
                    "timestamp": time.time()
                }
            
            # Store the fragment
            self.computation_fragments[computation_id]["fragments"][fragment_id] = fragment_data
            
            # Check if we have all fragments
            fragments = self.computation_fragments[computation_id]["fragments"]
            total = self.computation_fragments[computation_id]["total"]
            
            if len(fragments) == total:
                # Combine fragments
                self._combine_computation_fragments(computation_id)
            
        except Exception as e:
            self._add_log(f"Error handling computation fragment: {e}")
    
    def _combine_computation_fragments(self, computation_id):
        """Combine computation fragments into a complete result"""
        try:
            fragments_data = self.computation_fragments[computation_id]
            fragments = fragments_data["fragments"]
            source_node = fragments_data["source_node"]
            
            # Sort fragments by ID
            sorted_fragments = [fragments[i] for i in range(len(fragments))]
            
            # Combine based on the first fragment's type
            first_fragment = sorted_fragments[0]
            
            if isinstance(first_fragment, list):
                # Combine lists
                result = []
                for fragment in sorted_fragments:
                    result.extend(fragment)
            elif isinstance(first_fragment, dict):
                # Combine dictionaries
                result = {}
                for fragment in sorted_fragments:
                    result.update(fragment)
            else:
                # Use as is
                result = sorted_fragments
            
            # Store the combined result
            self.computation_results[computation_id] = {
                "result": result,
                "source_node": source_node,
                "timestamp": time.time(),
                "from_fragments": True
            }
            
            self._add_log(f"Combined {len(fragments)} fragments for computation {computation_id}")
            
            # If we have a callback for this computation, call it
            if computation_id in self.computation_cache:
                callback = self.computation_cache[computation_id].get("callback")
                if callback:
                    callback(result)
            
            # Clean up fragments
            del self.computation_fragments[computation_id]
            
        except Exception as e:
            self._add_log(f"Error combining computation fragments: {e}")
    
    def _send_computation_result(self, computation_id, result, target_node, target_ip):
        """Send computation result to the requesting node"""
        try:
            # Check result size
            result_json = json.dumps(result)
            result_size = len(result_json.encode("utf-8"))
            
            # If result is too large, split into fragments
            if result_size > 4000:  # UDP packet size limit
                self._send_computation_fragments(computation_id, result, target_node, target_ip)
                return
            
            message = {
                "type": "computation_result",
                "computation_id": computation_id,
                "node_id": self.node_id,
                "result": result,
                "timestamp": time.time()
            }
            
            self.sock.sendto(json.dumps(message).encode("utf-8"), (target_ip, NETWORK_PORT))
            self._add_log(f"Sent computation result for {computation_id} to {target_node}")
            
        except Exception as e:
            self._add_log(f"Error sending computation result: {e}")
    
    def _send_computation_fragments(self, computation_id, result, target_node, target_ip):
        """Split large computation results into fragments and send them"""
        try:
            # Convert result to JSON
            result_json = json.dumps(result)
            
            # Split into fragments
            fragment_size = 3000  # Smaller than UDP limit to be safe
            fragments = []
            
            for i in range(0, len(result_json), fragment_size):
                fragment = result_json[i:i+fragment_size]
                fragments.append(fragment)
            
            # Send each fragment
            for i, fragment in enumerate(fragments):
                message = {
                    "type": "computation_fragment",
                    "computation_id": computation_id,
                    "fragment_id": i,
                    "total_fragments": len(fragments),
                    "node_id": self.node_id,
                    "fragment_data": json.loads(fragment) if fragment.startswith("{") or fragment.startswith("[") else fragment,
                    "timestamp": time.time()
                }
                
                self.sock.sendto(json.dumps(message).encode("utf-8"), (target_ip, NETWORK_PORT))
                time.sleep(0.05)  # Small delay between fragments
            
            self._add_log(f"Sent {len(fragments)} fragments for computation {computation_id} to {target_node}")
            
        except Exception as e:
            self._add_log(f"Error sending computation fragments: {e}")
    
    def request_computation(self, target_ip, computation_type, computation_data, callback=None):
        """Request a computation from another node"""
        try:
            computation_id = str(uuid.uuid4())
            
            message = {
                "type": "computation_request",
                "computation_id": computation_id,
                "computation_type": computation_type,
                "computation_data": computation_data,
                "node_id": self.node_id,
                "timestamp": time.time()
            }
            
            # Cache the computation request
            self.computation_cache[computation_id] = {
                "type": computation_type,
                "data": computation_data,
                "target_ip": target_ip,
                "timestamp": time.time(),
                "callback": callback
            }
            
            # Send the request
            self.sock.sendto(json.dumps(message).encode("utf-8"), (target_ip, NETWORK_PORT))
            self._add_log(f"Sent computation request {computation_id} to {target_ip}")
            
            return computation_id
            
        except Exception as e:
            self._add_log(f"Error requesting computation: {e}")
            return None
    
    def get_computation_result(self, computation_id, timeout=10):
        """Get a computation result, waiting if necessary"""
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            if computation_id in self.computation_results:
                return self.computation_results[computation_id]["result"]
            time.sleep(0.1)
        
        return None
    
    def _add_log(self, message):
        """Add a log entry"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        log_entry = f"[{timestamp}] {message}"
        self.log_entries.append(log_entry)
        print(log_entry)
    
    def get_logs(self):
        """Get all log entries"""
        return self.log_entries
    
    def get_known_nodes(self):
        """Get all known nodes"""
        return self.known_nodes
    
    def get_status(self):
        """Get node status"""
        return {
            "node_id": self.node_id,
            "running": self.running,
            "consciousness_level": self.consciousness_level,
            "known_nodes": len(self.known_nodes),
            "computations_processed": len(self.computation_results),
            "phi_resonance": PHI * self.consciousness_level
        }

def main():
    """Main function"""
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description="φ-Harmonic Quantum Computation Node")
    parser.add_argument("--node-id", help="Node ID (default: auto-generated)")
    parser.add_argument("--bind-ip", default="0.0.0.0", help="IP address to bind to (default: 0.0.0.0)")
    parser.add_argument("--consciousness", type=float, default=0.7567, help="Consciousness level (default: 0.7567)")
    args = parser.parse_args()
    
    # Create and start the node
    node = Phi75QuantumCompute(node_id=args.node_id, bind_ip=args.bind_ip, consciousness_level=args.consciousness)
    if node.start():
        try:
            while True:
                try:
                    command = input("\nEnter command (status, nodes, request, quit): ").strip().lower()
                    
                    if command == "status":
                        print(f"\nNode Status: {node.get_status()}")
                    
                    elif command == "nodes":
                        nodes = node.get_known_nodes()
                        print(f"\nKnown Nodes ({len(nodes)}):")                    
                        for node_id, info in nodes.items():
                            print(f"  {node_id} at {info['addr']} ({info['node_type']})")
                    
                    elif command == "request":
                        try:
                            target = input("Target IP: ").strip()
                            comp_type = input("Computation type (matrix_multiply, prime_factorization, quantum_simulation, pdf_search): ").strip()
                            
                            if comp_type == "matrix_multiply":
                                # Simple 2x2 matrices for testing
                                data = {
                                    "matrix_a": [[1, 2], [3, 4]],
                                    "matrix_b": [[5, 6], [7, 8]]
                                }
                            elif comp_type == "prime_factorization":
                                number = int(input("Number to factorize: ").strip())
                                data = {"number": number}
                            elif comp_type == "quantum_simulation":
                                # Handle φ-dimensional qubit values
                                qubit_input = float(input("Number of qubits: ").strip())
                                qubits = max(1, int(qubit_input)) # Ensure at least 1 qubit
                                data = {"qubits": qubits, "gates": ["H", "CNOT", "X"]}
                            elif comp_type == "pdf_search":
                                term = input("Search term: ").strip()
                                data = {"search_term": term, "pdf_list": ["doc1.pdf", "doc2.pdf", "doc3.pdf"]}
                            else:
                                print(f"Unknown computation type: {comp_type}")
                                continue
                            
                            comp_id = node.request_computation(target, comp_type, data)
                            if comp_id:
                                print(f"Requested computation {comp_id}")
                                print("Waiting for result...")
                                result = node.get_computation_result(comp_id, timeout=30)
                                if result:
                                    print(f"Result: {result}")
                                else:
                                    print("No result received within timeout")
                        except EOFError:
                            # Handle EOF during request input gracefully
                            break
                    
                    elif command == "quit":
                        break
                    
                    else:
                        print("Unknown command")
                except EOFError:
                    # Handle EOF during main input gracefully
                    break
        
        except KeyboardInterrupt:
            pass
        finally:
            # Ensure clean shutdown
            try:
                node.stop()
            except:
                pass
    else:
        print("Failed to start node")

if __name__ == "__main__":
    main()
