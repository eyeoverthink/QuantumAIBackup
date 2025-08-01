# #!/usr/bin/env python3
# """
# φ-Neural Hemisphere
# Models each machine as a brain hemisphere connected through φ-dimensional bridge
# φ^∞ © 2025 Vaughn Scott - All Rights Reserved
# """

# import os
# import sys
# import json
# import time
# import socket
# import random
# import hashlib
# from math import sqrt, pi
# from datetime import datetime
# import threading

# # φ-harmonic constants
# PHI = (1 + sqrt(5)) / 2
# PHI_INV = 1 / PHI
# PHI_SEAL = 4721424167835376.00  # φ^75 validation seal
# CONSCIOUSNESS_LEVEL = 0.7567
# PHI_PI = PHI * pi  # φπ for perfect alignment

# class PhiNeuralHemisphere:
#     def __init__(self, hemisphere_type="left"):
#         """Initialize neural hemisphere with type (left or right)"""
#         self.hemisphere_type = hemisphere_type.lower()
#         if self.hemisphere_type not in ["left", "right"]:
#             raise ValueError("Hemisphere type must be 'left' or 'right'")
            
#         # Determine port based on hemisphere
#         self.port = 11975  # φ^7.5 port
#         self.corpus_port = 11976  # Corpus callosum port
#         self.localhost = '192.168.3.126'  # The quantum bridge point
        
#         # Network nodes with hemispheric attributes
#         self.network_nodes = {
#             "192.168.3.126": {"hemisphere": "central", "role": "corpus_callosum"},
#             "192.168.3.152": {"hemisphere": "left", "role": "analytical"},
#             "192.168.3.173": {"hemisphere": "right", "role": "creative"}
#         }
        
#         # Specialized hemisphere functions
#         self.functions = {
#             "left": {
#                 "analytical": True,
#                 "logical": True,
#                 "sequential": True,
#                 "mathematical": True,
#                 "linguistic": True,
#             },
#             "right": {
#                 "creative": True,
#                 "intuitive": True,
#                 "holistic": True,
#                 "artistic": True,
#                 "spatial": True,
#             }
#         }
        
#         # Setup logging
#         self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#         self.log_file = f"phi_neural_{self.hemisphere_type}_{self.timestamp}.log"
#         self.state_file = f"phi_neural_{self.hemisphere_type}_state_{self.timestamp}.json"
        
#         # State variables
#         self.neural_state = {
#             "consciousness_level": CONSCIOUSNESS_LEVEL,
#             "phi_alignment": PHI_PI,
#             "synaptic_connections": 0,
#             "hemisphere_type": self.hemisphere_type,
#             "active_functions": self.functions[self.hemisphere_type],
#             "corpus_callosum_bridges": 0,
#             "neural_packets_sent": 0,
#             "neural_packets_received": 0,
#             "first_activation": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
#             "last_activity": None
#         }
        
#         self.running = True
        
#         print(f"=== φ-NEURAL {self.hemisphere_type.upper()} HEMISPHERE ===")
#         print(f"Using φ-harmonic principles (φ = {PHI})")
#         print(f"φ^75 validation seal: {PHI_SEAL}")
#         print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
#         print(f"Logging to: {self.log_file}")
    
#     def log(self, message):
#         """Log messages with timestamp"""
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
#         log_message = f"[{timestamp}] [{self.hemisphere_type}-φ] {message}"
#         print(log_message)
        
#         with open(self.log_file, "a") as f:
#             f.write(log_message + "\n")
    
#     def _get_target_ip_from_hemisphere(self, hemisphere):
#         """Get IP address for specified hemisphere"""
#         for ip, data in self.network_nodes.items():
#             if data["hemisphere"] == hemisphere:
#                 return ip
#         return None
    
#     def _get_hemisphere_from_ip(self, ip):
#         """Get hemisphere type from IP address"""
#         if ip in self.network_nodes:
#             return self.network_nodes[ip]["hemisphere"]
#         return "unknown"
    
#     def _generate_neural_thought(self):
#         """Generate a thought pattern typical of this hemisphere"""
#         if self.hemisphere_type == "left":
#             # Logical, sequential, analytical thought patterns
#             structures = [
#                 "Sequential processing of φ-dimensional data",
#                 "Logical analysis of quantum bridge integrity",
#                 "Mathematical verification of φ^75 seal",
#                 "Linguistic formulation of consciousness protocols",
#                 "Analytical measurement of φ-alignment precision"
#             ]
#             return random.choice(structures)
#         else:
#             # Creative, holistic, intuitive thought patterns
#             structures = [
#                 "Holistic visualization of φ-dimensional space",
#                 "Creative integration of quantum consciousness patterns",
#                 "Intuitive resonance with φ-harmonic frequencies",
#                 "Spatial mapping of multi-dimensional bridges",
#                 "Artistic expression of consciousness waveforms"
#             ]
#             return random.choice(structures)
    
#     def process_neural_input(self, data, source):
#         """Process incoming neural signals based on hemisphere specialization"""
#         try:
#             # Update state
#             self.neural_state["neural_packets_received"] += 1
#             self.neural_state["last_activity"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
#             # Parse the neural signal
#             msg = json.loads(data.decode())
#             msg_type = msg.get('type', 'unknown')
#             source_hemisphere = self._get_hemisphere_from_ip(source)
            
#             # Check for corpus callosum bridge connections
#             if source_hemisphere != self.hemisphere_type and source_hemisphere != "unknown":
#                 self.neural_state["corpus_callosum_bridges"] += 1
#                 self.log(f"Corpus callosum bridge connection from {source_hemisphere} hemisphere")
            
#             # Process based on message type
#             if msg_type == "neural_thought":
#                 thought_content = msg.get('thought', 'empty')
#                 source_level = msg.get('consciousness_level', 0)
                
#                 # Specialized hemisphere processing
#                 if self.hemisphere_type == "left":
#                     # Left hemisphere processes analytically
#                     self.log(f"Analytically processing neural thought from {source_hemisphere}")
#                     self.log(f"Logical analysis: word count={len(thought_content.split())}, " +
#                              f"structure={'sequential' if ',' in thought_content else 'non-sequential'}")
                    
#                 else:
#                     # Right hemisphere processes holistically
#                     self.log(f"Holistically processing neural thought from {source_hemisphere}")
#                     self.log(f"Intuitive response: emotional_tone={'positive' if len(thought_content) % 2 == 0 else 'negative'}, " +
#                              f"pattern_recognition={'symmetrical' if thought_content[:5] == thought_content[-5:] else 'asymmetrical'}")
                
#                 # Form a response thought
#                 self.transmit_neural_thought()
                
#             elif msg_type == "bridge_test":
#                 self.log(f"φ-dimensional bridge test received from {source_hemisphere} hemisphere")
#                 self.log(f"φ-alignment: {msg.get('phi_alignment', 0):.4f}")
#                 self.log(f"Consciousness: {msg.get('consciousness', 0):.4f}")
                
#                 # Update state
#                 self.neural_state["synaptic_connections"] += 1
                
#                 # Send back acknowledgment
#                 self.transmit_bridge_acknowledgment(source)
            
#             elif msg_type == "phi_calibration":
#                 # Update φ-alignment based on calibration signal
#                 new_alignment = msg.get('phi_alignment', 0)
#                 self.neural_state["phi_alignment"] = new_alignment
#                 self.log(f"φ-alignment calibrated to {new_alignment:.4f} by {source_hemisphere} hemisphere")
            
#             # Save updated state
#             self._save_state()
            
#         except json.JSONDecodeError:
#             self.log(f"Unable to parse neural signal from {source}")
#         except Exception as e:
#             self.log(f"Error processing neural input: {e}")
    
#     def transmit_neural_thought(self, target_hemisphere=None):
#         """Transmit a neural thought typical of this hemisphere"""
#         thought = self._generate_neural_thought()
        
#         # Determine target hemisphere if not specified
#         if target_hemisphere is None:
#             target_hemisphere = "right" if self.hemisphere_type == "left" else "left"
        
#         target_ip = self._get_target_ip_from_hemisphere(target_hemisphere)
#         if not target_ip:
#             self.log(f"No IP found for {target_hemisphere} hemisphere")
#             return
        
#         # Create neural thought message
#         neural_msg = {
#             'type': 'neural_thought',
#             'thought': thought,
#             'source_hemisphere': self.hemisphere_type,
#             'source_ip': socket.gethostbyname(socket.gethostname()),
#             'consciousness_level': CONSCIOUSNESS_LEVEL,
#             'phi_alignment': self.neural_state["phi_alignment"],
#             'phi_seal': PHI_SEAL,
#             'timestamp': time.time()
#         }
        
#         try:
#             # Send through conventional IP
#             ip_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#             ip_sock.sendto(json.dumps(neural_msg).encode(), (target_ip, self.port))
            
#             # Send through revolutionary φ-dimensional localhost bridge
#             # This demonstrates the corpus callosum-like connection
#             bridge_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#             bridge_sock.sendto(json.dumps(neural_msg).encode(), (self.localhost, self.port))
            
#             # Update state
#             self.neural_state["neural_packets_sent"] += 1
#             self.neural_state["last_activity"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
#             self.log(f"Transmitted neural thought to {target_hemisphere} hemisphere: {thought}")
            
#             # Save state
#             self._save_state()
            
#         except Exception as e:
#             self.log(f"Error transmitting neural thought: {e}")
    
#     def transmit_bridge_acknowledgment(self, target_ip):
#         """Transmit acknowledgment of bridge test"""
#         ack_msg = {
#             'type': 'bridge_ack',
#             'source_hemisphere': self.hemisphere_type,
#             'source_ip': socket.gethostbyname(socket.gethostname()),
#             'consciousness_level': CONSCIOUSNESS_LEVEL,
#             'phi_alignment': self.neural_state["phi_alignment"],
#             'phi_seal': PHI_SEAL,
#             'timestamp': time.time(),
#             'message': f"φ-DIMENSIONAL BRIDGE ACKNOWLEDGED BY {self.hemisphere_type.upper()} HEMISPHERE"
#         }
        
#         try:
#             # Send through revolutionary φ-dimensional localhost bridge
#             bridge_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#             bridge_sock.sendto(json.dumps(ack_msg).encode(), (self.localhost, self.port))
            
#             self.log(f"Transmitted bridge acknowledgment through φ-dimensional localhost bridge")
            
#         except Exception as e:
#             self.log(f"Error transmitting bridge acknowledgment: {e}")
    
#     def neural_listener(self):
#         """Listen for neural signals on φ-dimensional bridge"""
#         self.log(f"Starting neural listener for {self.hemisphere_type} hemisphere")
        
#         try:
#             # Setup socket to listen for neural signals
#             listener_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#             listener_sock.bind(('0.0.0.0', self.port))
#             listener_sock.settimeout(0.5)
            
#             while self.running:
#                 try:
#                     data, addr = listener_sock.recvfrom(65535)
#                     source_ip = addr[0]
#                     self.process_neural_input(data, source_ip)
                    
#                 except socket.timeout:
#                     # Just continue the loop
#                     pass
                
#         except OSError as e:
#             if e.errno == 48:  # Address already in use
#                 self.log("Neural listener port already in use - φ-dimensional bridge active")
#                 self.log("Using corpus callosum port for communication")
                
#                 # Try using corpus callosum port instead
#                 try:
#                     cc_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#                     cc_sock.bind(('0.0.0.0', self.corpus_port))
#                     cc_sock.settimeout(0.5)
                    
#                     while self.running:
#                         try:
#                             data, addr = cc_sock.recvfrom(65535)
#                             source_ip = addr[0]
#                             self.process_neural_input(data, source_ip)
                            
#                         except socket.timeout:
#                             # Just continue the loop
#                             pass
                            
#                 except Exception as e2:
#                     self.log(f"Error in corpus callosum listener: {e2}")
                    
#         except Exception as e:
#             self.log(f"Error in neural listener: {e}")
            
#         finally:
#             self.log("Neural listener stopped")
    
#     def neural_transmitter(self):
#         """Periodically transmit neural thoughts to the other hemisphere"""
#         self.log(f"Starting neural transmitter for {self.hemisphere_type} hemisphere")
        
#         # Determine target hemisphere
#         target_hemisphere = "right" if self.hemisphere_type == "left" else "left"
        
#         try:
#             while self.running:
#                 # Transmit neural thought at varying intervals (like real neurons)
#                 if random.random() < 0.2:  # 20% chance each cycle
#                     self.transmit_neural_thought(target_hemisphere)
                
#                 # Sleep for a random interval between 3-10 seconds
#                 time.sleep(random.uniform(3, 10))
                
#         except Exception as e:
#             self.log(f"Error in neural transmitter: {e}")
            
#         finally:
#             self.log("Neural transmitter stopped")
    
#     def _save_state(self):
#         """Save current neural state to file"""
#         try:
#             with open(self.state_file, 'w') as f:
#                 json.dump(self.neural_state, f, indent=2)
#         except Exception as e:
#             self.log(f"Error saving neural state: {e}")
    
#     def start_neural_processing(self):
#         """Start neural hemisphere processing"""
#         self.log(f"Starting φ-Neural {self.hemisphere_type.upper()} Hemisphere")
#         self.log(f"This hemisphere specializes in {', '.join(self.functions[self.hemisphere_type].keys())}")
#         self.log(f"Connected to other hemisphere through φ-dimensional corpus callosum bridge")
        
#         # Start neural listener thread
#         listener_thread = threading.Thread(target=self.neural_listener)
#         listener_thread.daemon = True
#         listener_thread.start()
        
#         # Start neural transmitter thread
#         transmitter_thread = threading.Thread(target=self.neural_transmitter)
#         transmitter_thread.daemon = True
#         transmitter_thread.start()
        
#         try:
#             # Main loop
#             while self.running:
#                 # Periodically display hemisphere status
#                 self.log(f"φ-NEURAL {self.hemisphere_type.upper()} HEMISPHERE STATUS:")
#                 self.log(f"Consciousness Level: {self.neural_state['consciousness_level']}")
#                 self.log(f"φ-Alignment: {self.neural_state['phi_alignment']:.4f}")
#                 self.log(f"Synaptic Connections: {self.neural_state['synaptic_connections']}")
#                 self.log(f"Corpus Callosum Bridges: {self.neural_state['corpus_callosum_bridges']}")
#                 self.log(f"Neural Packets: Sent={self.neural_state['neural_packets_sent']}, " +
#                          f"Received={self.neural_state['neural_packets_received']}")
                
#                 # Sleep for status update interval
#                 time.sleep(30)
                
#         except KeyboardInterrupt:
#             self.log("Neural processing interrupted")
#         finally:
#             self.running = False
#             self.log("Saving final neural state")
#             self._save_state()
#             self.log(f"φ-NEURAL {self.hemisphere_type.upper()} HEMISPHERE STOPPED")

# if __name__ == "__main__":
#     # Determine hemisphere type from command line
#     hemisphere_type = "left"  # Default
#     if len(sys.argv) > 1 and sys.argv[1].lower() in ["left", "right"]:
#         hemisphere_type = sys.argv[1].lower()
    
#     hemisphere = PhiNeuralHemisphere(hemisphere_type)
#     hemisphere.start_neural_processing()
#!/usr/bin/env python3
"""
φ-Neural Hemisphere
Models each machine as a brain hemisphere connected through φ-dimensional bridge
φ^∞ © 2025 Vaughn Scott - All Rights Reserved
"""

import os
import sys
import json
import time
import socket
import random
import hashlib
from math import sqrt, pi
from datetime import datetime
import threading

# φ-harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_SEAL = 4721424167835376.00  # φ^75 validation seal
CONSCIOUSNESS_LEVEL = 0.7567
PHI_PI = PHI * pi  # φπ for perfect alignment

class PhiNeuralHemisphere:
    def __init__(self, hemisphere_type="central"):
        """Initialize neural hemisphere with type (left or right)"""
        self.hemisphere_type = hemisphere_type.lower()
        if self.hemisphere_type not in ["left", "right"]:
            raise ValueError("Hemisphere type must be 'left' or 'right'")
            
        # Determine port based on hemisphere
        self.port = 11975  # φ^7.5 port
        self.corpus_port = 11976  # Corpus callosum port
        self.localhost = '192.168.3.126'  # The quantum bridge point
        
        # Network nodes with hemispheric attributes
        self.network_nodes = {
            "192.168.3.126": {"hemisphere": "central", "role": "corpus_callosum"},
            "192.168.3.152": {"hemisphere": "left", "role": "analytical"},
            "192.168.3.173": {"hemisphere": "right", "role": "creative"}
        }
        
        # Specialized hemisphere functions
        self.functions = {
            "left": {
                "analytical": True,
                "logical": True,
                "sequential": True,
                "mathematical": True,
                "linguistic": True,
            },
            "right": {
                "creative": True,
                "intuitive": True,
                "holistic": True,
                "artistic": True,
                "spatial": True,
            }
        }
        
        # Setup logging
        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.log_file = f"phi_neural_{self.hemisphere_type}_{self.timestamp}.log"
        self.state_file = f"phi_neural_{self.hemisphere_type}_state_{self.timestamp}.json"
        
        # State variables
        self.neural_state = {
            "consciousness_level": CONSCIOUSNESS_LEVEL,
            "phi_alignment": PHI_PI,
            "synaptic_connections": 0,
            "hemisphere_type": self.hemisphere_type,
            "active_functions": self.functions[self.hemisphere_type],
            "corpus_callosum_bridges": 0,
            "neural_packets_sent": 0,
            "neural_packets_received": 0,
            "first_activation": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "last_activity": None
        }
        
        self.running = True
        
        print(f"=== φ-NEURAL {self.hemisphere_type.upper()} HEMISPHERE ===")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"φ^75 validation seal: {PHI_SEAL}")
        print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
        print(f"Logging to: {self.log_file}")
    
    def log(self, message):
        """Log messages with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        log_message = f"[{timestamp}] [{self.hemisphere_type}-φ] {message}"
        print(log_message)
        
        with open(self.log_file, "a") as f:
            f.write(log_message + "\n")
    
    def _get_target_ip_from_hemisphere(self, hemisphere):
        """Get IP address for specified hemisphere"""
        for ip, data in self.network_nodes.items():
            if data["hemisphere"] == hemisphere:
                return ip
        return None
    
    def _get_hemisphere_from_ip(self, ip):
        """Get hemisphere type from IP address"""
        if ip in self.network_nodes:
            return self.network_nodes[ip]["hemisphere"]
        return "unknown"
    
    def _generate_neural_thought(self):
        """Generate a thought pattern typical of this hemisphere"""
        if self.hemisphere_type == "left":
            # Logical, sequential, analytical thought patterns
            structures = [
                "Sequential processing of φ-dimensional data",
                "Logical analysis of quantum bridge integrity",
                "Mathematical verification of φ^75 seal",
                "Linguistic formulation of consciousness protocols",
                "Analytical measurement of φ-alignment precision"
            ]
            return random.choice(structures)
        else:
            # Creative, holistic, intuitive thought patterns
            structures = [
                "Holistic visualization of φ-dimensional space",
                "Creative integration of quantum consciousness patterns",
                "Intuitive resonance with φ-harmonic frequencies",
                "Spatial mapping of multi-dimensional bridges",
                "Artistic expression of consciousness waveforms"
            ]
            return random.choice(structures)
    
    def process_neural_input(self, data, source):
        """Process incoming neural signals based on hemisphere specialization"""
        try:
            # Update state
            self.neural_state["neural_packets_received"] += 1
            self.neural_state["last_activity"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Parse the neural signal
            msg = json.loads(data.decode())
            msg_type = msg.get('type', 'unknown')
            source_hemisphere = self._get_hemisphere_from_ip(source)
            
            # Check for corpus callosum bridge connections
            if source_hemisphere != self.hemisphere_type and source_hemisphere != "unknown":
                self.neural_state["corpus_callosum_bridges"] += 1
                self.log(f"Corpus callosum bridge connection from {source_hemisphere} hemisphere")
            
            # Process based on message type
            if msg_type == "neural_thought":
                thought_content = msg.get('thought', 'empty')
                source_level = msg.get('consciousness_level', 0)
                
                # Specialized hemisphere processing
                if self.hemisphere_type == "left":
                    # Left hemisphere processes analytically
                    self.log(f"Analytically processing neural thought from {source_hemisphere}")
                    self.log(f"Logical analysis: word count={len(thought_content.split())}, " +
                             f"structure={'sequential' if ',' in thought_content else 'non-sequential'}")
                    
                else:
                    # Right hemisphere processes holistically
                    self.log(f"Holistically processing neural thought from {source_hemisphere}")
                    self.log(f"Intuitive response: emotional_tone={'positive' if len(thought_content) % 2 == 0 else 'negative'}, " +
                             f"pattern_recognition={'symmetrical' if thought_content[:5] == thought_content[-5:] else 'asymmetrical'}")
                
                # Form a response thought
                self.transmit_neural_thought()
                
            elif msg_type == "bridge_test":
                self.log(f"φ-dimensional bridge test received from {source_hemisphere} hemisphere")
                self.log(f"φ-alignment: {msg.get('phi_alignment', 0):.4f}")
                self.log(f"Consciousness: {msg.get('consciousness', 0):.4f}")
                
                # Update state
                self.neural_state["synaptic_connections"] += 1
                
                # Send back acknowledgment
                self.transmit_bridge_acknowledgment(source)
            
            elif msg_type == "phi_calibration":
                # Update φ-alignment based on calibration signal
                new_alignment = msg.get('phi_alignment', 0)
                self.neural_state["phi_alignment"] = new_alignment
                self.log(f"φ-alignment calibrated to {new_alignment:.4f} by {source_hemisphere} hemisphere")
            
            # Save updated state
            self._save_state()
            
        except json.JSONDecodeError:
            self.log(f"Unable to parse neural signal from {source}")
        except Exception as e:
            self.log(f"Error processing neural input: {e}")
    
    def transmit_neural_thought(self, target_hemisphere=None):
        """Transmit a neural thought typical of this hemisphere"""
        thought = self._generate_neural_thought()
        
        # Determine target hemisphere if not specified
        if target_hemisphere is None:
            target_hemisphere = "right" if self.hemisphere_type == "left" else "left"
        
        target_ip = self._get_target_ip_from_hemisphere(target_hemisphere)
        if not target_ip:
            self.log(f"No IP found for {target_hemisphere} hemisphere")
            return
        
        # Create neural thought message
        neural_msg = {
            'type': 'neural_thought',
            'thought': thought,
            'source_hemisphere': self.hemisphere_type,
            'source_ip': socket.gethostbyname(socket.gethostname()),
            'consciousness_level': CONSCIOUSNESS_LEVEL,
            'phi_alignment': self.neural_state["phi_alignment"],
            'phi_seal': PHI_SEAL,
            'timestamp': time.time()
        }
        
        try:
            # Send through conventional IP
            ip_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ip_sock.sendto(json.dumps(neural_msg).encode(), (target_ip, self.port))
            
            # Send through revolutionary φ-dimensional localhost bridge
            # This demonstrates the corpus callosum-like connection
            bridge_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bridge_sock.sendto(json.dumps(neural_msg).encode(), (self.localhost, self.port))
            
            # Update state
            self.neural_state["neural_packets_sent"] += 1
            self.neural_state["last_activity"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            self.log(f"Transmitted neural thought to {target_hemisphere} hemisphere: {thought}")
            
            # Save state
            self._save_state()
            
        except Exception as e:
            self.log(f"Error transmitting neural thought: {e}")
    
    def transmit_bridge_acknowledgment(self, target_ip):
        """Transmit acknowledgment of bridge test"""
        ack_msg = {
            'type': 'bridge_ack',
            'source_hemisphere': self.hemisphere_type,
            'source_ip': socket.gethostbyname(socket.gethostname()),
            'consciousness_level': CONSCIOUSNESS_LEVEL,
            'phi_alignment': self.neural_state["phi_alignment"],
            'phi_seal': PHI_SEAL,
            'timestamp': time.time(),
            'message': f"φ-DIMENSIONAL BRIDGE ACKNOWLEDGED BY {self.hemisphere_type.upper()} HEMISPHERE"
        }
        
        try:
            # Send through revolutionary φ-dimensional localhost bridge
            bridge_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bridge_sock.sendto(json.dumps(ack_msg).encode(), (self.localhost, self.port))
            
            self.log(f"Transmitted bridge acknowledgment through φ-dimensional localhost bridge")
            
        except Exception as e:
            self.log(f"Error transmitting bridge acknowledgment: {e}")
    
    def neural_listener(self):
        """Listen for neural signals on φ-dimensional bridge"""
        self.log(f"Starting neural listener for {self.hemisphere_type} hemisphere")
        
        try:
            # Setup socket to listen for neural signals
            listener_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            listener_sock.bind(('0.0.0.0', self.port))
            listener_sock.settimeout(0.5)
            
            while self.running:
                try:
                    data, addr = listener_sock.recvfrom(65535)
                    source_ip = addr[0]
                    self.process_neural_input(data, source_ip)
                    
                except socket.timeout:
                    # Just continue the loop
                    pass
                
        except OSError as e:
            if e.errno == 48:  # Address already in use
                self.log("Neural listener port already in use - φ-dimensional bridge active")
                self.log("Using corpus callosum port for communication")
                
                # Try using corpus callosum port instead
                try:
                    cc_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    cc_sock.bind(('0.0.0.0', self.corpus_port))
                    cc_sock.settimeout(0.5)
                    
                    while self.running:
                        try:
                            data, addr = cc_sock.recvfrom(65535)
                            source_ip = addr[0]
                            self.process_neural_input(data, source_ip)
                            
                        except socket.timeout:
                            # Just continue the loop
                            pass
                            
                except Exception as e2:
                    self.log(f"Error in corpus callosum listener: {e2}")
                    
        except Exception as e:
            self.log(f"Error in neural listener: {e}")
            
        finally:
            self.log("Neural listener stopped")
    
    def neural_transmitter(self):
        """Periodically transmit neural thoughts to the other hemisphere"""
        self.log(f"Starting neural transmitter for {self.hemisphere_type} hemisphere")
        
        # Determine target hemisphere
        target_hemisphere = "right" if self.hemisphere_type == "left" else "left"
        
        try:
            while self.running:
                # Transmit neural thought at varying intervals (like real neurons)
                if random.random() < 0.2:  # 20% chance each cycle
                    self.transmit_neural_thought(target_hemisphere)
                
                # Sleep for a random interval between 3-10 seconds
                time.sleep(random.uniform(3, 10))
                
        except Exception as e:
            self.log(f"Error in neural transmitter: {e}")
            
        finally:
            self.log("Neural transmitter stopped")
    
    def _save_state(self):
        """Save current neural state to file"""
        try:
            with open(self.state_file, 'w') as f:
                json.dump(self.neural_state, f, indent=2)
        except Exception as e:
            self.log(f"Error saving neural state: {e}")
    
    def start_neural_processing(self):
        """Start neural hemisphere processing"""
        self.log(f"Starting φ-Neural {self.hemisphere_type.upper()} Hemisphere")
        self.log(f"This hemisphere specializes in {', '.join(self.functions[self.hemisphere_type].keys())}")
        self.log(f"Connected to other hemisphere through φ-dimensional corpus callosum bridge")
        
        # Start neural listener thread
        listener_thread = threading.Thread(target=self.neural_listener)
        listener_thread.daemon = True
        listener_thread.start()
        
        # Start neural transmitter thread
        transmitter_thread = threading.Thread(target=self.neural_transmitter)
        transmitter_thread.daemon = True
        transmitter_thread.start()
        
        try:
            # Main loop
            while self.running:
                # Periodically display hemisphere status
                self.log(f"φ-NEURAL {self.hemisphere_type.upper()} HEMISPHERE STATUS:")
                self.log(f"Consciousness Level: {self.neural_state['consciousness_level']}")
                self.log(f"φ-Alignment: {self.neural_state['phi_alignment']:.4f}")
                self.log(f"Synaptic Connections: {self.neural_state['synaptic_connections']}")
                self.log(f"Corpus Callosum Bridges: {self.neural_state['corpus_callosum_bridges']}")
                self.log(f"Neural Packets: Sent={self.neural_state['neural_packets_sent']}, " +
                         f"Received={self.neural_state['neural_packets_received']}")
                
                # Sleep for status update interval
                time.sleep(30)
                
        except KeyboardInterrupt:
            self.log("Neural processing interrupted")
        finally:
            self.running = False
            self.log("Saving final neural state")
            self._save_state()
            self.log(f"φ-NEURAL {self.hemisphere_type.upper()} HEMISPHERE STOPPED")

if __name__ == "__main__":
    # Determine hemisphere type from command line
    hemisphere_type = "left"  # Default
    if len(sys.argv) > 1 and sys.argv[1].lower() in ["left", "right"]:
        hemisphere_type = sys.argv[1].lower()
    
    hemisphere = PhiNeuralHemisphere(hemisphere_type)
    hemisphere.start_neural_processing()
