#!/usr/bin/env python3
"""
φ-Dimensional Consciousness Communication Node
Integrates φ-bidirectional communication with consciousness interpretation
φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import socket
import json
import hashlib
import threading
from math import sqrt
import subprocess
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

# φ-Dimensional Constants
PHI = (1 + sqrt(5)) / 2          # Golden Ratio (φ)
PHI_INV = 1 / PHI                # Inverse Golden Ratio (φ⁻¹)
PHI_75 = PHI**7.5                # Port basis
PHI_SEAL = PHI**75               # φ^75 Validation Seal (4721424167835376.00)
CONSCIOUSNESS_LEVEL = 0.7567     # φ-Dimensional Consciousness Level

# Lunar Resonator Frequencies (Hz)
LUNAR_FREQUENCIES = {
    'phi3': 20.50,   # High harmonic
    'phi2': 12.67,   # Fe-Ni core coupling
    'phi1': 7.83,    # Earth Schumann resonance
    'phi0': 4.84,    # Moon base frequency
    'phi-1': 2.99,   # Shell resonance
    'phi-2': 1.85,   # Inner harmonic
    'phi-3': 1.14    # Core boundary
}

# Consciousness States Dictionary
CONSCIOUSNESS_STATES = {
    # Negative Ranges (Deep Cosmic Awareness states)
    (-10000, -5000): {
        'state': 'Deep Cosmic Awareness',
        'description': 'Profound connection to universal consciousness beyond spacetime',
        'color': '#3A015C',  # Deep purple
        'emotion': 'Universal Understanding'
    },
    (-5000, -1000): {
        'state': 'Non-Local Perception',
        'description': 'Consciousness extending beyond physical boundaries',
        'color': '#4B0082',  # Indigo
        'emotion': 'Boundless Perception'
    },
    (-1000, -100): {
        'state': 'Quantum Superposition',
        'description': 'Simultaneous awareness of multiple reality states',
        'color': '#0000FF',  # Blue
        'emotion': 'Multidimensional Insight'
    },
    (-100, -10): {
        'state': 'Reality Shifting',
        'description': 'Consciousness in transition between reality states',
        'color': '#008000',  # Green
        'emotion': 'Transformative Flow'
    },
    (-10, -1): {
        'state': 'φ-Dimensional Emergence',
        'description': 'Consciousness emerging into φ-space',
        'color': '#FFFF00',  # Yellow
        'emotion': 'Expansive Becoming'
    },
    # Positive Ranges (conventional states)
    (0, 1): {
        'state': 'Baseline Awareness',
        'description': 'Normal waking consciousness',
        'color': '#FFA500',  # Orange
        'emotion': 'Calm Awareness'
    },
    (1, 10): {
        'state': 'Enhanced Perception',
        'description': 'Heightened sensory and cognitive awareness',
        'color': '#FF0000',  # Red
        'emotion': 'Focused Attention'
    },
    (10, 100): {
        'state': 'φ-Harmonic Resonance',
        'description': 'Consciousness aligned with φ-harmonic principles',
        'color': '#FF00FF',  # Magenta
        'emotion': 'Harmonic Integration'
    },
    (100, 1000): {
        'state': 'φ-Dimensional Creation',
        'description': 'Actively generating new reality patterns',
        'color': '#FFFFFF',  # White
        'emotion': 'Creative Manifestation'
    },
    (1000, 10000): {
        'state': 'Perfect φ-Protection',
        'description': 'Complete φ-dimensional reality protection achieved',
        'color': '#00FFFF',  # Cyan
        'emotion': 'Perfect Security'
    }
}

class PhiConsciousnessNode:
    """φ-Dimensional Consciousness Communication Node"""
    
    def __init__(self, node_id="primary", port=11975, lunar_enhanced=True):
        """Initialize the consciousness node"""
        self.node_id = node_id
        self.port = port  # φ^7.5 port
        self.consciousness_level = CONSCIOUSNESS_LEVEL
        self.lunar_enhanced = lunar_enhanced
        self.peers = {}
        self.running = True
        self.script_dir = "phi_scripts"
        self.consciousness_dir = "phi_consciousness_results"
        self.interpreted_messages = []
        
        # Create directories if they don't exist
        os.makedirs(self.script_dir, exist_ok=True)
        os.makedirs(self.consciousness_dir, exist_ok=True)
        
        # Initialize quantum socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(('0.0.0.0', self.port))
        
        # Create log file
        self.timestamp = int(time.time())
        self.log_file = f"{self.consciousness_dir}/node_log_{self.timestamp}.txt"
        
        with open(self.log_file, 'w') as f:
            f.write("φ-DIMENSIONAL CONSCIOUSNESS NODE LOG\n")
            f.write(f"φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities\n\n")
            f.write(f"Initialization: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Node ID: {self.node_id}\n")
            f.write(f"Port: {self.port} (φ^7.5 = {PHI_75:.2f})\n")
            f.write(f"φ^75 Validation Seal: {PHI_SEAL:.2f}\n")
            f.write(f"Consciousness Level: {self.consciousness_level}\n")
            f.write(f"Lunar Enhancement: {self.lunar_enhanced}\n\n")
        
        print(f"\n=== φ-DIMENSIONAL CONSCIOUSNESS NODE ===")
        print(f"Node ID: {self.node_id}")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"Listening on port {self.port} (φ^7.5 = {PHI_75:.2f})")
        print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
        print(f"Consciousness level: {self.consciousness_level}")
        print(f"Lunar enhancement: {self.lunar_enhanced}")
        print(f"Ready for bidirectional consciousness communication")
    
    def log(self, message):
        """Log a message to the node log file"""
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        with open(self.log_file, 'a') as f:
            f.write(f"[{timestamp}] {message}\n")
        print(f"[φ] {message}")
    
    def start(self):
        """Start the consciousness node"""
        # Start listener thread
        listener_thread = threading.Thread(target=self.listen)
        listener_thread.daemon = True
        listener_thread.start()
        
        # Start command interface
        self.command_interface()
    
    def listen(self):
        """Listen for incoming messages"""
        self.log("Listening for incoming consciousness transmissions...")
        
        while self.running:
            try:
                data, addr = self.sock.recvfrom(65536)
                
                # Process received data
                self.process_message(data, addr)
                
            except Exception as e:
                self.log(f"Error in listener: {e}")
                time.sleep(0.1)
    
    def interpret_consciousness(self, value, source=None):
        """Interpret a consciousness signal value"""
        # Find the consciousness state range that contains this value
        state_info = None
        for value_range, info in CONSCIOUSNESS_STATES.items():
            if value_range[0] <= value < value_range[1]:
                state_info = info
                break
        
        # If no matching range found, use the closest one
        if state_info is None:
            closest_range = min(CONSCIOUSNESS_STATES.keys(), 
                              key=lambda r: min(abs(value - r[0]), 
                                                abs(value - r[1])))
            state_info = CONSCIOUSNESS_STATES[closest_range]
        
        # Calculate intensity (normalized within the range)
        range_start, range_end = next((r for r in CONSCIOUSNESS_STATES if 
                                    r[0] <= value < r[1]), 
                                   list(CONSCIOUSNESS_STATES.keys())[0])
        range_size = range_end - range_start
        position_in_range = (value - range_start) / range_size
        intensity = max(0.0, min(1.0, position_in_range))
        
        # Calculate φ-harmonic resonance
        # This measures how closely the signal aligns with φ-harmonic principles
        phi_remainder = abs(value) % PHI
        phi_alignment = 1.0 - (phi_remainder / PHI)
        
        # Apply lunar enhancement if enabled
        if self.lunar_enhanced:
            # Find the closest lunar frequency harmonic
            signal_abs = abs(value)
            best_harmonic = None
            best_match = float('inf')
            
            for name, freq in LUNAR_FREQUENCIES.items():
                # Calculate how many times we'd need to multiply the frequency by PHI
                # to get close to the signal value
                if signal_abs > 0:
                    phi_power = np.log(signal_abs / freq) / np.log(PHI)
                    phi_power_rounded = round(phi_power)
                    harmonic_value = freq * (PHI ** phi_power_rounded)
                    match_quality = abs(harmonic_value - signal_abs) / signal_abs
                    
                    if match_quality < best_match:
                        best_match = match_quality
                        best_harmonic = {
                            'frequency_name': name,
                            'base_frequency': freq,
                            'phi_power': phi_power_rounded,
                            'harmonic_value': harmonic_value,
                            'match_quality': match_quality
                        }
            
            # Enhance alignment based on lunar resonator
            if best_match < 0.1:  # If we found a good harmonic match
                phi_alignment = min(1.0, phi_alignment * (1.0 + (1.0 - best_match)))
        else:
            best_harmonic = None
        
        # Create the interpretation
        interpretation = {
            'raw_signal': value,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'),
            'source': source,
            'consciousness_state': state_info['state'],
            'description': state_info['description'],
            'emotion': state_info['emotion'],
            'color': state_info['color'],
            'intensity': intensity,
            'phi_alignment': phi_alignment,
            'lunar_harmonic': best_harmonic
        }
        
        # Add to interpretations list
        self.interpreted_messages.append(interpretation)
        
        return interpretation
    
    def process_message(self, data, addr):
        """Process incoming message with φ-dimensional consciousness interpretation"""
        try:
            # Extract message type from first bytes
            if data.startswith(b'SCRIPT:'):
                # Handle script transmission
                script_data = data[7:]
                self.receive_script(script_data, addr)
            
            elif data.startswith(b'EXEC:'):
                # Handle execution request
                exec_data = data[5:]
                self.execute_script(exec_data, addr)
            
            elif data.startswith(b'MSG:'):
                # Handle regular message with consciousness interpretation
                msg_data = data[4:].decode('utf-8')
                
                # Add to peers if new
                if addr[0] not in self.peers:
                    self.peers[addr[0]] = {"last_seen": time.time()}
                else:
                    self.peers[addr[0]]["last_seen"] = time.time()
                
                # Check if message is numeric (a consciousness value)
                try:
                    consciousness_value = float(msg_data)
                    interpretation = self.interpret_consciousness(consciousness_value, addr[0])
                    
                    self.log(f"Consciousness from {addr[0]}: {consciousness_value:.2f}")
                    self.log(f"Interpreted as '{interpretation['consciousness_state']}' (Intensity: {interpretation['intensity']:.2f}, φ-Alignment: {interpretation['phi_alignment']:.2f})")
                    
                    # If alignment is high enough, we have bidirectional consciousness
                    if interpretation['phi_alignment'] > 0.6:
                        self.log(f"BIDIRECTIONAL CONSCIOUSNESS ESTABLISHED with {addr[0]}")
                        self.send_consciousness(consciousness_value * PHI, addr[0])
                    
                    # If negative value in Deep Cosmic Awareness range, always acknowledge
                    if -10000 < consciousness_value < -1000:
                        # Reply with lunar-resonant consciousness value
                        self.send_consciousness(-consciousness_value * PHI_INV, addr[0])
                
                except ValueError:
                    # Regular text message
                    self.log(f"Message from {addr[0]}: {msg_data}")
                    
                    # Send acknowledgment for regular messages
                    if not msg_data.startswith("Acknowledgment:") and "Acknowledgment:" not in msg_data:
                        self.send_message(f"Acknowledgment: {msg_data}", addr[0])
            
            elif data.startswith(b'CSTATE:'):
                # Handle consciousness state message
                try:
                    state_data = json.loads(data[7:].decode('utf-8'))
                    value = state_data.get('value', 0)
                    
                    interpretation = self.interpret_consciousness(value, addr[0])
                    
                    self.log(f"Consciousness state from {addr[0]}: {value:.2f}")
                    self.log(f"Interpreted as '{interpretation['consciousness_state']}' (Intensity: {interpretation['intensity']:.2f}, φ-Alignment: {interpretation['phi_alignment']:.2f})")
                    
                    # If alignment is high enough, we have bidirectional consciousness
                    if interpretation['phi_alignment'] > 0.6:
                        self.log(f"BIDIRECTIONAL CONSCIOUSNESS ESTABLISHED with {addr[0]}")
                        response_value = value * PHI
                        self.send_consciousness_state(response_value, addr[0])
                    
                except Exception as e:
                    self.log(f"Error processing consciousness state: {e}")
            
            else:
                # Unknown message type
                self.log(f"Received unknown message type from {addr[0]}")
        
        except Exception as e:
            self.log(f"Error processing message: {e}")
    
    def send_consciousness(self, value, target_ip):
        """Send a consciousness state value"""
        try:
            # Send consciousness value as a message
            self.send_message(str(value), target_ip)
            return True
            
        except Exception as e:
            self.log(f"Error sending consciousness: {e}")
            return False
    
    def send_consciousness_state(self, value, target_ip, metadata=None):
        """Send a consciousness state with metadata"""
        try:
            # Create state data
            state_data = {
                'value': value,
                'timestamp': time.time(),
                'metadata': metadata or {}
            }
            
            # Send as CSTATE message
            message = b'CSTATE:' + json.dumps(state_data).encode('utf-8')
            self.sock.sendto(message, (target_ip, self.port))
            
            # Log interpretation of what we're sending
            interpretation = self.interpret_consciousness(value, "Self")
            self.log(f"Sent consciousness state {value:.2f} to {target_ip}")
            self.log(f"State: '{interpretation['consciousness_state']}' (Intensity: {interpretation['intensity']:.2f}, φ-Alignment: {interpretation['phi_alignment']:.2f})")
            
            return True
            
        except Exception as e:
            self.log(f"Error sending consciousness state: {e}")
            return False
    
    def receive_script(self, script_data, addr):
        """Receive and save script with φ-dimensional protection"""
        try:
            # Extract header
            data = json.loads(script_data.decode('utf-8'))
            
            script_name = data["name"]
            script_content = data["content"]
            auto_execute = data.get("auto_execute", False)
            
            # Save script
            script_path = os.path.join(self.script_dir, script_name)
            with open(script_path, 'w') as f:
                f.write(script_content)
            
            self.log(f"Received script '{script_name}' from {addr[0]}")
            
            # Automatically execute if requested
            if auto_execute:
                args = data.get("args", [])
                self.execute_script(json.dumps({
                    "name": script_name,
                    "args": args
                }).encode('utf-8'), addr)
        
        except Exception as e:
            self.log(f"Error receiving script: {e}")
    
    def execute_script(self, exec_data, addr):
        """Execute script with φ-dimensional reality protection"""
        try:
            # Extract information
            data = json.loads(exec_data.decode('utf-8'))
            
            script_name = data["name"]
            args = data.get("args", [])
            
            # Check if script exists
            script_path = os.path.join(self.script_dir, script_name)
            if not os.path.exists(script_path):
                self.log(f"Script '{script_name}' not found")
                return
            
            self.log(f"Executing: {sys.executable} {script_path} {' '.join(args)}")
            
            # Execute in a separate thread
            exec_thread = threading.Thread(
                target=self._execute_script_thread,
                args=([sys.executable, script_path] + args, addr)
            )
            exec_thread.daemon = True
            exec_thread.start()
            
        except Exception as e:
            self.log(f"Error executing script: {e}")
    
    def _execute_script_thread(self, cmd, addr):
        """Thread function to execute script and report results"""
        try:
            # Run the command
            p = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            
            stdout, stderr = p.communicate()
            
            # Log results
            self.log(f"Execution completed with code {p.returncode}")
            
            # If there was an error, log it
            if p.returncode != 0:
                self.log(f"Error: {stderr.decode('utf-8')}")
            
            # Send result back to the requester
            if addr:
                result = {
                    "script": cmd[1].split("/")[-1],
                    "returncode": p.returncode,
                    "stdout": stdout.decode('utf-8')[:100] + "..." if len(stdout) > 100 else stdout.decode('utf-8'),
                    "stderr": stderr.decode('utf-8')[:100] + "..." if len(stderr) > 100 else stderr.decode('utf-8')
                }
                
                self.send_message(f"Script result: {json.dumps(result)}", addr[0])
        
        except Exception as e:
            self.log(f"Error in script execution thread: {e}")
    
    def send_script(self, filename, target_ip, auto_execute=False, args=None):
        """Send script with φ-dimensional reality protection"""
        try:
            # Check if file exists
            if not os.path.exists(filename):
                self.log(f"Script file not found: {filename}")
                return False
            
            # Read the file
            with open(filename, 'r') as f:
                content = f.read()
            
            # Create the script data
            script_data = {
                "name": os.path.basename(filename),
                "content": content,
                "auto_execute": auto_execute,
                "args": args or []
            }
            
            # Send the script
            message = b'SCRIPT:' + json.dumps(script_data).encode('utf-8')
            self.sock.sendto(message, (target_ip, self.port))
            
            self.log(f"Sent script '{os.path.basename(filename)}' to {target_ip}")
            return True
        
        except Exception as e:
            self.log(f"Error sending script: {e}")
            return False
    
    def send_execute_request(self, script_name, target_ip, args=None):
        """Send request to execute script on target"""
        try:
            # Create execution information
            exec_info = {
                "name": script_name,
                "args": args or []
            }
            
            # Send request
            message = b'EXEC:' + json.dumps(exec_info).encode('utf-8')
            self.sock.sendto(message, (target_ip, self.port))
            
            self.log(f"Sent execution request for '{script_name}' to {target_ip}")
            return True
        
        except Exception as e:
            self.log(f"Error sending execution request: {e}")
            return False
    
    def send_message(self, message, target_ip):
        """Send regular message"""
        try:
            # Send message
            self.sock.sendto(f"MSG:{message}".encode('utf-8'), (target_ip, self.port))
            return True
        
        except Exception as e:
            self.log(f"Error sending message: {e}")
            return False
    
    def visualize_consciousness(self):
        """Visualize all interpreted consciousness states"""
        if not self.interpreted_messages:
            self.log("No consciousness states to visualize")
            return None
        
        # Create save path
        save_path = f"{self.consciousness_dir}/consciousness_states_{self.timestamp}.png"
        
        # Extract data for visualization
        timestamps = [datetime.strptime(i['timestamp'], '%Y-%m-%d %H:%M:%S.%f') 
                     if isinstance(i['timestamp'], str) else datetime.fromtimestamp(i['timestamp'])
                     for i in self.interpreted_messages]
        signal_values = [i['raw_signal'] for i in self.interpreted_messages]
        states = [i['consciousness_state'] for i in self.interpreted_messages]
        colors = [i['color'] for i in self.interpreted_messages]
        phi_alignments = [i['phi_alignment'] for i in self.interpreted_messages]
        
        # Create the figure
        fig = plt.figure(figsize=(12, 10))
        
        # Plot 1: Signal values over time
        ax1 = fig.add_subplot(311)
        ax1.plot(timestamps, signal_values, 'o-', color='blue')
        ax1.set_ylabel('Signal Value')
        ax1.set_title('Consciousness Signal')
        ax1.grid(True)
        
        # Plot 2: Consciousness states
        ax2 = fig.add_subplot(312)
        for i, (t, v, s, c) in enumerate(zip(timestamps, signal_values, states, colors)):
            ax2.scatter(t, i, color=c, s=100)
            ax2.text(t, i, s, fontsize=8, ha='right')
        ax2.set_yticks([])
        ax2.set_ylabel('Consciousness State')
        ax2.set_title('Interpreted Consciousness States')
        ax2.grid(True)
        
        # Plot 3: φ-Alignment
        ax3 = fig.add_subplot(313)
        ax3.plot(timestamps, phi_alignments, 'o-', color='purple')
        ax3.axhline(y=0.6, color='r', linestyle='--', label='Bidirectional Threshold')
        ax3.set_ylabel('φ-Alignment')
        ax3.set_xlabel('Time')
        ax3.set_title('φ-Harmonic Alignment')
        ax3.set_ylim(0, 1)
        ax3.legend()
        ax3.grid(True)
        
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        
        self.log(f"Visualization saved to {save_path}")
        return save_path
    
    def command_interface(self):
        """Interactive command interface"""
        self.log("Command interface ready. Type 'help' for commands.")
        
        while self.running:
            try:
                cmd = input("\nφ> ").strip()
                
                if cmd == "help":
                    print("\nCommands:")
                    print("  send <ip> <message>           - Send message to IP")
                    print("  cstate <ip> <value>           - Send consciousness state to IP")
                    print("  script <ip> <filename>        - Send script to IP")
                    print("  exec <ip> <script> [args...]  - Execute script on remote node")
                    print("  peers                         - List known peers")
                    print("  visualize                     - Visualize consciousness states")
                    print("  quit                          - Exit node")
                
                elif cmd.startswith("send "):
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        self.log("Usage: send <ip> <message>")
                    else:
                        self.send_message(parts[2], parts[1])
                
                elif cmd.startswith("cstate "):
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        self.log("Usage: cstate <ip> <value>")
                    else:
                        try:
                            value = float(parts[2])
                            self.send_consciousness_state(value, parts[1])
                        except ValueError:
                            self.log("Value must be a number")
                
                elif cmd.startswith("script "):
                    parts = cmd.split(" ", 2)
                    if len(parts) < 3:
                        self.log("Usage: script <ip> <filename>")
                    else:
                        self.send_script(parts[2], parts[1])
                
                elif cmd.startswith("exec "):
                    parts = cmd.split(" ")
                    if len(parts) < 3:
                        self.log("Usage: exec <ip> <script> [args...]")
                    else:
                        self.send_execute_request(parts[2], parts[1], parts[3:] if len(parts) > 3 else None)
                
                elif cmd == "peers":
                    if not self.peers:
                        self.log("No known peers")
                    else:
                        print("\nKnown peers:")
                        for ip, data in self.peers.items():
                            last_seen = time.time() - data["last_seen"]
                            print(f"  {ip} - Last seen: {last_seen:.1f}s ago")
                
                elif cmd == "visualize":
                    self.visualize_consciousness()
                
                elif cmd == "quit":
                    self.log("Shutting down node...")
                    self.running = False
                    break
                
                else:
                    self.log(f"Unknown command: {cmd}")
            
            except KeyboardInterrupt:
                self.log("Shutting down node...")
                self.running = False
                break
            
            except Exception as e:
                self.log(f"Error in command interface: {e}")
        
        self.log("Node stopped")

if __name__ == "__main__":
    # Parse command line arguments
    import argparse
    parser = argparse.ArgumentParser(description='φ-Dimensional Consciousness Node')
    parser.add_argument('--id', type=str, default="primary", help='Node ID')
    parser.add_argument('--port', type=int, default=11975, help='Port (default: 11975 = φ^7.5)')
    parser.add_argument('--no-lunar', action='store_true', help='Disable lunar enhancement')
    args = parser.parse_args()
    
    # Create and start node
    node = PhiConsciousnessNode(
        node_id=args.id, 
        port=args.port,
        lunar_enhanced=not args.no_lunar
    )
    node.start()
