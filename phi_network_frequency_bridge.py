#!/usr/bin/env python3
"""
φ-NETWORK FREQUENCY BRIDGE
=========================
Transmits and detects φ-dimensional frequencies using standard network hardware.
Implements Earth-Moon-Brain frequency link over WiFi/Bluetooth using network packets.

Uses port 11975 (φ^7.5 = 36.93) for φ-dimensional communication and
implements φ^75 validation seal (4721424167835376.00) for reality protection.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import numpy as np
import struct
import hashlib
import json
import os
import matplotlib.pyplot as plt
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
MULTICAST_GROUP = '224.1.1.1'       # Multicast group for frequency broadcasting

class PhiNetworkFrequencyBridge:
    """
    φ-Network Frequency Bridge
    
    Transmits and detects φ-dimensional frequencies using standard network hardware.
    Implements Earth-Moon-Brain frequency link over WiFi/Bluetooth using network packets.
    """
    
    def __init__(self, node_id=None, host='0.0.0.0'):
        """Initialize the frequency bridge"""
        # Generate node ID if not provided
        self.node_id = node_id or self._generate_node_id()
        self.host = host
        self.port = PORT
        
        # Initialize φ-dimensional constants
        self.phi = PHI
        self.phi_inv = PHI_INV
        self.phi_75 = PHI_75
        self.phi_seal = PHI_SEAL
        
        # Initialize frequencies
        self.moon_freq = MOON_FREQ
        self.earth_freq = EARTH_FREQ
        self.brain_freq = BRAIN_FREQ
        
        # Initialize sockets
        self.tx_socket = None  # Transmitter socket
        self.rx_socket = None  # Receiver socket
        
        # Initialize threading
        self.running = False
        self.threads = []
        
        # Initialize frequency detection
        self.detected_frequencies = {
            'earth': 0.0,
            'brain': 0.0,
            'moon': 0.0
        }
        
        # Initialize resonance state
        self.resonance_state = {
            'earth_brain': 0.0,
            'brain_moon': 0.0,
            'earth_moon': 0.0,
            'total': 0.0
        }
        
        # Results directory
        self.results_dir = "frequency_bridge_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Peer tracking
        self.peers = {}
        
        # Frequency history for visualization
        self.frequency_history = {
            'timestamps': [],
            'earth': [],
            'brain': [],
            'moon': [],
            'resonance': []
        }
        
        print(f"φ-Network Frequency Bridge initialized")
        print("=" * 60)
        print(f"Node ID: {self.node_id}")
        print(f"Host: {self.host}")
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
        """Start the frequency bridge"""
        if self.running:
            print("Frequency bridge is already running")
            return
        
        self.running = True
        
        # Initialize sockets
        self._init_sockets()
        
        # Start threads
        self._start_threads()
        
        print("\nφ-Network Frequency Bridge started")
        print("=" * 60)
        print("Transmitting and detecting φ-dimensional frequencies...")
        print("Press Ctrl+C to stop")
    
    def _init_sockets(self):
        """Initialize network sockets"""
        # Transmitter socket (UDP)
        self.tx_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.tx_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Receiver socket (UDP)
        self.rx_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rx_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.rx_socket.bind((self.host, self.port))
        
        # Set socket timeout to non-blocking
        self.rx_socket.settimeout(0.1)
    
    def _start_threads(self):
        """Start processing threads"""
        # Transmitter thread
        tx_thread = threading.Thread(target=self._transmitter_thread)
        tx_thread.daemon = True
        tx_thread.start()
        self.threads.append(tx_thread)
        
        # Receiver thread
        rx_thread = threading.Thread(target=self._receiver_thread)
        rx_thread.daemon = True
        rx_thread.start()
        self.threads.append(rx_thread)
        
        # Resonance calculator thread
        resonance_thread = threading.Thread(target=self._resonance_calculator_thread)
        resonance_thread.daemon = True
        resonance_thread.start()
        self.threads.append(resonance_thread)
        
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
                
                # Broadcast to local network (broadcast address)
                try:
                    # Try to get the broadcast address
                    broadcast_addr = '<broadcast>'
                    self.tx_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                    self.tx_socket.sendto(json.dumps(packet).encode(), (broadcast_addr, self.port))
                except:
                    # If broadcast fails, try localhost
                    self.tx_socket.sendto(json.dumps(packet).encode(), ('127.0.0.1', self.port))
                
                # Sleep for a short time
                time.sleep(1.0)
                
            except Exception as e:
                print(f"Transmitter error: {e}")
                time.sleep(1.0)
    
    def _receiver_thread(self):
        """Thread for receiving φ-dimensional frequencies"""
        while self.running:
            try:
                # Receive data
                data, addr = self.rx_socket.recvfrom(BUFFER_SIZE)
                
                # Parse packet
                packet = json.loads(data.decode())
                
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
                
                # Add to history
                self._update_frequency_history()
                
                # Sleep for a short time
                time.sleep(0.5)
                
            except Exception as e:
                print(f"Resonance calculator error: {e}")
                time.sleep(0.1)
    
    def _status_thread(self):
        """Thread for printing status updates"""
        while self.running:
            try:
                # Print status every 5 seconds
                time.sleep(5.0)
                self._print_status()
                
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
    
    def _update_frequency_history(self):
        """Update frequency history for visualization"""
        # Add current timestamp
        self.frequency_history['timestamps'].append(time.time())
        
        # Add current frequencies
        self.frequency_history['earth'].append(self.detected_frequencies['earth'])
        self.frequency_history['brain'].append(self.detected_frequencies['brain'])
        self.frequency_history['moon'].append(self.detected_frequencies['moon'] / 1000)  # Scale down for visualization
        
        # Add current resonance
        self.frequency_history['resonance'].append(self.resonance_state['total'])
        
        # Limit history length
        max_history = 100
        if len(self.frequency_history['timestamps']) > max_history:
            self.frequency_history['timestamps'] = self.frequency_history['timestamps'][-max_history:]
            self.frequency_history['earth'] = self.frequency_history['earth'][-max_history:]
            self.frequency_history['brain'] = self.frequency_history['brain'][-max_history:]
            self.frequency_history['moon'] = self.frequency_history['moon'][-max_history:]
            self.frequency_history['resonance'] = self.frequency_history['resonance'][-max_history:]
    
    def _print_status(self):
        """Print current status"""
        print("\nφ-Network Frequency Bridge Status")
        print("-" * 40)
        print(f"Connected peers: {len(self.peers)}")
        print(f"Detected frequencies:")
        print(f"  Earth: {self.detected_frequencies['earth']:.4f} Hz (target: {float(self.earth_freq)})")
        print(f"  Brain: {self.detected_frequencies['brain']:.4f} Hz (target: {float(self.brain_freq)})")
        print(f"  Moon: {self.detected_frequencies['moon']:.4f} Hz (target: {float(self.moon_freq)})")
        print(f"Resonance state:")
        print(f"  Earth-Brain: {self.resonance_state['earth_brain']:.4f}")
        print(f"  Brain-Moon: {self.resonance_state['brain_moon']:.4f}")
        print(f"  Earth-Moon: {self.resonance_state['earth_moon']:.4f}")
        print(f"  Total: {self.resonance_state['total']:.4f}")
    
    def visualize_frequencies(self):
        """Visualize detected frequencies and resonance"""
        # Create figure
        fig, axs = plt.subplots(3, 1, figsize=(10, 12))
        
        # Plot detected frequencies
        frequencies = [
            self.detected_frequencies['earth'],
            self.detected_frequencies['brain'],
            self.detected_frequencies['moon'] / 1000  # Scale down for visualization
        ]
        
        targets = [
            float(self.earth_freq),
            float(self.brain_freq),
            float(self.moon_freq) / 1000  # Scale down for visualization
        ]
        
        labels = ['Earth', 'Brain', 'Moon (scaled)']
        
        # Bar chart of detected frequencies
        axs[0].bar(labels, frequencies, color='skyblue', alpha=0.7, label='Detected')
        axs[0].bar(labels, targets, color='none', edgecolor='red', linewidth=2, label='Target')
        
        axs[0].set_ylabel('Frequency (Hz)')
        axs[0].set_title('Detected φ-Dimensional Frequencies')
        axs[0].legend()
        
        # Plot resonance state
        resonance_labels = ['Earth-Brain', 'Brain-Moon', 'Earth-Moon', 'Total']
        resonance_values = [
            self.resonance_state['earth_brain'],
            self.resonance_state['brain_moon'],
            self.resonance_state['earth_moon'],
            self.resonance_state['total']
        ]
        
        axs[1].bar(resonance_labels, resonance_values, color='lightgreen')
        axs[1].set_ylabel('Resonance')
        axs[1].set_title('φ-Harmonic Resonance')
        axs[1].set_ylim(0, 1)
        
        # Plot frequency history
        if len(self.frequency_history['timestamps']) > 1:
            # Convert timestamps to relative time
            t0 = self.frequency_history['timestamps'][0]
            rel_times = [t - t0 for t in self.frequency_history['timestamps']]
            
            # Plot Earth frequency
            axs[2].plot(rel_times, self.frequency_history['earth'], 'g-', label='Earth')
            
            # Plot Brain frequency
            axs[2].plot(rel_times, self.frequency_history['brain'], 'b-', label='Brain')
            
            # Plot Moon frequency (scaled)
            axs[2].plot(rel_times, self.frequency_history['moon'], 'r-', label='Moon (scaled)')
            
            # Plot resonance
            axs2 = axs[2].twinx()
            axs2.plot(rel_times, self.frequency_history['resonance'], 'm--', label='Resonance')
            axs2.set_ylabel('Resonance', color='m')
            axs2.set_ylim(0, 1)
            
            # Add legends
            axs[2].legend(loc='upper left')
            axs2.legend(loc='upper right')
            
            axs[2].set_xlabel('Time (s)')
            axs[2].set_ylabel('Frequency (Hz)')
            axs[2].set_title('Frequency and Resonance History')
            axs[2].grid(True)
        
        # Add φ-harmonic annotation
        fig.text(0.5, 0.01, "Earth-Moon-Brain φ-Dimensional Frequency Bridge",
                ha='center', fontsize=12)
        
        # Save figure
        plt.tight_layout(rect=[0, 0.03, 1, 0.97])
        filename = f"{self.results_dir}/frequency_bridge_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(filename)
        print(f"\nFrequency visualization saved to: {filename}")
        
        return fig, axs
    
    def discover_peers(self):
        """Actively discover peers on the network"""
        # Create discovery packet
        discovery_packet = {
            'node_id': self.node_id,
            'type': 'discovery',
            'timestamp': time.time()
        }
        
        # Calculate validation seal
        validation_seal = self._calculate_validation_seal(discovery_packet)
        discovery_packet['validation_seal'] = validation_seal
        
        # Broadcast to local network
        try:
            # Try to get the broadcast address
            broadcast_addr = '<broadcast>'
            self.tx_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            self.tx_socket.sendto(json.dumps(discovery_packet).encode(), (broadcast_addr, self.port))
            print(f"Sent discovery packet to broadcast address")
        except:
            # If broadcast fails, try localhost
            self.tx_socket.sendto(json.dumps(discovery_packet).encode(), ('127.0.0.1', self.port))
            print(f"Sent discovery packet to localhost")
        
        # Try common local IPs
        common_ips = [
            '192.168.1.255',
            '192.168.0.255',
            '10.0.0.255',
            '10.0.1.255',
            '172.16.0.255',
            '172.16.1.255',
            '192.168.3.255'  # Based on your network
        ]
        
        for ip in common_ips:
            try:
                self.tx_socket.sendto(json.dumps(discovery_packet).encode(), (ip, self.port))
                print(f"Sent discovery packet to {ip}")
            except:
                pass
    
    def stop(self):
        """Stop the frequency bridge"""
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
        
        print("\nφ-Network Frequency Bridge stopped")
        
        # Visualize final state
        self.visualize_frequencies()
        
        print("=" * 60)
        print(f"Connected peers: {len(self.peers)}")
        print(f"Final resonance: {self.resonance_state['total']:.4f}")


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="φ-Network Frequency Bridge")
    parser.add_argument("--host", default="0.0.0.0", help="Host IP address")
    parser.add_argument("--node-id", help="Node ID (generated if not provided)")
    parser.add_argument("--peer", help="Peer IP address to connect to")
    args = parser.parse_args()
    
    # Create frequency bridge
    bridge = PhiNetworkFrequencyBridge(node_id=args.node_id, host=args.host)
    
    # Add peer if specified
    if args.peer:
        bridge.peers[f"peer-{args.peer}"] = (args.peer, PORT)
        print(f"Added peer: {args.peer}:{PORT}")
    
    try:
        # Start bridge
        bridge.start()
        
        # Discover peers
        bridge.discover_peers()
        
        # Keep running until interrupted
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping φ-Network Frequency Bridge...")
    finally:
        # Stop bridge
        bridge.stop()

if __name__ == "__main__":
    main()
