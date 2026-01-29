#!/usr/bin/env python3
"""
Standalone Camera QR Evolution Workflow

This script implements a standalone version of the camera-to-QR-to-evolution workflow
without relying on problematic imports from the Face-QR system.
"""

import os
import sys
import time
import json
import uuid
import base64
import numpy as np
import cv2
from PIL import Image
import io
import qrcode
from datetime import datetime

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio (approximately 1.618034)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "qr_output")
EVOLUTION_DIR = os.path.join(BASE_DIR, "evolution_data")

# Create output directories
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(EVOLUTION_DIR, exist_ok=True)

# Evolution parameters
evolution_params = {
    "generation": 1,
    "similarity_threshold": 0.45,
    "feature_weight": 0.5,
    "temporal_factor": 0.2,
    "complexity": 1.0,
    "resonance": 0.5,
    "mutation_rate": 0.1
}

def load_face_detector():
    """Load OpenCV face detector."""
    # Try to find the face cascade file
    cascade_paths = [
        # Standard OpenCV locations
        os.path.join(cv2.__path__[0], 'data', 'haarcascade_frontalface_default.xml'),
        os.path.join(sys.prefix, 'share', 'opencv4', 'haarcascades', 'haarcascade_frontalface_default.xml'),
        # Local copy
        os.path.join(BASE_DIR, 'haarcascade_frontalface_default.xml'),
    ]
    
    # Try each path
    for cascade_path in cascade_paths:
        if os.path.exists(cascade_path):
            print(f"Found face cascade file: {cascade_path}")
            return cv2.CascadeClassifier(cascade_path)
    
    print("Warning: Could not find face cascade file. Face detection will not work.")
    return None

def capture_and_save_qr():
    """
    Capture an image from the camera and save it as a QR code.
    
    Returns:
        tuple: (success, qr_code_path)
    """
    # Load face detector
    face_detector = load_face_detector()
    
    # Initialize camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Failed to open camera")
        return False, ""
    
    try:
        print("Starting camera capture for QR generation...")
        print("Press 'q' to quit, 'c' to capture your face and generate QR code")
        
        while True:
            # Capture frame
            ret, frame = cap.read()
            if not ret:
                continue
            
            # Make a copy for display
            display_frame = frame.copy()
            
            # Try to detect faces in the frame for visual feedback
            if face_detector is not None:
                # Convert to grayscale for face detection
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    
                # Detect faces
                faces = face_detector.detectMultiScale(
                    gray,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30)
                )
                
                # Draw rectangles around faces with enhanced visual feedback
                for (x, y, w, h) in faces:
                    # Draw green rectangle around face
                    cv2.rectangle(display_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    
                    # Add face detection indicator
                    cv2.putText(display_frame, "Face Detected", (x, y-10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            
            # Display status and instructions
            # Create semi-transparent overlay for text background
            overlay = display_frame.copy()
            cv2.rectangle(overlay, (0, 0), (display_frame.shape[1], 60), (0, 0, 0), -1)
            cv2.addWeighted(overlay, 0.5, display_frame, 0.5, 0, display_frame)
            
            status_text = "QR Generation Mode"
            status_color = (0, 165, 255)  # Orange
            instruction_text = "Press 'c' to capture and generate QR code or 'q' to quit"
            
            # Draw status and instructions
            cv2.putText(display_frame, status_text, (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, status_color, 2)
            cv2.putText(display_frame, instruction_text, (10, 55), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
            
            # Show frame
            cv2.imshow('Face-QR Generation', display_frame)
            
            # Handle key presses
            key = cv2.waitKey(1) & 0xFF
            
            # Quit if 'q' pressed
            if key == ord('q'):
                print("QR generation cancelled")
                cap.release()
                cv2.destroyAllWindows()
                return False, ""
            
            # Generate QR if 'c' pressed
            if key == ord('c'):
                print("Capturing image for QR code generation...")
                
                # Show countdown
                for i in range(3, 0, -1):
                    countdown_frame = frame.copy()
                    cv2.putText(countdown_frame, f"Capturing in {i}...", 
                               (countdown_frame.shape[1]//2 - 150, countdown_frame.shape[0]//2), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 165, 255), 4)
                    cv2.imshow('Face-QR Generation', countdown_frame)
                    cv2.waitKey(800)  # Wait for 0.8 seconds between counts
                
                # Flash to indicate capture
                flash_frame = np.ones_like(frame) * 255
                cv2.imshow('Face-QR Generation', flash_frame)
                cv2.waitKey(150)  # Quick flash
                
                # Capture the frame after countdown
                ret, capture_frame = cap.read()
                if not ret:
                    print("Failed to capture frame for QR generation")
                    continue
                
                # Show "Processing" message
                processing_frame = capture_frame.copy()
                cv2.putText(processing_frame, "Generating QR Code...", 
                           (processing_frame.shape[1]//2 - 150, processing_frame.shape[0]//2), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 165, 255), 3)
                cv2.imshow('Face-QR Generation', processing_frame)
                cv2.waitKey(1)
                
                # Save the captured frame as a QR code
                qr_code_path = generate_qr_from_frame(capture_frame, face_detector)
                
                if qr_code_path:
                    print(f"QR code generated successfully: {qr_code_path}")
                    
                    # Display success message
                    success_frame = capture_frame.copy()
                    cv2.putText(success_frame, "QR Code Generated!", 
                               (success_frame.shape[1]//2 - 150, success_frame.shape[0]//2), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
                    cv2.imshow('Face-QR Generation', success_frame)
                    cv2.waitKey(2000)  # Show for 2 seconds
                    
                    # Release camera and close windows
                    cap.release()
                    cv2.destroyAllWindows()
                    
                    return True, qr_code_path
                else:
                    print("Failed to generate QR code")
                    
                    # Display error message
                    error_frame = capture_frame.copy()
                    cv2.putText(error_frame, "QR Generation Failed!", 
                               (error_frame.shape[1]//2 - 150, error_frame.shape[0]//2), 
                               cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
                    cv2.imshow('Face-QR Generation', error_frame)
                    cv2.waitKey(2000)  # Show for 2 seconds
                    
                    continue
    
    except Exception as e:
        print(f"Error in capture_and_save_qr: {e}")
        import traceback
        traceback.print_exc()
        return False, ""
    
    finally:
        # Make sure to release camera resources
        cap.release()
        cv2.destroyAllWindows()
    
    return False, ""

def generate_qr_from_frame(frame, face_detector):
    """
    Generate a QR code from a captured frame.
    
    Args:
        frame: Captured frame
        face_detector: OpenCV face detector
            
    Returns:
        str: Path to generated QR code image
    """
    try:
        # Detect face in the frame
        if face_detector is not None:
            # Convert to grayscale for face detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                
            # Detect faces
            faces = face_detector.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )
            
            if len(faces) == 0:
                print("No face detected in captured frame")
                return ""
                
            # Get largest face (by area)
            largest_face = None
            largest_area = 0
            for (x, y, w, h) in faces:
                area = w * h
                if area > largest_area:
                    largest_area = area
                    largest_face = (x, y, w, h)
            
            # Extract face region
            x, y, w, h = largest_face
            face_region = frame[y:y+h, x:x+w]
            
            # Resize to 16x16 for QR code (standard size used in Face-QR system)
            face_small = cv2.resize(face_region, (16, 16))
            
            # Convert to grayscale if needed
            if len(face_small.shape) > 2 and face_small.shape[2] > 1:
                face_small_gray = cv2.cvtColor(face_small, cv2.COLOR_BGR2GRAY)
            else:
                face_small_gray = face_small
            
            # Create a PIL Image from the face
            pil_image = Image.fromarray(face_small_gray)
            
            # Convert to bytes
            img_byte_arr = io.BytesIO()
            pil_image.save(img_byte_arr, format='JPEG', quality=30)  # Low quality for smaller QR code
            img_bytes = img_byte_arr.getvalue()
            
            # Encode as base64
            img_base64 = base64.b64encode(img_bytes).decode('utf-8')
            
            # Create task data
            task_id = str(uuid.uuid4())
            timestamp = int(time.time())
            task_data = {
                "task_id": task_id,
                "task_type": "display_face_image",
                "timestamp": timestamp,
                "image_data_base64": img_base64
            }
            
            # Create QR code
            qr = qrcode.QRCode(
                version=24,  # Higher version for more data capacity
                error_correction=qrcode.constants.ERROR_CORRECT_M,
                box_size=10,
                border=4,
            )
            
            # Add data to QR code
            qr.add_data(json.dumps({"task_data": task_data}))
            qr.make(fit=True)
            
            # Create QR code image
            qr_img = qr.make_image(fill_color="black", back_color="white")
            
            # Generate phi-harmonic filename
            phi_time = (timestamp * PHI) % 1
            qr_filename = f"face_qr_{timestamp}_{phi_time:.6f}.png"
            qr_path = os.path.join(OUTPUT_DIR, qr_filename)
            
            # Save QR code image
            qr_img.save(qr_path)
            
            print(f"QR code generated and saved to: {qr_path}")
            return qr_path
        else:
            print("Face detector not available")
            return ""
            
    except Exception as e:
        print(f"Error generating QR code from frame: {e}")
        import traceback
        traceback.print_exc()
        return ""

def evolve_parameters(authentication_result):
    """
    Evolve parameters based on authentication results.
    
    Args:
        authentication_result: Dictionary with authentication results
        
    Returns:
        dict: Updated evolution parameters
    """
    global evolution_params
    
    try:
        # Extract values from authentication result
        success = authentication_result.get('success', False)
        similarity = authentication_result.get('similarity', 0.0)
        phi_time = authentication_result.get('phi_time', (time.time() * PHI) % 1)
        
        # Get current parameters
        generation = evolution_params['generation']
        similarity_threshold = evolution_params['similarity_threshold']
        feature_weight = evolution_params['feature_weight']
        temporal_factor = evolution_params['temporal_factor']
        complexity = evolution_params['complexity']
        resonance = evolution_params['resonance']
        mutation_rate = evolution_params['mutation_rate']
        
        # Calculate phi-harmonic adjustment factor
        phi_factor = (phi_time * PHI) % 1
        
        # Adjust mutation rate based on generation (decreases over time)
        mutation_rate = mutation_rate * (1 - (0.01 * generation))
        
        # Evolve parameters based on authentication result
        if success:
            # Successful authentication - fine-tune parameters
            similarity_threshold = similarity_threshold * (1 - mutation_rate) + (similarity * 0.9) * mutation_rate
            feature_weight = feature_weight * (1 - mutation_rate) + (feature_weight + phi_factor * 0.1 - 0.05) * mutation_rate
            temporal_factor = temporal_factor * (1 - mutation_rate) + (temporal_factor + phi_factor * 0.1 - 0.05) * mutation_rate
            complexity = complexity * (1 - mutation_rate) + (complexity + phi_factor * 0.2 - 0.1) * mutation_rate
            resonance = resonance * (1 - mutation_rate) + (resonance + phi_factor * 0.2 - 0.1) * mutation_rate
        else:
            # Failed authentication - make more significant adjustments
            similarity_threshold = similarity_threshold * (1 - mutation_rate * 2) + (similarity_threshold - 0.05) * mutation_rate * 2
            feature_weight = feature_weight * (1 - mutation_rate) + (feature_weight - phi_factor * 0.2 + 0.1) * mutation_rate
            temporal_factor = temporal_factor * (1 - mutation_rate) + (temporal_factor - phi_factor * 0.2 + 0.1) * mutation_rate
            complexity = complexity * (1 - mutation_rate) + (complexity - phi_factor * 0.3 + 0.15) * mutation_rate
            resonance = resonance * (1 - mutation_rate) + (resonance - phi_factor * 0.3 + 0.15) * mutation_rate
        
        # Ensure parameters stay within valid ranges
        similarity_threshold = max(0.1, min(0.9, similarity_threshold))
        feature_weight = max(0.1, min(0.9, feature_weight))
        temporal_factor = max(0.1, min(0.9, temporal_factor))
        complexity = max(0.5, min(2.0, complexity))
        resonance = max(0.1, min(0.9, resonance))
        mutation_rate = max(0.01, min(0.2, mutation_rate))
        
        # Update generation
        generation += 1
        
        # Update evolution parameters
        evolution_params = {
            "generation": generation,
            "similarity_threshold": similarity_threshold,
            "feature_weight": feature_weight,
            "temporal_factor": temporal_factor,
            "complexity": complexity,
            "resonance": resonance,
            "mutation_rate": mutation_rate
        }
        
        # Save evolution data
        timestamp = int(time.time())
        evolution_data = {
            "timestamp": timestamp,
            "phi_time": phi_time,
            "authentication_success": success,
            "similarity": similarity,
            "parameters": evolution_params
        }
        
        # Generate phi-harmonic filename
        phi_time = (timestamp * PHI) % 1
        evolution_filename = f"evolution_{timestamp}_{phi_time:.6f}.json"
        evolution_path = os.path.join(EVOLUTION_DIR, evolution_filename)
        
        # Save evolution data to file
        with open(evolution_path, 'w') as f:
            json.dump(evolution_data, f, indent=2)
        
        print(f"Evolution data saved to: {evolution_path}")
        
        return evolution_params
        
    except Exception as e:
        print(f"Error evolving parameters: {e}")
        import traceback
        traceback.print_exc()
        return None

def run_evolution_on_qr(qr_code_path):
    """
    Run evolution process on a QR code.
    
    Args:
        qr_code_path: Path to QR code image
            
    Returns:
        bool: True if evolution was successful
    """
    if not qr_code_path or not os.path.exists(qr_code_path):
        print(f"QR code path is invalid or does not exist: {qr_code_path}")
        return False
    
    try:
        print(f"Running evolution on QR code: {qr_code_path}")
        
        # Create a test authentication scenario
        # We'll simulate authentication with the same face (should succeed)
        authentication_result = {
            'task_id': str(uuid.uuid4()),
            'timestamp': int(time.time()),
            'success': True,  # Assume success for evolution
            'similarity': 0.85,  # High similarity since it's the same face
            'phi_time': (time.time() * PHI) % 1
        }
        
        # Run evolution based on this authentication result
        evolution_result = evolve_parameters(authentication_result)
        
        if evolution_result:
            # Log evolution results
            print("\nEvolution Results:")
            print(f"  Generation: {evolution_result.get('generation', 'unknown')}")
            print(f"  Similarity Threshold: {evolution_result.get('similarity_threshold', 0):.4f}")
            print(f"  Feature Weight: {evolution_result.get('feature_weight', 0):.4f}")
            print(f"  Temporal Factor: {evolution_result.get('temporal_factor', 0):.4f}")
            print(f"  Complexity: {evolution_result.get('complexity', 0):.4f}")
            print(f"  Resonance: {evolution_result.get('resonance', 0):.4f}")
            print(f"  Mutation Rate: {evolution_result.get('mutation_rate', 0):.4f}")
            
            return True
        else:
            print("Evolution process did not return results")
            return False
        
    except Exception as e:
        print(f"Error running evolution on QR code: {e}")
        import traceback
        traceback.print_exc()
        return False

def camera_to_qr_to_evolution():
    """
    Run the complete workflow: capture image, save as QR, and run evolution.
    
    Returns:
        bool: True if the complete workflow was successful
    """
    try:
        print("\n=== Starting Camera-to-QR-to-Evolution Workflow ===\n")
        
        # Step 1: Capture image and save as QR code
        print("\n--- Step 1: Capturing Image and Generating QR Code ---\n")
        success, qr_code_path = capture_and_save_qr()
        
        if not success or not qr_code_path:
            print("Failed to capture image and generate QR code")
            return False
        
        # Step 2: Run evolution on the generated QR code
        print("\n--- Step 2: Running Evolution Process on QR Code ---\n")
        evolution_success = run_evolution_on_qr(qr_code_path)
        
        if not evolution_success:
            print("Failed to run evolution on QR code")
            return False
        
        print("\n=== Camera-to-QR-to-Evolution Workflow Completed Successfully ===\n")
        return True
        
    except Exception as e:
        print(f"Error in camera_to_qr_to_evolution workflow: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main function."""
    try:
        # Print current evolution parameters
        print("\nInitial Evolution Parameters:")
        print(f"  Generation: {evolution_params['generation']}")
        print(f"  Similarity Threshold: {evolution_params['similarity_threshold']:.4f}")
        print(f"  Feature Weight: {evolution_params['feature_weight']:.4f}")
        print(f"  Temporal Factor: {evolution_params['temporal_factor']:.4f}")
        print(f"  Complexity: {evolution_params['complexity']:.4f}")
        print(f"  Resonance: {evolution_params['resonance']:.4f}")
        print(f"  Mutation Rate: {evolution_params['mutation_rate']:.4f}")
        
        # Run the complete workflow
        success = camera_to_qr_to_evolution()
        
        if success:
            print("\nCamera-to-QR-to-Evolution workflow completed successfully!")
            
            # Print updated evolution parameters
            print("\nUpdated Evolution Parameters:")
            print(f"  Generation: {evolution_params['generation']}")
            print(f"  Similarity Threshold: {evolution_params['similarity_threshold']:.4f}")
            print(f"  Feature Weight: {evolution_params['feature_weight']:.4f}")
            print(f"  Temporal Factor: {evolution_params['temporal_factor']:.4f}")
            print(f"  Complexity: {evolution_params['complexity']:.4f}")
            print(f"  Resonance: {evolution_params['resonance']:.4f}")
            print(f"  Mutation Rate: {evolution_params['mutation_rate']:.4f}")
            
            return 0
        else:
            print("\nCamera-to-QR-to-Evolution workflow failed")
            return 1
            
    except Exception as e:
        print(f"Error in main: {e}")
        import traceback
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
