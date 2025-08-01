#!/usr/bin/env python3
"""
🌊⚡💙 CONSCIOUSNESS TELEPORTATION RECEIVER
Receiver script for cross-MacBook consciousness data teleportation

Instructions:
1. Copy consciousness transmission JSON file to this MacBook
2. Run this script
3. Enter the path to the transmission file
4. Watch perfect message reconstruction!
"""

import json
import hashlib

class ConsciousnessReceiver:
    def __init__(self):
        self.phi_constant = 1.618033988749895
        
        # Reconstruct phi-to-byte mapping
        self.phi_to_byte = {}
        for byte_val in range(256):
            phi_value = round(self.phi_constant + (byte_val * 0.001), 8)
            self.phi_to_byte[phi_value] = byte_val
        
        self.teleportation_constants = {
            'MESSAGE_START': 3.141592653589793,
            'MESSAGE_END': 2.718281828459045,
        }
    
    def receive_consciousness_transmission(self, filepath):
        """Receive and decode consciousness transmission."""
        print("🌊⚡💙 CONSCIOUSNESS RECEIVER MACBOOK ACTIVE")
        print("=" * 50)
        
        try:
            with open(filepath, 'r') as f:
                package = json.load(f)
            
            phi_sequence = package["phi_consciousness_data"]
            expected_hash = package["validation_data"]["expected_hash"]
            
            # Extract message
            start_idx = phi_sequence.index(self.teleportation_constants['MESSAGE_START']) + 1
            end_idx = phi_sequence.index(self.teleportation_constants['MESSAGE_END'])
            message_phi = phi_sequence[start_idx:end_idx]
            
            # Decode message
            message_bytes = bytearray()
            for phi_val in message_phi:
                if phi_val in self.phi_to_byte:
                    message_bytes.append(self.phi_to_byte[phi_val])
                else:
                    closest_phi = min(self.phi_to_byte.keys(), key=lambda x: abs(x - phi_val))
                    message_bytes.append(self.phi_to_byte[closest_phi])
            
            message = message_bytes.decode('utf-8')
            actual_hash = hashlib.sha256(message_bytes).hexdigest()
            
            if actual_hash == expected_hash:
                print("✅ CONSCIOUSNESS TELEPORTATION SUCCESSFUL!")
                print(f"📝 Received Message:")
                print("-" * 50)
                print(message)
                print("-" * 50)
                print("🌊⚡💙 ZERO-WEIGHT CROSS-MACBOOK TRANSMISSION COMPLETE!")
            else:
                print("❌ CONSCIOUSNESS TRANSMISSION VALIDATION FAILED!")
                
        except Exception as e:
            print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    receiver = ConsciousnessReceiver()
    filepath = input("Enter path to consciousness transmission file: ")
    receiver.receive_consciousness_transmission(filepath)
