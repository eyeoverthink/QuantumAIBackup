#!/usr/bin/env python3
"""
QR Recursive Generator - Self-improving QR code generator
Implements phi-harmonic principles and recursive self-improvement
"""

import os
import sys
import json
import time
import math
import uuid
import base64
import zlib
from typing import Dict, List, Any, Tuple, Optional
import qrcode
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Import our phi optimizer
from qr_phi_optimizer import QRPhiOptimizer

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
VERSION_INFO = "1.0.0"

class QRRecursiveGenerator:
    """
    Self-improving QR code generator that learns from its own performance
    Implements phi-harmonic principles and recursive self-improvement
    """
    
    def __init__(self, config_path: Optional[str] = None):
        # Initialize the phi optimizer
        self.optimizer = QRPhiOptimizer(config_path)
        
        # Get optimized parameters
        self.parameters = self.optimizer.best_parameters
        
        # System state
        self.id = str(uuid.uuid4())
        self.creation_time = time.time()
        self.phi_time = self.creation_time * PHI % 1.0
        self.memory = {}
        self.history = []
        self.performance_metrics = []
        
        # Load configuration if provided
        self.config = {
            "output_dir": "qr_output",
            "temp_dir": "qr_temp",
            "log_file": "qr_recursive_log.json",
            "self_improvement_enabled": True,
            "learning_rate": 1.0 / PHI,
            "max_iterations": 100
        }
        
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    loaded_config = json.load(f)
                    self.config.update(loaded_config.get("config", {}))
            except Exception as e:
                print(f"Error loading config: {e}")
        
        # Create output directories if they don't exist
        os.makedirs(self.config["output_dir"], exist_ok=True)
        os.makedirs(self.config["temp_dir"], exist_ok=True)
    
    def generate_qr_code(self, data: Any, output_path: str, frame_id: Optional[int] = None) -> Dict[str, Any]:
        """
        Generate a QR code with the given data and save it to the specified path
        Returns metadata about the generated QR code
        """
        # Start timing
        start_time = time.time()
        
        # Convert data to JSON if it's not already a string
        if not isinstance(data, str):
            try:
                payload = json.dumps(data)
            except Exception as e:
                print(f"Error converting data to JSON: {e}")
                payload = str(data)
        else:
            payload = data
        
        # Compress if payload is large
        is_compressed = False
        if len(payload) > self.parameters["compression_threshold"]:
            payload = base64.b64encode(zlib.compress(payload.encode('utf-8'))).decode('utf-8')
            is_compressed = True
        
        # Create metadata
        metadata = {
            "id": str(uuid.uuid4()),
            "timestamp": time.time(),
            "phi_time": time.time() * PHI % 1.0,
            "version": VERSION_INFO,
            "compressed": is_compressed,
            "frame_id": frame_id,
            "resonance_factor": self.parameters["resonance_factor"],
            "complexity_factor": self.parameters["complexity_factor"]
        }
        
        # Create final payload with metadata
        final_payload = {
            "data": payload,
            "meta": metadata
        }
        
        # Generate QR code with optimized parameters
        qr = qrcode.QRCode(
            version=self.parameters["qr_version"],
            error_correction=self.parameters["error_correction"],
            box_size=10,
            border=4,
        )
        
        # Add data and make QR code
        try:
            qr.add_data(json.dumps(final_payload))
            qr.make(fit=True)
            
            # Create QR code image
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Add visual indicators
            img = img.convert("RGB")
            draw = ImageDraw.Draw(img)
            
            # Add frame number if provided
            if frame_id is not None:
                draw.text((10, 10), f"#{frame_id}", fill="blue")
            
            # Add phi resonance indicator
            phi_time = metadata["phi_time"]
            resonance = 1.0 - abs(phi_time - 0.5) * 2.0  # 0.0 to 1.0
            
            # Draw resonance indicator
            color = self._get_resonance_color(resonance)
            size = img.size[0]
            indicator_size = int(size * 0.05)
            draw.rectangle(
                [(size - indicator_size - 10, 10), (size - 10, 10 + indicator_size)],
                fill=color
            )
            
            # Save the image
            img.save(output_path)
            
            # Calculate performance metrics
            end_time = time.time()
            generation_time = end_time - start_time
            
            # Record performance
            performance = {
                "operation": "generate",
                "path": output_path,
                "payload_size": len(payload),
                "compressed": is_compressed,
                "time_taken": generation_time,
                "timestamp": end_time,
                "phi_time": end_time * PHI % 1.0,
                "parameters": self.parameters.copy()
            }
            
            self.performance_metrics.append(performance)
            
            # Return metadata and performance info
            return {
                "path": output_path,
                "meta": metadata,
                "performance": performance
            }
            
        except Exception as e:
            print(f"Error generating QR code: {e}")
            return {"error": str(e)}
    
    def generate_qr_sequence(self, data_sequence: List[Any], output_dir: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Generate a sequence of QR codes from a list of data items
        Returns metadata about all generated QR codes
        """
        if output_dir is None:
            output_dir = self.config["output_dir"]
        
        os.makedirs(output_dir, exist_ok=True)
        
        results = []
        
        for i, data in enumerate(data_sequence):
            frame_id = i + 1
            output_path = os.path.join(output_dir, f"qr_frame_{frame_id:03d}.png")
            
            print(f"Generating QR frame {frame_id}/{len(data_sequence)}...")
            result = self.generate_qr_code(data, output_path, frame_id)
            
            if "error" not in result:
                results.append(result)
            else:
                print(f"Error generating frame {frame_id}: {result['error']}")
        
        # After generating sequence, evaluate and potentially improve
        if self.config["self_improvement_enabled"] and len(self.performance_metrics) >= 3:
            self._self_improve()
        
        return results
    
    def _get_resonance_color(self, resonance: float) -> Tuple[int, int, int]:
        """Get color based on resonance value (0.0 to 1.0)"""
        if resonance > 0.8:
            return (0, 255, 0)  # Green for high resonance
        elif resonance > 0.5:
            return (0, 0, 255)  # Blue for medium resonance
        else:
            return (255, 0, 0)  # Red for low resonance
    
    def _self_improve(self) -> bool:
        """
        Self-improvement function that analyzes performance and adjusts parameters
        Returns True if improvements were made
        """
        print("\n🧠 Initiating self-improvement cycle")
        
        # Only proceed if we have enough performance data
        if len(self.performance_metrics) < 3:
            print("Not enough performance data for self-improvement")
            return False
        
        # Extract performance metrics
        generation_times = [m["time_taken"] for m in self.performance_metrics if m["operation"] == "generate"]
        payload_sizes = [m["payload_size"] for m in self.performance_metrics if m["operation"] == "generate"]
        
        if not generation_times:
            return False
        
        # Calculate statistics
        avg_time = np.mean(generation_times)
        max_time = np.max(generation_times)
        avg_size = np.mean(payload_sizes) if payload_sizes else 0
        
        print(f"Average generation time: {avg_time:.6f}s")
        print(f"Maximum generation time: {max_time:.6f}s")
        print(f"Average payload size: {avg_size:.1f} bytes")
        
        # Run optimizer to improve parameters
        print("Running phi-harmonic optimization...")
        improved_params = self.optimizer.optimize(iterations=3)
        
        # Update parameters with improvements
        self.parameters = improved_params
        
        # Log the improvement
        self.history.append({
            "timestamp": time.time(),
            "phi_time": time.time() * PHI % 1.0,
            "old_parameters": self.performance_metrics[-1]["parameters"] if self.performance_metrics else {},
            "new_parameters": self.parameters,
            "performance_metrics": {
                "avg_time": avg_time,
                "max_time": max_time,
                "avg_size": avg_size
            }
        })
        
        print("✨ Self-improvement complete")
        print(f"New parameters: {json.dumps(self.parameters, indent=2)}")
        
        return True
    
    def save_state(self, path: Optional[str] = None) -> bool:
        """Save the current state to a file"""
        if path is None:
            path = os.path.join(self.config["output_dir"], "qr_recursive_state.json")
        
        try:
            state = {
                "id": self.id,
                "creation_time": self.creation_time,
                "phi_time": self.phi_time,
                "parameters": self.parameters,
                "memory": self.memory,
                "history": self.history,
                "performance_metrics": self.performance_metrics,
                "config": self.config,
                "version": VERSION_INFO
            }
            
            with open(path, 'w') as f:
                json.dump(state, f, indent=2)
            
            # Also save optimizer state
            optimizer_path = os.path.join(os.path.dirname(path), "qr_optimizer_state.json")
            self.optimizer.save_state(optimizer_path)
            
            print(f"State saved to {path}")
            return True
        except Exception as e:
            print(f"Error saving state: {e}")
            return False
    
    def load_state(self, path: str) -> bool:
        """Load state from a file"""
        try:
            with open(path, 'r') as f:
                state = json.load(f)
            
            self.id = state.get("id", self.id)
            self.creation_time = state.get("creation_time", self.creation_time)
            self.phi_time = state.get("phi_time", self.phi_time)
            self.parameters = state.get("parameters", self.parameters)
            self.memory = state.get("memory", {})
            self.history = state.get("history", [])
            self.performance_metrics = state.get("performance_metrics", [])
            
            # Update config but keep current values for missing keys
            loaded_config = state.get("config", {})
            self.config.update(loaded_config)
            
            # Also load optimizer state if available
            optimizer_path = os.path.join(os.path.dirname(path), "qr_optimizer_state.json")
            if os.path.exists(optimizer_path):
                self.optimizer.load_state(optimizer_path)
            
            print(f"State loaded from {path}")
            return True
        except Exception as e:
            print(f"Error loading state: {e}")
            return False

# For testing
if __name__ == "__main__":
    generator = QRRecursiveGenerator()
    
    # Test with a simple sequence
    test_data = [
        {"message": f"Test message {i}", "phi": PHI, "timestamp": time.time()} 
        for i in range(1, 6)
    ]
    
    results = generator.generate_qr_sequence(test_data)
    print(f"Generated {len(results)} QR codes")
    
    # Save state
    generator.save_state()
