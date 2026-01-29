#!/usr/bin/env python3
"""
Face QR Recognition Module

This module handles face recognition and verification
for the Face-QR 2FA Security System.

It follows the 'lego' design principle, allowing it to be used independently
or combined with other modules for enhanced functionality.
"""

import os
import io
import json
import time
import hashlib
import numpy as np
from typing import Dict, Tuple, Optional, Union, Any, List
from PIL import Image

try:
    import cv2
    CV2_AVAILABLE = True
except ImportError:
    CV2_AVAILABLE = False

# Import core module
from face_qr_core import FaceQRBase, FaceQRConfig, PHI

class FaceQRRecognition(FaceQRBase):
    """
    Handles face recognition and verification.
    """
    
    def __init__(self, config_path: str = None):
        """
        Initialize the recognition module.
        
        Args:
            config_path: Path to configuration file
        """
        super().__init__()
        self.config = FaceQRConfig(config_path)
        
        # Create models directory if it doesn't exist
        self.models_dir = os.path.join(self.base_dir, "models")
        os.makedirs(self.models_dir, exist_ok=True)
        
        # Initialize face detection and recognition
        self.face_detector = None
        self.face_recognizer = None
        
        # Load models if available
        self.load_models()
    
    def load_models(self) -> bool:
        """
        Load face detection and recognition models.
        
        Returns:
            bool: True if successful
        """
        if not CV2_AVAILABLE:
            print("OpenCV not available. Using basic image comparison.")
            return False
        
        try:
            # Load face detection model
            face_cascade_path = os.path.join(cv2.data.haarcascades, 'haarcascade_frontalface_default.xml')
            if os.path.exists(face_cascade_path):
                self.face_detector = cv2.CascadeClassifier(face_cascade_path)
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
    
    def detect_faces(self, image_data: bytes) -> List[np.ndarray]:
        """
        Detect faces in an image.
        
        Args:
            image_data: Image data
            
        Returns:
            List[np.ndarray]: List of face images
        """
        if not CV2_AVAILABLE or self.face_detector is None:
            # Return the whole image as a single face
            image = Image.open(io.BytesIO(image_data))
            image_array = np.array(image)
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
            
            # Detect faces
            faces = self.face_detector.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )
            
            # Extract face images
            face_images = []
            for (x, y, w, h) in faces:
                face_images.append(gray[y:y+h, x:x+w])
            
            return face_images
            
        except Exception as e:
            print(f"Error detecting faces: {e}")
            return []
    
    def extract_features(self, face_image: np.ndarray) -> np.ndarray:
        """
        Extract features from a face image.
        
        Args:
            face_image: Face image
            
        Returns:
            np.ndarray: Feature vector
        """
        # For simplicity, we'll use the raw pixel values as features
        # In a production system, you would use a proper feature extraction method
        
        # Resize to a standard size
        try:
            if CV2_AVAILABLE:
                resized = cv2.resize(face_image, (100, 100))
                # Flatten to a feature vector
                features = resized.flatten()
                return features
            else:
                # Convert to PIL Image if needed
                if isinstance(face_image, np.ndarray):
                    face_image = Image.fromarray(face_image)
                
                # Resize and flatten
                resized = face_image.resize((100, 100))
                features = np.array(resized).flatten()
                return features
                
        except Exception as e:
            print(f"Error extracting features: {e}")
            return np.array([])
    
    def compare_faces(self, face1: np.ndarray, face2: np.ndarray) -> float:
        """
        Compare two faces and return similarity score.
        
        Args:
            face1: First face image
            face2: Second face image
            
        Returns:
            float: Similarity score (0-1)
        """
        try:
            # Extract features
            features1 = self.extract_features(face1)
            features2 = self.extract_features(face2)
            
            if len(features1) == 0 or len(features2) == 0:
                return 0.0
            
            # Calculate similarity (normalized Euclidean distance)
            distance = np.linalg.norm(features1 - features2)
            max_distance = np.sqrt(255**2 * len(features1))  # Maximum possible distance
            similarity = 1.0 - (distance / max_distance)
            
            return similarity
            
        except Exception as e:
            print(f"Error comparing faces: {e}")
            return 0.0
    
    def verify_face(self, reference_image_data: bytes, test_image_data: bytes,
                   threshold: float = None) -> Tuple[bool, float]:
        """
        Verify if two face images match.
        
        Args:
            reference_image_data: Reference face image data
            test_image_data: Test face image data
            threshold: Similarity threshold (0-1)
            
        Returns:
            Tuple[bool, float]: (is_match, similarity_score)
        """
        if threshold is None:
            threshold = 0.7  # Default threshold
        
        try:
            # Detect faces
            reference_faces = self.detect_faces(reference_image_data)
            test_faces = self.detect_faces(test_image_data)
            
            if not reference_faces or not test_faces:
                return False, 0.0
            
            # Compare the first face from each image
            similarity = self.compare_faces(reference_faces[0], test_faces[0])
            
            # Check if similarity exceeds threshold
            is_match = similarity >= threshold
            
            return is_match, similarity
            
        except Exception as e:
            print(f"Error verifying face: {e}")
            return False, 0.0
    
    def hash_face(self, image_data: bytes) -> str:
        """
        Generate a hash of face features.
        
        Args:
            image_data: Face image data
            
        Returns:
            str: Face hash
        """
        try:
            # Detect faces
            faces = self.detect_faces(image_data)
            
            if not faces:
                # If no face detected, hash the whole image
                return self.calculate_hash(image_data)
            
            # Extract features from the first face
            features = self.extract_features(faces[0])
            
            # Convert features to bytes and hash
            features_bytes = features.tobytes()
            face_hash = hashlib.sha256(features_bytes).hexdigest()
            
            return face_hash
            
        except Exception as e:
            print(f"Error hashing face: {e}")
            # Fallback to simple image hash
            return self.calculate_hash(image_data)
    
    def train_recognizer(self, face_images: List[bytes], labels: List[int]) -> bool:
        """
        Train face recognizer with labeled face images.
        
        Args:
            face_images: List of face image data
            labels: List of corresponding labels
            
        Returns:
            bool: True if successful
        """
        if not CV2_AVAILABLE or self.face_recognizer is None:
            print("OpenCV face recognition not available.")
            return False
        
        try:
            # Process each image
            processed_faces = []
            processed_labels = []
            
            for i, image_data in enumerate(face_images):
                # Detect faces
                faces = self.detect_faces(image_data)
                
                if faces:
                    # Add the first face and its label
                    processed_faces.append(cv2.resize(faces[0], (100, 100)))
                    processed_labels.append(labels[i])
            
            if not processed_faces:
                print("No faces detected in training images.")
                return False
            
            # Train recognizer
            self.face_recognizer.train(processed_faces, np.array(processed_labels))
            
            # Save model
            model_path = os.path.join(self.models_dir, "face_recognizer.yml")
            self.face_recognizer.write(model_path)
            
            print(f"Face recognizer trained and saved to {model_path}")
            return True
            
        except Exception as e:
            print(f"Error training face recognizer: {e}")
            return False
    
    def recognize_face(self, image_data: bytes) -> Dict:
        """
        Recognize a face using trained model.
        
        Args:
            image_data: Face image data
            
        Returns:
            Dict: Recognition result
        """
        if not CV2_AVAILABLE or self.face_recognizer is None:
            print("OpenCV face recognition not available.")
            return {
                "success": False,
                "error": "Face recognition not available"
            }
        
        try:
            # Detect faces
            faces = self.detect_faces(image_data)
            
            if not faces:
                return {
                    "success": False,
                    "error": "No face detected"
                }
            
            # Resize face for recognition
            face = cv2.resize(faces[0], (100, 100))
            
            # Predict
            label, confidence = self.face_recognizer.predict(face)
            
            # Convert confidence to similarity (OpenCV returns distance, not similarity)
            # Lower confidence means better match in OpenCV
            similarity = 1.0 - min(confidence / 100.0, 1.0)
            
            return {
                "success": True,
                "label": label,
                "similarity": similarity,
                "confidence": confidence
            }
            
        except Exception as e:
            print(f"Error recognizing face: {e}")
            return {
                "success": False,
                "error": str(e)
            }

# Main function for testing
if __name__ == "__main__":
    import sys
    
    # Parse command-line arguments
    if len(sys.argv) < 3:
        print("Usage: python face_qr_recognition.py <reference_image> <test_image>")
        sys.exit(1)
    
    reference_image_path = sys.argv[1]
    test_image_path = sys.argv[2]
    
    # Load images
    try:
        with open(reference_image_path, "rb") as f:
            reference_image_data = f.read()
        
        with open(test_image_path, "rb") as f:
            test_image_data = f.read()
    except Exception as e:
        print(f"Error loading images: {e}")
        sys.exit(1)
    
    # Create recognition module
    recognition = FaceQRRecognition()
    
    # Verify faces
    is_match, similarity = recognition.verify_face(reference_image_data, test_image_data)
    
    print(f"Face verification result:")
    print(f"  Match: {is_match}")
    print(f"  Similarity: {similarity:.4f}")
    
    # Generate face hash
    face_hash = recognition.hash_face(reference_image_data)
    print(f"Face hash: {face_hash}")
