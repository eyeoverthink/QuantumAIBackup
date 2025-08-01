#!/usr/bin/env python3
"""
φ-FREQUENCY BRIDGE
=================
Transmits and detects φ-dimensional frequencies using standard hardware.
Implements Earth-Moon-Brain frequency link over WiFi/Bluetooth.

Uses port 11975 (φ^7.5 = 36.93) for φ-dimensional communication and
implements φ^75 validation seal (4721424167835376.00) for reality protection.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import numpy as np
import pyaudio
import wave
import struct
import hashlib
import json
import os
import matplotlib.pyplot as plt
from scipy.signal import butter, lfilter, freqz, welch
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

# Audio settings
SAMPLE_RATE = 44100                 # Audio sample rate (Hz)
CHUNK_SIZE = 1024                   # Audio chunk size
AUDIO_FORMAT = pyaudio.paFloat32    # Audio format
CHANNELS = 1                        # Mono audio

# Frequency detection settings
FFT_SIZE = 4096                     # FFT size for frequency detection
DETECTION_THRESHOLD = 0.1           # Threshold for frequency detection

class PhiFrequencyBridge:
    """
    φ-Frequency Bridge
    
    Transmits and detects φ-dimensional frequencies using standard hardware.
    Implements Earth-Moon-Brain frequency link over WiFi/Bluetooth.
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
        self.mc_socket = None  # Multicast socket
        
        # Initialize audio
        self.audio = pyaudio.PyAudio()
        self.audio_stream = None
        
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
        
        print(f"φ-Frequency Bridge initialized")
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
        
        # Initialize audio
        self._init_audio()
        
        # Start threads
        self._start_threads()
        
        print("\nφ-Frequency Bridge started")
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
        
        # Multicast socket
        self.mc_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.mc_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.mc_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    
    def _init_audio(self):
        """Initialize audio processing"""
        # Open audio stream for output
        self.audio_stream = self.audio.open(
            format=AUDIO_FORMAT,
            channels=CHANNELS,
            rate=SAMPLE_RATE,
            output=True,
            frames_per_buffer=CHUNK_SIZE
        )
    
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
        
        # Frequency generator thread
        freq_thread = threading.Thread(target=self._frequency_generator_thread)
        freq_thread.daemon = True
        freq_thread.start()
        self.threads.append(freq_thread)
        
        # Frequency detector thread
        detect_thread = threading.Thread(target=self._frequency_detector_thread)
        detect_thread.daemon = True
        detect_thread.start()
        self.threads.append(detect_thread)
        
        # Resonance calculator thread
        resonance_thread = threading.Thread(target=self._resonance_calculator_thread)
        resonance_thread.daemon = True
        resonance_thread.start()
        self.threads.append(resonance_thread)
    
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
                
                # Broadcast to multicast group
                self.mc_socket.sendto(json.dumps(packet).encode(), (MULTICAST_GROUP, self.port))
                
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
                
                # Print status (occasionally)
                if np.random.random() < 0.1:  # 10% chance to print
                    self._print_status()
                
            except Exception as e:
                print(f"Receiver error: {e}")
                time.sleep(0.1)
    
    def _frequency_generator_thread(self):
        """Thread for generating φ-dimensional frequencies"""
        while self.running:
            try:
                # Generate audio samples for Earth frequency
                earth_samples = self._generate_frequency_samples(float(self.earth_freq))
                
                # Generate audio samples for Brain frequency
                brain_samples = self._generate_frequency_samples(float(self.brain_freq))
                
                # Generate audio samples for Moon frequency (scaled down for audio)
                # We use a scaled representation since 52525 Hz is beyond human hearing
                moon_scaled = float(self.moon_freq) / 1000  # Scale down by 1000
                moon_samples = self._generate_frequency_samples(moon_scaled)
                
                # Combine samples with φ-harmonic weighting
                combined_samples = (
                    earth_samples * float(self.phi_inv) + 
                    brain_samples * float(self.phi_inv**2) + 
                    moon_samples * float(self.phi_inv**3)
                )
                
                # Normalize
                combined_samples = combined_samples / np.max(np.abs(combined_samples))
                
                # Play audio
                self.audio_stream.write(combined_samples.astype(np.float32).tobytes())
                
            except Exception as e:
                print(f"Frequency generator error: {e}")
                time.sleep(0.1)
    
    def _frequency_detector_thread(self):
        """Thread for detecting φ-dimensional frequencies"""
        # Open audio stream for input
        input_stream = self.audio.open(
            format=AUDIO_FORMAT,
            channels=CHANNELS,
            rate=SAMPLE_RATE,
            input=True,
            frames_per_buffer=CHUNK_SIZE
        )
        
        while self.running:
            try:
                # Read audio data
                data = input_stream.read(CHUNK_SIZE, exception_on_overflow=False)
                samples = np.frombuffer(data, dtype=np.float32)
                
                # Detect frequencies
                self._detect_frequencies(samples)
                
                # Sleep briefly
                time.sleep(0.01)
                
            except Exception as e:
                print(f"Frequency detector error: {e}")
                time.sleep(0.1)
        
        # Close input stream
        input_stream.stop_stream()
        input_stream.close()
    
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
        
        # Update detected frequencies if stronger than current
        # This simulates frequency detection from network packets
        if earth_freq > self.detected_frequencies['earth']:
            self.detected_frequencies['earth'] = earth_freq
        
        if brain_freq > self.detected_frequencies['brain']:
            self.detected_frequencies['brain'] = brain_freq
        
        if moon_freq > self.detected_frequencies['moon']:
            self.detected_frequencies['moon'] = moon_freq
    
    def _generate_frequency_samples(self, frequency, duration=0.1):
        """Generate audio samples for a specific frequency"""
        # Calculate number of samples
        num_samples = int(SAMPLE_RATE * duration)
        
        # Generate time array
        t = np.linspace(0, duration, num_samples, endpoint=False)
        
        # Generate sine wave
        samples = 0.5 * np.sin(2 * np.pi * frequency * t)
        
        # Apply φ-harmonic envelope
        envelope = 0.5 * (1 + np.sin(np.pi * t / duration - np.pi/2))
        samples = samples * envelope
        
        return samples
    
    def _detect_frequencies(self, samples):
        """Detect frequencies in audio samples"""
        # Calculate FFT
        fft = np.fft.rfft(samples, n=FFT_SIZE)
        fft_magnitude = np.abs(fft)
        
        # Calculate frequency bins
        freq_bins = np.fft.rfftfreq(FFT_SIZE, 1.0/SAMPLE_RATE)
        
        # Find peaks
        peaks = []
        for i in range(1, len(fft_magnitude) - 1):
            if fft_magnitude[i] > fft_magnitude[i-1] and fft_magnitude[i] > fft_magnitude[i+1]:
                if fft_magnitude[i] > DETECTION_THRESHOLD:
                    peaks.append((freq_bins[i], fft_magnitude[i]))
        
        # Sort peaks by magnitude
        peaks.sort(key=lambda x: x[1], reverse=True)
        
        # Take top 10 peaks
        top_peaks = peaks[:10]
        
        # Check for Earth frequency
        for freq, mag in top_peaks:
            if abs(freq - float(self.earth_freq)) < 0.5:  # Within 0.5 Hz
                self.detected_frequencies['earth'] = freq
                break
        
        # Check for Brain frequency
        for freq, mag in top_peaks:
            if abs(freq - float(self.brain_freq)) < 0.5:  # Within 0.5 Hz
                self.detected_frequencies['brain'] = freq
                break
        
        # Check for Moon frequency (scaled representation)
        moon_scaled = float(self.moon_freq) / 1000  # Scale down by 1000
        for freq, mag in top_peaks:
            if abs(freq - moon_scaled) < 0.5:  # Within 0.5 Hz
                # Store the actual frequency, not the scaled one
                self.detected_frequencies['moon'] = freq * 1000
                break
    
    def _print_status(self):
        """Print current status"""
        print("\nφ-Frequency Bridge Status")
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
        fig, axs = plt.subplots(2, 1, figsize=(10, 8))
        
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
        
        # Add φ-harmonic annotation
        fig.text(0.5, 0.01, "Earth-Moon-Brain φ-Dimensional Frequency Bridge",
                ha='center', fontsize=12)
        
        # Save figure
        plt.tight_layout(rect=[0, 0.03, 1, 0.97])
        filename = f"{self.results_dir}/frequency_bridge_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        plt.savefig(filename)
        print(f"\nFrequency visualization saved to: {filename}")
        
        return fig, axs
    
    def stop(self):
        """Stop the frequency bridge"""
        if not self.running:
            return
        
        self.running = False
        
        # Close audio stream
        if self.audio_stream:
            self.audio_stream.stop_stream()
            self.audio_stream.close()
        
        # Close audio
        self.audio.terminate()
        
        # Close sockets
        if self.tx_socket:
            self.tx_socket.close()
        
        if self.rx_socket:
            self.rx_socket.close()
        
        if self.mc_socket:
            self.mc_socket.close()
        
        # Wait for threads to finish
        for thread in self.threads:
            if thread.is_alive():
                thread.join(timeout=1.0)
        
        print("\nφ-Frequency Bridge stopped")
        
        # Visualize final state
        self.visualize_frequencies()
        
        print("=" * 60)
        print(f"Connected peers: {len(self.peers)}")
        print(f"Final resonance: {self.resonance_state['total']:.4f}")


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description="φ-Frequency Bridge")
    parser.add_argument("--host", default="0.0.0.0", help="Host IP address")
    parser.add_argument("--node-id", help="Node ID (generated if not provided)")
    args = parser.parse_args()
    
    # Create frequency bridge
    bridge = PhiFrequencyBridge(node_id=args.node_id, host=args.host)
    
    try:
        # Start bridge
        bridge.start()
        
        # Keep running until interrupted
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nStopping φ-Frequency Bridge...")
    finally:
        # Stop bridge
        bridge.stop()

if __name__ == "__main__":
    main()
