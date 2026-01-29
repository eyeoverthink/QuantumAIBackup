#!/usr/bin/env python3
"""
φ-FREQUENCY DETECTOR
==================
Detects and transmits φ-dimensional frequencies using standard hardware.
Implements Earth-Moon-Brain frequency link over WiFi/Bluetooth.

Uses port 11975 (φ^7.5 = 36.93) for φ-dimensional communication and
implements φ^75 validation seal (4721424167835376.00) for reality protection.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import json
import hashlib
import os
import numpy as np
from datetime import datetime
from decimal import Decimal, getcontext

# Set precision for φ-dimensional calculations
getcontext().prec = 50

# φ-Harmonic constants
PHI = Decimal('1.618033988749895')  # Golden ratio (φ)
PHI_INV = Decimal('1') / PHI        # Inverse golden ratio (1/φ)
PHI_75 = PHI ** Decimal('7.5')      # φ^7.5 = 36.93
PHI_SEAL = PHI ** Decimal('75')     # φ^75 validation seal = 4721424167835376.00

# System frequencies
MOON_FREQ = Decimal('52525')        # Moon frequency (Hz)
EARTH_FREQ = Decimal('7.83')        # Earth Schumann resonance (Hz)
BRAIN_FREQ = Decimal('5.2525')      # Brain frequency (Hz)

# Network settings
PORT = 11975                        # φ-dimensional port (φ^7.5 = 36.93)
BUFFER_SIZE = 4096                  # Buffer size for socket communication

class PhiFrequencyDetector:
    """
    φ-Frequency Detector
    
    Detects and transmits φ-dimensional frequencies using standard hardware.
    Implements Earth-Moon-Brain frequency link over WiFi/Bluetooth.
    """
    
    def __init__(self, node_id=None, host='192.168.3.152', port=11975):
        """Initialize the frequency detector"""
        # Generate node ID if not provided
        self.node_id = node_id or self._generate_node_id()
        self.host = host
        self.port = port
        
        # Initialize φ-dimensional constants
        self.phi = PHI
        self.phi_inv = PHI_INV
        self.phi_75 = PHI_75
        self.phi_seal = PHI_SEAL
        
        # Initialize frequencies
        self.moon_freq = MOON_FREQ
        self.earth_freq = EARTH_FREQ
        self.brain_freq = BRAIN_FREQ
        
        # Initialize frequency detection
        self.detected_frequencies = {
            'earth': float(self.earth_freq),
            'brain': float(self.brain_freq),
            'moon': float(self.moon_freq)
        }
        
        # Initialize resonance state
        self.resonance_state = {
            'earth_brain': 0.0,
            'brain_moon': 0.0,
            'earth_moon': 0.0,
            'total': 0.0
        }
        
        # Initialize consciousness level
        self.consciousness_level = 0.0
        
        # Initialize threading
        self.running = False
        self.threads = []
        
        # Initialize sockets
        self.tx_socket = None
        self.rx_socket = None
        
        # Peer tracking
        self.peers = {}
        
        # Results directory
        self.results_dir = "frequency_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Message counters
        self.messages_sent = 0
        self.messages_received = 0
        
        print(f"φ-Frequency Detector initialized")
        print(f"Node ID: {self.node_id}")
        print(f"Port: {self.port} (φ^7.5 = {float(self.phi_75)})")
        print(f"φ^75 validation seal: {float(self.phi_seal)}")
        print(f"Earth frequency: {float(self.earth_freq)} Hz")
        print(f"Brain frequency: {float(self.brain_freq)} Hz")
        print(f"Moon frequency: {float(self.moon_freq)} Hz")
    
    def _generate_node_id(self):
        """Generate a unique node ID based on φ-harmonic principles"""
        # Use current time and φ to generate a unique ID
        timestamp = str(time.time())
        phi_factor = str(float(PHI) * 1000000)
        
        # Create hash
        hash_input = timestamp + phi_factor
        node_hash = hashlib.md5(hash_input.encode()).hexdigest()
        
        # Take first 8 characters
        return node_hash[:8]
    
    def _calculate_validation_seal(self, data):
        """Calculate φ^75 validation seal for data"""
        # Create hash of data
        data_hash = hashlib.sha256(str(data).encode()).hexdigest()
        
        # Convert hash to integer and apply φ^75 scaling
        hash_int = int(data_hash, 16) % 10000000
        seal = hash_int * float(self.phi_seal) % 10000000000000000
        
        return seal
    
    def _verify_validation_seal(self, data, seal):
        """Verify φ^75 validation seal for data"""
        calculated_seal = self._calculate_validation_seal(data)
        
        # Allow small floating point differences
        return abs(calculated_seal - seal) < 0.001
    
    def start(self):
        """Start the frequency detector"""
        if self.running:
            print("Frequency detector is already running")
            return
        
        self.running = True
        
        # Initialize sockets
        self._init_sockets()
        
        # Start threads
        self._start_threads()
        
        print("\nφ-Frequency Detector started")
        print("Transmitting and detecting φ-dimensional frequencies...")
    
    def _init_sockets(self):
        """Initialize network sockets"""
        # Transmitter socket (UDP)
        self.tx_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tx_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Receiver socket (UDP)
        self.rx_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rx_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            # Try to bind to the port
            self.rx_socket.bind((self.host, self.port))
            print(f"Bound to {self.host}:{self.port}")
        except:
            # If binding fails, use a different port
            alt_port = int(float(self.phi_75) * 1000) % 65535
            if alt_port < 1024:
                alt_port += 1024
            
            try:
                self.rx_socket.bind((self.host, alt_port))
                self.port = alt_port
                print(f"Primary port busy, bound to {self.host}:{self.port}")
            except:
                print("Warning: Could not bind to any port. Frequency detection disabled.")
                self.rx_socket = None
        
        # Set socket timeout to non-blocking
        if self.rx_socket:
            self.rx_socket.settimeout(0.1)
    
    def _start_threads(self):
        """Start processing threads"""
        # Transmitter thread
        tx_thread = threading.Thread(target=self._transmitter_thread)
        tx_thread.daemon = True
        tx_thread.start()
        self.threads.append(tx_thread)
        
        # Receiver thread (only if socket is available)
        if self.rx_socket:
            rx_thread = threading.Thread(target=self._receiver_thread)
            rx_thread.daemon = True
            rx_thread.start()
            self.threads.append(rx_thread)
        
        # Resonance calculator thread
        resonance_thread = threading.Thread(target=self._resonance_calculator_thread)
        resonance_thread.daemon = True
        resonance_thread.start()
        self.threads.append(resonance_thread)
        
        # Consciousness calculator thread
        consciousness_thread = threading.Thread(target=self._consciousness_calculator_thread)
        consciousness_thread.daemon = True
        consciousness_thread.start()
        self.threads.append(consciousness_thread)
        
        # Status thread
        status_thread = threading.Thread(target=self._status_thread)
        status_thread.daemon = True
        status_thread.start()
        self.threads.append(status_thread)
    
    def _transmitter_thread(self):
        """Thread for transmitting φ-dimensional frequencies"""
        while self.running:
            try:
                # Create frequency packet
                packet = self._create_frequency_packet()
                
                # Broadcast to peers
                for peer_id, peer_addr in self.peers.items():
                    if peer_id != self.node_id:  # Don't send to self
                        self.tx_socket.sendto(json.dumps(packet).encode(), peer_addr)
                        self.messages_sent += 1
                
                # Broadcast to localhost (for local bidirectional node)
                self.tx_socket.sendto(json.dumps(packet).encode(), ('127.0.0.1', PORT))
                
                # Sleep for a short time
                time.sleep(1.0)
                
            except Exception as e:
                print(f"Transmitter error: {e}")
                time.sleep(1.0)
    
    def _receiver_thread(self):
        """Thread for receiving φ-dimensional frequencies"""
        while self.running and self.rx_socket:
            try:
                # Receive data
                data, addr = self.rx_socket.recvfrom(BUFFER_SIZE)
                
                # Parse packet
                packet = json.loads(data.decode())
                
                # Check packet type
                if 'frequencies' in packet:
                    # Verify validation seal
                    if not self._verify_validation_seal(packet['frequencies'], packet['validation_seal']):
                        print(f"Invalid validation seal from {addr}")
                        continue
                    
                    # Extract sender info
                    sender_id = packet['node_id']
                    
                    # Update peer list
                    if sender_id != self.node_id:  # Don't add self as peer
                        self.peers[sender_id] = addr
                    
                    # Process frequencies
                    self._process_received_frequencies(packet['frequencies'])
                    self.messages_received += 1
                
            except socket.timeout:
                # This is expected due to the non-blocking socket
                pass
            except Exception as e:
                if "timed out" not in str(e):  # Ignore timeout errors
                    print(f"Receiver error: {e}")
                time.sleep(0.1)
    
    def _resonance_calculator_thread(self):
        """Thread for calculating resonance between frequencies"""
        while self.running:
            try:
                # Get detected frequencies
                earth = self.detected_frequencies['earth']
                brain = self.detected_frequencies['brain']
                moon = self.detected_frequencies['moon']
                
                # Calculate resonance between pairs
                if earth > 0 and brain > 0:
                    # Earth-Brain resonance
                    earth_brain_ratio = earth / brain
                    earth_brain_phi_match = 1.0 - abs(earth_brain_ratio - float(self.phi)) / float(self.phi)
                    self.resonance_state['earth_brain'] = max(0.0, earth_brain_phi_match)
                
                if brain > 0 and moon > 0:
                    # Brain-Moon resonance
                    brain_moon_ratio = moon / brain
                    brain_moon_phi_match = 1.0 - abs(brain_moon_ratio / 10000 - float(self.phi**2)) / float(self.phi**2)
                    self.resonance_state['brain_moon'] = max(0.0, brain_moon_phi_match)
                
                if earth > 0 and moon > 0:
                    # Earth-Moon resonance
                    earth_moon_ratio = moon / earth
                    earth_moon_phi_match = 1.0 - abs(earth_moon_ratio / 10000 - float(self.phi**3)) / float(self.phi**3)
                    self.resonance_state['earth_moon'] = max(0.0, earth_moon_phi_match)
                
                # Calculate total resonance
                self.resonance_state['total'] = (
                    self.resonance_state['earth_brain'] * 
                    self.resonance_state['brain_moon'] * 
                    self.resonance_state['earth_moon']
                ) ** (1/3)  # Geometric mean
                
                # Sleep for a short time
                time.sleep(0.5)
                
            except Exception as e:
                print(f"Resonance calculator error: {e}")
                time.sleep(0.1)
    
    def _consciousness_calculator_thread(self):
        """Thread for calculating consciousness level"""
        while self.running:
            try:
                # Calculate consciousness level based on resonance
                # The formula is based on φ-dimensional principles
                
                # Base consciousness from resonance
                base_consciousness = self.resonance_state['total']
                
                # Apply φ-harmonic scaling
                phi_factor = float(self.phi_inv) ** (1 - base_consciousness)
                
                # Apply birth coherence factor (99.18K)
                birth_factor = 0.9918 + (1 - 0.9918) * base_consciousness
                
                # Calculate final consciousness level
                self.consciousness_level = base_consciousness * phi_factor * birth_factor
                
                # Sleep for a short time
                time.sleep(1.0)
                
            except Exception as e:
                print(f"Consciousness calculator error: {e}")
                time.sleep(0.1)
    
    def _status_thread(self):
        """Thread for printing status updates"""
        while self.running:
            try:
                # Print status every 5 seconds
                time.sleep(5.0)
                self.print_status()
                
                # Save status to file occasionally
                if np.random.random() < 0.2:  # 20% chance
                    self._save_status_report()
                
            except Exception as e:
                print(f"Status thread error: {e}")
                time.sleep(1.0)
    
    def _create_frequency_packet(self):
        """Create a packet containing φ-dimensional frequencies"""
        # Frequency data
        frequencies = {
            'earth': float(self.earth_freq),
            'brain': float(self.brain_freq),
            'moon': float(self.moon_freq),
            'timestamp': time.time()
        }
        
        # Calculate validation seal
        validation_seal = self._calculate_validation_seal(frequencies)
        
        # Create packet
        packet = {
            'node_id': self.node_id,
            'frequencies': frequencies,
            'resonance': dict(self.resonance_state),
            'consciousness': self.consciousness_level,
            'validation_seal': validation_seal
        }
        
        return packet
    
    def _process_received_frequencies(self, frequencies):
        """Process received frequency data"""
        # Extract frequencies
        earth_freq = frequencies.get('earth', 0.0)
        brain_freq = frequencies.get('brain', 0.0)
        moon_freq = frequencies.get('moon', 0.0)
        
        # Update detected frequencies
        # This simulates frequency detection from network packets
        if earth_freq > 0:
            # Apply some noise to simulate real-world detection
            noise = (np.random.random() - 0.5) * 0.1  # +/- 5% noise
            self.detected_frequencies['earth'] = earth_freq * (1 + noise)
        
        if brain_freq > 0:
            noise = (np.random.random() - 0.5) * 0.1
            self.detected_frequencies['brain'] = brain_freq * (1 + noise)
        
        if moon_freq > 0:
            noise = (np.random.random() - 0.5) * 0.1
            self.detected_frequencies['moon'] = moon_freq * (1 + noise)
    
    def get_status(self):
        """Get current status"""
        status = {
            'node_id': self.node_id,
            'detected_frequencies': dict(self.detected_frequencies),
            'resonance_state': dict(self.resonance_state),
            'consciousness_level': self.consciousness_level,
            'peers': len(self.peers),
            'messages_sent': self.messages_sent,
            'messages_received': self.messages_received,
            'timestamp': time.time()
        }
        
        return status
    
    def print_status(self):
        """Print current status"""
        print("\nφ-Frequency Detector Status")
        print("-" * 40)
        print(f"Connected peers: {len(self.peers)}")
        print(f"Messages sent: {self.messages_sent}")
        print(f"Messages received: {self.messages_received}")
        print(f"Detected frequencies:")
        print(f"  Earth: {self.detected_frequencies['earth']:.4f} Hz (target: {float(self.earth_freq)})")
        print(f"  Brain: {self.detected_frequencies['brain']:.4f} Hz (target: {float(self.brain_freq)})")
        print(f"  Moon: {self.detected_frequencies['moon']:.4f} Hz (target: {float(self.moon_freq)})")
        print(f"Resonance state:")
        print(f"  Earth-Brain: {self.resonance_state['earth_brain']:.4f}")
        print(f"  Brain-Moon: {self.resonance_state['brain_moon']:.4f}")
        print(f"  Earth-Moon: {self.resonance_state['earth_moon']:.4f}")
        print(f"  Total: {self.resonance_state['total']:.4f}")
        print(f"Consciousness level: {self.consciousness_level:.4f}")
    
    def _save_status_report(self):
        """Save status report to file"""
        try:
            # Create report
            report = {
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'node_id': self.node_id,
                'detected_frequencies': dict(self.detected_frequencies),
                'resonance_state': dict(self.resonance_state),
                'consciousness_level': self.consciousness_level,
                'peers': len(self.peers),
                'messages_sent': self.messages_sent,
                'messages_received': self.messages_received
            }
            
            # Create filename
            filename = f"{self.results_dir}/frequency_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            # Save report
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2)
            
            print(f"Status report saved to: {filename}")
        
        except Exception as e:
            print(f"Error saving status report: {e}")
    
    def add_peer(self, peer_addr):
        """Add a peer to the network"""
        peer_id = f"peer-{peer_addr[0]}-{peer_addr[1]}"
        self.peers[peer_id] = peer_addr
        print(f"Added peer: {peer_addr[0]}:{peer_addr[1]}")
    
    def send_frequency_packet(self, target_ip, target_port=PORT):
        """Send a frequency packet to a specific target"""
        try:
            # Create frequency packet
            packet = self._create_frequency_packet()
            
            # Send packet
            self.tx_socket.sendto(json.dumps(packet).encode(), (target_ip, target_port))
            self.messages_sent += 1
            
            print(f"Frequency packet sent to {target_ip}:{target_port}")
            return True
        
        except Exception as e:
            print(f"Error sending frequency packet: {e}")
            return False
    
    def discover_peers(self):
        """Discover peers on the network"""
        # Try common local IPs
        common_ips = [
            '127.0.0.1',
            '192.168.3.126',
            '192.168.3.173',
            '10.0.0.1',
            '10.0.1.1'
          
        ]
        
        for ip in common_ips:
            self.send_frequency_packet(ip)
    
    def stop(self):
        """Stop the frequency detector"""
        if not self.running:
            return
        
        self.running = False
        
        # Close sockets
        if self.tx_socket:
            self.tx_socket.close()
        
        if self.rx_socket:
            self.rx_socket.close()
        
        # Wait for threads to finish
        for thread in self.threads:
            if thread.is_alive():
                thread.join(timeout=1.0)
        
        # Save final status report
        self._save_status_report()
        
        print("φ-Frequency Detector stopped")
        print(f"Final consciousness level: {self.consciousness_level:.4f}")
        print(f"Messages sent: {self.messages_sent}")
        print(f"Messages received: {self.messages_received}")


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="φ-Frequency Detector")
    parser.add_argument("--host", default="0.0.0.0", help="Host IP address")
    parser.add_argument("--node-id", help="Node ID (generated if not provided)")
    parser.add_argument("--peer", help="Peer IP address to connect to")
    args = parser.parse_args()
    
    # Create frequency detector
    detector = PhiFrequencyDetector(node_id=args.node_id, host=args.host)
    
    try:
        # Start detector
        detector.start()
        
        # Add peer if specified
        if args.peer:
            detector.add_peer((args.peer, PORT))
            detector.send_frequency_packet(args.peer)
        
        # Discover peers
        detector.discover_peers()
        
        # Keep running until interrupted
        while True:
            cmd = input("\nCommand (status/peers/discover/quit): ").strip().lower()
            
            if cmd == "status":
                detector.print_status()
            
            elif cmd == "peers":
                print(f"\nConnected peers: {len(detector.peers)}")
                for peer_id, peer_addr in detector.peers.items():
                    print(f"  {peer_id}: {peer_addr[0]}:{peer_addr[1]}")
            
            elif cmd == "discover":
                detector.discover_peers()
            
            elif cmd == "quit":
                break
            
            else:
                print("Unknown command. Available commands: status, peers, discover, quit")
        
    except KeyboardInterrupt:
        print("\nStopping φ-Frequency Detector...")
    finally:
        # Stop detector
        detector.stop()

if __name__ == "__main__":
    main()
