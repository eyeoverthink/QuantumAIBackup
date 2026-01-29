#!/usr/bin/env python3
"""
View Decoded Face Image

This script displays the decoded face image and prints its properties
to evaluate the quality of the face image QR code system.
"""

import os
import sys
import argparse
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def view_image(image_path):
    """
    Display an image and print its properties
    
    Args:
        image_path: Path to the image file
    """
    if not os.path.exists(image_path):
        print(f"Error: Image file not found at {image_path}")
        return False
    
    try:
        # Open the image
        img = Image.open(image_path)
        
        # Get image properties
        width, height = img.size
        mode = img.mode
        format_name = img.format
        
        # Print image properties
        print(f"\n=== Image Properties: {os.path.basename(image_path)} ===")
        print(f"Dimensions: {width}x{height} pixels")
        print(f"Mode: {mode}")
        print(f"Format: {format_name}")
        print(f"Size on disk: {os.path.getsize(image_path)} bytes")
        
        # Calculate image quality metrics
        img_array = np.array(img)
        if len(img_array.shape) > 2:
            # Color image
            print(f"Channels: {img_array.shape[2]}")
        else:
            # Grayscale image
            print("Channels: 1 (Grayscale)")
        
        print(f"Min pixel value: {img_array.min()}")
        print(f"Max pixel value: {img_array.max()}")
        print(f"Mean pixel value: {img_array.mean():.2f}")
        print(f"Std deviation: {img_array.std():.2f}")
        
        # Display the image
        plt.figure(figsize=(8, 8))
        plt.imshow(img, cmap='gray' if mode == 'L' else None)
        plt.title(f"Decoded Face Image: {os.path.basename(image_path)}")
        plt.axis('on')
        plt.grid(False)
        plt.show()
        
        return True
    
    except Exception as e:
        print(f"Error viewing image: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description="View decoded face image and print properties")
    parser.add_argument("--image", default="decoded_face_5fa4ec29-535f-4c8b-9bf2-6a453eb7faa7_2837117571.png", 
                        help="Path to the decoded face image")
    args = parser.parse_args()
    
    view_image(args.image)

if __name__ == "__main__":
    main()
