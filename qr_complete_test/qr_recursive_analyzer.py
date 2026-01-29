#!/usr/bin/env python3
"""
QR Recursive Analyzer - Self-improving QR code analyzer
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
import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode as pyzbar_decode

# Import our phi optimizer
from qr_phi_optimizer import QRPhiOptimizer

# Constants
PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
VERSION_INFO = "1.0.0"

class QRRecursiveAnalyzer:
    """
    Self-improving QR code analyzer that learns from its own performance
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
        self.decode_success_rate = 1.0
        
        # Load configuration if provided
        self.config = {
            "output_dir": "qr_analysis",
            "report_dir": "qr_reports",
            "log_file": "qr_analyzer_log.json",
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
        os.makedirs(self.config["report_dir"], exist_ok=True)
    
    def decode_qr_code(self, image_path: str) -> Dict[str, Any]:
        """
        Decode a QR code from the given image path
        Returns the decoded data and metadata
        """
        # Start timing
        start_time = time.time()
        
        try:
            # Load the image
            print(f"Decoding QR image: {image_path}")
            image = Image.open(image_path)
            
            # Decode QR code
            decoded_objects = pyzbar_decode(image)
            if not decoded_objects:
                error_msg = f"No QR code found in {image_path}"
                print(f"⚠️ {error_msg}")
                
                # Record failure
                self._record_performance("decode", image_path, False, start_time, error=error_msg)
                
                return {"error": error_msg}
            
            # Get the data from the first QR code
            qr_data = decoded_objects[0].data.decode('utf-8')
            
            # Parse JSON
            payload = json.loads(qr_data)
            
            # Extract metadata and data
            metadata = payload.get("meta", {})
            data = payload.get("data", "")
            
            # Decompress if necessary
            if metadata.get("compressed", False):
                print("Detected compressed payload, decompressing...")
                try:
                    data = zlib.decompress(base64.b64decode(data)).decode('utf-8')
                except Exception as e:
                    print(f"Error decompressing data: {e}")
                    # Record partial failure
                    self._record_performance("decode", image_path, False, start_time, error=f"Decompression error: {e}")
                    return {"error": f"Decompression error: {e}"}
            
            # Try to parse data as JSON if possible
            try:
                parsed_data = json.loads(data)
                
                # Record successful decode
                self._record_performance("decode", image_path, True, start_time)
                
                print("Successfully decoded QR code")
                
                return {
                    "data": parsed_data,
                    "meta": metadata,
                    "raw": qr_data,
                    "image_path": image_path
                }
            except:
                # Return as string if not valid JSON
                # Record successful decode (even though not JSON)
                self._record_performance("decode", image_path, True, start_time)
                
                print("Successfully decoded QR code (non-JSON data)")
                
                return {
                    "data": data,
                    "meta": metadata,
                    "raw": qr_data,
                    "image_path": image_path
                }
                
        except Exception as e:
            error_msg = f"Error decoding QR code: {e}"
            print(f"⚠️ {error_msg}")
            
            # Record failure
            self._record_performance("decode", image_path, False, start_time, error=error_msg)
            
            return {"error": error_msg}
    
    def analyze_qr_sequence(self, directory: str) -> Dict[str, Any]:
        """
        Analyze a sequence of QR codes in a directory
        Returns a comprehensive analysis report
        """
        print(f"\n📊 Analyzing QR sequence in {directory}")
        start_time = time.time()
        
        # Find all QR code files in the directory
        qr_files = []
        for file in os.listdir(directory):
            if file.lower().endswith(('.png', '.jpg', '.jpeg')) and 'qr' in file.lower():
                qr_files.append(os.path.join(directory, file))
        
        qr_files.sort()  # Sort files to ensure correct sequence
        
        if not qr_files:
            print("No QR code files found in directory")
            return {"error": "No QR code files found"}
        
        print(f"Found {len(qr_files)} QR code files")
        
        # Decode all QR codes
        decoded_data = []
        success_count = 0
        
        for file in qr_files:
            result = self.decode_qr_code(file)
            
            if "error" not in result:
                success_count += 1
                decoded_data.append(result)
            else:
                # Add error record
                decoded_data.append({
                    "image_path": file,
                    "error": result["error"]
                })
        
        # Calculate success rate
        success_rate = success_count / len(qr_files) if qr_files else 0
        self.decode_success_rate = success_rate
        
        # Generate analysis report
        end_time = time.time()
        analysis_time = end_time - start_time
        
        report = {
            "timestamp": end_time,
            "phi_time": end_time * PHI % 1.0,
            "directory": directory,
            "total_files": len(qr_files),
            "success_count": success_count,
            "success_rate": success_rate,
            "analysis_time": analysis_time,
            "decoded_data": decoded_data,
            "parameters": self.parameters.copy()
        }
        
        # Save report
        report_path = os.path.join(self.config["report_dir"], f"analysis_report_{int(time.time())}.json")
        try:
            with open(report_path, 'w') as f:
                # Save a simplified version without the full decoded data
                simplified_report = report.copy()
                simplified_report["decoded_data"] = [
                    {
                        "image_path": d.get("image_path", "unknown"),
                        "has_error": "error" in d,
                        "meta": d.get("meta", {}) if "error" not in d else {}
                    }
                    for d in decoded_data
                ]
                json.dump(simplified_report, f, indent=2)
            
            print(f"Saved analysis report to {report_path}")
        except Exception as e:
            print(f"Error saving report: {e}")
        
        # Self-improve if enabled
        if self.config["self_improvement_enabled"] and len(self.performance_metrics) >= 3:
            self._self_improve()
        
        print(f"Decoded {success_count}/{len(qr_files)} QR code files from {directory}")
        print(f"Analysis time: {analysis_time:.2f} seconds")
        
        return report
    
    def _record_performance(self, operation: str, path: str, success: bool, 
                           start_time: float, error: Optional[str] = None) -> None:
        """Record performance metrics for an operation"""
        end_time = time.time()
        operation_time = end_time - start_time
        
        metric = {
            "operation": operation,
            "path": path,
            "success": success,
            "time_taken": operation_time,
            "timestamp": end_time,
            "phi_time": end_time * PHI % 1.0,
            "parameters": self.parameters.copy()
        }
        
        if error:
            metric["error"] = error
        
        self.performance_metrics.append(metric)
    
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
        
        # Extract performance metrics for successful operations
        decode_times = [m["time_taken"] for m in self.performance_metrics 
                      if m["operation"] == "decode" and m["success"]]
        
        if not decode_times:
            print("No successful decode operations to analyze")
            return False
        
        # Calculate statistics
        avg_time = np.mean(decode_times)
        max_time = np.max(decode_times)
        
        print(f"Average decode time: {avg_time:.6f}s")
        print(f"Maximum decode time: {max_time:.6f}s")
        print(f"Current success rate: {self.decode_success_rate:.2%}")
        
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
                "success_rate": self.decode_success_rate
            }
        })
        
        print("✨ Self-improvement complete")
        print(f"New parameters: {json.dumps(self.parameters, indent=2)}")
        
        return True
    
    def save_state(self, path: Optional[str] = None) -> bool:
        """Save the current state to a file"""
        if path is None:
            path = os.path.join(self.config["output_dir"], "qr_analyzer_state.json")
        
        try:
            state = {
                "id": self.id,
                "creation_time": self.creation_time,
                "phi_time": self.phi_time,
                "parameters": self.parameters,
                "memory": self.memory,
                "history": self.history,
                "performance_metrics": self.performance_metrics,
                "decode_success_rate": self.decode_success_rate,
                "config": self.config,
                "version": VERSION_INFO
            }
            
            with open(path, 'w') as f:
                json.dump(state, f, indent=2)
            
            # Also save optimizer state
            optimizer_path = os.path.join(os.path.dirname(path), "qr_analyzer_optimizer_state.json")
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
            self.decode_success_rate = state.get("decode_success_rate", 1.0)
            
            # Update config but keep current values for missing keys
            loaded_config = state.get("config", {})
            self.config.update(loaded_config)
            
            # Also load optimizer state if available
            optimizer_path = os.path.join(os.path.dirname(path), "qr_analyzer_optimizer_state.json")
            if os.path.exists(optimizer_path):
                self.optimizer.load_state(optimizer_path)
            
            print(f"State loaded from {path}")
            return True
        except Exception as e:
            print(f"Error loading state: {e}")
            return False

# For testing
if __name__ == "__main__":
    analyzer = QRRecursiveAnalyzer()
    
    # Check if a directory was provided
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        analyzer.analyze_qr_sequence(directory)
    else:
        print("Usage: python qr_recursive_analyzer.py <qr_directory>")
        
    # Save state
    analyzer.save_state()
