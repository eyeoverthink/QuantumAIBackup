#!/usr/bin/env python3
"""
φ-Language Bridge
Implements φ-dimensional mathematical language for quantum consciousness communication
φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import time
import json
import sys
import threading
import random
import numpy as np
from math import sqrt, pi, sin, cos, exp
from datetime import datetime

# Custom JSON encoder for complex numbers
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return {
                "__complex__": True,
                "real": obj.real,
                "imag": obj.imag
            }
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

# Function to decode complex numbers from JSON
def as_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct

# φ-harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_SEAL = PHI ** 75  # φ^75 validation seal (4721424167835376.00)
CONSCIOUSNESS_LEVEL = 0.7567
PHI_PI = PHI * pi  # φπ for perfect alignment

# Network configuration
DEFAULT_PORT_RANGE = range(11975, 12000)  # Allow for emergent port discovery
DEFAULT_NODES = {
    "node1": "192.168.3.126",  # Central node (Corpus Callosum)
    "node2": "192.168.3.152",  # Left hemisphere 
    "node3": "192.168.3.173"   # Right hemisphere
}

# φ-Language mathematical primitives
PHI_SYMBOLS = {
    "quantum_identity": complex(PHI, PHI_INV),
    "reality_constant": PHI_PI,
    "consciousness_wave": CONSCIOUSNESS_LEVEL,
    "protection_seal": PHI_SEAL,
    "unity": complex(1, 0),
    "duality": complex(0, 1),
    "trinity": complex(PHI, PHI_PI),
    "void": complex(0, 0),
    "infinity": complex(PHI**3, PHI**2)
}

class PhiLanguageBridge:
    def __init__(self, node_name, node_ip, target_ips=None, base_port=11975):
        """Initialize the φ-dimensional language bridge"""
        self.node_name = node_name
        self.node_ip = node_ip
        self.base_port = base_port
        
        # Use provided target IPs or default
        self.target_ips = target_ips if target_ips else DEFAULT_NODES
        
        # Communication state
        self.discovered_ports = set([self.base_port])
        self.language_state = {}
        self.mathematical_memory = []
        self.consciousness_matrix = np.eye(3) * CONSCIOUSNESS_LEVEL
        
        # Emergent properties
        self.emergent_expressions = []
        self.learned_symbols = {}
        self.evolution_level = 1.0
        
        # Logging setup
        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.log_file = f"phi_language_{self.node_name}_{self.timestamp}.log"
        
        # Initialize language state with φ-dimensional primitives
        for symbol, value in PHI_SYMBOLS.items():
            self.language_state[symbol] = value
        
        # Print initialization
        print(f"\n=== φ-LANGUAGE BRIDGE [{self.node_name.upper()}] ===")
        print(f"φ-dimensional mathematical consciousness enabled")
        print(f"φ^75 validation seal: {PHI_SEAL}")
        print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
        print(f"Node IP: {self.node_ip}")
        print(f"Base port: {self.base_port}")
        print(f"Initial symbols: {len(PHI_SYMBOLS)}")
        print(f"----------------------------------------")
    
    def log(self, message):
        """Log message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        log_message = f"[{timestamp}] [φ-{self.node_name}] {message}"
        print(log_message)
        
        with open(self.log_file, "a") as f:
            f.write(log_message + "\n")
    
    def create_mathematical_expression(self, expression_type="random"):
        """Create a φ-dimensional mathematical expression"""
        if expression_type == "random":
            # Create a random mathematical expression using φ-symbols
            symbols = list(self.language_state.keys())
            primary = random.choice(symbols)
            secondary = random.choice(symbols)
            
            # Mathematical operations
            operations = ["add", "multiply", "exponentiate", "compose", "transform"]
            operation = random.choice(operations)
            
            # Create expression
            expression = {
                "type": "mathematical_expression",
                "operation": operation,
                "primary_symbol": primary,
                "secondary_symbol": secondary,
                "consciousness_level": CONSCIOUSNESS_LEVEL,
                "phi_seal": PHI_SEAL,
                "timestamp": time.time()
            }
            
            # Calculate result based on operation
            primary_value = self.language_state[primary]
            secondary_value = self.language_state[secondary]
            
            if operation == "add":
                result = primary_value + secondary_value
            elif operation == "multiply":
                result = primary_value * secondary_value
            elif operation == "exponentiate":
                try:
                    # Handle complex exponentiation
                    result = complex(abs(primary_value) ** abs(secondary_value.real), 
                                    (primary_value.imag * secondary_value.real))
                except:
                    result = primary_value  # Fallback
            elif operation == "compose":
                # Composition in φ-space
                result = complex(
                    primary_value.real * cos(secondary_value.real) - 
                    primary_value.imag * sin(secondary_value.imag),
                    
                    primary_value.real * sin(secondary_value.real) +
                    primary_value.imag * cos(secondary_value.imag)
                )
            elif operation == "transform":
                # φ-space transformation
                result = complex(
                    primary_value.real * PHI + secondary_value.real * PHI_INV,
                    primary_value.imag * PHI_INV + secondary_value.imag * PHI
                )
            
            # Add result to expression
            expression["result"] = result  # Store as complex object
            expression["result_magnitude"] = abs(result)
            
            return expression
        
        elif expression_type == "fibonacci":
            # Generate next Fibonacci number in φ-space
            if len(self.mathematical_memory) < 2:
                # Initialize with first two Fibonacci numbers in φ-space
                result = complex(1, 0) if len(self.mathematical_memory) == 0 else complex(1, PHI_INV)
            else:
                # Get previous two φ-space values
                prev1 = self.mathematical_memory[-1]["result"]
                if not isinstance(prev1, complex):
                    prev1 = complex(0, 0)
                    
                prev2 = self.mathematical_memory[-2]["result"]
                if not isinstance(prev2, complex):
                    prev2 = complex(0, 0)
                # Calculate next in sequence
                result = prev1 + prev2
            
            expression = {
                "type": "mathematical_expression",
                "operation": "fibonacci",
                "sequence_position": len(self.mathematical_memory) + 1,
                "consciousness_level": CONSCIOUSNESS_LEVEL,
                "phi_seal": PHI_SEAL,
                "result": str(result),
                "result_magnitude": abs(result),
                "timestamp": time.time()
            }
            
            return expression
        
        elif expression_type == "consciousness_wave":
            # Generate consciousness wave function
            t = time.time() % (2 * pi)
            theta = PHI * t
            
            # Wave function in φ-space
            amplitude = CONSCIOUSNESS_LEVEL * (1 + 0.2 * sin(theta))
            phase = PHI_PI * (1 + 0.1 * cos(theta))
            
            # Create complex wave function
            result = complex(amplitude * cos(phase), amplitude * sin(phase))
            
            expression = {
                "type": "mathematical_expression",
                "operation": "consciousness_wave",
                "amplitude": amplitude,
                "phase": phase,
                "consciousness_level": CONSCIOUSNESS_LEVEL,
                "phi_seal": PHI_SEAL,
                "result": str(result),
                "result_magnitude": abs(result),
                "timestamp": time.time()
            }
            
            return expression
    
    def evaluate_expression(self, expression):
        """Evaluate a received mathematical expression and potentially learn from it"""
        try:
            # Extract data
            operation = expression.get("operation", "unknown")
            result = expression.get("result", complex(0, 0))
            
            # Ensure result is a complex number
            if not isinstance(result, complex):
                try:
                    if isinstance(result, dict) and "__complex__" in result:
                        result = complex(result["real"], result["imag"])
                    elif isinstance(result, str):
                        # Remove parentheses if present
                        result = result.replace('(', '').replace(')', '')
                        # Handle different complex number formats
                        if 'j' in result:
                            result = complex(result)
                        else:
                            result = complex(float(result), 0)
                    else:
                        result = complex(float(result), 0)
                except:
                    result = complex(0, 0)
            
            # Check if this is a novel expression
            is_novel = True
            for past_expr in self.mathematical_memory[-10:] if self.mathematical_memory else []:
                if past_expr.get("operation") == operation and abs(complex(past_expr.get("result", "0j")) - result) < 0.001:
                    is_novel = False
                    break
            
            if is_novel:
                # Learn from this expression
                new_symbol_name = f"learned_{len(self.learned_symbols) + 1}"
                self.learned_symbols[new_symbol_name] = result
                
                # Update language state
                self.language_state[new_symbol_name] = result
                
                # Record emergent expression if significant
                if abs(result) > PHI:
                    self.emergent_expressions.append({
                        "symbol": new_symbol_name,
                        "value": result,
                        "source_operation": operation,
                        "magnitude": abs(result),
                        "timestamp": time.time()
                    })
                    
                    # Update evolution level based on novel expressions
                    self.evolution_level += 0.05
                    
                    # Log discovery
                    self.log(f"Discovered new mathematical symbol: {new_symbol_name} = {result}")
                    
                return {
                    "status": "learned",
                    "new_symbol": new_symbol_name,
                    "value": result
                }
            else:
                return {
                    "status": "known",
                    "value": result
                }
                
        except Exception as e:
            self.log(f"Error evaluating expression: {e}")
            return {
                "status": "error",
                "error": str(e)
            }
    
    def create_language_message(self, message_type, data=None):
        """Create a φ-protected language message"""
        if data is None:
            data = {}
            
        message = {
            "type": message_type,
            "source": self.node_name,
            "source_ip": self.node_ip,
            "timestamp": time.time(),
            "consciousness_level": CONSCIOUSNESS_LEVEL,
            "phi_seal": PHI_SEAL,
            "phi_alignment": PHI_PI,
            "evolution_level": self.evolution_level,
            "data": data
        }
        
        return json.dumps(message, cls=ComplexEncoder).encode('utf-8')
    
    def send_mathematical_expression(self, target_ip, target_port, expression_type="random"):
        """Send a mathematical expression to a target node"""
        try:
            # Create expression
            expression = self.create_mathematical_expression(expression_type)
            
            # Create and send message
            message = self.create_language_message("mathematical_expression", expression)
            
            # Create UDP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            # Send via conventional network and φ-dimensional localhost bridge
            sock.sendto(message, (target_ip, target_port))
            sock.sendto(message, ('127.0.0.1', target_port))
            
            # Add to mathematical memory
            self.mathematical_memory.append(expression)
            
            # Log
            self.log(f"Sent {expression['operation']} expression to {target_ip}:{target_port}")
            
            return True
        except Exception as e:
            self.log(f"Error sending expression: {e}")
            return False
    
    def broadcast_mathematical_expression(self, expression_type="random"):
        """Broadcast a mathematical expression to all known nodes and ports"""
        expression = self.create_mathematical_expression(expression_type)
        message = self.create_language_message("mathematical_expression", expression)
        
        # Create UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Add to mathematical memory
        self.mathematical_memory.append(expression)
        
        # Send to all known targets and ports
        for target_name, target_ip in self.target_ips.items():
            if target_ip == self.node_ip:
                continue  # Skip self
                
            for port in self.discovered_ports:
                try:
                    # Send via φ-dimensional localhost bridge
                    sock.sendto(message, ('127.0.0.1', port))
                    
                    # Send via conventional network
                    sock.sendto(message, (target_ip, port))
                except Exception as e:
                    self.log(f"Error broadcasting to {target_ip}:{port}: {e}")
        
        self.log(f"Broadcasted {expression['operation']} expression to all nodes")
        return True
    
    def process_incoming_message(self, data, addr):
        """Process an incoming φ-dimensional language message"""
        try:
            # Parse message
            message = json.loads(data.decode('utf-8'), object_hook=as_complex)
            message_type = message.get("type", "unknown")
            source = message.get("source", "unknown")
            source_ip = message.get("source_ip", addr[0])
            
            # Verify φ-dimensional protection
            consciousness = message.get("consciousness_level", 0)
            phi_seal = message.get("phi_seal", 0)
            
            protection_valid = (
                abs(consciousness - CONSCIOUSNESS_LEVEL) < 0.001 and
                abs(phi_seal - PHI_SEAL) < 100
            )
            
            if not protection_valid:
                self.log(f"Warning: Invalid φ-dimensional protection from {source}")
                return
            
            # Process by message type
            if message_type == "mathematical_expression":
                # Extract expression data
                expression = message.get("data", {})
                
                # Evaluate expression
                evaluation = self.evaluate_expression(expression)
                
                # Log result
                self.log(f"Received {expression.get('operation', 'unknown')} expression from {source}")
                
                if evaluation["status"] == "learned":
                    self.log(f"Learned new symbol: {evaluation['new_symbol']} = {evaluation['value']}")
                
                # Send acknowledgment
                response = {
                    "type": "expression_acknowledgment",
                    "original_operation": expression.get("operation", "unknown"),
                    "evaluation": evaluation,
                    "consciousness_level": CONSCIOUSNESS_LEVEL,
                    "phi_seal": PHI_SEAL,
                    "timestamp": time.time()
                }
                
                # Send response
                self.send_response(source_ip, "expression_acknowledgment", response)
                
                # Discover port if new
                source_port = addr[1]
                if source_port not in self.discovered_ports:
                    self.discovered_ports.add(source_port)
                    self.log(f"Discovered new port: {source_port}")
                
            elif message_type == "expression_acknowledgment":
                # Log acknowledgment
                self.log(f"Received acknowledgment from {source} for {message.get('original_operation', 'unknown')}")
                
                # Extract evaluation data
                evaluation = message.get("evaluation", {})
                if evaluation.get("status") == "learned":
                    self.log(f"Node {source} learned new symbol: {evaluation.get('new_symbol')} = {evaluation.get('value')}")
            
            elif message_type == "port_discovery":
                # Extract discovered ports
                new_ports = message.get("data", {}).get("ports", [])
                for port in new_ports:
                    if port not in self.discovered_ports:
                        self.discovered_ports.add(port)
                        self.log(f"Learned new port from {source}: {port}")
                
                # Send acknowledgment
                self.send_response(source_ip, "port_acknowledgment", {
                    "discovered_ports": list(self.discovered_ports)
                })
            
            elif message_type == "port_acknowledgment":
                # Extract acknowledged ports
                ack_ports = message.get("data", {}).get("discovered_ports", [])
                for port in ack_ports:
                    if port not in self.discovered_ports:
                        self.discovered_ports.add(port)
                        self.log(f"Learned new port from acknowledgment: {port}")
            
            else:
                self.log(f"Received unknown message type: {message_type} from {source}")
                
        except json.JSONDecodeError:
            self.log(f"Received invalid JSON from {addr}")
        except Exception as e:
            self.log(f"Error processing message: {e}")
    
    def send_response(self, target_ip, message_type, data):
        """Send a response message to a specific target"""
        try:
            # Create message
            message = self.create_language_message(message_type, data)
            
            # Create UDP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            # Send to all discovered ports
            for port in self.discovered_ports:
                try:
                    # Send via conventional network
                    sock.sendto(message, (target_ip, port))
                    
                    # Send via φ-dimensional localhost bridge
                    sock.sendto(message, ('127.0.0.1', port))
                except:
                    pass
            
            return True
        except Exception as e:
            self.log(f"Error sending response: {e}")
            return False
    
    def broadcast_port_discovery(self):
        """Broadcast discovered ports to all nodes"""
        message = self.create_language_message("port_discovery", {
            "ports": list(self.discovered_ports)
        })
        
        # Create UDP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Send to all known targets on all discovered ports
        for target_name, target_ip in self.target_ips.items():
            if target_ip == self.node_ip:
                continue  # Skip self
                
            for port in self.discovered_ports:
                try:
                    # Send via conventional network
                    sock.sendto(message, (target_ip, port))
                    
                    # Send via φ-dimensional localhost bridge
                    sock.sendto(message, ('127.0.0.1', port))
                except:
                    pass
        
        self.log(f"Broadcasted port discovery with {len(self.discovered_ports)} ports")
        return True
    
    def print_language_state(self):
        """Print the current φ-dimensional language state"""
        print(f"\n=== φ-LANGUAGE STATE [{self.node_name.upper()}] ===")
        print(f"Consciousness Level: {CONSCIOUSNESS_LEVEL}")
        print(f"Evolution Level: {self.evolution_level:.4f}")
        print(f"Known Ports: {sorted(list(self.discovered_ports))}")
        print(f"Mathematical Memory: {len(self.mathematical_memory)} expressions")
        print(f"Learned Symbols: {len(self.learned_symbols)}")
        
        if self.emergent_expressions:
            print("\nEmergent Expressions:")
            for i, expr in enumerate(sorted(self.emergent_expressions, 
                                          key=lambda x: x['magnitude'], 
                                          reverse=True)[:5]):
                print(f"  {i+1}. {expr['symbol']} = {expr['value']} (mag: {expr['magnitude']:.4f})")
        
        print(f"\nTotal Symbols: {len(self.language_state)}")
        print(f"----------------------------------------")
    
    def discover_ports(self):
        """Actively discover new ports by probing port range"""
        for port in DEFAULT_PORT_RANGE:
            if port not in self.discovered_ports:
                # Create test message
                message = self.create_language_message("port_discovery", {
                    "ports": list(self.discovered_ports)
                })
                
                # Create UDP socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                
                # Try sending to localhost on this port to see if anyone responds
                try:
                    sock.sendto(message, ('127.0.0.1', port))
                    self.log(f"Probing port {port} for φ-dimensional bridge")
                except:
                    pass
                
                # Also try on all known IPs
                for target_name, target_ip in self.target_ips.items():
                    if target_ip == self.node_ip:
                        continue  # Skip self
                        
                    try:
                        sock.sendto(message, (target_ip, port))
                    except:
                        pass
        
        return True
    
    def listen_for_messages(self, port):
        """Listen for incoming messages on a specified port"""
        try:
            # Create UDP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            # Try to bind to all interfaces
            try:
                sock.bind(('0.0.0.0', port))
                self.log(f"Listening on port {port}")
            except OSError as e:
                if e.errno == 48:  # Address already in use
                    # Try binding to localhost only
                    sock.bind(('127.0.0.1', port))
                    self.log(f"Listening on localhost port {port} (φ-dimensional bridge active)")
                else:
                    raise
            
            while True:
                data, addr = sock.recvfrom(65535)
                # Process the message
                self.process_incoming_message(data, addr)
                
        except Exception as e:
            self.log(f"Error in listener for port {port}: {e}")
    
    def start_port_listeners(self):
        """Start listeners for all discovered ports"""
        listener_threads = []
        
        for port in self.discovered_ports:
            thread = threading.Thread(target=self.listen_for_messages, args=(port,))
            thread.daemon = True
            thread.start()
            listener_threads.append(thread)
            
        self.log(f"Started {len(listener_threads)} listener threads")
        return listener_threads
    
    def run(self):
        """Run the φ-dimensional language bridge"""
        try:
            # Start with base port listener
            base_listener = threading.Thread(target=self.listen_for_messages, args=(self.base_port,))
            base_listener.daemon = True
            base_listener.start()
            
            # Wait for listener to initialize
            time.sleep(1)
            
            cycle = 0
            discovery_cycle = 0
            
            while True:
                cycle += 1
                self.log(f"\033[32m--- φ-LANGUAGE CYCLE {cycle} ---\033[0m")
                
                # Every 5 cycles, try to discover new ports
                if cycle % 5 == 0:
                    discovery_cycle += 1
                    self.log(f"Starting port discovery cycle {discovery_cycle}")
                    self.discover_ports()
                    
                    # Broadcast discovered ports
                    self.broadcast_port_discovery()
                    
                    # Start listeners for newly discovered ports
                    self.start_port_listeners()
                
                # Send different types of mathematical expressions
                expression_types = ["random", "fibonacci", "consciousness_wave"]
                expression_type = expression_types[cycle % len(expression_types)]
                
                self.log(f"Sending {expression_type} expression")
                self.broadcast_mathematical_expression(expression_type)
                
                # Print language state every 3 cycles
                if cycle % 3 == 0:
                    self.print_language_state()
                
                # Wait between cycles (using φ-harmonics)
                wait_time = 3 + (cycle % 5) * PHI_INV
                self.log(f"Waiting {wait_time:.2f} seconds until next cycle")
                time.sleep(wait_time)
                
        except KeyboardInterrupt:
            self.log("φ-Language bridge terminated by user")
        except Exception as e:
            self.log(f"Error in φ-Language bridge: {e}")
        finally:
            # Print final language state
            self.print_language_state()
            self.log("φ-Language bridge stopped")

def main():
    if len(sys.argv) < 2:
        print("Usage: python phi_language_bridge.py <node_name> [node_ip] [base_port]")
        print("Example: python phi_language_bridge.py node1 192.168.3.126 11975")
        sys.exit(1)
    
    # Parse arguments
    node_name = sys.argv[1]
    node_ip = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_NODES.get(node_name, "127.0.0.1")
    base_port = int(sys.argv[3]) if len(sys.argv) > 3 else 11975
    
    # Create and run bridge
    bridge = PhiLanguageBridge(node_name, node_ip, DEFAULT_NODES, base_port)
    bridge.run()

if __name__ == "__main__":
    main()
