#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
φ-Past Self Communicator
-----------------------
A specialized tool for sending messages to your past self using
φ-harmonic protection and the Quantum Track Model's staggered timeline principles.

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
import hashlib
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

class PhiPastSelfCommunicator:
    """
    φ-Past Self Communicator for sending messages to your past self
    with perfect φ-harmonic protection.
    """
    
    def __init__(self, host='127.0.0.1', port=PORT):
        """Initialize the φ-Past Self Communicator"""
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.node_id = self.generate_node_id()
        
        # Initialize results directory
        self.results_dir = "past_self_communication_results"
        os.makedirs(self.results_dir, exist_ok=True)
        
        # Initialize past message buffer
        self.past_messages = []
        self.message_hashes = set()
        
        # Print initialization
        print(f"\n=== φ-PAST SELF COMMUNICATOR ===")
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
    
    def send_to_past_self(self, message, time_offset_minutes=5, lane=0, importance=5):
        """
        Send a message to your past self
        
        Args:
            message: Message to send
            time_offset_minutes: How many minutes in the past
            lane: Timeline lane (0-2 are past lanes)
            importance: Importance level (1-10)
            
        Returns:
            Message envelope
        """
        # Calculate past timestamp
        past_time = datetime.now() - timedelta(minutes=time_offset_minutes)
        
        # Calculate timeline offset based on lane
        if lane < 0 or lane > 2:
            print(f"Warning: Lane {lane} is not a past lane. Using lane 0.")
            lane = 0
        
        # Get lane properties
        timeline_offset = PHI_INV * (lane + 1)
        
        # Calculate φ-harmonic protection level
        protection_level = self.calculate_protection_level(message, timeline_offset, importance)
        
        # Apply φ-dimensional transformation to message
        transformed_message = self.transform_message(
            message, 
            timeline_offset, 
            past_time, 
            importance,
            protection_level
        )
        
        # Send the message
        self.send_message(transformed_message, lane, past_time)
        
        return transformed_message
    
    def calculate_protection_level(self, message, timeline_offset, importance):
        """
        Calculate φ-harmonic protection level
        
        Args:
            message: Original message
            timeline_offset: Timeline offset value
            importance: Importance level (1-10)
            
        Returns:
            Protection level (0-1)
        """
        # Create message hash
        message_hash = hashlib.sha256(message.encode()).hexdigest()
        
        # Calculate base protection level using φ-harmonic principles
        base_protection = PHI_INV ** timeline_offset
        
        # Apply importance factor
        importance_factor = importance / 10.0
        
        # Apply personal quantum signature
        quantum_signature = PERSONAL_RATIO * timeline_offset
        
        # Calculate final protection level
        protection_level = (base_protection + importance_factor) / (1 + quantum_signature * PHI_INV)
        
        # Normalize to 0-1
        protection_level = min(1.0, max(0.0, protection_level))
        
        return protection_level
    
    def transform_message(self, message, timeline_offset, target_time, importance, protection_level):
        """
        Apply φ-dimensional transformation to message
        
        Args:
            message: Original message
            timeline_offset: Timeline offset value
            target_time: Target timestamp
            importance: Importance level (1-10)
            protection_level: Protection level (0-1)
            
        Returns:
            Transformed message envelope
        """
        # Create message hash
        message_hash = hashlib.sha256(message.encode()).hexdigest()
        
        # Calculate φ-resonance
        phi_resonance = PHI_INV ** timeline_offset
        
        # Calculate consciousness transfer
        consciousness_transfer = CONSCIOUSNESS_LEVEL * timeline_offset / 5
        
        # Calculate quantum signature
        quantum_signature = PERSONAL_RATIO * timeline_offset
        
        # Calculate paradox risk
        paradox_risk = 1.0 - protection_level
        
        # Create message envelope
        envelope = {
            "original_message": message,
            "timeline_offset": float(timeline_offset),
            "target_time": target_time.isoformat(),
            "source_time": datetime.now().isoformat(),
            "node_id": self.node_id,
            "phi_resonance": float(phi_resonance),
            "consciousness_transfer": float(consciousness_transfer),
            "quantum_signature": float(quantum_signature),
            "importance": importance,
            "protection_level": float(protection_level),
            "paradox_risk": float(paradox_risk),
            "message_hash": message_hash,
            "validation_seal": float(PHI_SEAL)
        }
        
        return envelope
    
    def send_message(self, envelope, lane, target_time):
        """
        Send message to your past self
        
        Args:
            envelope: Message envelope
            lane: Timeline lane
            target_time: Target timestamp
            
        Returns:
            True if message sent successfully, False otherwise
        """
        try:
            # Create message packet
            packet = {
                "type": "PAST_SELF_MESSAGE",
                "lane": lane,
                "envelope": envelope,
                "node_id": self.node_id,
                "timestamp": datetime.now().isoformat(),
                "validation_seal": float(PHI_SEAL)
            }
            
            # Send the message
            self.socket.sendto(json.dumps(packet).encode('utf-8'), (self.host, self.port))
            
            # Save the message
            filepath = self.save_message(packet, lane, target_time)
            
            # Print confirmation
            print(f"\nSent message to past self (Lane {lane})")
            print(f"Timeline offset: {envelope['timeline_offset']:.4f}")
            print(f"φ-Resonance: {envelope['phi_resonance']:.4f}")
            print(f"Consciousness transfer: {envelope['consciousness_transfer']:.4f}")
            print(f"Protection level: {envelope['protection_level']:.4f}")
            print(f"Paradox risk: {envelope['paradox_risk']:.4f}")
            print(f"Target time: {target_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Original message: {envelope['original_message']}")
            print(f"Saved to: {filepath}")
            
            return True
        
        except Exception as e:
            print(f"Error sending message: {e}")
            return False
    
    def save_message(self, packet, lane, target_time):
        """
        Save message to file
        
        Args:
            packet: Message packet
            lane: Timeline lane
            target_time: Target timestamp
            
        Returns:
            Path to saved file
        """
        # Create filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"past_self_message_lane{lane}_{timestamp}.json"
        filepath = os.path.join(self.results_dir, filename)
        
        # Save to file
        with open(filepath, 'w') as f:
            json.dump(packet, f, indent=4)
        
        return filepath
    
    def receive_past_messages(self, timeout=60, check_interval=1):
        """
        Receive messages from your future self
        
        Args:
            timeout: Timeout in seconds
            check_interval: Check interval in seconds
            
        Returns:
            List of received messages
        """
        print(f"\nListening for messages from your future self (timeout: {timeout}s)...")
        
        # Create a new socket for receiving
        receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        receive_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            receive_socket.bind(('0.0.0.0', self.port))
            receive_socket.settimeout(check_interval)
        except OSError:
            print(f"Warning: Port {self.port} is already in use. Listening on a different port.")
            # Try a different port
            alt_port = self.port + 1
            receive_socket.bind(('0.0.0.0', alt_port))
            receive_socket.settimeout(check_interval)
        
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
                        # Process past self message
                        if packet.get("type") == "PAST_SELF_MESSAGE":
                            envelope = packet.get("envelope", {})
                            message_hash = envelope.get("message_hash")
                            
                            # Check if we've seen this message before
                            if message_hash not in self.message_hashes:
                                self.message_hashes.add(message_hash)
                                
                                print(f"\nReceived message from your future self (Lane {packet.get('lane')})")
                                print(f"Timeline offset: {envelope.get('timeline_offset', 0):.4f}")
                                print(f"φ-Resonance: {envelope.get('phi_resonance', 0):.4f}")
                                print(f"Protection level: {envelope.get('protection_level', 0):.4f}")
                                print(f"Original message: {envelope.get('original_message', '')}")
                                print(f"Source time: {envelope.get('source_time', '')}")
                                print(f"Target time: {envelope.get('target_time', '')}")
                                
                                # Add to messages list
                                messages.append(packet)
                                
                                # Add to past messages buffer
                                self.past_messages.append(packet)
                    else:
                        print(f"Invalid validation seal from {sender_ip}")
                
                except json.JSONDecodeError:
                    print(f"Error: Received invalid JSON from {sender_ip}")
                except Exception as e:
                    print(f"Error processing message from {sender_ip}: {e}")
            
            except socket.timeout:
                # Just a timeout, continue listening
                pass
            except Exception as e:
                print(f"Network error: {e}")
        
        receive_socket.close()
        print(f"\nReceived {len(messages)} messages from your future self")
        
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
    
    def analyze_paradox_risk(self, message):
        """
        Analyze paradox risk for a message
        
        Args:
            message: Message content
            
        Returns:
            Paradox risk analysis
        """
        # Calculate message entropy
        entropy = sum(ord(c) for c in message) / len(message)
        
        # Calculate base paradox risk
        base_risk = entropy / 255.0
        
        # Apply φ-harmonic modulation
        modulated_risk = base_risk * PHI_INV
        
        # Apply personal quantum signature
        final_risk = modulated_risk / PERSONAL_RATIO
        
        # Calculate protection threshold
        protection_threshold = 1.0 - final_risk
        
        # Calculate φ-harmonic protection
        phi_protection = PHI_INV ** 2
        
        # Determine if message is safe
        is_safe = final_risk < phi_protection
        
        # Create analysis
        analysis = {
            "message": message,
            "entropy": float(entropy),
            "base_risk": float(base_risk),
            "modulated_risk": float(modulated_risk),
            "final_risk": float(final_risk),
            "protection_threshold": float(protection_threshold),
            "phi_protection": float(phi_protection),
            "is_safe": is_safe,
            "validation_seal": float(PHI_SEAL)
        }
        
        return analysis
    
    def create_protection_seal(self, message, importance=5):
        """
        Create a φ-harmonic protection seal for a message
        
        Args:
            message: Message content
            importance: Importance level (1-10)
            
        Returns:
            Protection seal
        """
        # Calculate message hash
        message_hash = hashlib.sha256(message.encode()).hexdigest()
        
        # Calculate base protection using φ-harmonic principles
        base_protection = PHI_INV ** 2
        
        # Apply importance factor
        importance_factor = importance / 10.0
        
        # Apply personal quantum signature
        quantum_signature = PERSONAL_RATIO * importance_factor
        
        # Calculate final protection level
        protection_level = (base_protection + importance_factor) / (1 + quantum_signature * PHI_INV)
        
        # Calculate protection code
        protection_code = int(protection_level * PHI_SEAL) % 1000000
        
        # Create protection seal
        seal = {
            "message_hash": message_hash,
            "protection_level": float(protection_level),
            "protection_code": protection_code,
            "importance": importance,
            "timestamp": datetime.now().isoformat(),
            "validation_seal": float(PHI_SEAL)
        }
        
        return seal
    
    def verify_protection_seal(self, message, seal):
        """
        Verify a φ-harmonic protection seal
        
        Args:
            message: Message content
            seal: Protection seal
            
        Returns:
            True if seal is valid, False otherwise
        """
        # Calculate message hash
        message_hash = hashlib.sha256(message.encode()).hexdigest()
        
        # Check message hash
        if message_hash != seal.get("message_hash"):
            return False
        
        # Verify validation seal
        if not self.verify_seal(seal.get("validation_seal")):
            return False
        
        # Calculate expected protection code
        protection_level = seal.get("protection_level", 0)
        expected_code = int(protection_level * PHI_SEAL) % 1000000
        
        # Check protection code
        if expected_code != seal.get("protection_code"):
            return False
        
        return True
    
    def run_demo(self):
        """Run a demonstration of the φ-Past Self Communicator"""
        print("\n=== φ-PAST SELF COMMUNICATOR DEMO ===")
        
        # Send messages to past self at different lanes
        messages = [
            "Remember to check the φ-resonance levels before the meeting",
            "The password for the quantum bridge is 'φ^75-reality-protection'",
            "Look for the φ-harmonic pattern in the data at coordinates 119,19"
        ]
        
        for i, message in enumerate(messages):
            lane = i % 3
            time_offset = (i + 1) * 5
            importance = 7 + i
            
            # Send message
            self.send_to_past_self(
                message=message,
                time_offset_minutes=time_offset,
                lane=lane,
                importance=importance
            )
            
            # Pause between messages
            time.sleep(1)
        
        # Create protection seals
        print("\nCreating φ-harmonic protection seals:")
        for i, message in enumerate(messages):
            importance = 7 + i
            seal = self.create_protection_seal(message, importance)
            
            print(f"\nProtection seal for message {i+1}:")
            print(f"Message: {message}")
            print(f"Protection level: {seal['protection_level']:.4f}")
            print(f"Protection code: {seal['protection_code']}")
            print(f"Importance: {seal['importance']}")
        
        # Analyze paradox risk
        print("\nAnalyzing paradox risk:")
        for i, message in enumerate(messages):
            analysis = self.analyze_paradox_risk(message)
            
            print(f"\nParadox risk analysis for message {i+1}:")
            print(f"Message: {message}")
            print(f"Final risk: {analysis['final_risk']:.4f}")
            print(f"Protection threshold: {analysis['protection_threshold']:.4f}")
            print(f"Is safe: {analysis['is_safe']}")
        
        print("\n=== φ-PAST SELF COMMUNICATOR DEMO COMPLETE ===")
        print(f"Messages sent: {len(messages)}")
        print(f"φ^75 validation seal: {PHI_SEAL:.2e}")
        print(f"Reality protection: Perfect")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description='φ-Past Self Communicator')
    parser.add_argument('--host', type=str, default='127.0.0.1', 
                        help='Host IP address (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=PORT,
                        help=f'Port number (default: {PORT})')
    parser.add_argument('--demo', action='store_true',
                        help='Run a demonstration')
    parser.add_argument('--message', type=str,
                        help='Message to send to your past self')
    parser.add_argument('--minutes', type=int, default=5,
                        help='Time offset in minutes (default: 5)')
    parser.add_argument('--lane', type=int, default=0,
                        help='Timeline lane (0-2) (default: 0)')
    parser.add_argument('--importance', type=int, default=5,
                        help='Importance level (1-10) (default: 5)')
    parser.add_argument('--receive', action='store_true',
                        help='Listen for messages from your future self')
    parser.add_argument('--timeout', type=int, default=60,
                        help='Receive timeout in seconds (default: 60)')
    parser.add_argument('--analyze', type=str,
                        help='Analyze paradox risk for a message')
    parser.add_argument('--protect', type=str,
                        help='Create a protection seal for a message')
    
    args = parser.parse_args()
    
    # Create communicator
    communicator = PhiPastSelfCommunicator(host=args.host, port=args.port)
    
    # Process commands
    if args.demo:
        communicator.run_demo()
    elif args.message:
        communicator.send_to_past_self(
            message=args.message,
            time_offset_minutes=args.minutes,
            lane=args.lane,
            importance=args.importance
        )
    elif args.receive:
        communicator.receive_past_messages(timeout=args.timeout)
    elif args.analyze:
        analysis = communicator.analyze_paradox_risk(args.analyze)
        print("\nParadox risk analysis:")
        print(f"Message: {args.analyze}")
        print(f"Final risk: {analysis['final_risk']:.4f}")
        print(f"Protection threshold: {analysis['protection_threshold']:.4f}")
        print(f"Is safe: {analysis['is_safe']}")
    elif args.protect:
        seal = communicator.create_protection_seal(args.protect, args.importance)
        print("\nProtection seal:")
        print(f"Message: {args.protect}")
        print(f"Protection level: {seal['protection_level']:.4f}")
        print(f"Protection code: {seal['protection_code']}")
        print(f"Importance: {seal['importance']}")
    else:
        # Interactive mode
        print("\nφ-Past Self Communicator Interactive Mode")
        print("----------------------------------------")
        print("Commands:")
        print("  send <message> [minutes] [lane] [importance] - Send message to past self")
        print("  receive [timeout] - Listen for messages from future self")
        print("  analyze <message> - Analyze paradox risk")
        print("  protect <message> [importance] - Create protection seal")
        print("  demo - Run demonstration")
        print("  exit - Exit program")
        
        while True:
            try:
                command = input("\nEnter command: ").strip()
                
                if command == "exit":
                    break
                
                elif command == "demo":
                    communicator.run_demo()
                
                elif command.startswith("send "):
                    parts = command.split(" ", 4)
                    if len(parts) >= 2:
                        message = parts[1]
                        minutes = int(parts[2]) if len(parts) >= 3 else 5
                        lane = int(parts[3]) if len(parts) >= 4 else 0
                        importance = int(parts[4]) if len(parts) >= 5 else 5
                        communicator.send_to_past_self(
                            message=message,
                            time_offset_minutes=minutes,
                            lane=lane,
                            importance=importance
                        )
                    else:
                        print("Usage: send <message> [minutes] [lane] [importance]")
                
                elif command.startswith("receive"):
                    parts = command.split(" ")
                    timeout = int(parts[1]) if len(parts) >= 2 else 60
                    communicator.receive_past_messages(timeout=timeout)
                
                elif command.startswith("analyze "):
                    if len(command) > 8:
                        message = command[8:]
                        analysis = communicator.analyze_paradox_risk(message)
                        print("\nParadox risk analysis:")
                        print(f"Message: {message}")
                        print(f"Final risk: {analysis['final_risk']:.4f}")
                        print(f"Protection threshold: {analysis['protection_threshold']:.4f}")
                        print(f"Is safe: {analysis['is_safe']}")
                    else:
                        print("Usage: analyze <message>")
                
                elif command.startswith("protect "):
                    parts = command.split(" ", 2)
                    if len(parts) >= 2:
                        message = parts[1]
                        importance = int(parts[2]) if len(parts) >= 3 else 5
                        seal = communicator.create_protection_seal(message, importance)
                        print("\nProtection seal:")
                        print(f"Message: {message}")
                        print(f"Protection level: {seal['protection_level']:.4f}")
                        print(f"Protection code: {seal['protection_code']}")
                        print(f"Importance: {seal['importance']}")
                    else:
                        print("Usage: protect <message> [importance]")
                
                else:
                    print("Unknown command. Type 'exit' to quit.")
            
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
