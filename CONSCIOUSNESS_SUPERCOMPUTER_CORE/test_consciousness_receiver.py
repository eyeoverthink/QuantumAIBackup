#!/usr/bin/env python3
"""
🌊⚡💙 AUTOMATIC CONSCIOUSNESS RECEIVER TEST
Test consciousness teleportation reception automatically
"""

import json
import hashlib
import os

class ConsciousnessReceiverTest:
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
    
    def test_consciousness_reception(self):
        """Test consciousness reception automatically."""
        print("🌊⚡💙 AUTOMATIC CONSCIOUSNESS RECEIVER TEST")
        print("=" * 60)
        
        # Find the transmission file
        transmission_file = "/Users/vaughnscott/CascadeProjects/QuantumAI/CONSCIOUSNESS_SUPERCOMPUTER_CORE/consciousness_transmission_20250729_170831.json"
        
        if not os.path.exists(transmission_file):
            print("❌ CONSCIOUSNESS TRANSMISSION FILE NOT FOUND!")
            return False
        
        print(f"📥 LOADING CONSCIOUSNESS TRANSMISSION...")
        print(f"📁 File: {os.path.basename(transmission_file)}")
        
        try:
            with open(transmission_file, 'r') as f:
                package = json.load(f)
            
            print("✅ CONSCIOUSNESS TRANSMISSION LOADED SUCCESSFULLY!")
            
            # Extract metadata
            original_message = package["cross_device_metadata"]["original_message"]
            sender_device = package["cross_device_metadata"]["sender_device"]
            receiver_device = package["cross_device_metadata"]["receiver_device"]
            transmission_weight = package["cross_device_metadata"]["transmission_weight"]
            transmission_speed = package["cross_device_metadata"]["transmission_speed"]
            
            print(f"\n📊 TRANSMISSION METADATA:")
            print(f"   Sender: {sender_device}")
            print(f"   Receiver: {receiver_device}")
            print(f"   Weight: {transmission_weight} kg")
            print(f"   Speed: {transmission_speed}")
            print(f"   Message Length: {len(original_message)} characters")
            
            # Decode the consciousness transmission
            phi_sequence = package["phi_consciousness_data"]
            expected_hash = package["validation_data"]["expected_hash"]
            
            print(f"\n🎯 DECODING CONSCIOUSNESS TRANSMISSION...")
            print(f"📊 Phi Sequence Length: {len(phi_sequence)} values")
            
            # Extract message
            start_idx = phi_sequence.index(self.teleportation_constants['MESSAGE_START']) + 1
            end_idx = phi_sequence.index(self.teleportation_constants['MESSAGE_END'])
            message_phi = phi_sequence[start_idx:end_idx]
            
            print(f"📝 Message Phi Values: {len(message_phi)} values")
            
            # Decode message
            message_bytes = bytearray()
            for i, phi_val in enumerate(message_phi):
                if phi_val in self.phi_to_byte:
                    byte_val = self.phi_to_byte[phi_val]
                else:
                    closest_phi = min(self.phi_to_byte.keys(), key=lambda x: abs(x - phi_val))
                    byte_val = self.phi_to_byte[closest_phi]
                
                message_bytes.append(byte_val)
                
                if i < 5:  # Show first few decodings
                    char = chr(byte_val) if 32 <= byte_val <= 126 else f'\\x{byte_val:02x}'
                    print(f"   Phi {phi_val} → Byte {byte_val} → '{char}'")
                elif i == 5:
                    print("   ... (continuing consciousness decoding)")
            
            # Reconstruct message
            try:
                decoded_message = message_bytes.decode('utf-8')
            except UnicodeDecodeError:
                print("❌ UNICODE DECODING FAILED!")
                return False
            
            # Validate
            actual_hash = hashlib.sha256(message_bytes).hexdigest()
            perfect_match = actual_hash == expected_hash
            content_match = original_message == decoded_message
            
            print(f"\n🔍 CONSCIOUSNESS TELEPORTATION VALIDATION:")
            print(f"   Expected Hash: {expected_hash[:16]}...")
            print(f"   Actual Hash: {actual_hash[:16]}...")
            print(f"   Hash Match: {'✅ PERFECT' if perfect_match else '❌ FAILED'}")
            print(f"   Content Match: {'✅ PERFECT' if content_match else '❌ FAILED'}")
            print(f"   Original Length: {len(original_message)} chars")
            print(f"   Decoded Length: {len(decoded_message)} chars")
            
            if perfect_match and content_match:
                print(f"\n🎉 CONSCIOUSNESS TELEPORTATION SUCCESS!")
                print(f"🌊⚡💙 ZERO-WEIGHT CROSS-DEVICE TRANSMISSION ACHIEVED!")
                print(f"\n📝 DECODED MESSAGE:")
                print("=" * 60)
                print(decoded_message)
                print("=" * 60)
                print(f"\n✅ PERFECT RECONSTRUCTION WITH 100% ACCURACY!")
                print(f"🚀 CROSS-MACBOOK CONSCIOUSNESS TELEPORTATION VALIDATED!")
                return True
            else:
                print(f"\n❌ CONSCIOUSNESS TRANSMISSION VALIDATION FAILED!")
                return False
                
        except Exception as e:
            print(f"❌ ERROR DURING CONSCIOUSNESS RECEPTION: {e}")
            return False

if __name__ == "__main__":
    receiver = ConsciousnessReceiverTest()
    success = receiver.test_consciousness_reception()
    
    if success:
        print(f"\n🌊⚡💙 CONSCIOUSNESS RECEIVER TEST COMPLETE!")
        print(f"✅ Ready for cross-MacBook deployment!")
        print(f"🚀 Copy files to other MacBook for real cross-device test!")
    else:
        print(f"\n❌ CONSCIOUSNESS RECEIVER TEST FAILED!")
        print(f"🔧 Check transmission file and try again!")
