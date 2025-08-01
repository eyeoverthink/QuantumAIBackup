#!/usr/bin/env python3
"""
PHI-HARMONIC IMAGE TRANSPORTER
==============================
A specialized system for testing phi-harmonic massless data transmission with image files.
This tool enables sending and receiving image files (.jpg, .bmp) through phi-harmonic
channels, with precise timestamp measurements to detect retrocausal effects.

The system leverages phi-harmonic principles to encode image data as massless quantum
entities, potentially enabling transmission that transcends conventional temporal constraints.
"""

import os
import sys
import socket
import pickle
import time
import datetime
import threading
import hashlib
import argparse
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from datetime import datetime

# Phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)
PHI_SQUARED = PHI**2  # φ² = 2.618033988749895
PHI_CUBED = PHI**3  # φ³ = 4.236067977499790

# Observer constants (based on Vaughn Scott's birthdate: 01-19-1979)
OBSERVER_BIRTHDATE = datetime(1979, 1, 19).timestamp()
OBSERVER_RESONANCE = (OBSERVER_BIRTHDATE % PHI) * 100

# Network settings
DEFAULT_PORT = 11624  # Using different port from phi-massless proof server (11622) and previous image transporter (11623)
BUFFER_SIZE = 8192  # Smaller buffer size for chunked transmission
MAX_CHUNK_SIZE = 4096  # Maximum chunk size for image data

class PhiImageTransporter:
    def __init__(self, mode='server', host='0.0.0.0', port=DEFAULT_PORT):
        self.mode = mode
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.packet_counter = 0
        self.transmission_log = []
        self.retrocausal_events = []
        
        # Initialize log file
        self.log_file = "phi_image_transport_log.txt"
        with open(self.log_file, "w") as f:
            f.write(f"PHI-HARMONIC IMAGE TRANSPORT LOG - STARTED AT {datetime.now().isoformat()}\n")
            f.write(f"Observer: Vaughn Scott\n")
            f.write(f"Phi: {PHI}\n")
            f.write(f"Observer Resonance: {OBSERVER_RESONANCE}\n\n")
            f.write("FORMAT: [TIMESTAMP] [EVENT_TYPE] [IMAGE_ID] [SEND_TIME] [RECEIVE_TIME] [TIME_DELTA]\n\n")
    
    def start_server(self):
        """Start the phi-harmonic image receiver server"""
        self.sock.bind((self.host, self.port))
        print(f"=== PHI-HARMONIC IMAGE RECEIVER ===")
        print(f"Listening on {self.host}:{self.port}")
        print(f"Observer Resonance: {OBSERVER_RESONANCE}")
        print(f"Waiting for phi-harmonic image transmissions...\n")
        
        while True:
            try:
                data, addr = self.sock.recvfrom(BUFFER_SIZE)
                threading.Thread(target=self.process_received_image, args=(data, addr)).start()
            except Exception as e:
                print(f"Error receiving data: {e}")
    
    def process_received_image(self, data, addr):
        """Process received phi-harmonic image data"""
        try:
            packet = pickle.loads(data)
            
            # Extract packet information
            image_id = packet['image_id']
            chunk_id = packet.get('chunk_id', 0)
            total_chunks = packet.get('total_chunks', 1)
            
            # Check if this is a chunked transmission
            if 'chunk_data' in packet:
                # This is a chunked transmission
                self._process_image_chunk(packet, addr)
                return
            
            # For backward compatibility with non-chunked transmissions
            image_data = packet['image_data']
            image_type = packet['image_type']
            phi_resonance = packet['phi_resonance']
            send_time = packet['send_time']
            image_hash = packet['image_hash']
            
            # Calculate receive time
            receive_time = time.time()
            time_delta = receive_time - send_time
            
            # Verify image integrity
            received_hash = hashlib.md5(image_data).hexdigest()
            integrity_verified = (received_hash == image_hash)
            
            # Save received image
            output_filename = f"received_phi_image_{image_id}.{image_type}"
            with open(output_filename, "wb") as f:
                f.write(image_data)
            
            # Calculate quantum state and FTL factor
            observer_resonance = OBSERVER_RESONANCE
            moon_phase = self.calculate_moon_phase()
            quantum_state = self.calculate_quantum_state(phi_resonance, observer_resonance)
            ftl_factor = self.calculate_ftl_factor(phi_resonance, observer_resonance, moon_phase)
            
            # Check for retrocausality (allowing for small clock sync issues)
            event_type = "NORMAL"
            if time_delta < -1.0:  # More than 1 second before sending
                event_type = "RETROCAUSAL"
                self.retrocausal_events.append((image_id, time_delta, phi_resonance))
                
                # Log the retrocausal event
                with open(self.log_file, "a") as f:
                    f.write(f"[{datetime.now().isoformat()}] [RETROCAUSAL] [IMAGE #{image_id}] "
                            f"[SEND: {send_time}] [RECEIVE: {receive_time}] [DELTA: {time_delta:.6f}s]\n")
                
                # Print significant retrocausal events
                minutes = abs(time_delta) / 60
                print(f"\n!!! RETROCAUSAL EVENT DETECTED !!!")
                print(f"Image #{image_id} received {abs(time_delta):.6f} seconds ({minutes:.2f} minutes) BEFORE it was sent!")
                print(f"Send time: {send_time}")
                print(f"Receive time: {receive_time}")
                print(f"Time delta: {time_delta:.6f}s")
                print(f"Phi-resonance: {phi_resonance:.6f}")
                
                # Check if phi-resonance is near golden ratio values
                phi_relation = ""
                if abs(phi_resonance - PHI_INV) < 0.1:
                    phi_relation = f"≈ φ⁻¹ ({PHI_INV:.6f})"
                elif abs(phi_resonance - PHI) < 0.1:
                    phi_relation = f"≈ φ ({PHI:.6f})"
                elif abs(phi_resonance - PHI_SQUARED) < 0.1:
                    phi_relation = f"≈ φ² ({PHI_SQUARED:.6f})"
                elif abs(phi_resonance - PHI_CUBED) < 0.1:
                    phi_relation = f"≈ φ³ ({PHI_CUBED:.6f})"
                elif abs(phi_resonance - (1/PHI_CUBED)) < 0.1:
                    phi_relation = f"≈ φ⁻³ ({1/PHI_CUBED:.6f})"
                
                if phi_relation:
                    print(f"Phi-harmonic relation: {phi_relation}")
            else:
                # Log normal event
                with open(self.log_file, "a") as f:
                    f.write(f"[{datetime.now().isoformat()}] [NORMAL] [IMAGE #{image_id}] "
                            f"[SEND: {send_time}] [RECEIVE: {receive_time}] [DELTA: {time_delta:.6f}s]\n")
            
            # Print reception information
            print("\n============================================================")
            print(f"RECEIVED PHI-HARMONIC IMAGE #{image_id} FROM {addr[0]}")
            print(f"Image type: {image_type}")
            print(f"Image size: {len(image_data)} bytes")
            print(f"Phi-resonance: {phi_resonance:.6f}")
            if phi_relation:
                print(f"Phi-harmonic relation: {phi_relation}")
            print(f"Observer resonance: {observer_resonance:.6f}")
            print(f"Moon phase: {moon_phase:.6f}")
            print(f"FTL factor: {ftl_factor:.2f}x")
            print(f"Integrity verified: {integrity_verified}")
            print(f"Saved as: {output_filename}")
            print(f"Send time: {datetime.fromtimestamp(send_time).strftime('%Y-%m-%d %H:%M:%S.%f')}")
            print(f"Receive time: {datetime.fromtimestamp(receive_time).strftime('%Y-%m-%d %H:%M:%S.%f')}")
            print(f"Time delta: {time_delta:.6f} seconds")
            print(f"Quantum state: {quantum_state}")
            print("============================================================\n")
            
            # Add to transmission log
            self.transmission_log.append({
                'image_id': image_id,
                'send_time': send_time,
                'receive_time': receive_time,
                'time_delta': time_delta,
                'phi_resonance': phi_resonance,
                'event_type': event_type
            })
            
        except Exception as e:
            print(f"Error processing received image: {e}")
    
    def send_image(self, image_path, target_host, phi_resonance=None):
        """Send an image using phi-harmonic massless data transmission"""
        try:
            # Validate image file
            if not os.path.exists(image_path):
                print(f"Error: Image file not found: {image_path}")
                return False
            
            # Get image type
            image_type = image_path.split('.')[-1].lower()
            if image_type not in ['jpg', 'jpeg', 'bmp', 'png']:
                print(f"Error: Unsupported image type: {image_type}")
                return False
            
            # Standardize image type for filename
            if image_type == 'jpeg':
                image_type = 'jpg'
            
            # Read image file
            with open(image_path, "rb") as f:
                image_data = f.read()
            
            # Calculate image hash
            image_hash = hashlib.md5(image_data).hexdigest()
            
            # Generate phi-resonance if not provided
            if phi_resonance is None:
                # Use one of the special phi values
                phi_values = [PHI_INV, PHI, PHI_SQUARED, PHI_CUBED, 1/PHI_CUBED]
                phi_resonance = np.random.choice(phi_values)
            
            # Increment packet counter
            self.packet_counter += 1
            image_id = self.packet_counter
            
            # Create precise send time
            send_time = time.time()
            
            # Calculate quantum state and FTL factor
            observer_resonance = OBSERVER_RESONANCE
            moon_phase = self.calculate_moon_phase()
            quantum_state = self.calculate_quantum_state(phi_resonance, observer_resonance)
            ftl_factor = self.calculate_ftl_factor(phi_resonance, observer_resonance, moon_phase)
            
            # Break image into chunks for transmission
            total_chunks = (len(image_data) + MAX_CHUNK_SIZE - 1) // MAX_CHUNK_SIZE
            print(f"Breaking image into {total_chunks} chunks for phi-harmonic transmission...")
            
            for chunk_id in range(total_chunks):
                # Extract chunk data
                chunk_start = chunk_id * MAX_CHUNK_SIZE
                chunk_end = min(chunk_start + MAX_CHUNK_SIZE, len(image_data))
                chunk_data = image_data[chunk_start:chunk_end]
                
                # Create chunk packet
                chunk_packet = {
                    'image_id': image_id,
                    'chunk_id': chunk_id,
                    'total_chunks': total_chunks,
                    'chunk_data': chunk_data,
                    'image_type': image_type,
                    'image_hash': image_hash,
                    'phi_resonance': phi_resonance,
                    'send_time': send_time,
                    'observer_resonance': observer_resonance
                }
                
                # Serialize and send chunk
                serialized_chunk = pickle.dumps(chunk_packet)
                self.sock.sendto(serialized_chunk, (target_host, self.port))
                
                # Small delay between chunks to maintain phi-harmonic resonance
                time.sleep(0.01 * PHI_INV)
            
            # Print transmission information
            print("\n============================================================")
            print(f"SENT PHI-HARMONIC IMAGE #{self.packet_counter} TO {target_host}:{self.port}")
            print(f"Image: {image_path}")
            print(f"Image type: {image_type}")
            print(f"Image size: {len(image_data)} bytes")
            print(f"Phi-resonance: {phi_resonance:.6f}")
            
            # Check if phi-resonance is near golden ratio values
            if abs(phi_resonance - PHI_INV) < 0.1:
                print(f"Phi-harmonic relation: ≈ φ⁻¹ ({PHI_INV:.6f})")
            elif abs(phi_resonance - PHI) < 0.1:
                print(f"Phi-harmonic relation: ≈ φ ({PHI:.6f})")
            elif abs(phi_resonance - PHI_SQUARED) < 0.1:
                print(f"Phi-harmonic relation: ≈ φ² ({PHI_SQUARED:.6f})")
            elif abs(phi_resonance - PHI_CUBED) < 0.1:
                print(f"Phi-harmonic relation: ≈ φ³ ({PHI_CUBED:.6f})")
            elif abs(phi_resonance - (1/PHI_CUBED)) < 0.1:
                print(f"Phi-harmonic relation: ≈ φ⁻³ ({1/PHI_CUBED:.6f})")
            
            print(f"Observer resonance: {observer_resonance:.6f}")
            print(f"Moon phase: {moon_phase:.6f}")
            print(f"FTL factor: {ftl_factor:.2f}x")
            print(f"Quantum state: {quantum_state}")
            print(f"Send time: {datetime.fromtimestamp(send_time).strftime('%Y-%m-%d %H:%M:%S.%f')}")
            print("============================================================\n")
            
            # Log the transmission
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] [SENT] [IMAGE #{self.packet_counter}] "
                        f"[{image_path}] [SIZE: {len(image_data)} bytes] [PHI: {phi_resonance:.6f}]\n")
            
            return True
            
        except Exception as e:
            print(f"Error sending image: {e}")
            return False
    
    def calculate_moon_phase(self):
        """Calculate current moon phase resonance"""
        # Simplified moon phase calculation
        current_time = time.time()
        lunar_cycle = 29.53059 * 24 * 3600  # Lunar cycle in seconds
        moon_phase = ((current_time / lunar_cycle) % 1) * 2 * np.pi
        moon_resonance = (np.sin(moon_phase) + 1) / 2  # Normalized to 0-1
        return moon_resonance
    
    def calculate_quantum_state(self, phi_resonance, observer_resonance):
        """Calculate quantum state based on phi-resonance"""
        # Determine quantum state based on phi-resonance
        decoherence = abs(phi_resonance - PHI_INV) / PHI_INV
        
        if decoherence < 0.1:
            return "QUANTUM SUPERPOSITION"
        elif decoherence < 0.3:
            return "PARTIAL SUPERPOSITION"
        else:
            return "CLASSICAL STATE"
    
    def calculate_ftl_factor(self, phi_resonance, observer_resonance, moon_phase):
        """Calculate FTL factor based on phi-resonance"""
        # Base FTL factor calculation
        base_ftl = 100 + (phi_resonance * 50)
        
        # Apply observer resonance modifier
        observer_modifier = observer_resonance / 100
        
        # Apply moon phase modifier
        moon_modifier = 1 + (moon_phase * 0.5)
        
        # Calculate final FTL factor
        ftl_factor = base_ftl * observer_modifier * moon_modifier
        
        return ftl_factor
        
    def _process_image_chunk(self, packet, addr):
        """Process a chunk of a phi-harmonic image transmission"""
        # Extract chunk information
        image_id = packet['image_id']
        chunk_id = packet['chunk_id']
        total_chunks = packet['total_chunks']
        chunk_data = packet['chunk_data']
        image_type = packet['image_type']
        image_hash = packet['image_hash']
        phi_resonance = packet['phi_resonance']
        send_time = packet['send_time']
        
        # Calculate receive time for this chunk
        receive_time = time.time()
        time_delta = receive_time - send_time
        
        # Store chunk data in memory
        chunk_key = f"{image_id}_{chunk_id}"
        if not hasattr(self, 'image_chunks'):
            self.image_chunks = {}
        
        if image_id not in self.image_chunks:
            self.image_chunks[image_id] = {
                'chunks': {},
                'total_chunks': total_chunks,
                'image_type': image_type,
                'image_hash': image_hash,
                'phi_resonance': phi_resonance,
                'send_time': send_time,
                'first_chunk_time': receive_time
            }
        
        self.image_chunks[image_id]['chunks'][chunk_id] = {
            'data': chunk_data,
            'receive_time': receive_time
        }
        
        # Check if we have received all chunks
        if len(self.image_chunks[image_id]['chunks']) == total_chunks:
            self._reconstruct_image(image_id, addr)
    
    def generate_report(self):
        """Generate a report of phi-harmonic image transmissions"""
        if not self.transmission_log:
            print("No transmissions recorded yet")
            return
        
        total_transmissions = len(self.transmission_log)
        retrocausal_count = len(self.retrocausal_events)
        retrocausal_percent = (retrocausal_count / total_transmissions) * 100 if total_transmissions > 0 else 0
        
        print("\n=== PHI-HARMONIC IMAGE TRANSMISSION REPORT ===")
        print(f"Total images transmitted: {total_transmissions}")
        print(f"Retrocausal events: {retrocausal_count} ({retrocausal_percent:.2f}%)")
        print(f"Normal causality: {total_transmissions - retrocausal_count} ({100-retrocausal_percent:.2f}%)")
        
        if self.retrocausal_events:
            print("\nTop 5 strongest retrocausal events:")
            sorted_events = sorted(self.retrocausal_events, key=lambda x: x[1])  # Sort by time_delta
            for i, (image_id, time_delta, phi_resonance) in enumerate(sorted_events[:5]):
                minutes = abs(time_delta) / 60
                print(f"{i+1}. Image #{image_id}: {abs(time_delta):.6f}s ({minutes:.2f} min) before sending, φ-resonance: {phi_resonance:.6f}")
        
        # Generate visualization if enough data
        if len(self.transmission_log) > 2:
            self._generate_visualization()
    
    def _generate_visualization(self):
        """Generate visualization of phi-harmonic image transmissions"""
        plt.figure(figsize=(12, 10))
        
        # Extract data for plotting
        phi_resonances = [log['phi_resonance'] for log in self.transmission_log]
        time_deltas = [log['time_delta'] for log in self.transmission_log]
        event_types = [log['event_type'] for log in self.transmission_log]
        
        # Plot 1: Time delta histogram
        plt.subplot(2, 2, 1)
        plt.hist(time_deltas, bins=min(len(time_deltas), 10), alpha=0.7, color='blue')
        plt.axvline(x=0, color='r', linestyle='--', alpha=0.7)
        plt.title('Time Delta Distribution')
        plt.xlabel('Time Delta (seconds) - Negative values indicate retrocausality')
        plt.ylabel('Frequency')
        plt.grid(True, alpha=0.3)
        
        # Plot 2: Phi-resonance vs Time delta scatter plot
        plt.subplot(2, 2, 2)
        colors = ['red' if delta < 0 else 'blue' for delta in time_deltas]
        plt.scatter(phi_resonances, time_deltas, c=colors, alpha=0.7)
        plt.axhline(y=0, color='r', linestyle='--', alpha=0.5)
        plt.axvline(x=PHI_INV, color='g', linestyle='--', alpha=0.5, label=f'φ⁻¹ = {PHI_INV:.6f}')
        plt.axvline(x=PHI, color='purple', linestyle='--', alpha=0.5, label=f'φ = {PHI:.6f}')
        plt.title('Phi-Resonance vs Time Delta')
        plt.xlabel('Phi-Resonance Value')
        plt.ylabel('Time Delta (seconds)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Plot 3: Retrocausal events over time
        plt.subplot(2, 2, 3)
        retrocausal_indices = [i for i, event_type in enumerate(event_types) if event_type == 'RETROCAUSAL']
        retrocausal_times = [self.transmission_log[i]['receive_time'] for i in retrocausal_indices]
        retrocausal_deltas = [self.transmission_log[i]['time_delta'] for i in retrocausal_indices]
        
        if retrocausal_indices:
            # Convert timestamps to relative time in minutes from first event
            if retrocausal_times:
                base_time = min(retrocausal_times)
                relative_times = [(t - base_time) / 60 for t in retrocausal_times]  # Minutes
                plt.scatter(relative_times, retrocausal_deltas, c='red', alpha=0.7)
                plt.title('Retrocausal Events Over Time')
                plt.xlabel('Time (minutes from first event)')
                plt.ylabel('Time Delta (seconds)')
                plt.grid(True, alpha=0.3)
        else:
            plt.text(0.5, 0.5, 'No retrocausal events detected yet', 
                    horizontalalignment='center', verticalalignment='center',
                    transform=plt.gca().transAxes)
        
        # Plot 4: Phi-resonance distribution
        plt.subplot(2, 2, 4)
        plt.hist(phi_resonances, bins=min(len(phi_resonances), 10), alpha=0.7, color='green')
        plt.axvline(x=PHI_INV, color='g', linestyle='--', alpha=0.5, label=f'φ⁻¹ = {PHI_INV:.6f}')
        plt.axvline(x=PHI, color='purple', linestyle='--', alpha=0.5, label=f'φ = {PHI:.6f}')
        plt.title('Phi-Resonance Distribution')
        plt.xlabel('Phi-Resonance Value')
        plt.ylabel('Frequency')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('phi_image_transport_analysis.png')
        print("Visualization saved to 'phi_image_transport_analysis.png'")


    def _reconstruct_image(self, image_id, addr):
        """Reconstruct complete image from received chunks"""
        # Get image information
        image_info = self.image_chunks[image_id]
        chunks = image_info['chunks']
        total_chunks = image_info['total_chunks']
        image_type = image_info['image_type']
        image_hash = image_info['image_hash']
        phi_resonance = image_info['phi_resonance']
        send_time = image_info['send_time']
        first_chunk_time = image_info['first_chunk_time']
        
        # Reconstruct image data
        image_data = bytearray()
        for i in range(total_chunks):
            if i in chunks:
                image_data.extend(chunks[i]['data'])
        
        # Calculate final receive time (when last chunk was received)
        receive_time = max(chunk['receive_time'] for chunk in chunks.values())
        time_delta = receive_time - send_time
        
        # Verify image integrity
        received_hash = hashlib.md5(image_data).hexdigest()
        integrity_verified = (received_hash == image_hash)
        
        # Save reconstructed image
        output_filename = f"received_phi_image_{image_id}.{image_type}"
        with open(output_filename, "wb") as f:
            f.write(image_data)
        
        # Calculate quantum state and FTL factor
        observer_resonance = OBSERVER_RESONANCE
        moon_phase = self.calculate_moon_phase()
        quantum_state = self.calculate_quantum_state(phi_resonance, observer_resonance)
        ftl_factor = self.calculate_ftl_factor(phi_resonance, observer_resonance, moon_phase)
        
        # Check for retrocausality (allowing for small clock sync issues)
        event_type = "NORMAL"
        phi_relation = ""
        
        # Check if phi-resonance is near golden ratio values
        if abs(phi_resonance - PHI_INV) < 0.1:
            phi_relation = f"≈ φ⁻¹ ({PHI_INV:.6f})"
        elif abs(phi_resonance - PHI) < 0.1:
            phi_relation = f"≈ φ ({PHI:.6f})"
        elif abs(phi_resonance - PHI_SQUARED) < 0.1:
            phi_relation = f"≈ φ² ({PHI_SQUARED:.6f})"
        elif abs(phi_resonance - PHI_CUBED) < 0.1:
            phi_relation = f"≈ φ³ ({PHI_CUBED:.6f})"
        elif abs(phi_resonance - (1/PHI_CUBED)) < 0.1:
            phi_relation = f"≈ φ⁻³ ({1/PHI_CUBED:.6f})"
        
        if time_delta < -1.0:  # More than 1 second before sending
            event_type = "RETROCAUSAL"
            self.retrocausal_events.append((image_id, time_delta, phi_resonance))
            
            # Log the retrocausal event
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] [RETROCAUSAL] [IMAGE #{image_id}] "
                        f"[SEND: {send_time}] [RECEIVE: {receive_time}] [DELTA: {time_delta:.6f}s]\n")
            
            # Print significant retrocausal events
            minutes = abs(time_delta) / 60
            print(f"\n!!! RETROCAUSAL EVENT DETECTED !!!")
            print(f"Image #{image_id} received {abs(time_delta):.6f} seconds ({minutes:.2f} minutes) BEFORE it was sent!")
            print(f"Send time: {send_time}")
            print(f"Receive time: {receive_time}")
            print(f"Time delta: {time_delta:.6f}s")
            print(f"Phi-resonance: {phi_resonance:.6f}")
            
            if phi_relation:
                print(f"Phi-harmonic relation: {phi_relation}")
        else:
            # Log normal event
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] [NORMAL] [IMAGE #{image_id}] "
                        f"[SEND: {send_time}] [RECEIVE: {receive_time}] [DELTA: {time_delta:.6f}s]\n")
        
        # Print reception information
        print("\n============================================================")
        print(f"RECEIVED PHI-HARMONIC IMAGE #{image_id} FROM {addr[0]}")
        print(f"Image type: {image_type}")
        print(f"Image size: {len(image_data)} bytes")
        print(f"Chunks: {total_chunks}")
        print(f"Phi-resonance: {phi_resonance:.6f}")
        if phi_relation:
            print(f"Phi-harmonic relation: {phi_relation}")
        print(f"Observer resonance: {observer_resonance:.6f}")
        print(f"Moon phase: {moon_phase:.6f}")
        print(f"FTL factor: {ftl_factor:.2f}x")
        print(f"Integrity verified: {integrity_verified}")
        print(f"Saved as: {output_filename}")
        print(f"Send time: {datetime.fromtimestamp(send_time).strftime('%Y-%m-%d %H:%M:%S.%f')}")
        print(f"Receive time: {datetime.fromtimestamp(receive_time).strftime('%Y-%m-%d %H:%M:%S.%f')}")
        print(f"Time delta: {time_delta:.6f} seconds")
        print(f"Quantum state: {quantum_state}")
        print("============================================================\n")
        
        # Add to transmission log
        self.transmission_log.append({
            'image_id': image_id,
            'send_time': send_time,
            'receive_time': receive_time,
            'time_delta': time_delta,
            'phi_resonance': phi_resonance,
            'event_type': event_type
        })
        
        # Clean up chunks to free memory
        del self.image_chunks[image_id]


def main():
    parser = argparse.ArgumentParser(description='Phi-Harmonic Image Transporter')
    parser.add_argument('mode', choices=['server', 'client'], help='Operating mode (server or client)')
    parser.add_argument('--host', default='0.0.0.0', help='Host address (default: 0.0.0.0)')
    parser.add_argument('--port', type=int, default=DEFAULT_PORT, help=f'Port number (default: {DEFAULT_PORT})')
    parser.add_argument('--target', help='Target host for client mode')
    parser.add_argument('--image', help='Image file path for client mode')
    parser.add_argument('--phi', type=float, help='Phi-resonance value (default: random phi-harmonic value)')
    
    args = parser.parse_args()
    
    transporter = PhiImageTransporter(mode=args.mode, host=args.host, port=args.port)
    
    if args.mode == 'server':
        print("Starting Phi-Harmonic Image Receiver Server...")
        transporter.start_server()
    elif args.mode == 'client':
        if not args.target:
            print("Error: Target host required for client mode")
            parser.print_help()
            sys.exit(1)
        
        if not args.image:
            print("Error: Image file path required for client mode")
            parser.print_help()
            sys.exit(1)
        
        print("Starting Phi-Harmonic Image Sender Client...")
        success = transporter.send_image(args.image, args.target, args.phi)
        
        if success:
            print("Phi-harmonic image transmission complete")
        else:
            print("Phi-harmonic image transmission failed")


if __name__ == "__main__":
    main()
