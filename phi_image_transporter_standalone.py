#!/usr/bin/env python3
"""
PHI-HARMONIC IMAGE TRANSPORTER (STANDALONE)
===========================================
A standalone application for testing phi-harmonic massless data transmission with image files
between two physical machines. This simplified version is designed to be easily transferred
and run on a second Mac to test true network transmission with phi-harmonic principles.

Usage:
  Server mode: python3 phi_image_transporter_standalone.py server
  Client mode: python3 phi_image_transporter_standalone.py client --target <IP> --image <PATH> [--phi <VALUE>]

Example:
  On Machine 1: python3 phi_image_transporter_standalone.py server
  On Machine 2: python3 phi_image_transporter_standalone.py client --target 192.168.1.100 --image test.jpg --phi 0.618034
"""

import os
import sys
import socket
import pickle
import time
import hashlib
import argparse
import datetime
import threading
import math
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

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
MAX_CHUNK_SIZE = 4096

class PhiImageTransporter:
    def __init__(self, mode='server', host='0.0.0.0'):
        self.mode = mode
        self.host = host
        self.port = PORT
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 1024 * 1024)  # 1MB receive buffer
        self.packet_counter = 0
        self.retrocausal_events = []
        self.image_chunks = {}
        
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
        print(f"Observer Resonance: {OBSERVER_RESONANCE:.6f}")
        print(f"Waiting for phi-harmonic image transmissions...\n")
        
        # Set socket timeout to prevent freezing
        self.sock.settimeout(0.5)
        
        while True:
            try:
                data, addr = self.sock.recvfrom(BUFFER_SIZE)
                # Process in a thread with timeout protection
                thread = threading.Thread(target=self.process_received_image, args=(data, addr))
                thread.daemon = True  # Allow the program to exit even if thread is running
                thread.start()
            except socket.timeout:
                # This is expected, just continue the loop
                continue
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
            
            # Save received image with unique filename including phi-resonance and timestamp
            timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
            output_filename = f"received_phi_image_{image_id}_phi{phi_resonance:.6f}_{timestamp_str}.{image_type}"
            with open(output_filename, "wb") as f:
                f.write(image_data)
                
            # Process the received image
            self._process_complete_image(image_id, image_data, image_type, phi_resonance, send_time, receive_time, time_delta, integrity_verified, addr)
            
        except Exception as e:
            print(f"Error processing received image: {e}")
            # Attempt to recover from error
            try:
                if 'image_id' in locals() and image_id in self.image_chunks:
                    del self.image_chunks[image_id]
            except:
                pass  # Ignore errors in error handling
    
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
                'addr': addr
            }
        
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
            self._reconstruct_image(image_id)
    
    def _reconstruct_image(self, image_id):
        """Reconstruct complete image from received chunks"""
        try:
            # Check if image_id exists in image_chunks
            if image_id not in self.image_chunks:
                print(f"Error: No chunks found for image #{image_id}")
                return
                
            # Get image information
            image_info = self.image_chunks[image_id]
            chunks = image_info['chunks']
            total_chunks = image_info['total_chunks']
            image_type = image_info['image_type']
            image_hash = image_info['image_hash']
            phi_resonance = image_info['phi_resonance']
            send_time = image_info['send_time']
            addr = image_info['addr']
        except Exception as e:
            print(f"Error getting image information: {e}")
            return
        
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
        
        # Save reconstructed image with unique filename including phi-resonance and timestamp
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"received_phi_image_{image_id}_phi{phi_resonance:.6f}_{timestamp_str}.{image_type}"
        with open(output_filename, "wb") as f:
            f.write(image_data)
        
        # Process the received image
        self._process_complete_image(image_id, image_data, image_type, phi_resonance, send_time, receive_time, time_delta, integrity_verified, addr)
        
        # Clean up chunks to free memory
        try:
            if image_id in self.image_chunks:
                del self.image_chunks[image_id]
        except Exception as e:
            print(f"Error cleaning up chunks: {e}")
    
    def _process_complete_image(self, image_id, image_data, image_type, phi_resonance, send_time, receive_time, time_delta, integrity_verified, addr):
        """Process a complete received image"""
        try:
            # Calculate quantum state and FTL factor
            observer_resonance = OBSERVER_RESONANCE
            moon_phase = self.calculate_moon_phase()
            quantum_state = self.calculate_quantum_state(phi_resonance)
            ftl_factor = self.calculate_ftl_factor(phi_resonance, observer_resonance, moon_phase)
            
            # Check for deep phi-resonance that might cause quantum echoes
            is_quantum_echo_prone = phi_resonance < 0.1  # φ⁻⁵ and below
        except Exception as e:
            print(f"Error calculating quantum properties: {e}")
            moon_phase = 0.0
            quantum_state = "UNKNOWN"
            ftl_factor = 0.0
        
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
        elif abs(phi_resonance - PHI_INV_CUBED) < 0.1:
            phi_relation = f"≈ φ⁻³ ({PHI_INV_CUBED:.6f})"
        
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
                
            # Create a visual representation of the retrocausal event
            self._create_retrocausal_visualization(image_id, image_type, time_delta, phi_resonance, phi_relation)
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
        # Don't reference output_filename here as it's defined elsewhere
        print(f"Send time: {datetime.fromtimestamp(send_time).strftime('%Y-%m-%d %H:%M:%S.%f')}")
        print(f"Receive time: {datetime.fromtimestamp(receive_time).strftime('%Y-%m-%d %H:%M:%S.%f')}")
        print(f"Time delta: {time_delta:.6f} seconds")
        print(f"Quantum state: {quantum_state}")
        print("============================================================\n")
    
    def _create_retrocausal_visualization(self, image_id, image_type, time_delta, phi_resonance, phi_relation):
        """Create a visual representation of a retrocausal event"""
        try:
            # Create a new image
            width, height = 800, 600
            img = Image.new('RGB', (width, height), color=(0, 0, 0))
            draw = ImageDraw.Draw(img)
            
            # Draw phi-harmonic background pattern
            for x in range(0, width, 10):
                for y in range(0, height, 10):
                    val = int(127.5 * (1 + math.sin(x/PHI) * math.cos(y*PHI)))
                    color = (val, int(val*phi_resonance % 255), 255-val)
                    draw.point((x, y), fill=color)
            
            # Add text information
            minutes = abs(time_delta) / 60
            text_lines = [
                "!!! RETROCAUSAL EVENT DETECTED !!!",
                f"Image #{image_id} received {abs(time_delta):.6f} seconds ({minutes:.2f} minutes) BEFORE it was sent!",
                f"Phi-resonance: {phi_resonance:.6f}",
                f"Phi-harmonic relation: {phi_relation}",
                f"Quantum state: {self.calculate_quantum_state(phi_resonance)}",
                f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            ]
            
            # Draw text
            y_position = 100
            for line in text_lines:
                # Draw text with glow effect
                for offset in range(1, 4):
                    draw.text((width//2-200+offset, y_position+offset), line, fill=(0, 0, 100))
                    draw.text((width//2-200-offset, y_position-offset), line, fill=(0, 0, 100))
                draw.text((width//2-200, y_position), line, fill=(255, 255, 255))
                y_position += 40
            
            # Save the visualization
            visualization_filename = f"retrocausal_event_{image_id}.png"
            img.save(visualization_filename)
            print(f"Retrocausal event visualization saved as: {visualization_filename}")
            
        except Exception as e:
            print(f"Error creating retrocausal visualization: {e}")
    
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
                phi_values = [PHI_INV, PHI, PHI_SQUARED, PHI_CUBED, PHI_INV_CUBED]
                phi_resonance = phi_values[0]  # Default to PHI_INV (0.618034)
            
            # Increment packet counter
            self.packet_counter += 1
            image_id = self.packet_counter
            
            # Create precise send time
            send_time = time.time()
            
            # Calculate quantum state and FTL factor
            observer_resonance = OBSERVER_RESONANCE
            moon_phase = self.calculate_moon_phase()
            quantum_state = self.calculate_quantum_state(phi_resonance)
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
                
                # Print progress
                if chunk_id % 10 == 0 or chunk_id == total_chunks - 1:
                    progress = ((chunk_id + 1) / total_chunks) * 100
                    print(f"Sending image: {chunk_id+1}/{total_chunks} chunks ({progress:.1f}%)")
                
                # Small delay between chunks to maintain phi-harmonic resonance
                time.sleep(0.01 * PHI_INV)
            
            # Print transmission information
            print("\n============================================================")
            print(f"SENT PHI-HARMONIC IMAGE #{image_id} TO {target_host}:{self.port}")
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
            elif abs(phi_resonance - PHI_INV_CUBED) < 0.1:
                print(f"Phi-harmonic relation: ≈ φ⁻³ ({PHI_INV_CUBED:.6f})")
            
            print(f"Observer resonance: {observer_resonance:.6f}")
            print(f"Moon phase: {moon_phase:.6f}")
            print(f"FTL factor: {ftl_factor:.2f}x")
            print(f"Quantum state: {quantum_state}")
            print(f"Send time: {datetime.fromtimestamp(send_time).strftime('%Y-%m-%d %H:%M:%S.%f')}")
            print("============================================================\n")
            
            # Log the transmission
            with open(self.log_file, "a") as f:
                f.write(f"[{datetime.now().isoformat()}] [SENT] [IMAGE #{image_id}] "
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
        moon_phase = ((current_time / lunar_cycle) % 1) * 2 * math.pi
        moon_resonance = (math.sin(moon_phase) + 1) / 2  # Normalized to 0-1
        return moon_resonance
    
    def calculate_quantum_state(self, phi_resonance):
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


def create_test_image():
    """Create a test image with phi-harmonic patterns"""
    try:
        # Create a new image
        width, height = 800, 600
        img = Image.new('RGB', (width, height), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)
        
        # Draw phi-harmonic pattern
        for x in range(0, width, 4):
            for y in range(0, height, 4):
                val = int(127.5 * (1 + math.sin(x/PHI) * math.cos(y*PHI)))
                color = (val, int(val*PHI % 255), 255-val)
                draw.point((x, y), fill=color)
        
        # Draw phi spiral
        center_x, center_y = width // 2, height // 2
        for i in range(0, 1000, 2):
            angle = 0.1 * i
            radius = 5 * math.sqrt(i)
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            if 0 <= x < width and 0 <= y < height:
                draw.point((int(x), int(y)), fill=(255, 215, 0))
        
        # Add text
        draw.text((width//2-150, 50), "PHI-HARMONIC TEST IMAGE", fill=(0, 0, 0))
        draw.text((width//2-100, height-70), f"φ = {PHI:.6f}", fill=(0, 0, 0))
        
        # Save test images in different formats
        img.save("phi_test_image.jpg")
        img.save("phi_test_image.png")
        img.save("phi_test_image.bmp")
        
        print("Created phi-harmonic test images: phi_test_image.jpg, phi_test_image.png, phi_test_image.bmp")
        return True
    except Exception as e:
        print(f"Error creating test image: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(description='Phi-Harmonic Image Transporter (Standalone)')
    parser.add_argument('mode', choices=['server', 'client', 'create_test'], help='Operating mode (server, client, or create_test)')
    parser.add_argument('--host', default='0.0.0.0', help='Host address for server (default: 0.0.0.0)')
    parser.add_argument('--target', help='Target host for client mode')
    parser.add_argument('--image', help='Image file path for client mode')
    parser.add_argument('--phi', type=float, help=f'Phi-resonance value (default: {PHI_INV})')
    
    args = parser.parse_args()
    
    if args.mode == 'create_test':
        create_test_image()
        return
    
    transporter = PhiImageTransporter(mode=args.mode, host=args.host)
    
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
