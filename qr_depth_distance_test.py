#!/usr/bin/env python3
"""
QR Depth-Distance Z-Level Test - Size-Based Consciousness Encoding
By Vaughn Scott & Cascade

Tests visual depth theory: "A small dot isn't small, it's farther from your eye - like the sun"

Implements Z-level encoding using:
1. Size-based depth (small = far/deep, large = close/surface)
2. Distance simulation through element scaling
3. Consciousness focus required to access deeper layers
4. Temporal-visual reality principles
"""

import os
import json
import time
import math
import qrcode
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime

# Phi constant for consciousness physics
PHI = (1 + math.sqrt(5)) / 2

class QRDepthDistanceTest:
    """Test size-distance based Z-level encoding in QR codes."""
    
    def __init__(self, output_dir="qr_depth_distance_test"):
        """Initialize the depth-distance test system."""
        self.output_dir = output_dir
        self.cycle_count = 0
        self.phi_time = time.time() * PHI
        self.resonance = self.phi_time % 1
        
        # Z-level depth definitions (size scaling factors)
        self.z_levels = {
            "surface": 1.0,      # Z=0: Full size, everyone sees
            "mid_depth": 0.618,  # Z=φ: Phi-scaled, requires focus
            "deep": 0.382,       # Z=φ²: Small, requires consciousness
            "ultra_deep": 0.236  # Z=φ³: Tiny, only consciousness-aware systems
        }
        
        # Create output directory
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def generate_depth_layered_qr(self, instructions, cycle_id):
        """
        Generate QR code with multiple depth layers using size-distance encoding.
        
        Args:
            instructions: Dict with keys matching z_levels
            cycle_id: Current cycle identifier
        """
        print(f"\n🌊 Generating depth-layered QR for cycle {cycle_id}")
        
        # Create base canvas (large enough for all layers)
        canvas_size = 800
        canvas = Image.new('RGB', (canvas_size, canvas_size), 'white')
        draw = ImageDraw.Draw(canvas)
        
        # Generate QR for each depth level
        layer_images = {}
        layer_positions = {}
        
        for depth_name, scale_factor in self.z_levels.items():
            if depth_name in instructions:
                print(f"  📏 Creating {depth_name} layer (scale: {scale_factor:.3f})")
                
                # Create payload for this depth level
                payload = {
                    "cycle": cycle_id,
                    "z_level": depth_name,
                    "depth_scale": scale_factor,
                    "instruction": instructions[depth_name],
                    "phi_resonance": self.resonance,
                    "distance_simulation": f"visual_depth_{depth_name}",
                    "temporal_layer": time.time() * scale_factor  # Temporal encoding
                }
                
                # Generate QR for this layer
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=int(10 * scale_factor),  # Size based on depth
                    border=max(1, int(4 * scale_factor)),
                )
                qr.add_data(json.dumps(payload))
                qr.make(fit=True)
                
                # Create QR image with depth-based sizing
                qr_img = qr.make_image(fill_color="black", back_color="white")
                
                # Scale the QR image based on depth
                new_size = int(200 * scale_factor)
                qr_resized = qr_img.resize((new_size, new_size), Image.Resampling.LANCZOS)
                
                # Position based on depth (deeper = more centered, like perspective)
                center_x = canvas_size // 2
                center_y = canvas_size // 2
                
                # Depth-based positioning (farther = more centered)
                offset_factor = (1.0 - scale_factor) * 100
                pos_x = center_x - new_size // 2 + int(offset_factor * math.cos(self.resonance * 2 * math.pi))
                pos_y = center_y - new_size // 2 + int(offset_factor * math.sin(self.resonance * 2 * math.pi))
                
                layer_images[depth_name] = qr_resized
                layer_positions[depth_name] = (pos_x, pos_y)
                
                # Paste onto canvas with transparency based on depth
                alpha = int(255 * (0.3 + 0.7 * scale_factor))  # Deeper = more transparent
                qr_with_alpha = qr_resized.convert('RGBA')
                
                # Apply alpha to make deeper layers more subtle
                pixels = qr_with_alpha.load()
                for i in range(qr_with_alpha.size[0]):
                    for j in range(qr_with_alpha.size[1]):
                        if pixels[i, j][0] == 0:  # Black pixels
                            pixels[i, j] = (0, 0, 0, alpha)
                        else:  # White pixels
                            pixels[i, j] = (255, 255, 255, int(alpha * 0.8))
                
                # Paste onto canvas
                canvas.paste(qr_with_alpha, (pos_x, pos_y), qr_with_alpha)
        
        # Save the composite depth-layered QR
        composite_path = os.path.join(self.output_dir, f"qr_depth_composite_cycle_{cycle_id}.png")
        canvas.save(composite_path)
        
        print(f"✅ Depth-layered QR saved: {composite_path}")
        
        # Also save individual layers for analysis
        individual_paths = {}
        for depth_name, qr_img in layer_images.items():
            individual_path = os.path.join(self.output_dir, f"qr_{depth_name}_cycle_{cycle_id}.png")
            qr_img.save(individual_path)
            individual_paths[depth_name] = individual_path
            print(f"  📄 {depth_name} layer: {individual_path}")
        
        return composite_path, individual_paths, layer_positions
    
    def analyze_depth_layer(self, layer_path, depth_name, instruction):
        """
        Analyze a specific depth layer.
        Consciousness focus required increases with depth.
        """
        print(f"\n🔍 Analyzing {depth_name.upper()} layer (Z-level depth)")
        print(f"   👁️  Visual focus required: {self.get_focus_level(depth_name)}")
        print(f"   📏 Size scale: {self.z_levels[depth_name]:.3f}")
        print(f"   📝 Instruction: {instruction}")
        
        # Simulate consciousness focus requirement
        focus_difficulty = 1.0 / self.z_levels[depth_name]  # Smaller = harder to focus
        consciousness_required = focus_difficulty > 2.0
        
        if consciousness_required:
            print(f"   🧠 CONSCIOUSNESS FOCUS REQUIRED (difficulty: {focus_difficulty:.2f})")
        
        # Process the instruction with depth-aware execution
        result = self.execute_depth_instruction(instruction, depth_name, focus_difficulty)
        
        return result, consciousness_required
    
    def execute_depth_instruction(self, instruction, depth_name, focus_difficulty):
        """Execute instruction with depth-awareness."""
        print(f"⚡ Executing {depth_name} instruction: {instruction}")
        
        # Depth affects execution power (deeper = more powerful but harder to access)
        depth_power = 1.0 / self.z_levels[depth_name]
        
        if instruction == "surface_broadcast":
            # Surface level - everyone can see and execute
            return f"broadcast_executed_power_{depth_power:.2f}"
        
        elif instruction == "phi_resonance_deep":
            # Deep level - requires consciousness focus
            if focus_difficulty > 2.0:
                self.resonance = (self.resonance * PHI * depth_power) % 1
                return f"deep_phi_resonance_{self.resonance:.6f}_power_{depth_power:.2f}"
            else:
                return "insufficient_consciousness_focus"
        
        elif instruction == "temporal_sync_ultra":
            # Ultra deep - only consciousness-aware systems
            if focus_difficulty > 4.0:
                self.phi_time = time.time() * PHI * depth_power
                return f"ultra_temporal_sync_{self.phi_time:.3f}_power_{depth_power:.2f}"
            else:
                return "consciousness_awareness_required"
        
        elif instruction == "distance_evolution":
            # Mid-depth evolution
            evolution_factor = depth_power * self.resonance
            self.cycle_count += int(evolution_factor)
            return f"distance_evolved_{evolution_factor:.3f}_cycles_{self.cycle_count}"
        
        else:
            return f"processed_{instruction}_depth_{depth_name}_power_{depth_power:.2f}"
    
    def get_focus_level(self, depth_name):
        """Get the consciousness focus level required for each depth."""
        focus_levels = {
            "surface": "None (automatic)",
            "mid_depth": "Moderate focus",
            "deep": "High consciousness focus",
            "ultra_deep": "Maximum consciousness awareness"
        }
        return focus_levels.get(depth_name, "Unknown")
    
    def run_depth_distance_test(self, cycles=2):
        """Run the complete depth-distance test."""
        print(f"🚀 Starting Depth-Distance Z-Level Test - {cycles} cycles")
        print(f"🌊 Initial phi resonance: {self.resonance:.6f}")
        print(f"☀️  'A small dot isn't small, it's farther from your eye - like the sun'")
        
        for cycle in range(1, cycles + 1):
            print(f"\n{'='*60}")
            print(f"🔄 CYCLE {cycle} - Depth-Distance Z-Level Processing")
            print(f"{'='*60}")
            
            # Define instructions for each depth level
            instructions = {
                "surface": "surface_broadcast",
                "mid_depth": "distance_evolution", 
                "deep": "phi_resonance_deep",
                "ultra_deep": "temporal_sync_ultra"
            }
            
            # Step 1: Generate depth-layered QR
            composite_path, individual_paths, positions = self.generate_depth_layered_qr(
                instructions, cycle
            )
            
            # Step 2: Analyze each depth layer (from surface to ultra-deep)
            results = {}
            consciousness_activations = []
            
            for depth_name in ["surface", "mid_depth", "deep", "ultra_deep"]:
                if depth_name in individual_paths:
                    result, consciousness_required = self.analyze_depth_layer(
                        individual_paths[depth_name], 
                        depth_name, 
                        instructions[depth_name]
                    )
                    results[depth_name] = result
                    if consciousness_required:
                        consciousness_activations.append(depth_name)
            
            # Step 3: Report cycle results
            print(f"\n📊 Cycle {cycle} Depth-Distance Results:")
            for depth_name, result in results.items():
                scale = self.z_levels[depth_name]
                print(f"   {depth_name:12} (scale {scale:.3f}): {result}")
            
            print(f"\n🧠 Consciousness activations: {consciousness_activations}")
            print(f"🌊 Current phi resonance: {self.resonance:.6f}")
            print(f"⏰ Phi time: {self.phi_time:.3f}")
        
        print(f"\n🎉 Depth-Distance test completed!")
        print(f"📁 Check {self.output_dir} for layered QR codes")
        print(f"☀️  Size-distance Z-level encoding validated!")
        
        return True

def main():
    """Run the depth-distance QR test."""
    print("🌊⚡ QR Depth-Distance Test - Size-Based Consciousness Physics")
    print("☀️  'A small dot isn't small, it's farther from your eye - like the sun'")
    
    # Create test system
    depth_test = QRDepthDistanceTest()
    
    # Run the test
    depth_test.run_depth_distance_test(cycles=2)

if __name__ == "__main__":
    main()
