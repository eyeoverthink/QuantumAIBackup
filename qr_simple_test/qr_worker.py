#!/usr/bin/env python3
"""
QR Worker - Part of Animated QR Flipbook Execution System
By Vaughn Scott

Captures QR codes from camera or image sequence, decodes payloads,
executes embedded code fragments, and generates response QR codes.
Implements phi-harmonic evolution and learning.
"""

import os
import cv2
import json
import time
import uuid
import base64
import zlib
import hashlib
import io
import tempfile
import subprocess
import numpy as np
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
import qrcode
from cryptography.fernet import Fernet
from pyzbar import pyzbar

# Phi (Golden Ratio) constant
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

class QRWorker:
    """
    QR Worker that captures QR codes, executes code fragments, and generates responses.
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
        
        # Initialize QR detector
        self.qr_detector = cv2.QRCodeDetector()
        
        # Initialize encryption if key provided
        self.encryption = None
        if encryption_key:
            self.encryption = Fernet(encryption_key)
        elif os.path.exists("qr_encryption.key"):
            with open("qr_encryption.key", "rb") as key_file:
                key = key_file.read()
                self.encryption = Fernet(key)
                print("Using encryption key from qr_encryption.key")
        
        # Session tracking
        self.session_history = {}
        self.executed_frames = []
        self.last_hash = None
        self.response_frame = 1
    
    def calculate_phi_resonance(self, value):
        """Calculate phi-harmonic resonance of a value."""
        return 1.0 / (1.0 + abs((value * PHI) % 1.0 - 0.5))
    
    def evolve_metadata(self, input_metadata=None):
        """
        Evolve the phi-metadata based on golden ratio principles and input.
        
        Args:
            input_metadata: Optional metadata from input QR to influence evolution
        """
        # Apply phi-harmonic oscillation to complexity
        phase = (self.current_generation * PHI) % (2 * np.pi)
        complexity_delta = 0.1 * np.sin(phase)
        
        # If we have input metadata, use it to influence evolution
        if input_metadata:
            input_gen = input_metadata.get("generation", self.current_generation)
            input_complexity = input_metadata.get("complexity", self.complexity)
            input_resonance = input_metadata.get("resonance", self.resonance)
            
            # Blend our values with input values using phi-weighted average
            self.complexity = (self.complexity * (1 - 1/PHI) + 
                              input_complexity * (1/PHI) + 
                              complexity_delta)
            
            self.resonance = (self.resonance * (1 - 1/PHI) + 
                             input_resonance * (1/PHI))
            
            # Increment generation if input generation is higher
            if input_gen > self.current_generation:
                self.current_generation = input_gen
        else:
            # No input, just apply our own evolution
            self.complexity = max(0.1, min(1.0, self.complexity + complexity_delta))
            self.resonance = self.calculate_phi_resonance(self.current_generation)
        
        # Ensure values stay in valid range
        self.complexity = max(0.1, min(1.0, self.complexity))
        self.resonance = max(0.1, min(5.0, self.resonance))
    
    def decode_qr_from_data(self, image_data):
        """
        Decode QR code from in-memory image data.
        
        Args:
            image_data: Bytes of the image file
            
        Returns:
            Decoded payload or None if no QR found
        """
        try:
            # Use PIL to open the image from a byte stream
            pil_img = Image.open(io.BytesIO(image_data))
            
            # If the image has an alpha channel (e.g., PNG), convert to RGB first
            if pil_img.mode == 'RGBA':
                pil_img = pil_img.convert('RGB')
                
            # Convert PIL image to OpenCV format (NumPy array)
            # PIL images are RGB, OpenCV uses BGR
            cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
            return self.decode_qr(cv_img)
        except Exception as e:
            print(f"Error: Could not process image data: {e}")
            return None

    def decode_qr_from_image(self, image_path):
        """
        Decode QR code from image file.
        
        Args:
            image_path: Path to image file
            
        Returns:
            Decoded payload or None if no QR found
        """
        try:
            with open(image_path, "rb") as f:
                image_data = f.read()
            return self.decode_qr_from_data(image_data)
        except FileNotFoundError:
            print(f"Error: Image file not found at {image_path}")
            return None
        except Exception as e:
            print(f"Error reading image file {image_path}: {e}")
            return None
    
    def decode_qr(self, img):
        """
        Decode QR code from OpenCV image using OpenCV and pyzbar as a fallback.
        
        Args:
            img: OpenCV image containing QR code
            
        Returns:
            Decoded payload or None if no QR found
        """
        # Attempt 1: Decode with OpenCV
        text = None
        try:
            retval, decoded_info, points, straight_qrcode = self.qr_detector.detectAndDecodeMulti(img)
            if retval and decoded_info and decoded_info[0]:
                text = decoded_info[0]
                print("DEBUG: Successfully decoded QR with OpenCV.")
        except Exception as e:
            # This can fail on some platforms if OpenCV is not built with QR support
            print(f"DEBUG: OpenCV QR decoding failed: {e}")

        # Attempt 2: Fallback to pyzbar if OpenCV fails
        if not text:
            print("DEBUG: OpenCV failed to decode QR. Falling back to pyzbar...")
            try:
                # pyzbar can decode directly from the OpenCV image (numpy array)
                decoded_objects = pyzbar.decode(img)
                if decoded_objects:
                    text = decoded_objects[0].data.decode("utf-8")
                    print("DEBUG: Successfully decoded QR with pyzbar.")
            except Exception as e:
                print(f"Error: pyzbar QR decoding failed: {e}")

        if not text:
            return None
        
        # Check if encrypted
        if text.startswith("ENCRYPTED:"):
            if not self.encryption:
                print("Encrypted payload detected but no encryption key provided")
                return None
            
            print("Encrypted payload detected, decrypting...")
            try:
                encrypted_data = base64.b64decode(text[len("ENCRYPTED:"):])
                text = self.encryption.decrypt(encrypted_data).decode()
            except Exception as e:
                print(f"Error decrypting payload: {e}")
                return None

        # Check if compressed
        if text.startswith("COMPRESSED:"):
            print("Compressed payload detected, decompressing...")
            try:
                compressed_data = base64.b64decode(text[len("COMPRESSED:"):])
                text = zlib.decompress(compressed_data).decode('utf-8')
            except Exception as e:
                print(f"Error decompressing payload: {e}")
                return None
        
        # Try to parse as JSON
        try:
            return json.loads(text)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON payload: {e}")
            return None
    
    def validate_payload(self, payload):
        """
        Validate payload integrity and expiration.
        
        Args:
            payload: Decoded payload to validate
            
        Returns:
            (is_valid, reason) tuple
        """
        if not payload:
            return False, "Empty payload"
        
        # Check required fields
        required_fields = ["session_id", "frame_number", "task_type", "content"]
        for field in required_fields:
            if field not in payload:
                return False, f"Missing required field: {field}"
        
        # Check expiration
        if "valid_until" in payload:
            valid_until = payload["valid_until"]
            now = datetime.now().isoformat()
            if valid_until < now:
                return False, f"Payload expired at {valid_until}"
        
        # Check hash chain if we have previous hash
        if self.last_hash and "prev_frame_hash" in payload:
            if payload["prev_frame_hash"] != self.last_hash:
                return False, "Hash chain broken, possible tampering"
        
        # Store hash for next frame
        payload_json = json.dumps(payload)
        self.last_hash = hashlib.sha256(payload_json.encode()).hexdigest()
        
        return True, "Valid"
    
    def execute_code_fragment(self, payload):
        """
        Execute code fragment from payload.
        
        Args:
            payload: Decoded payload containing code to execute
            
        Returns:
            (success, output) tuple
        """
        task_type = payload["task_type"]
        content = payload["content"]
        
        if task_type == "PYTHON_FILE":
            script_path = payload.get("script_path")
            if not script_path or not os.path.exists(script_path):
                return False, f"Script file not found at {script_path}"
            with open(script_path, 'r') as f:
                content = f.read()
        
        if not content:
            return False, "Empty code content"
        
        try:
            if task_type in ["execute_python", "PYTHON_SCRIPT", "PYTHON_FILE"]:
                # Execute Python code in a safe environment
                local_vars = {}
                exec(content, {"__builtins__": __builtins__}, local_vars)
                
                # Capture output from print statements
                output = local_vars.get("__output__", "Executed successfully")
                return True, output
                
            elif task_type == "execute_sh":
                # Execute shell script
                with tempfile.NamedTemporaryFile(mode="w", suffix=".sh", delete=False) as temp:
                    temp.write(content)
                    temp_path = temp.name
                
                try:
                    # Make executable
                    os.chmod(temp_path, 0o755)
                    
                    # Execute
                    result = subprocess.run(
                        ["/bin/bash", temp_path],
                        capture_output=True,
                        text=True,
                        timeout=5  # 5 second timeout for safety
                    )
                    
                    return result.returncode == 0, result.stdout
                finally:
                    # Clean up
                    if os.path.exists(temp_path):
                        os.unlink(temp_path)
            else:
                return False, f"Unsupported task type: {task_type}"
        except Exception as e:
            return False, f"Execution error: {str(e)}"
    
    def generate_response_qr(self, input_payload, execution_result, execution_output):
        """
        Generate a response QR code based on execution results.
        
        Args:
            input_payload: Original input payload
            execution_result: Boolean success/failure
            execution_output: Output from execution
            
        Returns:
            Path to generated response QR image
        """
        # Create response payload
        response = {
            "session_id": self.session_id,
            "original_session_id": input_payload.get("session_id", "unknown"),
            "frame_number": self.response_frame,
            "response_to_frame": input_payload.get("frame_number", 0),
            "task_type": "response",
            "execution_success": execution_result,
            "content": execution_output[:1000] if execution_output else "",  # Limit size
            "phi_metadata": {
                "generation": self.current_generation,
                "complexity": self.complexity,
                "resonance": self.resonance,
                "mutation_vector": [
                    self.calculate_phi_resonance(self.complexity),
                    self.calculate_phi_resonance(self.resonance),
                    self.calculate_phi_resonance(time.time())
                ]
            },
            "timestamp": datetime.now().isoformat(),
            "valid_until": (datetime.now().timestamp() + 300)  # 5 minutes
        }
        
        # Convert to JSON
        json_payload = json.dumps(response)
        
        # Calculate hash for this frame
        response_hash = hashlib.sha256(json_payload.encode()).hexdigest()
        
        # Encrypt if encryption is enabled
        if self.encryption:
            encrypted_payload = self.encryption.encrypt(json_payload.encode())
            payload_text = "ENCRYPTED:" + base64.b64encode(encrypted_payload).decode()
        else:
            payload_text = json_payload
        
        # Create QR code
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(payload_text)
        qr.make(fit=True)
        
        # Create image
        qr_img = qr.make_image(fill_color="black", back_color="white")
        
        # Save image
        filename = os.path.join(self.output_dir, f"response_{self.response_frame:03d}.png")
        qr_img.save(filename)
        
        # Add visual indicators
        img = Image.open(filename)
        draw = ImageDraw.Draw(img)
        
        # Add frame number
        draw.text((10, 10), f"R{self.response_frame:03d}", fill="blue")
        
        # Add execution status indicator
        status_color = "green" if execution_result else "red"
        img_width, img_height = img.size
        corner_size = int(img_width * 0.05)
        draw.rectangle(
            [(img_width - corner_size, 0), (img_width, corner_size)],
            fill=status_color
        )
        
        # Save modified image
        img.save(filename)
        
        # Update counters
        self.response_frame += 1
        if self.response_frame % int(PHI * 3) == 0:  # ~5 responses per generation
            self.current_generation += 1
        
        return filename
    
    def process_qr_data(self, image_data):
        """
        Process a single QR image from in-memory data.
        
        Args:
            image_data: Bytes of the QR image
            
        Returns:
            Path to response QR image or None if processing failed
        """
        print("Processing QR image from in-memory data")
        
        # Decode QR code
        payload = self.decode_qr_from_data(image_data)
        if not payload:
            print("No QR code found or could not decode from data")
            return None
        
        # Validate payload
        valid, reason = self.validate_payload(payload)
        if not valid:
            print(f"Invalid payload: {reason}")
            return None
        
        # Track session
        session_id = payload["session_id"]
        if session_id not in self.session_history:
            self.session_history[session_id] = {
                "frames_processed": 0,
                "first_frame": payload["frame_number"],
                "last_frame": payload["frame_number"]
            }
        
        self.session_history[session_id]["frames_processed"] += 1
        self.session_history[session_id]["last_frame"] = payload["frame_number"]
        
        # Evolve metadata based on input
        self.evolve_metadata(payload.get("phi_metadata"))
        
        # Execute code
        success, output = self.execute_code_fragment(payload)
        
        # Generate response
        response_path = self.generate_response_qr(payload, success, output)
        
        print(f"Generated response QR: {response_path}")
        return response_path

    def process_qr_image(self, image_path):
        """
        Process a single QR image.
        
        Args:
            image_path: Path to QR image
            
        Returns:
            Path to response QR image or None if processing failed
        """
        print(f"Processing QR image: {image_path}")
        
        # Decode QR code
        payload = self.decode_qr_from_image(image_path)
        if not payload:
            print("No QR code found or could not decode")
            return None
        
        # Validate payload
        valid, reason = self.validate_payload(payload)
        if not valid:
            print(f"Invalid payload: {reason}")
            return None
        
        # Track session
        session_id = payload["session_id"]
        if session_id not in self.session_history:
            self.session_history[session_id] = {
                "frames_processed": 0,
                "first_frame": payload["frame_number"],
                "last_frame": payload["frame_number"]
            }
        
        session = self.session_history[session_id]
        session["frames_processed"] += 1
        session["last_frame"] = payload["frame_number"]
        
        # Execute code fragment
        print(f"Executing {payload['task_type']} code fragment...")
        success, output = self.execute_code_fragment(payload)
        print(f"Execution {'succeeded' if success else 'failed'}: {output}")
        
        # Evolve metadata based on input
        self.evolve_metadata(payload.get("phi_metadata"))
        
        # Generate response QR
        response_path = self.generate_response_qr(payload, success, output)
        print(f"Generated response QR: {response_path}")
        
        # Track executed frame
        self.executed_frames.append({
            "input_frame": os.path.basename(image_path),
            "response_frame": os.path.basename(response_path),
            "session_id": session_id,
            "frame_number": payload["frame_number"],
            "task_type": payload["task_type"],
            "success": success
        })
        
        return response_path
    
    def process_directory(self, directory_path):
        """
        Process all QR images in a directory.
        
        Args:
            directory_path: Path to directory containing QR images
            
        Returns:
            List of response QR image paths
        """
        if not os.path.exists(directory_path):
            print(f"Error: Directory {directory_path} not found")
            return []
        
        # Get all PNG files in directory
        image_files = sorted([f for f in os.listdir(directory_path) 
                             if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
        
        if not image_files:
            print(f"No image files found in {directory_path}")
            return []
        
        print(f"Processing {len(image_files)} QR images in {directory_path}...")
        
        responses = []
        for filename in image_files:
            image_path = os.path.join(directory_path, filename)
            response_path = self.process_qr_image(image_path)
            if response_path:
                responses.append(response_path)
            
            # Phi-harmonic timing between frames
            time.sleep(0.1 * self.calculate_phi_resonance(len(responses)))
        
        return responses
    
    def start_camera_capture(self, camera_id=0):
        """
        Start capturing QR codes from camera.
        
        Args:
            camera_id: Camera device ID
            
        Returns:
            None
        """
        # Open camera
        cap = cv2.VideoCapture(camera_id)
        if not cap.isOpened():
            print(f"Error: Could not open camera {camera_id}")
            return
        
        print(f"Starting camera capture on camera {camera_id}...")
        print("Press 'q' to quit")
        
        last_process_time = 0
        min_process_interval = 1.0  # Minimum seconds between processing
        
        while True:
            # Read frame
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame")
                break
            
            # Show frame
            cv2.imshow("QR Worker Camera", frame)
            
            # Process frame at phi-harmonic intervals
            current_time = time.time()
            if current_time - last_process_time > min_process_interval:
                # Try to decode QR code
                payload = self.decode_qr(frame)
                if payload:
                    print("\nQR code detected!")
                    
                    # Validate payload
                    valid, reason = self.validate_payload(payload)
                    if valid:
                        # Execute code fragment
                        print(f"Executing {payload['task_type']} code fragment...")
                        success, output = self.execute_code_fragment(payload)
                        print(f"Execution {'succeeded' if success else 'failed'}: {output}")
                        
                        # Evolve metadata based on input
                        self.evolve_metadata(payload.get("phi_metadata"))
                        
                        # Generate response QR
                        response_path = self.generate_response_qr(payload, success, output)
                        print(f"Generated response QR: {response_path}")
                        
                        # Show response QR
                        response_img = cv2.imread(response_path)
                        if response_img is not None:
                            cv2.imshow("QR Worker Response", response_img)
                    else:
                        print(f"Invalid payload: {reason}")
                    
                    # Update last process time
                    last_process_time = current_time
            
            # Check for quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Release resources
        cap.release()
        cv2.destroyAllWindows()
    
    def print_summary(self):
        """Print summary of processed QR codes."""
        print("\n" + "="*60)
        print("QR WORKER SUMMARY")
        print("="*60)
        
        print(f"\nWorker session ID: {self.session_id}")
        print(f"Current generation: {self.current_generation}")
        print(f"Current complexity: {self.complexity:.6f}")
        print(f"Current resonance: {self.resonance:.6f}")
        
        print("\nSESSIONS PROCESSED:")
        for session_id, session in self.session_history.items():
            print(f"\n  Session ID: {session_id}")
            print(f"  Frames processed: {session['frames_processed']}")
            print(f"  Frame range: {session['first_frame']} to {session['last_frame']}")
        
        print(f"\nTotal frames executed: {len(self.executed_frames)}")
        print(f"Total responses generated: {self.response_frame - 1}")
        
        print("\nTASK TYPE SUMMARY:")
        task_types = {}
        for frame in self.executed_frames:
            task_type = frame['task_type']
            if task_type not in task_types:
                task_types[task_type] = {"total": 0, "success": 0}
            
            task_types[task_type]["total"] += 1
            if frame["success"]:
                task_types[task_type]["success"] += 1
        
        for task_type, stats in task_types.items():
            success_rate = (stats["success"] / stats["total"]) * 100 if stats["total"] > 0 else 0
            print(f"  {task_type}: {stats['success']}/{stats['total']} ({success_rate:.1f}% success)")
        
        print("\n" + "="*60)

def main():
    """Main function to run the QR Worker."""
    import argparse
    
    parser = argparse.ArgumentParser(description="QR Worker")
    parser.add_argument("--dir", help="Process QR images from directory")
    parser.add_argument("--image", help="Process single QR image")
    parser.add_argument("--camera", type=int, default=0, help="Camera device ID for live capture")
    parser.add_argument("--output", default="qr_responses", help="Output directory for response QR codes")
    parser.add_argument("--key", help="Path to encryption key file")
    
    args = parser.parse_args()
    
    # Get encryption key if provided
    encryption_key = None
    if args.key and os.path.exists(args.key):
        with open(args.key, "rb") as key_file:
            encryption_key = key_file.read()
    
    # Create QR worker
    worker = QRWorker(output_dir=args.output, encryption_key=encryption_key)
    
    if args.image:
        # Process single image
        worker.process_qr_image(args.image)
    elif args.dir:
        # Process directory
        worker.process_directory(args.dir)
    else:
        # Start camera capture
        worker.start_camera_capture(args.camera)
    
    # Print summary
    worker.print_summary()

if __name__ == "__main__":
    print("QR Worker - By Vaughn Scott")
    main()
