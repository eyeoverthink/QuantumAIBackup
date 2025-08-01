#!/usr/bin/env python3
"""
PHI-HARMONIC SIMPLE TEST FILE GENERATOR
=======================================
Creates test files with phi-harmonic patterns for transmission experiments.
Uses only standard libraries and PIL which is already installed.
"""

import os
import math
import random
from datetime import datetime
from PIL import Image, ImageDraw

# Phi-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Inverse golden ratio (φ⁻¹ = 0.618033988749895)

def create_phi_image_jpg(size=(1024, 768), filename="phi_test_large.jpg"):
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

def create_phi_text_file(size_kb=100, filename="phi_test_text.txt"):
    """Create a test text file with phi-harmonic content"""
    # Calculate approximate number of characters
    chars_per_kb = 1024  # Roughly 1024 characters per KB
    target_chars = size_kb * chars_per_kb
    
    # Phi-harmonic words
    phi_words = [
        "golden", "ratio", "divine", "proportion", "fibonacci", 
        "harmony", "balance", "nature", "spiral", "quantum",
        "resonance", "consciousness", "universe", "pattern", "mathematics",
        "phi", "sacred", "geometry", "perfection", "beauty",
        "retrocausality", "temporal", "superposition", "entanglement", "wave"
    ]
    
    # Generate phi-harmonic text
    text = f"PHI-HARMONIC TEST TEXT FILE\n{'='*30}\n\n"
    text += f"Phi (φ): {PHI}\nInverse Phi (φ⁻¹): {PHI_INV}\n"
    text += f"Timestamp: {datetime.now().isoformat()}\n\n"
    
    # Add phi-harmonic content
    chars_so_far = len(text)
    paragraph_length = int(PHI * 100)  # ~162 words per paragraph
    
    while chars_so_far < target_chars:
        # Generate a paragraph with phi-harmonic structure
        paragraph = ""
        for _ in range(paragraph_length):
            # Select word using phi
            word_index = int((chars_so_far * PHI) % len(phi_words))
            word = phi_words[word_index]
            
            # Add word
            paragraph += word + " "
            chars_so_far += len(word) + 1
            
            # Add phi-harmonic line breaks
            if chars_so_far % int(PHI * 50) < 1:
                paragraph += "\n"
                chars_so_far += 1
        
        # Add paragraph
        text += paragraph + "\n\n"
        chars_so_far += 2
        
        # Check if we've reached the target size
        if chars_so_far >= target_chars:
            break
    
    # Write to file
    with open(filename, 'w') as f:
        f.write(text)
    
    file_size = os.path.getsize(filename) / 1024  # KB
    print(f"Created phi-harmonic text file: {filename} ({file_size:.2f} KB)")
    return filename

def main():
    """Create all test files"""
    print("PHI-HARMONIC SIMPLE TEST FILE GENERATOR")
    print("=======================================")
    print(f"Phi (φ): {PHI}")
    print(f"Inverse Phi (φ⁻¹): {PHI_INV}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print()
    
    # Create test files
    jpg_file = create_phi_image_jpg(size=(1024, 768))
    png_file = create_phi_image_png(size=(1500, 1200))
    bin_file = create_phi_binary_file(size_kb=1024)
    txt_file = create_phi_text_file(size_kb=256)
    
    print("\nAll test files created successfully!")
    print("Use these files with the phi-harmonic image transporter to test different data types.")

if __name__ == "__main__":
    main()
