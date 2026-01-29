#!/usr/bin/env python3
"""
Face QR Recognition Extension Module

This extension ensures proper activation and usage of OpenCV in the Face-QR system.
It follows the 'lego' design principle, extending functionality without modifying core files.
"""

import os
import sys
import numpy as np
from typing import List, Optional, Tuple, Dict, Any
import cv2

from face_qr_recognition import FaceQRRecognition, CV2_AVAILABLE

class OpenCVActivator:
    """
    Activates and verifies OpenCV installation and models.
    """
    
    @staticmethod
    def get_haarcascade_path() -> str:
        """
        Get the path to the Haar cascade file, trying multiple possible locations.
        
        Returns:
            str: Path to the Haar cascade file
        """
        # Try standard OpenCV data path
        if hasattr(cv2, 'data'):
            standard_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
            if os.path.exists(standard_path):
                return standard_path
        
        # Try common installation paths
        possible_paths = [
            # Standard OpenCV path
            '/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml',
            '/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml',
            '/usr/local/share/opencv/haarcascades/haarcascade_frontalface_default.xml',
            '/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml',
            # Python package paths
            os.path.join(sys.prefix, 'share/opencv4/haarcascades/haarcascade_frontalface_default.xml'),
            os.path.join(sys.prefix, 'share/opencv/haarcascades/haarcascade_frontalface_default.xml'),
            # Current directory and subdirectories
            'haarcascade_frontalface_default.xml',
            'models/haarcascade_frontalface_default.xml',
            'data/haarcascade_frontalface_default.xml',
        ]
        
        for path in possible_paths:
            if os.path.exists(path):
                return path
        
        # If not found, download the file
        return OpenCVActivator.download_haarcascade()
    
    @staticmethod
    def download_haarcascade() -> str:
        """
        Download the Haar cascade file if not found locally.
        
        Returns:
            str: Path to the downloaded Haar cascade file
        """
        import urllib.request
        
        # Create models directory if it doesn't exist
        models_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "models")
        os.makedirs(models_dir, exist_ok=True)
        
        # Download the file
        cascade_url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
        cascade_path = os.path.join(models_dir, "haarcascade_frontalface_default.xml")
        
        if not os.path.exists(cascade_path):
            print(f"Downloading Haar cascade file to {cascade_path}...")
            urllib.request.urlretrieve(cascade_url, cascade_path)
            print("Download complete.")
        
        return cascade_path

def patch_face_qr_recognition():
    """
    Patch the FaceQRRecognition class to ensure OpenCV is properly activated.
    """
    original_load_models = FaceQRRecognition.load_models
    
    def enhanced_load_models(self) -> bool:
        """
        Enhanced version of load_models that ensures OpenCV is properly activated.
        
        Returns:
            bool: True if successful
        """
        if not CV2_AVAILABLE:
            print("OpenCV not available. Using basic image comparison.")
            return False
        
        try:
            # Get Haar cascade path using our activator
            face_cascade_path = OpenCVActivator.get_haarcascade_path()
            
            if os.path.exists(face_cascade_path):
                print(f"Loading face cascade from: {face_cascade_path}")
                self.face_detector = cv2.CascadeClassifier(face_cascade_path)
                
                # Verify the classifier loaded correctly
                if self.face_detector.empty():
                    print("Warning: Cascade classifier is empty after loading!")
                    return False
                else:
                    print("Cascade classifier loaded successfully.")
            else:
                print(f"Face cascade file not found: {face_cascade_path}")
                return False
            
            # Load face recognition model if available
            if hasattr(cv2, 'face') and hasattr(cv2.face, 'LBPHFaceRecognizer_create'):
                self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
                
                # Check if model file exists
                model_path = os.path.join(self.models_dir, "face_recognizer.yml")
                if os.path.exists(model_path):
                    self.face_recognizer.read(model_path)
                    print(f"Loaded face recognition model from {model_path}")
                else:
                    print("No face recognition model found. Will create one when trained.")
            else:
                print("OpenCV face recognition module not available.")
            
            return True
            
        except Exception as e:
            print(f"Error loading face models: {e}")
            return False
    
    # Apply the patch
    FaceQRRecognition.load_models = enhanced_load_models
    
    # Patch the detect_faces method to better handle errors
    original_detect_faces = FaceQRRecognition.detect_faces
    
    def enhanced_detect_faces(self, image_data: bytes) -> List[np.ndarray]:
        """
        Enhanced version of detect_faces with better error handling.
        
        Args:
            image_data: Image data
            
        Returns:
            List[np.ndarray]: List of face images
        """
        if not CV2_AVAILABLE or self.face_detector is None:
            # Return the whole image as a single face
            image = Image.open(io.BytesIO(image_data))
            image_array = np.array(image)
            print("Using whole image as face (OpenCV not available or face detector not loaded)")
            return [image_array]
        
        try:
            # Convert image data to OpenCV format
            image = Image.open(io.BytesIO(image_data))
            image_array = np.array(image)
            
            # Convert to grayscale if needed
            if len(image_array.shape) > 2 and image_array.shape[2] > 1:
                gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
            else:
                gray = image_array
            
            # Verify detector is loaded
            if self.face_detector.empty():
                print("Warning: Face detector is empty! Reloading...")
                face_cascade_path = OpenCVActivator.get_haarcascade_path()
                self.face_detector = cv2.CascadeClassifier(face_cascade_path)
                
                if self.face_detector.empty():
                    print("Still empty after reload. Using whole image as face.")
                    return [gray]
            
            # Detect faces with more robust parameters
            faces = self.face_detector.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=3,  # Reduced from 5 for better detection
                minSize=(20, 20)  # Smaller minimum size
            )
            
            # Extract face images
            face_images = []
            for (x, y, w, h) in faces:
                face_images.append(gray[y:y+h, x:x+w])
            
            if not face_images:
                print("No faces detected. Using whole image as fallback.")
                return [gray]
                
            print(f"Successfully detected {len(face_images)} faces")
            return face_images
            
        except Exception as e:
            print(f"Error detecting faces: {e}")
            # Return whole image as fallback
            try:
                image = Image.open(io.BytesIO(image_data))
                return [np.array(image)]
            except:
                return []
    
    # Apply the patch
    FaceQRRecognition.detect_faces = enhanced_detect_faces

# Patch the class when this module is imported
patch_face_qr_recognition()

# Add missing import
import io
from PIL import Image

print("Face QR Recognition Extension loaded - OpenCV activated and patched")
