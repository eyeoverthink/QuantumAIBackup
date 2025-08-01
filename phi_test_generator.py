#!/usr/bin/env python3
"""
PHI-HARMONIC TEST FILE GENERATOR
================================
Creates test files with phi-harmonic patterns for transmission experiments.
"""

import os
import math
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import cv2
from datetime import datetime

# Phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)

def create_phi_image_jpg(size=(800, 600), filename="phi_test_large.jpg"):
    """Create a test JPG image with phi-harmonic patterns"""
    width, height = size
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw phi-harmonic pattern
    for x in range(0, width, 2):
        for y in range(0, height, 2):
            val = int(127.5 * (1 + math.sin(x/PHI) * math.cos(y*PHI)))
            color = (val, int(val*PHI % 255), 255-val)
            draw.point((x, y), fill=color)
    
    # Draw phi spiral
    center_x, center_y = width // 2, height // 2
    radius = min(width, height) // 4
    for angle in range(0, 1440, 5):
        rad = math.radians(angle)
        r = radius * math.exp(PHI_INV * rad)
        x = center_x + int(r * math.cos(rad))
        y = center_y + int(r * math.sin(rad))
        if 0 <= x < width and 0 <= y < height:
            draw.point((x, y), fill=(0, 0, 0))
    
    # Add text
    draw.text((width//2-150, 50), "PHI-HARMONIC TEST IMAGE (JPG)", fill=(0, 0, 0))
    draw.text((width//2-100, height-70), f"φ = {PHI:.6f}", fill=(0, 0, 0))
    draw.text((width//2-100, height-50), f"Size: {width}x{height}", fill=(0, 0, 0))
    
    # Save image with high quality
    img.save(filename, quality=95)
    file_size = os.path.getsize(filename) / 1024  # KB
    print(f"Created phi-harmonic JPG test image: {filename} ({file_size:.2f} KB)")
    return filename

def create_phi_image_png(size=(1200, 900), filename="phi_test_large.png"):
    """Create a test PNG image with phi-harmonic patterns"""
    width, height = size
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)
    
    # Draw phi-harmonic grid
    for x in range(0, width, 4):
        for y in range(0, height, 4):
            phi_val = (x * PHI + y * PHI_INV) % 1
            color = (
                int(255 * math.sin(phi_val * math.pi)),
                int(255 * math.cos(phi_val * math.pi * PHI)),
                int(255 * math.sin(phi_val * math.pi * PHI_INV))
            )
            draw.point((x, y), fill=color)
    
    # Draw golden rectangles
    rect_size = min(width, height) // 3
    for i in range(5):
        scale = PHI ** i
        rect_w = int(rect_size / scale)
        rect_h = int(rect_size / scale / PHI)
        x = width // 2 - rect_w // 2
        y = height // 2 - rect_h // 2
        draw.rectangle([x, y, x+rect_w, y+rect_h], outline=(0, 0, 0))
    
    # Add text
    draw.text((width//2-150, 50), "PHI-HARMONIC TEST IMAGE (PNG)", fill=(0, 0, 0))
    draw.text((width//2-100, height-70), f"φ = {PHI:.6f}", fill=(0, 0, 0))
    draw.text((width//2-100, height-50), f"Size: {width}x{height}", fill=(0, 0, 0))
    
    # Save image with compression
    img.save(filename, compress_level=1)
    file_size = os.path.getsize(filename) / 1024  # KB
    print(f"Created phi-harmonic PNG test image: {filename} ({file_size:.2f} KB)")
    return filename

def create_phi_video_mp4(size=(640, 480), duration=5, fps=30, filename="phi_test_video.mp4"):
    """Create a test MP4 video with phi-harmonic patterns"""
    width, height = size
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(filename, fourcc, fps, size)
    
    frames = duration * fps
    for frame in range(frames):
        # Create a frame with phi-harmonic patterns
        img = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Time-varying phi pattern
        t = frame / frames
        for y in range(0, height, 4):
            for x in range(0, width, 4):
                phi_val = (x * PHI + y * PHI_INV + t * PHI**2) % 1
                b = int(255 * math.sin(phi_val * math.pi * 2))
                g = int(255 * math.cos(phi_val * math.pi * PHI))
                r = int(255 * math.sin(phi_val * math.pi * PHI_INV))
                img[y:y+4, x:x+4] = [b, g, r]
        
        # Draw phi spiral that grows with time
        center_x, center_y = width // 2, height // 2
        radius = min(width, height) // 4
        spiral_growth = 0.5 + 0.5 * t
        for angle in range(0, 1440, 10):
            rad = math.radians(angle)
            r = radius * spiral_growth * math.exp(PHI_INV * rad)
            x = center_x + int(r * math.cos(rad))
            y = center_y + int(r * math.sin(rad))
            if 0 <= x < width and 0 <= y < height:
                cv2.circle(img, (x, y), 1, (255, 255, 255), -1)
        
        # Add text
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, "PHI-HARMONIC TEST VIDEO", (width//2-150, 50), font, 0.7, (255, 255, 255), 2)
        cv2.putText(img, f"φ = {PHI:.6f}", (width//2-100, height-50), font, 0.7, (255, 255, 255), 2)
        cv2.putText(img, f"Frame: {frame}/{frames}", (width//2-100, height-30), font, 0.7, (255, 255, 255), 2)
        
        # Add frame to video
        video.write(img)
    
    # Release video
    video.release()
    file_size = os.path.getsize(filename) / 1024  # KB
    print(f"Created phi-harmonic MP4 test video: {filename} ({file_size:.2f} KB)")
    return filename

def create_phi_binary_file(size_kb=512, filename="phi_test_binary.dat"):
    """Create a test binary file with phi-harmonic patterns"""
    # Calculate number of bytes
    size_bytes = size_kb * 1024
    
    # Create binary data with phi-harmonic patterns
    data = bytearray()
    for i in range(size_bytes):
        # Use phi to generate byte values
        phi_val = (i * PHI) % 1
        byte_val = int(255 * phi_val)
        data.append(byte_val)
    
    # Write to file
    with open(filename, 'wb') as f:
        f.write(data)
    
    file_size = os.path.getsize(filename) / 1024  # KB
    print(f"Created phi-harmonic binary test file: {filename} ({file_size:.2f} KB)")
    return filename

def main():
    """Create all test files"""
    print("PHI-HARMONIC TEST FILE GENERATOR")
    print("================================")
    print(f"Phi (φ): {PHI}")
    print(f"Inverse Phi (φ⁻¹): {PHI_INV}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print()
    
    # Create test files
    jpg_file = create_phi_image_jpg(size=(1024, 768))
    png_file = create_phi_image_png(size=(1200, 900))
    mp4_file = create_phi_video_mp4(duration=3)
    bin_file = create_phi_binary_file(size_kb=256)
    
    print("\nAll test files created successfully!")
    print("Use these files with the phi-harmonic image transporter to test different data types.")

if __name__ == "__main__":
    main()
