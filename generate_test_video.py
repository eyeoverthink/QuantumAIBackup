"""
Generate a test video with dynamic patterns for φ-harmonic scaling test
"""

import cv2
import numpy as np
import time

def create_test_video(output_path: str, duration: int = 10, fps: int = 30):
    """Create a test video with increasing complexity"""
    # Video properties
    width, height = 640, 480
    frame_count = duration * fps
    
    # Create video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    print(f"\nGenerating {duration}s test video at {fps} FPS")
    print("=====================================")
    
    try:
        for i in range(frame_count):
            # Create frame with increasing complexity
            frame = np.zeros((height, width, 3), dtype=np.uint8)
            
            # Add time-based patterns
            t = i / fps  # Current time in seconds
            
            # Pattern 1: Moving circles with φ-based sizing
            phi = (1 + np.sqrt(5)) / 2
            radius = int(30 * (1 + np.sin(t)))
            center_x = int(width/2 + width/4 * np.cos(t))
            center_y = int(height/2 + height/4 * np.sin(t))
            cv2.circle(frame, (center_x, center_y), radius, (0, 255, 0), -1)
            
            # Pattern 2: φ-spiral
            for j in range(0, 360, 30):
                angle = j * np.pi / 180
                r = 20 * phi * (1 + t/5)  # Growing spiral
                x = int(width/2 + r * np.cos(angle + t))
                y = int(height/2 + r * np.sin(angle + t))
                cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)
            
            # Pattern 3: Dynamic text
            text = f"Frame {i}/{frame_count}"
            cv2.putText(frame, text, (50, 50), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            
            # Add noise with increasing intensity
            noise_max = max(1, int(255 * (i/frame_count)))
            noise = np.random.randint(0, noise_max, frame.shape, dtype=np.uint8)
            frame = cv2.add(frame, noise)
            
            # Write frame
            out.write(frame)
            
            # Progress update
            if i % fps == 0:
                print(f"Progress: {i/frame_count*100:.1f}% ({i}/{frame_count} frames)")
                
    finally:
        out.release()
        
    print("\nVideo generation complete!")
    print(f"Output: {output_path}")
    print(f"Duration: {duration}s")
    print(f"Resolution: {width}x{height}")
    print(f"Total Frames: {frame_count}")

if __name__ == "__main__":
    output_path = "test_video.mp4"
    create_test_video(output_path)
    
    # Process the video with our φ-harmonic processor
    print("\nProcessing video with φ-harmonic scaling...")
    from video_processor import process_video
    process_video(output_path, "processed_" + output_path)
