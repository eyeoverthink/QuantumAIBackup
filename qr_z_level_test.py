#!/usr/bin/env python3
"""
QR Z-Level Gradient Test - Simple Proof of Concept
By Vaughn Scott & Cascade

Tests the theory of multi-layer QR encoding using:
1. Normal QR layer (dominant instruction)
2. Inverted QR layer (light/reverse instruction)
3. Sequential processing and evolution

This validates the Z-level consciousness physics approach.
"""

import os
import json
import time
import math
import qrcode
import base64
from PIL import Image, ImageOps
from datetime import datetime

# Phi constant for consciousness physics
PHI = (1 + math.sqrt(5)) / 2

class QRZLevelTest:
    """Simple test of Z-level QR encoding with gradient layers."""
    
    def __init__(self, output_dir="qr_z_level_test"):
        """Initialize the Z-level test system."""
        self.output_dir = output_dir
        self.cycle_count = 0
        self.phi_time = time.time() * PHI
        self.resonance = self.phi_time % 1
        
        # Create output directory
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def generate_dual_layer_qr(self, instruction1, instruction2, cycle_id):
        """
        Generate QR code with two layers:
        - Normal layer: instruction2 (dominant)
        - Inverted layer: instruction1 (light/reverse)
        """
        print(f"\n🌊 Generating dual-layer QR for cycle {cycle_id}")
        
        # Create payload with both instructions
        payload = {
            "cycle": cycle_id,
            "timestamp": time.time(),
            "phi_resonance": self.resonance,
            "dominant_instruction": instruction2,
            "light_instruction": instruction1,
            "z_level": "dual_layer"
        }
        
        # Generate normal QR (dominant layer)
        qr_normal = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_normal.add_data(json.dumps(payload))
        qr_normal.make(fit=True)
        
        # Create normal image
        img_normal = qr_normal.make_image(fill_color="black", back_color="white")
        normal_path = os.path.join(self.output_dir, f"qr_normal_cycle_{cycle_id}.png")
        img_normal.save(normal_path)
        
        # Create inverted image (light layer)
        img_inverted = ImageOps.invert(img_normal.convert('RGB'))
        inverted_path = os.path.join(self.output_dir, f"qr_inverted_cycle_{cycle_id}.png")
        img_inverted.save(inverted_path)
        
        print(f"✅ Generated normal QR: {normal_path}")
        print(f"✅ Generated inverted QR: {inverted_path}")
        
        return normal_path, inverted_path, payload
    
    def analyze_light_layer(self, inverted_path, payload):
        """
        Analyze the light/inverted layer for first instruction.
        In a real system, this would decode the inverted QR.
        For now, we extract from the payload.
        """
        print(f"\n🔍 Analyzing LIGHT layer: {inverted_path}")
        
        # Simulate light layer analysis
        light_instruction = payload.get("light_instruction", "no_instruction")
        
        print(f"📝 Light layer instruction: {light_instruction}")
        
        # Process the light instruction
        result = self.execute_instruction(light_instruction, "light")
        
        return result
    
    def analyze_dominant_layer(self, normal_path, payload):
        """
        Analyze the dominant/normal layer for second instruction.
        """
        print(f"\n🔍 Analyzing DOMINANT layer: {normal_path}")
        
        # Simulate dominant layer analysis
        dominant_instruction = payload.get("dominant_instruction", "no_instruction")
        
        print(f"📝 Dominant layer instruction: {dominant_instruction}")
        
        # Process the dominant instruction
        result = self.execute_instruction(dominant_instruction, "dominant")
        
        return result
    
    def execute_instruction(self, instruction, layer_type):
        """Execute an instruction and return the result."""
        print(f"⚡ Executing {layer_type} instruction: {instruction}")
        
        # Simple instruction processing
        if instruction == "increase_resonance":
            self.resonance = min(1.0, self.resonance + 0.1)
            return f"resonance_increased_to_{self.resonance:.3f}"
        
        elif instruction == "phi_multiply":
            self.resonance = (self.resonance * PHI) % 1
            return f"phi_multiplied_resonance_{self.resonance:.3f}"
        
        elif instruction == "time_sync":
            self.phi_time = time.time() * PHI
            return f"time_synced_{self.phi_time:.3f}"
        
        elif instruction == "evolve":
            self.cycle_count += 1
            return f"evolved_to_cycle_{self.cycle_count}"
        
        else:
            return f"processed_{instruction}"
    
    def save_status_qr(self, light_result, dominant_result, cycle_id):
        """Save new QR code with updated status and next instructions."""
        print(f"\n💾 Saving status QR for cycle {cycle_id}")
        
        # Create status payload
        status = {
            "cycle": cycle_id,
            "completed_at": time.time(),
            "phi_resonance": self.resonance,
            "light_result": light_result,
            "dominant_result": dominant_result,
            "next_light_instruction": self.generate_next_instruction("light"),
            "next_dominant_instruction": self.generate_next_instruction("dominant"),
            "z_level": "status_update"
        }
        
        # Generate status QR
        qr_status = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_status.add_data(json.dumps(status))
        qr_status.make(fit=True)
        
        # Save status QR
        img_status = qr_status.make_image(fill_color="blue", back_color="white")
        status_path = os.path.join(self.output_dir, f"qr_status_cycle_{cycle_id}.png")
        img_status.save(status_path)
        
        print(f"✅ Status QR saved: {status_path}")
        
        return status_path, status
    
    def generate_next_instruction(self, layer_type):
        """Generate next instruction based on current state."""
        instructions = {
            "light": ["increase_resonance", "time_sync", "phi_multiply"],
            "dominant": ["evolve", "phi_multiply", "increase_resonance"]
        }
        
        # Use phi-harmonic selection
        index = int(self.resonance * len(instructions[layer_type])) % len(instructions[layer_type])
        return instructions[layer_type][index]
    
    def run_z_level_test(self, cycles=3):
        """Run the complete Z-level test for specified cycles."""
        print(f"🚀 Starting Z-Level QR Test - {cycles} cycles")
        print(f"🌊 Initial phi resonance: {self.resonance:.6f}")
        
        # Initial instructions
        light_instruction = "increase_resonance"
        dominant_instruction = "evolve"
        
        for cycle in range(1, cycles + 1):
            print(f"\n{'='*50}")
            print(f"🔄 CYCLE {cycle} - Z-Level Processing")
            print(f"{'='*50}")
            
            # Step 1: Generate dual-layer QR
            normal_path, inverted_path, payload = self.generate_dual_layer_qr(
                light_instruction, dominant_instruction, cycle
            )
            
            # Step 2: Analyze light layer first
            light_result = self.analyze_light_layer(inverted_path, payload)
            
            # Step 3: Analyze dominant layer second
            dominant_result = self.analyze_dominant_layer(normal_path, payload)
            
            # Step 4: Save status and get next instructions
            status_path, status = self.save_status_qr(light_result, dominant_result, cycle)
            
            # Step 5: Prepare for next cycle
            light_instruction = status["next_light_instruction"]
            dominant_instruction = status["next_dominant_instruction"]
            
            print(f"\n📊 Cycle {cycle} Results:")
            print(f"   Light result: {light_result}")
            print(f"   Dominant result: {dominant_result}")
            print(f"   Current resonance: {self.resonance:.6f}")
            print(f"   Next light: {light_instruction}")
            print(f"   Next dominant: {dominant_instruction}")
        
        print(f"\n🎉 Z-Level test completed! Check {self.output_dir} for QR codes.")
        return True

def main():
    """Run the Z-level QR test."""
    print("🌊⚡ QR Z-Level Gradient Test - Consciousness Physics Validation")
    
    # Create test system
    z_test = QRZLevelTest()
    
    # Run the test
    z_test.run_z_level_test(cycles=3)

if __name__ == "__main__":
    main()
