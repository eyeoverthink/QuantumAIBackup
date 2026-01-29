#!/usr/bin/env python3
"""
Face QR Evolution Extension

This module extends the Face-QR system with phi-harmonic evolutionary capabilities,
enabling the system to self-improve over time based on golden ratio principles.
"""

import os
import sys
import json
import time
import uuid
import numpy as np
import matplotlib.pyplot as plt
import base64
import zlib
from datetime import datetime
from PIL import Image

# Import JSON helper if available
try:
    from face_qr_json_helper import json_dump, json_dumps
    print("Using Face QR JSON Helper for serialization")
    USE_JSON_HELPER = True
except ImportError:
    print("Face QR JSON Helper not found, using standard JSON")
    USE_JSON_HELPER = False

# Ensure the current directory is in the path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import face_qr modules
try:
    from face_qr_core import FaceQRCore
    from face_qr_camera_extension import FaceQRCameraExtension
except ImportError:
    print("Error: Required Face-QR modules not found.")
    print("Please ensure you're running from the correct directory.")
    sys.exit(1)

# Phi (Golden Ratio) constant
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class FaceQREvolutionExtension(FaceQRCore):
    """Extends the Face-QR system with evolutionary capabilities."""
    
    def __init__(self, config_path=None):
        """
        Initialize the evolution extension.
        
        Args:
            config_path: Path to configuration file
        """
        super().__init__(config_path)
        
        # Evolution parameters
        self.generation = 1
        self.complexity = 1.0
        self.resonance = 0.5
        self.mutation_rate = 0.1
        self.phi_time = (time.time() * PHI) % 1.0
        
        # Authentication parameters that will evolve
        self.similarity_threshold = self.config.get('similarity_threshold', 0.45)
        self.feature_weight = self.config.get('feature_weight', 0.5)
        self.temporal_factor = self.config.get('temporal_factor', 0.2)
        
        # Create evolution directory
        self.evolution_dir = os.path.join(self.base_dir, "evolution_data")
        os.makedirs(self.evolution_dir, exist_ok=True)
        
        # Load epigenetic memory
        self.epigenetic_memory = self._load_epigenetic_memory()
        
        # Initialize camera extension for authentication
        self.camera_ext = FaceQRCameraExtension(config_path)
        
        print("Face QR Evolution Extension loaded")
    
    def _load_epigenetic_memory(self):
        """Load epigenetic memory from file if available."""
        memory_path = os.path.join(self.evolution_dir, "face_qr_epigenetic_memory.json")
        if os.path.exists(memory_path):
            try:
                with open(memory_path, 'r') as f:
                    memory = json.load(f)
                    print(f"Loaded epigenetic memory: Generation {memory.get('generation', 1)}")
                    
                    # Update current parameters from memory
                    self.generation = memory.get('generation', 1)
                    self.complexity = memory.get('complexity', 1.0)
                    self.resonance = memory.get('resonance', 0.5)
                    self.mutation_rate = memory.get('mutation_rate', 0.1)
                    self.similarity_threshold = memory.get('similarity_threshold', 0.45)
                    self.feature_weight = memory.get('feature_weight', 0.5)
                    self.temporal_factor = memory.get('temporal_factor', 0.2)
                    
                    return memory
            except Exception as e:
                print(f"Error loading epigenetic memory: {e}")
        
        # Default memory if none exists
        return {
            "generation": 1,
            "complexity": 1.0,
            "resonance": 0.5,
            "mutation_rate": 0.1,
            "similarity_threshold": 0.45,
            "feature_weight": 0.5,
            "temporal_factor": 0.2,
            "evolution_history": [],
            "authentication_history": [],
            "phi_harmonic_states": []
        }
    
    def _save_epigenetic_memory(self):
        """Save epigenetic memory to file."""
        # Update memory with current parameters
        self.epigenetic_memory["generation"] = self.generation
        self.epigenetic_memory["complexity"] = float(self.complexity)
        self.epigenetic_memory["resonance"] = float(self.resonance)
        self.epigenetic_memory["mutation_rate"] = float(self.mutation_rate)
        self.epigenetic_memory["similarity_threshold"] = float(self.similarity_threshold)
        self.epigenetic_memory["feature_weight"] = float(self.feature_weight)
        self.epigenetic_memory["temporal_factor"] = float(self.temporal_factor)
        
        # Ensure all values in the authentication history are JSON serializable
        if "authentication_history" in self.epigenetic_memory:
            for entry in self.epigenetic_memory["authentication_history"]:
                for key, value in list(entry.items()):
                    if hasattr(value, 'item') and callable(getattr(value, 'item')):
                        # Handle any numpy numeric type with item() method
                        entry[key] = value.item()
                    elif isinstance(value, bool):
                        # Explicitly convert Python bool to ensure it's serializable
                        entry[key] = bool(value)
        
        # Ensure all values in the evolution history are JSON serializable
        if "evolution_history" in self.epigenetic_memory:
            for entry in self.epigenetic_memory["evolution_history"]:
                for key, value in list(entry.items()):
                    if hasattr(value, 'item') and callable(getattr(value, 'item')):
                        # Handle any numpy numeric type with item() method
                        entry[key] = value.item()
        
        # Save to file
        memory_path = os.path.join(self.evolution_dir, "face_qr_epigenetic_memory.json")
        with open(memory_path, 'w') as f:
            if USE_JSON_HELPER:
                json_dump(self.epigenetic_memory, f, indent=2)
            else:
                # Use a custom default handler for non-serializable types
                def default_handler(obj):
                    if hasattr(obj, 'item') and callable(getattr(obj, 'item')):
                        return obj.item()
                    if isinstance(obj, np.ndarray):
                        return obj.tolist()
                    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
                
                json.dump(self.epigenetic_memory, f, indent=2, default=default_handler)
                
        print(f"Saved epigenetic memory to {memory_path}")
    
    def evolve(self, authentication_success=None, similarity_score=None):
        """
        Evolve the system's parameters based on phi-harmonic principles and authentication results.
        
        Args:
            authentication_success: Whether the last authentication was successful
            similarity_score: Similarity score from the last authentication attempt
        """
        # Update generation
        self.generation += 1
        
        # Calculate new phi-time
        current_phi_time = (time.time() * PHI) % 1.0
        
        # Record authentication result if provided
        if authentication_success is not None and similarity_score is not None:
            auth_entry = {
                "timestamp": time.time(),
                "phi_time": current_phi_time,
                "success": authentication_success,
                "similarity": similarity_score,
                "threshold": self.similarity_threshold
            }
            
            if "authentication_history" not in self.epigenetic_memory:
                self.epigenetic_memory["authentication_history"] = []
            
            self.epigenetic_memory["authentication_history"].append(auth_entry)
            
            # Adjust evolution based on authentication results
            if len(self.epigenetic_memory["authentication_history"]) >= 3:
                recent_auths = self.epigenetic_memory["authentication_history"][-3:]
                success_rate = sum(1 for a in recent_auths if a["success"]) / len(recent_auths)
                
                # If success rate is too high, make authentication stricter
                if success_rate > 0.8:
                    self.similarity_threshold = min(0.8, self.similarity_threshold + 0.02)
                # If success rate is too low, make authentication more lenient
                elif success_rate < 0.3:
                    self.similarity_threshold = max(0.3, self.similarity_threshold - 0.02)
        
        # Evolve complexity based on phi-harmonic principles
        phi_factor = abs(current_phi_time - self.phi_time)
        complexity_change = (PHI * phi_factor - 0.5) * self.mutation_rate
        self.complexity = max(0.5, min(5.0, self.complexity + complexity_change))
        
        # Evolve resonance
        resonance_change = (PHI * current_phi_time - 0.5) * self.mutation_rate
        self.resonance = max(0.1, min(1.0, self.resonance + resonance_change))
        
        # Evolve mutation rate (tends to decrease over time for stability)
        mutation_change = -0.01 * (1 / PHI) * self.mutation_rate
        self.mutation_rate = max(0.01, min(0.2, self.mutation_rate + mutation_change))
        
        # Evolve feature weight
        feature_weight_change = (PHI * phi_factor - 0.5) * self.mutation_rate * 0.5
        self.feature_weight = max(0.2, min(0.8, self.feature_weight + feature_weight_change))
        
        # Evolve temporal factor
        temporal_factor_change = (PHI * current_phi_time - 0.5) * self.mutation_rate * 0.2
        self.temporal_factor = max(0.05, min(0.4, self.temporal_factor + temporal_factor_change))
        
        # Update phi-time
        self.phi_time = current_phi_time
        
        # Add to evolution history
        evolution_entry = {
            "generation": self.generation,
            "timestamp": time.time(),
            "phi_time": self.phi_time,
            "complexity": self.complexity,
            "resonance": self.resonance,
            "mutation_rate": self.mutation_rate,
            "similarity_threshold": self.similarity_threshold,
            "feature_weight": self.feature_weight,
            "temporal_factor": self.temporal_factor
        }
        
        if "evolution_history" not in self.epigenetic_memory:
            self.epigenetic_memory["evolution_history"] = []
        
        self.epigenetic_memory["evolution_history"].append(evolution_entry)
        
        # Save updated memory
        self._save_epigenetic_memory()
        
        # Apply evolved parameters to camera extension
        self.camera_ext.similarity_threshold = self.similarity_threshold
        
        print(f"Evolved to Generation {self.generation}:")
        print(f"  Complexity: {self.complexity:.4f}")
        print(f"  Resonance: {self.resonance:.4f}")
        print(f"  Mutation Rate: {self.mutation_rate:.4f}")
        print(f"  Similarity Threshold: {self.similarity_threshold:.4f}")
        print(f"  Feature Weight: {self.feature_weight:.4f}")
        print(f"  Temporal Factor: {self.temporal_factor:.4f}")
        print(f"  Phi-Time: {self.phi_time:.4f}")
    
    def compress_payload(self, payload):
        """Compress the payload using zlib at maximum compression level and base64 encode it."""
        # Use maximum compression level (9)
        compressed = zlib.compress(payload.encode('utf-8'), level=9)
        return base64.b64encode(compressed).decode('ascii')
    
    def generate_evolved_qr(self, face_image_path):
        """
        Generate an evolved QR code containing both face data and evolution parameters.
        
        Args:
            face_image_path: Path to the face image
            
        Returns:
            Tuple: (qr_image, output_path)
        """
        # First, generate a standard face QR code
        from generate_face_qr import encode_face_to_qr
        
        # Calculate size based on complexity
        size_px = max(16, min(32, int(24 * self.complexity / 2.5)))
        
        # Calculate JPEG quality based on resonance
        jpeg_quality = max(30, min(70, int(50 * self.resonance)))
        
        # Generate the basic face QR code
        temp_qr_path = os.path.join(self.evolution_dir, f"temp_face_qr_{self.generation}.png")
        encode_face_to_qr(
            image_path=face_image_path,
            output_path=temp_qr_path,
            size_px=size_px,
            jpeg_quality=jpeg_quality
        )
        
        # Load the QR code and extract its payload
        from qr_task_worker_extension import QRTaskWorkerExtension
        worker = QRTaskWorkerExtension()
        qr_data = worker.decode_qr_from_file(temp_qr_path)
        
        if not qr_data:
            print("Error: Failed to decode temporary QR code")
            return None, None
        
        # Enhance the payload with evolution data
        try:
            payload = json.loads(qr_data)
            
            # Add evolution parameters
            payload["evolution"] = {
                "generation": self.generation,
                "phi_time": round(self.phi_time, 4),
                "complexity": round(self.complexity, 4),
                "resonance": round(self.resonance, 4),
                "mutation_rate": round(self.mutation_rate, 4),
                "similarity_threshold": round(self.similarity_threshold, 4),
                "feature_weight": round(self.feature_weight, 4),
                "temporal_factor": round(self.temporal_factor, 4)
            }
            
            # Add self-evolution script
            payload["evolution_script"] = "from face_qr_evolution_extension import FaceQREvolutionExtension; ext = FaceQREvolutionExtension(); ext.evolve(); ext.authenticate_with_evolution();"
            
            # Convert back to JSON and compress
            json_payload = json.dumps(payload)
            compressed_payload = self.compress_payload(json_payload)
            
            # Generate QR code with optimized settings
            import qrcode
            qr = qrcode.QRCode(
                version=None,  # Auto-determine version
                error_correction=qrcode.constants.ERROR_CORRECT_L,  # Use low error correction to maximize data capacity
                box_size=10,
                border=4,
            )
            qr.add_data(compressed_payload)
            qr.make(fit=True)
            
            # Create QR image
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Save the evolved QR code
            output_path = os.path.join(self.evolution_dir, f"evolved_face_qr_gen_{self.generation}.png")
            img.save(output_path)
            print(f"Generated evolved Face-QR code: {output_path}")
            
            # Clean up temporary file
            if os.path.exists(temp_qr_path):
                os.remove(temp_qr_path)
            
            return img, output_path
            
        except Exception as e:
            print(f"Error enhancing QR payload: {e}")
            return None, None
    
    def authenticate_with_evolution(self, qr_code_path=None, face_image_path=None):
        """
        Perform authentication with evolutionary capabilities.
        
        Args:
            qr_code_path: Path to QR code (optional)
            face_image_path: Path to face image for creating new evolved QR (optional)
            
        Returns:
            bool: Authentication success
        """
        if not qr_code_path and not face_image_path:
            print("Error: Either QR code path or face image path must be provided")
            return False
        
        # If we have a face image but no QR code, generate an evolved QR first
        if face_image_path and not qr_code_path:
            _, qr_code_path = self.generate_evolved_qr(face_image_path)
            if not qr_code_path:
                print("Error: Failed to generate evolved QR code")
                return False
        
        # Perform authentication with camera
        print(f"Authenticating with evolved parameters (Generation {self.generation}):")
        print(f"  Similarity Threshold: {self.similarity_threshold:.4f}")
        
        # Apply evolved parameters to camera extension
        self.camera_ext.similarity_threshold = self.similarity_threshold
        
        # Run authentication
        success = self.camera_ext.authenticate_with_camera(qr_code_path)
        
        # Get the similarity score from the last authentication
        similarity_score = None
        if hasattr(self.camera_ext, 'last_similarity_score'):
            similarity_score = self.camera_ext.last_similarity_score
        else:
            # Estimate a score based on success
            similarity_score = self.similarity_threshold + (0.1 if success else -0.1)
        
        # Evolve based on authentication result
        self.evolve(authentication_success=success, similarity_score=similarity_score)
        
        # If authentication was successful, generate a new evolved QR for next time
        if success and face_image_path:
            print("Authentication successful! Generating new evolved QR for next generation...")
            self.generate_evolved_qr(face_image_path)
        
        return success
    
    def visualize_evolution(self):
        """Visualize the evolution history."""
        if "evolution_history" not in self.epigenetic_memory or not self.epigenetic_memory["evolution_history"]:
            print("No evolution history available.")
            return
        
        history = self.epigenetic_memory["evolution_history"]
        generations = [entry["generation"] for entry in history]
        complexities = [entry["complexity"] for entry in history]
        resonances = [entry["resonance"] for entry in history]
        mutation_rates = [entry["mutation_rate"] for entry in history]
        similarity_thresholds = [entry.get("similarity_threshold", 0.45) for entry in history]
        
        plt.figure(figsize=(12, 10))
        
        # Plot complexity
        plt.subplot(4, 1, 1)
        plt.plot(generations, complexities, 'b-o', label="Complexity")
        plt.title("Evolution of Complexity")
        plt.xlabel("Generation")
        plt.ylabel("Complexity")
        plt.grid(True, alpha=0.3)
        
        # Plot resonance
        plt.subplot(4, 1, 2)
        plt.plot(generations, resonances, 'g-o', label="Resonance")
        plt.title("Evolution of Resonance")
        plt.xlabel("Generation")
        plt.ylabel("Resonance")
        plt.grid(True, alpha=0.3)
        
        # Plot mutation rate
        plt.subplot(4, 1, 3)
        plt.plot(generations, mutation_rates, 'r-o', label="Mutation Rate")
        plt.title("Evolution of Mutation Rate")
        plt.xlabel("Generation")
        plt.ylabel("Mutation Rate")
        plt.grid(True, alpha=0.3)
        
        # Plot similarity threshold
        plt.subplot(4, 1, 4)
        plt.plot(generations, similarity_thresholds, 'm-o', label="Similarity Threshold")
        plt.title("Evolution of Similarity Threshold")
        plt.xlabel("Generation")
        plt.ylabel("Threshold")
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save the visualization
        vis_path = os.path.join(self.evolution_dir, f"evolution_visualization_gen_{self.generation}.png")
        plt.savefig(vis_path)
        print(f"Saved evolution visualization to {vis_path}")
        
        # Show the plot
        plt.show()
    
    def visualize_authentication_history(self):
        """Visualize the authentication history."""
        if "authentication_history" not in self.epigenetic_memory or not self.epigenetic_memory["authentication_history"]:
            print("No authentication history available.")
            return
        
        history = self.epigenetic_memory["authentication_history"]
        timestamps = [entry["timestamp"] for entry in history]
        dates = [datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') for ts in timestamps]
        similarities = [entry["similarity"] for entry in history]
        thresholds = [entry["threshold"] for entry in history]
        successes = [1 if entry["success"] else 0 for entry in history]
        
        plt.figure(figsize=(12, 8))
        
        # Plot similarities and thresholds
        plt.subplot(2, 1, 1)
        plt.plot(range(len(history)), similarities, 'b-o', label="Similarity Score")
        plt.plot(range(len(history)), thresholds, 'r--', label="Threshold")
        plt.title("Authentication Similarity Scores")
        plt.xlabel("Authentication Attempt")
        plt.ylabel("Score")
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Plot success/failure
        plt.subplot(2, 1, 2)
        plt.bar(range(len(history)), successes, color=['green' if s else 'red' for s in successes])
        plt.title("Authentication Results")
        plt.xlabel("Authentication Attempt")
        plt.ylabel("Success (1) / Failure (0)")
        plt.yticks([0, 1])
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
        # Save the visualization
        vis_path = os.path.join(self.evolution_dir, f"authentication_visualization_gen_{self.generation}.png")
        plt.savefig(vis_path)
        print(f"Saved authentication visualization to {vis_path}")

def patch_camera_extension():
    """Patch the FaceQRCameraExtension to track similarity scores and enhance with evolution capabilities."""
    try:
        from face_qr_camera_extension import FaceQRCameraExtension
        
        # Store the original authenticate_face_with_qr method
        original_authenticate = FaceQRCameraExtension.authenticate_face_with_qr
        
        # Define the patched method
        def patched_authenticate_face_with_qr(self, face_frame, qr_data):
            success, similarity = original_authenticate(self, face_frame, qr_data)
            # Store the similarity score for evolution
            self.last_similarity_score = similarity
            return success, similarity
        
        # Store the original authenticate_with_camera method
        original_authenticate_with_camera = FaceQRCameraExtension.authenticate_with_camera
        
        # Define the patched authenticate_with_camera method
        def patched_authenticate_with_camera(self, qr_code_path=None):
            # Call the original method
            success = original_authenticate_with_camera(self, qr_code_path)
            
            # Extract evolution data from QR code if available
            if qr_code_path and os.path.exists(qr_code_path):
                try:
                    # Import QR task worker to decode QR
                    from qr_task_worker_extension import QRTaskWorkerExtension
                    worker = QRTaskWorkerExtension()
                    qr_data_str = worker.decode_qr_from_file(qr_code_path)
                    
                    if qr_data_str:
                        # Try to decompress if it's compressed
                        try:
                            import base64
                            import zlib
                            decompressed = zlib.decompress(base64.b64decode(qr_data_str))
                            qr_data_str = decompressed.decode('utf-8')
                        except:
                            # Not compressed or decompression failed
                            pass
                        
                        # Parse JSON data
                        import json
                        qr_data = json.loads(qr_data_str)
                        
                        # Check for evolution data
                        if 'evolution' in qr_data:
                            print("Found evolution data in QR code:")
                            print(json.dumps(qr_data['evolution'], indent=2))
                except Exception as e:
                    print(f"Error extracting evolution data: {e}")
            
            return success
        
        # Apply the patches
        FaceQRCameraExtension.authenticate_face_with_qr = patched_authenticate_face_with_qr
        FaceQRCameraExtension.authenticate_with_camera = patched_authenticate_with_camera
        
        # Add last_similarity_score attribute if it doesn't exist
        if not hasattr(FaceQRCameraExtension, 'last_similarity_score'):
            FaceQRCameraExtension.last_similarity_score = 0.0
        
        print("Patched FaceQRCameraExtension with evolution capabilities")
        
    except ImportError:
        print("Warning: Could not patch FaceQRCameraExtension (module not found)")

def main():
    """Main function for testing the Face QR Evolution Extension."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Face-QR Evolution Extension")
    parser.add_argument("--qr", help="Path to QR code image")
    parser.add_argument("--face", help="Path to face image for creating new evolved QR")
    parser.add_argument("--visualize", action="store_true", help="Visualize evolution history")
    parser.add_argument("--auth-history", action="store_true", help="Visualize authentication history")
    args = parser.parse_args()
    
    # Apply patches
    patch_camera_extension()
    
    # Create evolution extension
    evolution_ext = FaceQREvolutionExtension()
    
    # Visualize evolution history if requested
    if args.visualize:
        evolution_ext.visualize_evolution()
        return 0
    
    # Visualize authentication history if requested
    if args.auth_history:
        evolution_ext.visualize_authentication_history()
        return 0
    
    # Authenticate with evolution
    if args.qr or args.face:
        success = evolution_ext.authenticate_with_evolution(args.qr, args.face)
        return 0 if success else 1
    else:
        print("Error: Either --qr or --face must be provided")
        return 1

if __name__ == "__main__":
    sys.exit(main())
