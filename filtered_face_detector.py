#!/usr/bin/env python3
"""
Filtered Face Detector for Camera QR Evolution

This script implements a filtered face detection system that removes false positives
and background detections for more accurate face detection.
"""

import os
import sys
import time
import cv2
import numpy as np

def load_face_detector():
    """Load OpenCV face detector with multiple options."""
    # Try to find the face cascade files
    cascade_paths = [
        # Standard OpenCV locations
        os.path.join(cv2.__path__[0], 'data', 'haarcascade_frontalface_default.xml'),
        os.path.join(cv2.__path__[0], 'data', 'haarcascade_frontalface_alt.xml'),
        os.path.join(cv2.__path__[0], 'data', 'haarcascade_frontalface_alt2.xml'),
        os.path.join(sys.prefix, 'share', 'opencv4', 'haarcascades', 'haarcascade_frontalface_default.xml'),
        os.path.join(sys.prefix, 'share', 'opencv4', 'haarcascades', 'haarcascade_frontalface_alt.xml'),
        os.path.join(sys.prefix, 'share', 'opencv4', 'haarcascades', 'haarcascade_frontalface_alt2.xml'),
        # Local copies
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'haarcascade_frontalface_default.xml'),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'haarcascade_frontalface_alt.xml'),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'haarcascade_frontalface_alt2.xml'),
    ]
    
    # Try each path
    for cascade_path in cascade_paths:
        if os.path.exists(cascade_path):
            print(f"Found face cascade file: {cascade_path}")
            detector = cv2.CascadeClassifier(cascade_path)
            if not detector.empty():
                return detector
    
    print("Warning: Could not find face cascade file. Face detection will not work.")
    return None

def filter_faces(faces, frame_shape, min_face_size=60, max_faces=1):
    """
    Filter detected faces to remove false positives.
    
    Args:
        faces: List of detected faces (x, y, w, h)
        frame_shape: Shape of the frame (height, width, channels)
        min_face_size: Minimum size for a valid face
        max_faces: Maximum number of faces to return
        
    Returns:
        list: Filtered list of faces
    """
    if len(faces) == 0:
        return []
    
    # Filter by size
    valid_faces = []
    for (x, y, w, h) in faces:
        # Minimum size check
        if w < min_face_size or h < min_face_size:
            continue
        
        # Aspect ratio check (faces should be roughly square)
        aspect_ratio = float(w) / h
        if aspect_ratio < 0.5 or aspect_ratio > 2.0:
            continue
        
        # Position check (face should be in reasonable position in frame)
        center_x = x + w//2
        center_y = y + h//2
        
        # Face should be in the central region of the frame
        frame_height, frame_width = frame_shape[:2]
        if (center_x < frame_width * 0.1 or center_x > frame_width * 0.9 or
            center_y < frame_height * 0.1 or center_y > frame_height * 0.9):
            continue
        
        # Add to valid faces
        valid_faces.append((x, y, w, h))
    
    # If no valid faces, return empty list
    if not valid_faces:
        return []
    
    # Sort by size (largest first) and take only the largest faces
    valid_faces.sort(key=lambda face: face[2] * face[3], reverse=True)
    return valid_faces[:max_faces]

def detect_face_filtered(frame, face_detector):
    """
    Enhanced face detection with filtering to remove false positives.
    
    Args:
        frame: Input frame
        face_detector: OpenCV face detector
        
    Returns:
        tuple: (faces, display_frame) where faces is a list of (x,y,w,h) tuples
    """
    if face_detector is None or face_detector.empty():
        print("Face detector not available or empty")
        return [], frame.copy()
    
    # Make a copy for display
    display_frame = frame.copy()
    
    # Convert to grayscale for face detection
    if len(frame.shape) > 2 and frame.shape[2] > 1:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        gray = frame
    
    # Apply histogram equalization to improve contrast
    gray = cv2.equalizeHist(gray)
    
    # Try multiple detection parameters
    detection_params = [
        # (scaleFactor, minNeighbors, minSize)
        (1.2, 5, (60, 60)),   # Standard, more strict
        (1.1, 6, (60, 60)),   # More sensitive but stricter neighbors
        (1.3, 5, (80, 80)),   # Less sensitive, larger minimum size
    ]
    
    all_faces = []
    for scale_factor, min_neighbors, min_size in detection_params:
        faces = face_detector.detectMultiScale(
            gray,
            scaleFactor=scale_factor,
            minNeighbors=min_neighbors,
            minSize=min_size
        )
        
        if len(faces) > 0:
            all_faces.extend(faces)
            print(f"Detected {len(faces)} faces with params: scale={scale_factor}, neighbors={min_neighbors}, size={min_size}")
    
    # Convert to numpy array for easier processing
    if len(all_faces) > 0:
        all_faces = np.array(all_faces)
        
        # Remove duplicates (faces that overlap significantly)
        final_faces = []
        for i in range(len(all_faces)):
            x1, y1, w1, h1 = all_faces[i]
            area1 = w1 * h1
            is_duplicate = False
            
            for j in range(len(final_faces)):
                x2, y2, w2, h2 = final_faces[j]
                area2 = w2 * h2
                
                # Calculate intersection
                xx1 = max(x1, x2)
                yy1 = max(y1, y2)
                xx2 = min(x1 + w1, x2 + w2)
                yy2 = min(y1 + h1, y2 + h2)
                
                # Check if there is an intersection
                if xx2 < xx1 or yy2 < yy1:
                    continue
                
                intersection_area = (xx2 - xx1) * (yy2 - yy1)
                overlap_ratio = intersection_area / min(area1, area2)
                
                # If overlap is significant, consider it a duplicate
                if overlap_ratio > 0.5:
                    is_duplicate = True
                    
                    # Keep the larger face
                    if area1 > area2:
                        final_faces[j] = all_faces[i]
                    break
            
            if not is_duplicate:
                final_faces.append(all_faces[i])
        
        # Filter faces to remove false positives
        filtered_faces = filter_faces(final_faces, frame.shape)
        
        print(f"Detected {len(all_faces)} total faces, filtered to {len(filtered_faces)} valid faces")
    else:
        filtered_faces = []
    
    # Draw rectangles around filtered faces
    for (x, y, w, h) in filtered_faces:
        # Draw green rectangle around face
        cv2.rectangle(display_frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        # Add face detection indicator
        cv2.putText(display_frame, "Face Detected", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    return filtered_faces, display_frame

def run_face_detection():
    """Run face detection with filtering."""
    # Load face detector
    face_detector = load_face_detector()
    if face_detector is None:
        print("Failed to load face detector")
        return False
    
    # Initialize camera
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Failed to open camera")
        return False
    
    try:
        print("Starting filtered face detection...")
        print("Press 'q' to quit, 'c' to capture a frame")
        
        while True:
            # Capture frame
            ret, frame = cap.read()
            if not ret:
                continue
            
            # Detect faces with filtering
            faces, display_frame = detect_face_filtered(frame, face_detector)
            
            # Display status
            status_text = "Filtered Face Detection"
            cv2.putText(display_frame, status_text, (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 165, 255), 2)
            
            # Add face count
            face_status = f"Faces: {len(faces)}"
            face_color = (0, 255, 0) if len(faces) > 0 else (0, 0, 255)
            cv2.putText(display_frame, face_status, (10, 60), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, face_color, 2)
            
            # Show frame
            cv2.imshow('Filtered Face Detection', display_frame)
            
            # Handle key presses
            key = cv2.waitKey(1) & 0xFF
            
            # Quit if 'q' pressed
            if key == ord('q'):
                print("Exiting face detection")
                break
            
            # Capture if 'c' pressed
            if key == ord('c') and len(faces) > 0:
                print(f"Captured frame with {len(faces)} faces")
                cv2.imwrite("captured_face.jpg", frame)
                print("Saved to captured_face.jpg")
    
    except Exception as e:
        print(f"Error in face detection: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    finally:
        # Make sure to release camera resources
        cap.release()
        cv2.destroyAllWindows()
    
    return True

def main():
    """Main function."""
    success = run_face_detection()
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main())
