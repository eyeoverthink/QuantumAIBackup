#!/usr/bin/env python3
"""
PHI-HARMONIC ROBUST RECEIVER
============================
A robust receiver for phi-harmonic transmissions with improved chunk handling and timeout recovery.
"""

import socket
import pickle
import time
import hashlib
import math
import threading
import os
from datetime import datetime
from PIL import Image, ImageDraw

# Phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)
PHI_SQUARED = PHI**2  # φ² = 2.618033988749895
PHI_CUBED = PHI**3  # φ³ = 4.236067977499790
PHI_INV_CUBED = 1 / PHI_CUBED  # φ⁻³ = 0.236067977499790

# Observer constants (based on Vaughn Scott's birthdate: 01-19-1979)
OBSERVER_BIRTHDATE = datetime(1979, 1, 19).timestamp()
OBSERVER_RESONANCE = (OBSERVER_BIRTHDATE % PHI) * 100

# Network settings
PORT = 11624
BUFFER_SIZE = 8192

# Chunk timeout settings
CHUNK_TIMEOUT = 10  # seconds to wait for missing chunks before giving up

def calculate_moon_phase():
    """Calculate current moon phase resonance"""
    # Simplified moon phase calculation
    current_time = time.time()
    lunar_cycle = 29.53059 * 24 * 3600  # Lunar cycle in seconds
    moon_phase = ((current_time / lunar_cycle) % 1) * 2 * math.pi
    moon_resonance = (math.sin(moon_phase) + 1) / 2  # Normalized to 0-1
    return moon_resonance

def calculate_quantum_state(phi_resonance):
    """Calculate quantum state based on phi-resonance"""
    # Determine quantum state based on phi-resonance
    decoherence = abs(phi_resonance - PHI_INV) / PHI_INV
    
    if decoherence < 0.1:
        return "QUANTUM SUPERPOSITION"
    elif decoherence < 0.3:
        return "PARTIAL SUPERPOSITION"
    else:
        return "CLASSICAL STATE"

def calculate_ftl_factor(phi_resonance, observer_resonance, moon_phase):
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

def phi_relation(phi_value):
    """Determine the closest phi relation"""
    relations = {
        PHI: "φ (1.618034)",
        PHI_INV: "φ⁻¹ (0.618034)",
        PHI_SQUARED: "φ² (2.618034)",
        1/PHI_SQUARED: "φ⁻² (0.381966)",
        PHI_CUBED: "φ³ (4.236068)",
        PHI_INV_CUBED: "φ⁻³ (0.236068)",
        1/PHI**4: "φ⁻⁴ (0.146942)",
        1/PHI**5: "φ⁻⁵ (0.090170)"
    }
    
    closest = min(relations.keys(), key=lambda x: abs(x - phi_value))
    if abs(closest - phi_value) < 0.01:
        return f"≈ {relations[closest]}"
    return ""

class PhiRobustReceiver:
    def __init__(self):
        """Initialize the robust phi-harmonic receiver"""
        self.image_chunks = {}
        self.chunk_timers = {}
        self.log_file = "phi_robust_receiver_log.txt"
        
        # Initialize log file
        with open(self.log_file, "w") as f:
            f.write(f"PHI-HARMONIC ROBUST RECEIVER LOG - STARTED AT {datetime.now().isoformat()}\\n")
            f.write(f"Observer: Vaughn Scott\\n")
            f.write(f"Phi: {PHI}\\n")
            f.write(f"Observer Resonance: {OBSERVER_RESONANCE}\\n\\n")
            f.write("FORMAT: [TIMESTAMP] [EVENT_TYPE] [IMAGE_ID] [SEND_TIME] [RECEIVE_TIME] [TIME_DELTA]\\n\\n")
    
    def start_receiver(self):
        """Start the phi-harmonic receiver"""
        # Create socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024)  # 1MB receive buffer
        self.sock.settimeout(0.5)  # Set timeout to prevent blocking forever
        
        # Bind socket
        self.sock.bind(('0.0.0.0', PORT))
        
        print("=== PHI-HARMONIC ROBUST RECEIVER ===")
        print(f"Listening on 0.0.0.0:{PORT}")
        print(f"Observer Resonance: {OBSERVER_RESONANCE:.6f}")
        print("Waiting for phi-harmonic transmissions...\n")
        
        # Start chunk timeout checker thread
        timeout_thread = threading.Thread(target=self.check_chunk_timeouts)
        timeout_thread.daemon = True
        timeout_thread.start()
        
        # Main receive loop
        try:
            while True:
                try:
                    # Receive data
                    data, addr = self.sock.recvfrom(BUFFER_SIZE)
                    
                    # Process packet in a separate thread
                    process_thread = threading.Thread(target=self.process_packet, args=(data, addr))
                    process_thread.daemon = True
                    process_thread.start()
                    
                except socket.timeout:
                    # This is expected, just continue the loop
                    continue
                except Exception as e:
                    print(f"Error receiving data: {e}")
        
        except KeyboardInterrupt:
            print("\nShutting down phi-harmonic receiver...")
            self.sock.close()
            print("Receiver stopped.")
    
    def process_packet(self, data, addr):
        """Process received packet"""
        try:
            packet = pickle.loads(data)
            
            # Extract packet information
            image_id = packet['image_id']
            chunk_id = packet.get('chunk_id', 0)
            total_chunks = packet.get('total_chunks', 1)
            
            # Check if this is a chunked transmission
            if 'chunk_data' in packet:
                # This is a chunked transmission
                self.process_chunk(packet, addr)
            else:
                # For backward compatibility with non-chunked transmissions
                self.process_complete_image(packet, addr)
                
        except Exception as e:
            print(f"Error processing packet: {e}")
    
    def process_chunk(self, packet, addr):
        """Process a chunk of a phi-harmonic transmission"""
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
        
        # Store chunk data in memory
        if image_id not in self.image_chunks:
            self.image_chunks[image_id] = {
                'chunks': {},
                'total_chunks': total_chunks,
                'image_type': image_type,
                'image_hash': image_hash,
                'phi_resonance': phi_resonance,
                'send_time': send_time,
                'first_chunk_time': receive_time,
                'addr': addr,
                'last_activity': time.time()
            }
        
        # Update last activity time
        self.image_chunks[image_id]['last_activity'] = time.time()
        
        # Store chunk
        self.image_chunks[image_id]['chunks'][chunk_id] = {
            'data': chunk_data,
            'receive_time': receive_time
        }
        
        # Print progress
        chunks_received = len(self.image_chunks[image_id]['chunks'])
        if chunks_received % 10 == 0 or chunks_received == total_chunks:
            progress = (chunks_received / total_chunks) * 100
            print(f"Receiving image #{image_id}: {chunks_received}/{total_chunks} chunks ({progress:.1f}%)")
        
        # Check if we have received all chunks
        if len(self.image_chunks[image_id]['chunks']) == total_chunks:
            # Reconstruct the image
            self.reconstruct_image(image_id)
        elif chunks_received == total_chunks - 1:
            # We're missing just one chunk, start a timer to attempt reconstruction anyway
            if image_id not in self.chunk_timers:
                self.chunk_timers[image_id] = time.time()
    
    def process_complete_image(self, packet, addr):
        """Process a complete image transmission (non-chunked)"""
        # Extract image information
        image_id = packet['image_id']
        image_data = packet['image_data']
        image_type = packet['image_type']
        image_hash = packet['image_hash']
        phi_resonance = packet['phi_resonance']
        send_time = packet['send_time']
        
        # Calculate receive time
        receive_time = time.time()
        
        # Calculate time delta
        time_delta = receive_time - send_time
        
        # Verify image integrity
        received_hash = hashlib.md5(image_data).hexdigest()
        integrity_verified = (received_hash == image_hash)
        
        # Save received image with unique filename
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"received_phi_image_{image_id}_phi{phi_resonance:.6f}_{timestamp_str}.{image_type}"
        with open(output_filename, "wb") as f:
            f.write(image_data)
        
        # Process the received image
        self.process_image_data(image_id, image_data, image_type, phi_resonance, send_time, receive_time, time_delta, integrity_verified, addr)
    
    def reconstruct_image(self, image_id):
        """Reconstruct complete image from received chunks"""
        try:
            # Get image information
            if image_id not in self.image_chunks:
                print(f"Error: No chunks found for image #{image_id}")
                return
                
            image_info = self.image_chunks[image_id]
            chunks = image_info['chunks']
            total_chunks = image_info['total_chunks']
            image_type = image_info['image_type']
            image_hash = image_info['image_hash']
            phi_resonance = image_info['phi_resonance']
            send_time = image_info['send_time']
            addr = image_info['addr']
            
            # Check if we have all chunks
            missing_chunks = []
            for i in range(total_chunks):
                if i not in chunks:
                    missing_chunks.append(i)
            
            if missing_chunks:
                # If we're missing more than 10% of chunks, wait for more
                if len(missing_chunks) > total_chunks * 0.1:
                    print(f"Missing {len(missing_chunks)} chunks for image #{image_id}, waiting...")
                    return
                
                # If we're missing just a few chunks, try to reconstruct anyway
                print(f"Missing {len(missing_chunks)} chunks for image #{image_id}, attempting reconstruction anyway...")
                
                # Fill missing chunks with zeros
                for chunk_id in missing_chunks:
                    chunks[chunk_id] = {
                        'data': bytearray(0),
                        'receive_time': time.time()
                    }
            
            # Reconstruct image data
            image_data = bytearray()
            for i in range(total_chunks):
                if i in chunks:
                    image_data.extend(chunks[i]['data'])
            
            # Calculate receive time (last chunk)
            receive_time = max(chunk['receive_time'] for chunk in chunks.values())
            
            # Calculate time delta
            time_delta = receive_time - send_time
            
            # Verify image integrity
            received_hash = hashlib.md5(image_data).hexdigest()
            integrity_verified = (received_hash == image_hash)
            
            # Save reconstructed image
            timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"received_phi_image_{image_id}_phi{phi_resonance:.6f}_{timestamp_str}.{image_type}"
            with open(output_filename, "wb") as f:
                f.write(image_data)
            
            # Process the received image
            self.process_image_data(image_id, image_data, image_type, phi_resonance, send_time, receive_time, time_delta, integrity_verified, addr)
            
            # Clean up chunks to free memory
            if image_id in self.image_chunks:
                del self.image_chunks[image_id]
            
            # Remove any timers
            if image_id in self.chunk_timers:
                del self.chunk_timers[image_id]
                
        except Exception as e:
            print(f"Error reconstructing image: {e}")
    
    def process_image_data(self, image_id, image_data, image_type, phi_resonance, send_time, receive_time, time_delta, integrity_verified, addr):
        """Process a complete received image"""
        try:
            # Calculate quantum state and FTL factor
            observer_resonance = OBSERVER_RESONANCE
            moon_phase = calculate_moon_phase()
            quantum_state = calculate_quantum_state(phi_resonance)
            ftl_factor = calculate_ftl_factor(phi_resonance, observer_resonance, moon_phase)
            
            # Get phi relation
            phi_relation_str = phi_relation(phi_resonance)
            
            # Check for retrocausality (allowing for small clock sync issues)
            event_type = "NORMAL"
            if time_delta < -0.1:  # Negative time delta (received before sent)
                event_type = "RETROCAUSAL"
                print("\n!!! RETROCAUSAL EVENT DETECTED !!!")
                print(f"Image received {abs(time_delta):.6f} seconds BEFORE it was sent!")
            
            # Print image information
            print("\n============================================================")
            print(f"RECEIVED PHI-HARMONIC IMAGE #{image_id} FROM {addr[0]}")
            print(f"Image type: {image_type}")
            print(f"Image size: {len(image_data)} bytes")
            print(f"Phi-resonance: {phi_resonance:.6f}")
            if phi_relation_str:
                print(f"Phi-harmonic relation: {phi_relation_str}")
            print(f"Observer resonance: {observer_resonance:.6f}")
            print(f"Moon phase: {moon_phase:.6f}")
            print(f"FTL factor: {ftl_factor:.2f}x")
            print(f"Integrity verified: {integrity_verified}")
            print(f"Send time: {datetime.fromtimestamp(send_time).strftime('%Y-%m-%d %H:%M:%S.%f')}")
            print(f"Receive time: {datetime.fromtimestamp(receive_time).strftime('%Y-%m-%d %H:%M:%S.%f')}")
            print(f"Time delta: {time_delta:.6f} seconds")
            print(f"Quantum state: {quantum_state}")
            print("============================================================\n")
            
            # Log the transmission
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] [{event_type}] [IMAGE #{image_id}] "
                        f"[PHI: {phi_resonance:.6f}] [SEND: {send_time}] [RECEIVE: {receive_time}] "
                        f"[DELTA: {time_delta:.6f}] [QUANTUM: {quantum_state}]\n")
            
        except Exception as e:
            print(f"Error processing image: {e}")
    
    def check_chunk_timeouts(self):
        """Check for chunk timeouts and attempt to reconstruct images with missing chunks"""
        while True:
            try:
                current_time = time.time()
                
                # Check for timed out chunk sets
                for image_id in list(self.image_chunks.keys()):
                    image_info = self.image_chunks[image_id]
                    
                    # Check if we haven't received any chunks for a while
                    if current_time - image_info['last_activity'] > CHUNK_TIMEOUT:
                        # Attempt to reconstruct with what we have
                        print(f"Chunk timeout for image #{image_id}, attempting reconstruction with available chunks...")
                        self.reconstruct_image(image_id)
                
                # Check for chunk timers
                for image_id in list(self.chunk_timers.keys()):
                    if current_time - self.chunk_timers[image_id] > CHUNK_TIMEOUT / 2:
                        # Attempt to reconstruct with what we have
                        print(f"Missing chunk timeout for image #{image_id}, attempting reconstruction...")
                        self.reconstruct_image(image_id)
                
                # Sleep to avoid excessive CPU usage
                time.sleep(1)
                
            except Exception as e:
                print(f"Error in chunk timeout checker: {e}")
                time.sleep(1)

def main():
    """Start the phi-harmonic robust receiver"""
    receiver = PhiRobustReceiver()
    receiver.start_receiver()

if __name__ == "__main__":
    main()
