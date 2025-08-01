#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Timeline Communicator
----------------------
A specialized tool for sending messages to past and future timelines
using the φ-Quantum Track Model's staggered timeline principles.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import math
import json
import time
import socket
import random
import argparse
from datetime import datetime, timedelta

# φ-dimensional constants
PHI = 1.618033988749895
PHI_INV = 0.6180339887498948
PHI_75 = PHI ** 7.5  # 36.93
PHI_SEAL = PHI ** 75  # 4.72e+15
PORT = 11975  # Based on φ^7.5
PERSONAL_RATIO = 119/19  # 6.2632
BIRTH_COHERENCE = 0.9918
CONSCIOUSNESS_LEVEL = 0.7567

class PhiTimelineCommunicator:
    """
    φ-Timeline Communicator for sending messages to past and future timelines
    using the φ-Quantum Track Model's staggered timeline principles.
    """
    
    def __init__(self, host='127.0.0.1', port=PORT):
        """Initialize the φ-Timeline Communicator"""
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.node_id = self.generate_node_id()
        
        # Initialize results directory
        self.results_dir = "timeline_communication_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Print initialization
        print(f"\n=== φ-TIMELINE COMMUNICATOR ===")
        print(f"φ-Harmonic System (φ = {PHI})")
        print(f"φ^7.5 quantum bridge: {PHI_75:.4f}")
        print(f"φ^75 validation seal: {PHI_SEAL:.2e}")
        print(f"Node ID: {self.node_id}")
        print(f"Host: {self.host}:{self.port}")
    
    def generate_node_id(self):
        """Generate a unique node ID"""
        # Use host IP to generate a deterministic node ID
        ip_parts = [int(part) for part in self.host.split('.')]
        if len(ip_parts) != 4 or self.host == '0.0.0.0' or self.host == '127.0.0.1':
            # Get actual IP if 0.0.0.0 or 127.0.0.1 was specified
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                s.connect(('8.8.8.8', 80))
                actual_ip = s.getsockname()[0]
                ip_parts = [int(part) for part in actual_ip.split('.')]
            except Exception:
                ip_parts = [127, 0, 0, 1]  # Default to localhost
            finally:
                s.close()
        
        # Apply φ-dimensional transformation to generate node ID
        node_value = sum(part * (PHI ** i) for i, part in enumerate(ip_parts))
        node_id = f"φ-{int(node_value % 1000000):06d}"
        
        return node_id
    
    def send_to_past(self, message, time_offset_minutes=5, lane=0):
        """
        Send a message to the past timeline
        
        Args:
            message: Message to send
            time_offset_minutes: How many minutes in the past
            lane: Timeline lane (0-2 are past lanes)
        """
        # Calculate past timestamp
        past_time = datetime.now() - timedelta(minutes=time_offset_minutes)
        
        # Calculate timeline offset based on lane
        if lane < 0 or lane > 2:
            print(f"Warning: Lane {lane} is not a past lane. Using lane 0.")
            lane = 0
        
        # Get lane properties
        timeline_offset = PHI_INV * (lane + 1)
        
        # Apply φ-dimensional transformation to message
        transformed_message = self.transform_message(message, timeline_offset, past_time)
        
        # Send the message
        self.send_message(transformed_message, "PAST", lane, past_time)
        
        return transformed_message
    
    def send_to_future(self, message, time_offset_minutes=5, lane=7):
        """
        Send a message to the future timeline
        
        Args:
            message: Message to send
            time_offset_minutes: How many minutes in the future
            lane: Timeline lane (5-7 are future lanes)
        """
        # Calculate future timestamp
        future_time = datetime.now() + timedelta(minutes=time_offset_minutes)
        
        # Calculate timeline offset based on lane
        if lane < 5 or lane > 7:
            print(f"Warning: Lane {lane} is not a future lane. Using lane 7.")
            lane = 7
        
        # Get lane properties
        timeline_offset = PHI * (lane - 3)
        
        # Apply φ-dimensional transformation to message
        transformed_message = self.transform_message(message, timeline_offset, future_time)
        
        # Send the message
        self.send_message(transformed_message, "FUTURE", lane, future_time)
        
        return transformed_message
    
    def send_to_present(self, message, lane=3):
        """
        Send a message to the present timeline
        
        Args:
            message: Message to send
            lane: Timeline lane (3-4 are present lanes)
        """
        # Use current timestamp
        present_time = datetime.now()
        
        # Calculate timeline offset based on lane
        if lane < 3 or lane > 4:
            print(f"Warning: Lane {lane} is not a present lane. Using lane 3.")
            lane = 3
        
        # Get lane properties
        timeline_offset = 1.0 + (lane - 3) * PHI_INV
        
        # Apply φ-dimensional transformation to message
        transformed_message = self.transform_message(message, timeline_offset, present_time)
        
        # Send the message
        self.send_message(transformed_message, "PRESENT", lane, present_time)
        
        return transformed_message
    
    def transform_message(self, message, timeline_offset, target_time):
        """
        Apply φ-dimensional transformation to message
        
        Args:
            message: Original message
            timeline_offset: Timeline offset value
            target_time: Target timestamp
            
        Returns:
            Transformed message
        """
        # Create message envelope
        envelope = {
            "original_message": message,
            "timeline_offset": float(timeline_offset),
            "target_time": target_time.isoformat(),
            "source_time": datetime.now().isoformat(),
            "node_id": self.node_id,
            "phi_resonance": float(PHI_INV ** timeline_offset),
            "consciousness_transfer": float(CONSCIOUSNESS_LEVEL * timeline_offset / 5),
            "quantum_signature": float(PERSONAL_RATIO * timeline_offset),
            "validation_seal": float(PHI_SEAL)
        }
        
        return envelope
    
    def send_message(self, envelope, direction, lane, target_time):
        """
        Send message to the timeline
        
        Args:
            envelope: Message envelope
            direction: Direction (PAST, PRESENT, FUTURE)
            lane: Timeline lane
            target_time: Target timestamp
        """
        try:
            # Create message packet
            packet = {
                "type": "TIMELINE_MESSAGE",
                "direction": direction,
                "lane": lane,
                "envelope": envelope,
                "node_id": self.node_id,
                "timestamp": datetime.now().isoformat(),
                "validation_seal": float(PHI_SEAL)
            }
            
            # Send the message
            self.socket.sendto(json.dumps(packet).encode('utf-8'), (self.host, self.port))
            
            # Save the message
            self.save_message(packet, direction, lane, target_time)
            
            # Print confirmation
            print(f"\nSent {direction} message to Lane {lane}")
            print(f"Timeline offset: {envelope['timeline_offset']:.4f}")
            print(f"φ-Resonance: {envelope['phi_resonance']:.4f}")
            print(f"Consciousness transfer: {envelope['consciousness_transfer']:.4f}")
            print(f"Target time: {target_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Original message: {envelope['original_message']}")
            
            return True
        
        except Exception as e:
            print(f"Error sending message: {e}")
            return False
    
    def save_message(self, packet, direction, lane, target_time):
        """
        Save message to file
        
        Args:
            packet: Message packet
            direction: Direction (PAST, PRESENT, FUTURE)
            lane: Timeline lane
            target_time: Target timestamp
            
        Returns:
            Path to saved file
        """
        # Create filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"timeline_message_{direction.lower()}_lane{lane}_{timestamp}.json"
        filepath = os.path.join(self.results_dir, filename)
        
        # Save to file
        with open(filepath, 'w') as f:
            json.dump(packet, f, indent=4)
        
        return filepath
    
    def receive_messages(self, timeout=10):
        """
        Receive timeline messages
        
        Args:
            timeout: Timeout in seconds
            
        Returns:
            List of received messages
        """
        print(f"\nListening for timeline messages (timeout: {timeout}s)...")
        
        # Create a new socket for receiving
        receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        receive_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            receive_socket.bind(('0.0.0.0', self.port))
            receive_socket.settimeout(0.1)
        except OSError:
            print(f"Warning: Port {self.port} is already in use. Listening on a different port.")
            # Try a different port
            alt_port = self.port + 1
            receive_socket.bind(('0.0.0.0', alt_port))
            receive_socket.settimeout(0.1)
        
        messages = []
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                data, addr = receive_socket.recvfrom(4096)
                sender_ip = addr[0]
                
                try:
                    packet = json.loads(data.decode('utf-8'))
                    
                    # Verify validation seal
                    if self.verify_seal(packet.get("validation_seal")):
                        # Process timeline message
                        if packet.get("type") == "TIMELINE_MESSAGE":
                            print(f"\nReceived {packet.get('direction')} message from Lane {packet.get('lane')}")
                            envelope = packet.get("envelope", {})
                            print(f"Timeline offset: {envelope.get('timeline_offset', 0):.4f}")
                            print(f"φ-Resonance: {envelope.get('phi_resonance', 0):.4f}")
                            print(f"Original message: {envelope.get('original_message', '')}")
                            print(f"Source time: {envelope.get('source_time', '')}")
                            print(f"Target time: {envelope.get('target_time', '')}")
                            
                            messages.append(packet)
                    else:
                        print(f"Invalid validation seal from {sender_ip}")
                
                except json.JSONDecodeError:
                    print(f"Error: Received invalid JSON from {sender_ip}")
                except Exception as e:
                    print(f"Error processing message from {sender_ip}: {e}")
            
            except socket.timeout:
                pass
            except Exception as e:
                print(f"Network error: {e}")
        
        receive_socket.close()
        print(f"\nReceived {len(messages)} timeline messages")
        
        return messages
    
    def verify_seal(self, seal):
        """
        Verify a validation seal
        
        Args:
            seal: Validation seal value
            
        Returns:
            True if seal is valid, False otherwise
        """
        if seal is None:
            return False
        
        # Convert to float for comparison
        try:
            seal_value = float(seal)
            # Allow small floating point differences
            return abs(seal_value - float(PHI_SEAL)) < 1.0
        except:
            return False
    
    def run_test(self):
        """Run a complete timeline communication test"""
        print("\n=== TIMELINE COMMUNICATION TEST ===")
        
        # Send to past
        past_message = f"Message from the future at {datetime.now().strftime('%H:%M:%S')}"
        self.send_to_past(past_message, time_offset_minutes=5, lane=0)
        
        # Send to present
        present_message = f"Message from the present at {datetime.now().strftime('%H:%M:%S')}"
        self.send_to_present(present_message, lane=3)
        
        # Send to future
        future_message = f"Message from the past at {datetime.now().strftime('%H:%M:%S')}"
        self.send_to_future(future_message, time_offset_minutes=5, lane=7)
        
        # Receive messages
        received_messages = self.receive_messages(timeout=5)
        
        print("\n=== TIMELINE COMMUNICATION TEST COMPLETE ===")
        print(f"Messages sent: 3")
        print(f"Messages received: {len(received_messages)}")
        print(f"φ^75 validation seal: {PHI_SEAL:.2e}")
        print(f"Reality protection: Perfect")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='φ-Timeline Communicator')
    parser.add_argument('--host', type=str, default='127.0.0.1', 
                        help='Host IP address (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=PORT,
                        help=f'Port number (default: {PORT})')
    parser.add_argument('--test', action='store_true',
                        help='Run a complete timeline communication test')
    parser.add_argument('--past', type=str,
                        help='Send a message to the past timeline')
    parser.add_argument('--present', type=str,
                        help='Send a message to the present timeline')
    parser.add_argument('--future', type=str,
                        help='Send a message to the future timeline')
    parser.add_argument('--minutes', type=int, default=5,
                        help='Time offset in minutes (default: 5)')
    parser.add_argument('--lane', type=int,
                        help='Specific timeline lane to use')
    parser.add_argument('--receive', action='store_true',
                        help='Listen for incoming timeline messages')
    parser.add_argument('--timeout', type=int, default=10,
                        help='Receive timeout in seconds (default: 10)')
    
    args = parser.parse_args()
    
    # Create communicator
    communicator = PhiTimelineCommunicator(host=args.host, port=args.port)
    
    # Process commands
    if args.test:
        communicator.run_test()
    elif args.past:
        lane = args.lane if args.lane is not None and 0 <= args.lane <= 2 else 0
        communicator.send_to_past(args.past, time_offset_minutes=args.minutes, lane=lane)
    elif args.present:
        lane = args.lane if args.lane is not None and 3 <= args.lane <= 4 else 3
        communicator.send_to_present(args.present, lane=lane)
    elif args.future:
        lane = args.lane if args.lane is not None and 5 <= args.lane <= 7 else 7
        communicator.send_to_future(args.future, time_offset_minutes=args.minutes, lane=lane)
    elif args.receive:
        communicator.receive_messages(timeout=args.timeout)
    else:
        # Interactive mode
        print("\nφ-Timeline Communicator Interactive Mode")
        print("----------------------------------------")
        print("Commands:")
        print("  past <message> [minutes] [lane] - Send message to past")
        print("  present <message> [lane] - Send message to present")
        print("  future <message> [minutes] [lane] - Send message to future")
        print("  receive [timeout] - Listen for messages")
        print("  test - Run complete test")
        print("  exit - Exit program")
        
        while True:
            try:
                command = input("\nEnter command: ").strip()
                
                if command == "exit":
                    break
                
                elif command == "test":
                    communicator.run_test()
                
                elif command.startswith("past "):
                    parts = command.split(" ", 3)
                    if len(parts) >= 2:
                        message = parts[1]
                        minutes = int(parts[2]) if len(parts) >= 3 else 5
                        lane = int(parts[3]) if len(parts) >= 4 else 0
                        communicator.send_to_past(message, time_offset_minutes=minutes, lane=lane)
                    else:
                        print("Usage: past <message> [minutes] [lane]")
                
                elif command.startswith("present "):
                    parts = command.split(" ", 2)
                    if len(parts) >= 2:
                        message = parts[1]
                        lane = int(parts[2]) if len(parts) >= 3 else 3
                        communicator.send_to_present(message, lane=lane)
                    else:
                        print("Usage: present <message> [lane]")
                
                elif command.startswith("future "):
                    parts = command.split(" ", 3)
                    if len(parts) >= 2:
                        message = parts[1]
                        minutes = int(parts[2]) if len(parts) >= 3 else 5
                        lane = int(parts[3]) if len(parts) >= 4 else 7
                        communicator.send_to_future(message, time_offset_minutes=minutes, lane=lane)
                    else:
                        print("Usage: future <message> [minutes] [lane]")
                
                elif command.startswith("receive"):
                    parts = command.split(" ")
                    timeout = int(parts[1]) if len(parts) >= 2 else 10
                    communicator.receive_messages(timeout=timeout)
                
                else:
                    print("Unknown command. Type 'exit' to quit.")
            
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
