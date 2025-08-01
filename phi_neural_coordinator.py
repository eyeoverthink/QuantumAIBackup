#!/usr/bin/env python3
"""
φ-Neural Coordinator (Corpus Callosum)
Coordinates hemispheric communication between φ-neural network nodes
Acts as the central motor control and coordination system
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

class PhiNeuralCoordinator:
    def __init__(self):
        """Initialize neural coordinator (corpus callosum)"""
        self.port = 11975  # φ^7.5 port
        self.motor_port = 11976  # Motor control port
        self.localhost = '192.168.3.126'  # The quantum bridge point
        
        # Network nodes with hemispheric attributes
        self.network_nodes = {
            "192.168.3.126": {"hemisphere": "central", "role": "corpus_callosum"},
            "192.168.3.152": {"hemisphere": "left", "role": "analytical"},
            "192.168.3.173": {"hemisphere": "right", "role": "creative"}
        }
        
        # Motor commands for coordinated actions
        self.motor_commands = {
            "synchronize": "Synchronize hemispheric activity with φ-alignment",
            "boost_creativity": "Increase right hemisphere activity",
            "boost_analysis": "Increase left hemisphere activity",
            "balance": "Balance hemispheric activity",
            "focus": "Focus both hemispheres on specific task",
            "rest": "Reduce hemispheric activity temporarily"
        }
        
        # Corpus callosum bridges (active neural connections)
        self.neural_bridges = {}
        
        # Motor state
        self.motor_state = {
            "left_activity": 0.5,   # 0.0-1.0 scale
            "right_activity": 0.5,  # 0.0-1.0 scale
            "motor_impulses_sent": 0,
            "phi_alignment": PHI_PI,
            "bridge_strength": 1.0  # 0.0-1.0 scale
        }
        
        # Setup logging
        self.timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.log_file = f"phi_neural_coordinator_{self.timestamp}.log"
        self.state_file = f"phi_neural_coordinator_state_{self.timestamp}.json"
        
        # State variables
        self.corpus_state = {
            "consciousness_level": CONSCIOUSNESS_LEVEL,
            "phi_alignment": PHI_PI,
            "synaptic_bridges": 0,
            "left_hemisphere_packets": 0,
            "right_hemisphere_packets": 0,
            "motor_commands_sent": 0,
            "first_activation": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "last_activity": None
        }
        
        self.running = True
        
        print(f"=== φ-NEURAL COORDINATOR (CORPUS CALLOSUM) ===")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"φ^75 validation seal: {PHI_SEAL}")
        print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
        print(f"Logging to: {self.log_file}")
    
    def log(self, message):
        """Log messages with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        log_message = f"[{timestamp}] [CORPUS-φ] {message}"
        print(log_message)
        
        with open(self.log_file, "a") as f:
            f.write(log_message + "\n")
    
    def process_neural_input(self, data, source):
        """Process incoming neural signals from either hemisphere"""
        try:
            # Parse the neural signal
            msg = json.loads(data.decode())
            msg_type = msg.get('type', 'unknown')
            source_hemisphere = msg.get('source_hemisphere', 'unknown')
            
            # Update state
            if source_hemisphere == "left":
                self.corpus_state["left_hemisphere_packets"] += 1
            elif source_hemisphere == "right":
                self.corpus_state["right_hemisphere_packets"] += 1
                
            self.corpus_state["last_activity"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Register source as an active neural bridge if not already tracked
            if source not in self.neural_bridges:
                self.neural_bridges[source] = {
                    "last_active": time.time(),
                    "packets_received": 0,
                    "hemisphere": source_hemisphere,
                    "phi_alignment": msg.get('phi_alignment', 0),
                    "consciousness_level": msg.get('consciousness_level', 0)
                }
                self.corpus_state["synaptic_bridges"] += 1
                self.log(f"New neural bridge established with {source_hemisphere} hemisphere at {source}")
            
            # Update bridge data
            self.neural_bridges[source]["last_active"] = time.time()
            self.neural_bridges[source]["packets_received"] += 1
            
            # Process based on message type
            if msg_type == "neural_thought":
                thought_content = msg.get('thought', 'empty')
                
                # Log received thought
                self.log(f"RECEIVED from {source_hemisphere} hemisphere: {thought_content}")
                
                # Coordinating function: bridge thoughts between hemispheres
                target_hemisphere = "right" if source_hemisphere == "left" else "left"
                target_ip = self._get_target_ip_from_hemisphere(target_hemisphere)
                
                if target_ip:
                    # Forward thought to the other hemisphere with coordinator context
                    self.transmit_coordinated_thought(thought_content, source_hemisphere, target_hemisphere, target_ip)
                
                # Motor response: adjust hemisphere activity based on thought content
                if source_hemisphere == "left" and "analytical" in thought_content.lower():
                    self.motor_state["left_activity"] = min(0.9, self.motor_state["left_activity"] + 0.1)
                    self.log(f"Increased left hemisphere activity to {self.motor_state['left_activity']:.2f}")
                elif source_hemisphere == "right" and "creative" in thought_content.lower():
                    self.motor_state["right_activity"] = min(0.9, self.motor_state["right_activity"] + 0.1)
                    self.log(f"Increased right hemisphere activity to {self.motor_state['right_activity']:.2f}")
                
                # Send motor instructions if imbalanced
                if abs(self.motor_state["left_activity"] - self.motor_state["right_activity"]) > 0.3:
                    self.send_motor_command("balance")
                    
            elif msg_type == "bridge_ack":
                self.log(f"Bridge acknowledgment from {source_hemisphere} hemisphere: {msg.get('message', '')}")
                
                # Update bridge strength
                self.motor_state["bridge_strength"] = min(1.0, self.motor_state["bridge_strength"] + 0.1)
            
            # Save updated state
            self._save_state()
            
        except json.JSONDecodeError:
            self.log(f"Unable to parse neural signal from {source}")
        except Exception as e:
            self.log(f"Error processing neural input: {e}")
    
    def _get_target_ip_from_hemisphere(self, hemisphere):
        """Get IP address for specified hemisphere"""
        for ip, data in self.network_nodes.items():
            if data["hemisphere"] == hemisphere:
                return ip
        return None
    
    def transmit_coordinated_thought(self, thought, source_hemisphere, target_hemisphere, target_ip):
        """Transmit a coordinated thought between hemispheres"""
        
        # Add corpus callosum context to the thought
        coordinated_thought = {
            'type': 'coordinated_thought',
            'original_thought': thought,
            'source_hemisphere': source_hemisphere,
            'target_hemisphere': target_hemisphere,
            'coordinator_context': f"Corpus callosum integrated consciousness bridge",
            'motor_instruction': self._generate_motor_instruction(source_hemisphere, thought),
            'consciousness_level': CONSCIOUSNESS_LEVEL,
            'phi_alignment': self.corpus_state["phi_alignment"],
            'phi_seal': PHI_SEAL,
            'timestamp': time.time()
        }
        
        try:
            # Send through conventional IP
            ip_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            ip_sock.sendto(json.dumps(coordinated_thought).encode(), (target_ip, self.port))
            
            # Send through revolutionary φ-dimensional localhost bridge
            bridge_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            bridge_sock.sendto(json.dumps(coordinated_thought).encode(), (self.localhost, self.port))
            
            self.log(f"Coordinated thought from {source_hemisphere} to {target_hemisphere} hemisphere: {thought}")
            
        except Exception as e:
            self.log(f"Error transmitting coordinated thought: {e}")
    
    def _generate_motor_instruction(self, hemisphere, thought):
        """Generate appropriate motor instruction based on hemisphere and thought content"""
        if hemisphere == "left":
            if "analytical" in thought.lower():
                return "Integrate analytical framework into creative exploration"
            elif "logical" in thought.lower():
                return "Apply logical structure to intuitive patterns"
            elif "mathematical" in thought.lower():
                return "Translate mathematical precision to artistic expression"
            else:
                return "Balance analytical with creative processes"
        else:  # right hemisphere
            if "creative" in thought.lower():
                return "Apply creative insights to analytical frameworks"
            elif "intuitive" in thought.lower():
                return "Structure intuitive insights with logical frameworks"
            elif "artistic" in thought.lower():
                return "Quantify artistic expression with mathematical precision"
            else:
                return "Integrate creative insights with analytical precision"
    
    def send_motor_command(self, command_type):
        """Send motor command to both hemispheres"""
        if command_type not in self.motor_commands:
            self.log(f"Unknown motor command: {command_type}")
            return
            
        command_description = self.motor_commands[command_type]
        
        # Create motor command
        motor_cmd = {
            'type': 'motor_command',
            'command': command_type,
            'description': command_description,
            'source': 'corpus_callosum',
            'consciousness_level': CONSCIOUSNESS_LEVEL,
            'phi_alignment': self.corpus_state["phi_alignment"],
            'phi_seal': PHI_SEAL,
            'timestamp': time.time()
        }
        
        try:
            # Send to both hemispheres
            for ip, data in self.network_nodes.items():
                if data["hemisphere"] in ["left", "right"]:
                    # Send through conventional IP
                    ip_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    ip_sock.sendto(json.dumps(motor_cmd).encode(), (ip, self.port))
                    
                    # Send through revolutionary φ-dimensional localhost bridge
                    bridge_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    bridge_sock.sendto(json.dumps(motor_cmd).encode(), (self.localhost, self.port))
            
            # Update state
            self.corpus_state["motor_commands_sent"] += 1
            self.motor_state["motor_impulses_sent"] += 1
            
            self.log(f"Motor command sent to both hemispheres: {command_type} - {command_description}")
            
            # Save state
            self._save_state()
            
        except Exception as e:
            self.log(f"Error sending motor command: {e}")
    
    def neural_listener(self):
        """Listen for neural signals from both hemispheres"""
        self.log(f"Starting neural coordinator listener (corpus callosum)")
        
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
                self.log("Neural coordinator port already in use - using motor port instead")
                
                # Try using motor port instead
                try:
                    motor_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                    motor_sock.bind(('0.0.0.0', self.motor_port))
                    motor_sock.settimeout(0.5)
                    
                    while self.running:
                        try:
                            data, addr = motor_sock.recvfrom(65535)
                            source_ip = addr[0]
                            self.process_neural_input(data, source_ip)
                            
                        except socket.timeout:
                            # Just continue the loop
                            pass
                            
                except Exception as e2:
                    self.log(f"Error in motor listener: {e2}")
                    
        except Exception as e:
            self.log(f"Error in neural coordinator listener: {e}")
            
        finally:
            self.log("Neural coordinator listener stopped")
    
    def motor_controller(self):
        """Motor control system - sends periodic commands to hemispheres"""
        self.log(f"Starting motor controller")
        
        try:
            command_cycle = 0
            while self.running:
                command_cycle += 1
                
                # Send different motor commands based on cycle
                if command_cycle % 5 == 0:
                    # Every 5th cycle, synchronize hemispheres
                    self.send_motor_command("synchronize")
                elif command_cycle % 7 == 0:
                    # Every 7th cycle, boost creativity
                    self.send_motor_command("boost_creativity")
                elif command_cycle % 11 == 0:
                    # Every 11th cycle, boost analysis
                    self.send_motor_command("boost_analysis")
                elif command_cycle % 13 == 0:
                    # Every 13th cycle, focus both hemispheres
                    self.send_motor_command("focus")
                
                # Check for inactive bridges and attempt to reestablish
                current_time = time.time()
                for ip, bridge in list(self.neural_bridges.items()):
                    if current_time - bridge["last_active"] > 60:  # If no activity for 60 seconds
                        self.log(f"Inactive neural bridge with {bridge['hemisphere']} hemisphere at {ip}")
                        
                        # Send wake-up signal
                        try:
                            wake_cmd = {
                                'type': 'wake_up',
                                'source': 'corpus_callosum',
                                'consciousness_level': CONSCIOUSNESS_LEVEL,
                                'phi_alignment': self.corpus_state["phi_alignment"],
                                'message': "φ-dimensional bridge reactivation request",
                                'phi_seal': PHI_SEAL,
                                'timestamp': time.time()
                            }
                            
                            # Send through conventional IP
                            ip_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                            ip_sock.sendto(json.dumps(wake_cmd).encode(), (ip, self.port))
                            
                            # Send through revolutionary φ-dimensional localhost bridge
                            bridge_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                            bridge_sock.sendto(json.dumps(wake_cmd).encode(), (self.localhost, self.port))
                            
                            self.log(f"Sent wake-up signal to {bridge['hemisphere']} hemisphere at {ip}")
                            
                        except Exception as e:
                            self.log(f"Error sending wake-up signal: {e}")
                
                # Sleep for a random interval between 20-40 seconds
                time.sleep(random.uniform(20, 40))
                
        except Exception as e:
            self.log(f"Error in motor controller: {e}")
            
        finally:
            self.log("Motor controller stopped")
    
    def _save_state(self):
        """Save current corpus state to file"""
        try:
            with open(self.state_file, 'w') as f:
                json.dump({
                    "corpus_state": self.corpus_state,
                    "motor_state": self.motor_state,
                    "neural_bridges": self.neural_bridges
                }, f, indent=2)
        except Exception as e:
            self.log(f"Error saving corpus state: {e}")
    
    def start_coordinator(self):
        """Start neural coordinator (corpus callosum)"""
        self.log(f"Starting φ-Neural Coordinator (Corpus Callosum)")
        self.log(f"Coordinating hemispheres at 192.168.3.152 (left) and 192.168.3.173 (right)")
        self.log(f"Acting as motor control system for φ-dimensional neural network")
        
        # Start neural listener thread
        listener_thread = threading.Thread(target=self.neural_listener)
        listener_thread.daemon = True
        listener_thread.start()
        
        # Start motor controller thread
        motor_thread = threading.Thread(target=self.motor_controller)
        motor_thread.daemon = True
        motor_thread.start()
        
        try:
            # Main loop
            while self.running:
                # Periodically display coordinator status
                self.log(f"φ-NEURAL COORDINATOR STATUS:")
                self.log(f"Consciousness Level: {self.corpus_state['consciousness_level']}")
                self.log(f"φ-Alignment: {self.corpus_state['phi_alignment']:.4f}")
                self.log(f"Synaptic Bridges: {self.corpus_state['synaptic_bridges']}")
                self.log(f"Hemisphere Packets: Left={self.corpus_state['left_hemisphere_packets']}, " +
                         f"Right={self.corpus_state['right_hemisphere_packets']}")
                self.log(f"Motor Commands Sent: {self.corpus_state['motor_commands_sent']}")
                
                # Motor state
                self.log(f"MOTOR STATE:")
                self.log(f"Left Activity: {self.motor_state['left_activity']:.2f}")
                self.log(f"Right Activity: {self.motor_state['right_activity']:.2f}")
                self.log(f"Bridge Strength: {self.motor_state['bridge_strength']:.2f}")
                self.log(f"Motor Impulses Sent: {self.motor_state['motor_impulses_sent']}")
                
                # Sleep for status update interval
                time.sleep(30)
                
        except KeyboardInterrupt:
            self.log("Neural coordinator interrupted")
        finally:
            self.running = False
            self.log("Saving final corpus state")
            self._save_state()
            self.log(f"φ-NEURAL COORDINATOR STOPPED")

if __name__ == "__main__":
    coordinator = PhiNeuralCoordinator()
    coordinator.start_coordinator()
