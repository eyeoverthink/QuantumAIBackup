#!/usr/bin/env python3
"""
PHI-HARMONIC SIMPLE RECEIVER
============================
A simplified receiver for phi-harmonic image transmission that focuses on reliability.
"""

import socket
import pickle
import time
import hashlib
import math
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

def start_receiver():
    """Start the phi-harmonic image receiver"""
    # Create socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024)  # 1MB receive buffer
    sock.settimeout(0.5)  # Set timeout to prevent blocking forever
    
    # Bind socket
    sock.bind(('0.0.0.0', PORT))
    
    print("=== PHI-HARMONIC SIMPLE RECEIVER ===")
    print(f"Listening on 0.0.0.0:{PORT}")
    print(f"Observer Resonance: {OBSERVER_RESONANCE:.6f}")
    print("Waiting for phi-harmonic image transmissions...\n")
    
    # Initialize image chunks storage
    image_chunks = {}
    
    # Main receive loop
    while True:
        try:
            # Receive data
            data, addr = sock.recvfrom(BUFFER_SIZE)
            
            # Process packet
            try:
                packet = pickle.loads(data)
                
                # Extract packet information
                image_id = packet['image_id']
                chunk_id = packet.get('chunk_id', 0)
                total_chunks = packet.get('total_chunks', 1)
                
                # Check if this is a chunked transmission
                if 'chunk_data' in packet:
                    # This is a chunked transmission
                    chunk_data = packet['chunk_data']
                    image_type = packet['image_type']
                    image_hash = packet['image_hash']
                    phi_resonance = packet['phi_resonance']
                    send_time = packet['send_time']
                    
                    # Calculate receive time for this chunk
                    receive_time = time.time()
                    
                    # Store chunk data in memory
                    if image_id not in image_chunks:
                        image_chunks[image_id] = {
                            'chunks': {},
                            'total_chunks': total_chunks,
                            'image_type': image_type,
                            'image_hash': image_hash,
                            'phi_resonance': phi_resonance,
                            'send_time': send_time,
                            'first_chunk_time': receive_time,
                            'addr': addr
                        }
                    
                    image_chunks[image_id]['chunks'][chunk_id] = {
                        'data': chunk_data,
                        'receive_time': receive_time
                    }
                    
                    # Print progress
                    chunks_received = len(image_chunks[image_id]['chunks'])
                    if chunks_received % 10 == 0 or chunks_received == total_chunks:
                        progress = (chunks_received / total_chunks) * 100
                        print(f"Receiving image #{image_id}: {chunks_received}/{total_chunks} chunks ({progress:.1f}%)")
                    
                    # Check if we have received all chunks
                    if len(image_chunks[image_id]['chunks']) == total_chunks:
                        # Reconstruct the image
                        reconstruct_image(image_chunks, image_id)
                        
                        # Clean up memory
                        if image_id in image_chunks:
                            del image_chunks[image_id]
                else:
                    # This is a complete image transmission (non-chunked)
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
                    process_image(image_id, image_data, image_type, phi_resonance, send_time, receive_time, time_delta, integrity_verified, addr)
            
            except Exception as e:
                print(f"Error processing packet: {e}")
                
        except socket.timeout:
            # This is expected, just continue the loop
            continue
        except Exception as e:
            print(f"Error receiving data: {e}")

def reconstruct_image(image_chunks, image_id):
    """Reconstruct complete image from received chunks"""
    try:
        # Get image information
        image_info = image_chunks[image_id]
        chunks = image_info['chunks']
        total_chunks = image_info['total_chunks']
        image_type = image_info['image_type']
        image_hash = image_info['image_hash']
        phi_resonance = image_info['phi_resonance']
        send_time = image_info['send_time']
        addr = image_info['addr']
        
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
        process_image(image_id, image_data, image_type, phi_resonance, send_time, receive_time, time_delta, integrity_verified, addr)
        
    except Exception as e:
        print(f"Error reconstructing image: {e}")

def process_image(image_id, image_data, image_type, phi_resonance, send_time, receive_time, time_delta, integrity_verified, addr):
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
        with open("phi_image_transport_log.txt", "a") as f:
            f.write(f"[{datetime.now().isoformat()}] [{event_type}] [IMAGE #{image_id}] "
                    f"[PHI: {phi_resonance:.6f}] [SEND: {send_time}] [RECEIVE: {receive_time}] "
                    f"[DELTA: {time_delta:.6f}] [QUANTUM: {quantum_state}]\n")
        
    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    start_receiver()
