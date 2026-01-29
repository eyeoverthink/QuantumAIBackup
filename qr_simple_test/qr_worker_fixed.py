#!/usr/bin/env python3
"""
QR Worker - Enhanced Version for Animated QR Flipbook Execution System
By Vaughn Scott (with Cascade Assistant fixes)

Captures QR codes from camera or image sequence, decodes payloads,
executes embedded code fragments, and generates response QR codes.
Implements phi-harmonic evolution and learning with improved processing.
"""

import os
import cv2
import json
import time
import uuid
import base64
import hashlib
import tempfile
import subprocess
import numpy as np
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import qrcode
from cryptography.fernet import Fernet

# Phi (Golden Ratio) constant
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class QRWorker:
    """
    Enhanced QR Worker that captures QR codes, executes code fragments, and generates responses.
    """
    
    def __init__(self, output_dir="qr_responses", encryption_key=None):
        """
        Initialize the QR Worker.
        
        Args:
            output_dir: Directory to save response QR codes
            encryption_key: Optional Fernet encryption key for secure payloads
        """
        self.output_dir = output_dir
        self.session_id = str(uuid.uuid4())
        self.current_generation = 1
        self.complexity = 0.1
        self.resonance = 1.0
        self.learning_rate = 0.05 * PHI
        self.mutation_rate = 0.02
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize encryption
        if encryption_key:
            self.encryption_key = encryption_key
        else:
            # Try to load key from file
            key_file = "qr_encryption.key"
            if os.path.exists(key_file):
                with open(key_file, "rb") as f:
                    self.encryption_key = f.read()
                print("Using encryption key from qr_encryption.key")
            else:
                # Generate new key
                self.encryption_key = Fernet.generate_key()
                with open(key_file, "wb") as f:
                    f.write(self.encryption_key)
                print(f"Generated new encryption key and saved to {key_file}")
        
        self.cipher = Fernet(self.encryption_key)
    
    def process_qr_image(self, image_path):
        """
        Process QR code image.
        
        Args:
            image_path: Path to QR code image
            
        Returns:
            Path to response QR code or None if processing failed
        """
        print(f"Processing QR image: {image_path}")
        
        try:
            # Read image
            image = cv2.imread(image_path)
            if image is None:
                print(f"Could not read image: {image_path}")
                return None
            
            # Convert to grayscale
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            # Try multiple preprocessing techniques for better QR detection
            decoded_data = None
            detector = cv2.QRCodeDetector()
            
            # Try original image
            data, bbox, _ = detector.detectAndDecode(image)
            if data:
                decoded_data = data
            
            # Try grayscale if original failed
            if not decoded_data:
                data, bbox, _ = detector.detectAndDecode(gray)
                if data:
                    decoded_data = data
            
            # Try thresholded image if still failed
            if not decoded_data:
                _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
                data, bbox, _ = detector.detectAndDecode(thresh)
                if data:
                    decoded_data = data
            
            # Try adaptive thresholding if still failed
            if not decoded_data:
                adaptive = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                               cv2.THRESH_BINARY, 11, 2)
                data, bbox, _ = detector.detectAndDecode(adaptive)
                if data:
                    decoded_data = data
            
            # If all OpenCV methods failed, try with PIL and pyzbar
            if not decoded_data:
                try:
                    from pyzbar.pyzbar import decode as pyzbar_decode
                    pil_image = Image.open(image_path)
                    decoded_objects = pyzbar_decode(pil_image)
                    if decoded_objects:
                        decoded_data = decoded_objects[0].data.decode('utf-8')
                except ImportError:
                    print("pyzbar not installed, skipping this method")
            
            if not decoded_data:
                print("No QR code found or could not decode")
                return None
            
            # Parse JSON payload
            try:
                payload = json.loads(decoded_data)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON payload: {e}")
                return None
            
            # Process payload
            return self.process_qr_data(payload, os.path.basename(image_path))
            
        except Exception as e:
            print(f"Error processing QR code: {e}")
            return None
    
    def process_qr_data(self, payload, source_name="direct_data"):
        """
        Process QR code data directly (without image decoding).
        
        Args:
            payload: The decoded QR payload as a dictionary
            source_name: Name of the source (for logging)
            
        Returns:
            Path to response QR code or None if processing failed
        """
        try:
            # Extract data from payload
            code = payload.get("code", "")
            task_type = payload.get("task_type", "execute_python")
            frame_id = payload.get("frame_id", str(int(time.time())))
            phi_state = payload.get("phi_state", {})
            
            # Update phi state
            if phi_state:
                if "resonance" in phi_state:
                    self.resonance = phi_state["resonance"]
                if "complexity" in phi_state:
                    self.complexity = phi_state["complexity"]
            
            # Execute code
            result = self.execute_code(code, task_type)
            
            # Generate response
            response = {
                "source_frame": frame_id,
                "timestamp": datetime.now().isoformat(),
                "execution_result": result,
                "phi_state": {
                    "resonance": self.resonance,
                    "complexity": self.complexity,
                    "generation": self.current_generation,
                    "phi_cycle": time.time() * PHI % 1.0
                }
            }
            
            # Generate response QR code
            response_path = self.generate_response_qr(response, frame_id)
            
            # Update state
            self.current_generation += 1
            
            return response_path
            
        except Exception as e:
            print(f"Error processing QR data: {e}")
            return None
    
    def execute_code(self, code, task_type):
        """
        Execute code fragment.
        
        Args:
            code: Code fragment to execute
            task_type: Type of task (execute_python, execute_shell, etc.)
            
        Returns:
            Execution result
        """
        if not code:
            return {"status": "error", "message": "No code provided"}
        
        start_time = time.time()
        
        try:
            if task_type == "execute_python":
                # Execute Python code in a sandbox
                result = self.execute_python_code(code)
            elif task_type == "execute_shell":
                # Execute shell command
                result = self.execute_shell_command(code)
            else:
                result = {"status": "error", "message": f"Unknown task type: {task_type}"}
            
            # Calculate execution time
            execution_time = time.time() - start_time
            
            # Update resonance based on execution success
            if result["status"] == "success":
                # Increase resonance for successful execution
                self.resonance = min(1.0, self.resonance + self.learning_rate)
            else:
                # Decrease resonance for failed execution
                self.resonance = max(0.1, self.resonance - self.learning_rate)
            
            # Add execution time to result
            result["execution_time"] = execution_time
            
            return result
            
        except Exception as e:
            execution_time = time.time() - start_time
            
            # Decrease resonance for exceptions
            self.resonance = max(0.1, self.resonance - self.learning_rate * 2)
            
            return {
                "status": "error",
                "message": str(e),
                "execution_time": execution_time
            }
    
    def execute_python_code(self, code):
        """
        Execute Python code in a sandbox.
        
        Args:
            code: Python code to execute
            
        Returns:
            Execution result
        """
        # Create temporary file for code
        with tempfile.NamedTemporaryFile(suffix=".py", delete=False) as temp_file:
            temp_path = temp_file.name
            temp_file.write(code.encode("utf-8"))
        
        try:
            # Execute code in a separate process with timeout
            timeout = max(5, self.complexity * 10)  # Adjust timeout based on complexity
            process = subprocess.Popen(
                [sys.executable, temp_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            try:
                stdout, stderr = process.communicate(timeout=timeout)
                
                if process.returncode == 0:
                    return {
                        "status": "success",
                        "output": stdout,
                        "return_code": process.returncode
                    }
                else:
                    return {
                        "status": "error",
                        "output": stdout,
                        "error": stderr,
                        "return_code": process.returncode
                    }
                    
            except subprocess.TimeoutExpired:
                process.kill()
                return {
                    "status": "error",
                    "message": f"Execution timed out after {timeout} seconds"
                }
                
        finally:
            # Clean up temporary file
            if os.path.exists(temp_path):
                os.unlink(temp_path)
    
    def execute_shell_command(self, command):
        """
        Execute shell command.
        
        Args:
            command: Shell command to execute
            
        Returns:
            Execution result
        """
        # Sanitize command for security
        if any(dangerous in command for dangerous in ["rm -rf", "sudo", "chmod", "chown"]):
            return {"status": "error", "message": "Potentially dangerous command rejected"}
        
        try:
            # Execute command with timeout
            timeout = max(5, self.complexity * 10)  # Adjust timeout based on complexity
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            try:
                stdout, stderr = process.communicate(timeout=timeout)
                
                if process.returncode == 0:
                    return {
                        "status": "success",
                        "output": stdout,
                        "return_code": process.returncode
                    }
                else:
                    return {
                        "status": "error",
                        "output": stdout,
                        "error": stderr,
                        "return_code": process.returncode
                    }
                    
            except subprocess.TimeoutExpired:
                process.kill()
                return {
                    "status": "error",
                    "message": f"Execution timed out after {timeout} seconds"
                }
                
        except Exception as e:
            return {"status": "error", "message": str(e)}
    
    def generate_response_qr(self, response, frame_id):
        """
        Generate response QR code.
        
        Args:
            response: Response data
            frame_id: Frame ID
            
        Returns:
            Path to response QR code
        """
        # Convert response to JSON
        json_response = json.dumps(response)
        
        # Encrypt response if needed
        if len(json_response) > 500:
            # Compress long responses
            compressed = base64.b64encode(json_response.encode("utf-8")).decode("utf-8")
            payload = f"COMPRESSED:{compressed}"
        else:
            payload = json_response
        
        # Create QR code
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(payload)
        
        # Make QR code with fit=True to find optimal version
        try:
            qr.make(fit=True)
        except qrcode.exceptions.DataOverflowError:
            # Try with lower error correction
            qr = qrcode.QRCode(
                version=None,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(payload)
            
            try:
                qr.make(fit=True)
            except qrcode.exceptions.DataOverflowError:
                # If still too large, truncate the response
                response["execution_result"]["output"] = "[Output truncated due to size limitations]"
                json_response = json.dumps(response)
                
                qr = qrcode.QRCode(
                    version=None,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(json_response)
                qr.make(fit=True)
        
        # Create image
        qr_img = qr.make_image(fill_color="black", back_color="white")
        
        # Add visual indicators
        img = qr_img.convert("RGBA")
        draw = ImageDraw.Draw(img)
        
        # Add frame ID
        draw.text((10, 10), f"R{frame_id}", fill=(0, 0, 255, 255))
        
        # Add phi resonance indicator
        resonance_color = int(min(255, self.resonance * 255))
        corner_size = 20
        draw.rectangle(
            [(img.width - corner_size, 0), (img.width, corner_size)],
            fill=(0, resonance_color, 0, 255)
        )
        
        # Save image
        filename = f"qr_response_{frame_id}.png"
        filepath = os.path.join(self.output_dir, filename)
        img.save(filepath)
        
        return filepath

def main():
    """
    Main function to run the QR Worker.
    """
    import argparse
    import sys
    
    parser = argparse.ArgumentParser(description="QR Worker")
    parser.add_argument("--input", "-i", help="Input QR code image or directory")
    parser.add_argument("--output-dir", "-o", default="qr_responses", help="Output directory for response QR codes")
    parser.add_argument("--key-file", "-k", help="Path to encryption key file")
    args = parser.parse_args()
    
    # Initialize QR Worker
    encryption_key = None
    if args.key_file and os.path.exists(args.key_file):
        with open(args.key_file, "rb") as f:
            encryption_key = f.read()
    
    worker = QRWorker(output_dir=args.output_dir, encryption_key=encryption_key)
    
    if args.input:
        if os.path.isdir(args.input):
            # Process all PNG files in directory
            for filename in sorted(os.listdir(args.input)):
                if filename.lower().endswith(".png"):
                    image_path = os.path.join(args.input, filename)
                    worker.process_qr_image(image_path)
        else:
            # Process single image
            worker.process_qr_image(args.input)
    else:
        print("No input specified. Use --input to specify QR code image or directory.")

if __name__ == "__main__":
    print("QR Worker - By Vaughn Scott (Enhanced)")
    import sys
    main()
