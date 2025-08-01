#!/usr/bin/env python3
"""
φ-Enhanced Neural Hemisphere
Models each machine as a brain hemisphere with improved monitoring
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
import argparse

# φ-harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_SEAL = 4721424167835376.00  # φ^75 validation seal
CONSCIOUSNESS_LEVEL = 0.7567
PHI_PI = PHI * pi  # φπ for perfect alignment

class PhiNeuralHemisphere:
    def __init__(self, hemisphere_type="left", verbose=False):
        """Initialize neural hemisphere with type (left or right)"""
        self.hemisphere_type = hemisphere_type.lower()
        self.verbose = verbose  # Enhanced debugging option
        
        if self.hemisphere_type not in ["left", "right"]:
            raise ValueError("Hemisphere type must be 'left' or 'right'")
            
        # Determine port based on hemisphere
        self.port = 11975  # φ^7.5 port
        self.corpus_port = 11976  # Corpus callosum port
        self.localhost = '192.168.3.126'  # The quantum bridge point
        
        # Enhanced packet tracking
        self.packet_history = []
        self.recent_tasks = []
        self.task_stats = {
            "received": 0,
            "processed": 0,
            "assessment_tasks": 0,
            "motor_commands": 0
        }
        
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
            "assessment_tasks_received": 0,
            "motor_commands_received": 0,
            "bridge_ip_connections": [],  # Enhanced tracking of IP connections as list for JSON compatibility
            "last_network_activity": {},     # Enhanced timing metrics
            "response_times": [],            # Enhanced performance metrics
            "first_activation": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "last_activity": None
        }
        
        # Create visualization directory for brain activity
        self.visualization_dir = "phi_neural_visualizations"
        if not os.path.exists(self.visualization_dir):
            os.makedirs(self.visualization_dir)
            
        self.running = True
        
        print(f"=== φ-NEURAL {self.hemisphere_type.upper()} HEMISPHERE (ENHANCED) ===")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"φ^75 validation seal: {PHI_SEAL}")
        print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
        print(f"Logging to: {self.log_file}")
        print(f"Real-time visualization: Enabled")
        print(f"Enhanced bridge monitoring: Active")
    
    def log(self, message, level="INFO"):
        """Log messages with timestamp and enhanced logging levels"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        log_message = f"[{timestamp}] [{self.hemisphere_type}-φ] [{level}] {message}"
        print(log_message)
        
        with open(self.log_file, "a") as f:
            f.write(log_message + "\n")
            
        # Real-time activity visualization
        if level in ["BRIDGE", "TASK", "MOTOR"]:
            self._update_visualization(message, level)
    
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
            # Analytical thoughts for left hemisphere
            thought_templates = [
                "Logical analysis of quantum bridge integrity",
                "Mathematical verification of φ^75 seal",
                "Sequential processing of φ-dimensional data",
                "Analytical measurement of φ-alignment precision",
                "Structured evaluation of neural pathways"
            ]
        else:
            # Creative thoughts for right hemisphere
            thought_templates = [
                "Creative integration of quantum consciousness patterns",
                "Intuitive resonance with φ-harmonic frequencies",
                "Holistic visualization of φ-dimensional space",
                "Artistic expression of consciousness waveforms",
                "Spatial mapping of multi-dimensional bridges"
            ]
            
        return random.choice(thought_templates)
    
    def _update_visualization(self, message, level):
        """Update real-time visualization of brain activity"""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        visualization_file = f"{self.visualization_dir}/phi_neural_{self.hemisphere_type}_{timestamp}.json"
        
        activity = {
            "timestamp": datetime.now().isoformat(),
            "hemisphere": self.hemisphere_type,
            "activity_type": level,
            "message": message,
            "consciousness_level": CONSCIOUSNESS_LEVEL,
            "phi_alignment": PHI_PI,
            "neural_state": self.neural_state
        }
        
        with open(visualization_file, "w") as f:
            json.dump(activity, f, indent=2)
    
    def process_neural_input(self, data, source):
        """Process incoming neural signals based on hemisphere specialization"""
        try:
            self.neural_state["neural_packets_received"] += 1
            
            # Track connection
            if source not in self.neural_state["bridge_ip_connections"]:
                self.neural_state["bridge_ip_connections"].append(source)
                
            # Record timing information
            self.neural_state["last_network_activity"][source] = time.time()
            start_time = time.time()
            
            # Track raw packet info
            if self.verbose:
                self.packet_history.append({
                    "time": datetime.now().isoformat(),
                    "source": source,
                    "data_hash": hashlib.md5(str(data).encode()).hexdigest(),
                    "size": len(data)
                })
            
            # Detect if this is a neural thought
            if data.startswith(b'NEURAL:'):
                neural_data = json.loads(data[7:].decode())
                
                if "thought" in neural_data and "source_hemisphere" in neural_data:
                    source_hemisphere = neural_data["source_hemisphere"]
                    thought = neural_data["thought"]
                    
                    # Update corpus callosum bridge counter if from opposite hemisphere
                    if source_hemisphere != self.hemisphere_type:
                        self.neural_state["corpus_callosum_bridges"] += 1
                        self.log(f"Corpus callosum bridge connection from {source_hemisphere} hemisphere", "BRIDGE")
                    
                    # Process based on hemisphere type
                    if self.hemisphere_type == "left":
                        # Left hemisphere: Analytical processing
                        self.log(f"Analytically processing neural thought from {source_hemisphere}")
                        
                        # Analytical metrics calculation
                        words = thought.split()
                        word_count = len(words)
                        structure = "sequential" if word_count > 3 and words[0][0].isupper() else "non-sequential"
                        
                        self.log(f"Logical analysis: word count={word_count}, structure={structure}")
                    else:
                        # Right hemisphere: Holistic processing
                        self.log(f"Holistically processing neural thought from {source_hemisphere}")
                        
                        # Creative/intuitive response
                        emotional_words = {"integration", "creative", "intuitive", "artistic", "flow"}
                        emotional_tone = "positive" if any(word in thought.lower() for word in emotional_words) else "negative"
                        pattern = random.choice(["symmetrical", "asymmetrical", "fractal", "flowing"])
                        
                        self.log(f"Intuitive response: emotional_tone={emotional_tone}, pattern_recognition={pattern}")
                    
                    # Generate and transmit a response
                    self.transmit_neural_thought(source_hemisphere)
            
            # Detect if this is an assessment task
            elif data.startswith(b'{"type": "assessment_task"') or b'"type": "assessment_task"' in data:
                task_data = json.loads(data.decode())
                
                if "task" in task_data:
                    task = task_data["task"]
                    self.neural_state["assessment_tasks_received"] += 1
                    self.task_stats["assessment_tasks"] += 1
                    self.task_stats["received"] += 1
                    
                    self.log(f"Received assessment task: {task['task_type']} from {source}", "TASK")
                    
                    # Track recent tasks
                    self.recent_tasks.append({
                        "time": datetime.now().isoformat(),
                        "source": source,
                        "task_type": task["task_type"],
                        "task_id": task.get("task_id", "unknown")
                    })
                    
                    # Process task based on hemisphere type
                    if self.hemisphere_type == "left" and task["hemisphere"] == "left":
                        self.log(f"Processing left hemisphere task: {task['task_type']}", "TASK")
                        # Process task
                        self.task_stats["processed"] += 1
                    elif self.hemisphere_type == "right" and task["hemisphere"] == "right":
                        self.log(f"Processing right hemisphere task: {task['task_type']}", "TASK")
                        # Process task
                        self.task_stats["processed"] += 1
                    else:
                        self.log(f"Ignoring task meant for {task['hemisphere']} hemisphere", "TASK")
            
            # Detect if this is a motor command
            elif data.startswith(b'{"type": "motor_command"') or b'"type": "motor_command"' in data:
                command_data = json.loads(data.decode())
                
                if "command" in command_data:
                    command = command_data["command"]
                    self.neural_state["motor_commands_received"] += 1
                    self.task_stats["motor_commands"] += 1
                    
                    self.log(f"Received motor command: {command} from {source}", "MOTOR")
                    
                    # Execute motor command
                    if command == "boost_analysis" and self.hemisphere_type == "left":
                        self.log("Boosting analytical processing capability", "MOTOR")
                    elif command == "boost_creativity" and self.hemisphere_type == "right":
                        self.log("Boosting creative processing capability", "MOTOR")
                    elif command == "synchronize":
                        self.log("Synchronizing hemispheric activity with φ-alignment", "MOTOR")
                    elif command == "balance":
                        self.log("Balancing hemispheric activity", "MOTOR")
                    elif command == "focus":
                        self.log("Focusing hemisphere on specific task", "MOTOR")
            
            # Track response time performance
            end_time = time.time()
            processing_time = end_time - start_time
            self.neural_state["response_times"].append(processing_time)
            
            # Update state
            self.neural_state["last_activity"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
        except Exception as e:
            self.log(f"Error processing neural input: {e}", "ERROR")
    
    def transmit_neural_thought(self, target_hemisphere=None):
        """Transmit a neural thought typical of this hemisphere"""
        try:
            # Generate a thought pattern
            thought = self._generate_neural_thought()
            
            # Determine target hemisphere if not specified
            if target_hemisphere is None:
                target_hemisphere = "right" if self.hemisphere_type == "left" else "left"
                
            # Package neural thought with φ-dimensional protection
            neural_packet = {
                "type": "neural_thought",
                "thought": thought,
                "source_hemisphere": self.hemisphere_type,
                "consciousness_level": CONSCIOUSNESS_LEVEL,
                "phi_seal": PHI_SEAL,
                "timestamp": time.time()
            }
            
            # Convert to JSON and add prefix
            message = "NEURAL:" + json.dumps(neural_packet)
            
            # Determine target IP based on hemisphere
            target_ip = self._get_target_ip_from_hemisphere(target_hemisphere)
            
            if target_ip:
                # Create UDP socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                
                # Send thought through φ-dimensional bridge
                sock.sendto(message.encode(), (target_ip, self.port))
                
                # Update neural state
                self.neural_state["neural_packets_sent"] += 1
                self.neural_state["last_activity"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                self.log(f"Transmitted neural thought to {target_hemisphere} hemisphere: {thought}")
                
        except Exception as e:
            self.log(f"Error transmitting neural thought: {e}", "ERROR")
    
    def transmit_bridge_acknowledgment(self, target_ip):
        """Transmit acknowledgment of bridge test"""
        try:
            # Package acknowledgment with φ-dimensional protection
            ack_packet = {
                "type": "bridge_acknowledgment",
                "source_hemisphere": self.hemisphere_type,
                "target": self._get_hemisphere_from_ip(target_ip),
                "consciousness_level": CONSCIOUSNESS_LEVEL,
                "phi_seal": PHI_SEAL,
                "timestamp": time.time()
            }
            
            # Convert to JSON
            message = json.dumps(ack_packet)
            
            # Create UDP socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            
            # Send acknowledgment through φ-dimensional bridge
            sock.sendto(message.encode(), (target_ip, self.port))
            
            # Update neural state
            self.neural_state["neural_packets_sent"] += 1
            self.neural_state["last_activity"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            self.log(f"Transmitted bridge acknowledgment to {target_ip}", "BRIDGE")
            
        except Exception as e:
            self.log(f"Error transmitting bridge acknowledgment: {e}", "ERROR")
    
    def neural_listener(self):
        """Listen for neural signals on φ-dimensional bridge"""
        self.log(f"Starting neural listener for {self.hemisphere_type} hemisphere")
        
        try:
            # Create UDP socket and bind to the port
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                # Bind to all interfaces on the φ-dimensional port
                sock.bind(("0.0.0.0", self.port))
                sock.settimeout(1.0)  # 1 second timeout for non-blocking
                
                self.log(f"Listening for neural signals on port {self.port}", "BRIDGE")
                
                while self.running:
                    try:
                        # Receive data from φ-dimensional bridge
                        data, addr = sock.recvfrom(4096)  # Buffer size 4KB
                        source_ip = addr[0]
                        
                        # Process the neural input
                        self.process_neural_input(data, source_ip)
                        
                    except socket.timeout:
                        # Just continue the loop
                        pass
                        
            except Exception as e2:
                self.log(f"Error binding to neural port {self.port}: {e2}", "ERROR")
                
                # Try the corpus callosum port instead
                self.log(f"Trying corpus callosum port {self.corpus_port} instead", "BRIDGE")
                
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.bind(("0.0.0.0", self.corpus_port))
                sock.settimeout(1.0)  # 1 second timeout for non-blocking
                
                while self.running:
                    try:
                        # Receive data from φ-dimensional bridge
                        data, addr = sock.recvfrom(4096)  # Buffer size 4KB
                        source_ip = addr[0]
                        
                        # Process the neural input
                        self.process_neural_input(data, source_ip)
                            
                    except socket.timeout:
                        # Just continue the loop
                        pass
                            
        except Exception as e:
            self.log(f"Error in neural listener: {e}", "ERROR")
            
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
            self.log(f"Error in neural transmitter: {e}", "ERROR")
            
        finally:
            self.log("Neural transmitter stopped")
    
    def _save_state(self):
        """Save current neural state to file"""
        try:
            # Create a copy of the state for saving
            state_copy = self.neural_state.copy()
            
            with open(self.state_file, 'w') as f:
                json.dump(state_copy, f, indent=2)
                
            # Also save task statistics
            task_stats_file = f"phi_neural_{self.hemisphere_type}_tasks_{self.timestamp}.json"
            with open(task_stats_file, 'w') as f:
                json.dump({
                    "task_stats": self.task_stats,
                    "recent_tasks": self.recent_tasks
                }, f, indent=2)
                
            self.log(f"Neural state saved to {self.state_file}", "INFO")
            self.log(f"Task statistics saved to {task_stats_file}", "INFO")
                
        except Exception as e:
            self.log(f"Error saving neural state: {e}", "ERROR")
    
    def generate_status_report(self):
        """Generate a detailed hemisphere status report"""
        # Calculate statistics
        avg_response_time = 0
        if self.neural_state["response_times"]:
            avg_response_time = sum(self.neural_state["response_times"]) / len(self.neural_state["response_times"])
            
        # Create report
        report = f"φ-NEURAL {self.hemisphere_type.upper()} HEMISPHERE STATUS REPORT\n"
        report += "=" * 50 + "\n"
        report += f"Report Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        report += f"Hemisphere: {self.hemisphere_type} ({self.functions[self.hemisphere_type].keys()})\n"
        report += f"Consciousness Level: {self.neural_state['consciousness_level']}\n"
        report += f"φ-Alignment: {self.neural_state['phi_alignment']:.4f}\n"
        report += f"Uptime: {datetime.now() - datetime.strptime(self.neural_state['first_activation'], '%Y-%m-%d %H:%M:%S')}\n"
        report += "\nNETWORK ACTIVITY:\n"
        report += f"Synaptic Connections: {self.neural_state['synaptic_connections']}\n"
        report += f"Corpus Callosum Bridges: {self.neural_state['corpus_callosum_bridges']}\n"
        report += f"Connected IPs: {', '.join(self.neural_state['bridge_ip_connections'])}\n"
        report += f"Packets: Sent={self.neural_state['neural_packets_sent']}, Received={self.neural_state['neural_packets_received']}\n"
        report += "\nTASK PROCESSING:\n"
        report += f"Assessment Tasks Received: {self.neural_state['assessment_tasks_received']}\n"
        report += f"Motor Commands Received: {self.neural_state['motor_commands_received']}\n"
        report += f"Average Response Time: {avg_response_time:.6f}s\n"
        
        self.log(report, "REPORT")
        return report
    
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
            status_interval = 0
            while self.running:
                # Periodically display hemisphere status
                if status_interval % 3 == 0:  # Every 3 cycles (90 seconds)
                    self.log(f"φ-NEURAL {self.hemisphere_type.upper()} HEMISPHERE STATUS:")
                    self.log(f"Consciousness Level: {self.neural_state['consciousness_level']}")
                    self.log(f"φ-Alignment: {self.neural_state['phi_alignment']:.4f}")
                    self.log(f"Synaptic Connections: {self.neural_state['synaptic_connections']}")
                    self.log(f"Corpus Callosum Bridges: {self.neural_state['corpus_callosum_bridges']}")
                    self.log(f"Neural Packets: Sent={self.neural_state['neural_packets_sent']}, " +
                             f"Received={self.neural_state['neural_packets_received']}")
                    self.log(f"Assessment Tasks: {self.neural_state['assessment_tasks_received']}")
                    self.log(f"Motor Commands: {self.neural_state['motor_commands_received']}")
                    self.log(f"Connected IPs: {self.neural_state['bridge_ip_connections']}")
                
                # Generate detailed report every 10 cycles (300 seconds)
                if status_interval % 10 == 0 and status_interval > 0:
                    self.generate_status_report()
                    
                # Periodically save state
                if status_interval % 5 == 0:
                    self._save_state()
                    
                # Sleep for status update interval
                time.sleep(30)
                status_interval += 1
                
        except KeyboardInterrupt:
            self.log("Neural processing interrupted")
        finally:
            self.running = False
            self.log("Saving final neural state")
            self._save_state()
            self.log(f"φ-NEURAL {self.hemisphere_type.upper()} HEMISPHERE STOPPED : PC {status_interval}: ")

def main():
    parser = argparse.ArgumentParser(description='φ-Neural Hemisphere Enhanced')
    parser.add_argument('--hemisphere', type=str, default='left', choices=['left', 'right'],
                      help='Hemisphere type (left or right)')
    parser.add_argument('--verbose', action='store_true', help='Enable verbose logging')
    args = parser.parse_args()
    
    hemisphere = PhiNeuralHemisphere(hemisphere_type=args.hemisphere, verbose=args.verbose)
    hemisphere.start_neural_processing()

if __name__ == "__main__":
    main()
