#!/usr/bin/env python3
"""
Test script for Face QR Evolution Extension

This script demonstrates the evolutionary capabilities of the Face-QR system,
showing how it can self-improve over time based on phi-harmonic principles.
"""

import os
import sys
import argparse
import time
import matplotlib.pyplot as plt
from PIL import Image

# Ensure the current directory is in the path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import face_qr modules
try:
    from face_qr_evolution_extension import FaceQREvolutionExtension, patch_camera_extension
except ImportError:
    print("Error: Required Face-QR Evolution Extension not found.")
    print("Please ensure you're running from the correct directory.")
    sys.exit(1)

def run_evolution_demo(face_image_path, generations=3):
    """
    Run a demonstration of the Face QR Evolution system.
    
    Args:
        face_image_path: Path to the face image to use
        generations: Number of evolution generations to simulate
    """
    print(f"\n{'='*60}")
    print(f"FACE-QR EVOLUTION DEMONSTRATION - {generations} GENERATIONS")
    print(f"{'='*60}\n")
    
    # Apply patches
    patch_camera_extension()
    
    # Create evolution extension
    evolution_ext = FaceQREvolutionExtension()
    
    # Initial QR generation
    print("\n[Generation 1] Generating initial evolved QR code...")
    qr_img, qr_path = evolution_ext.generate_evolved_qr(face_image_path)
    
    if not qr_path:
        print("Error: Failed to generate initial QR code")
        return False
    
    # Display the QR code
    plt.figure(figsize=(8, 8))
    plt.imshow(qr_img, cmap='gray')
    plt.title(f"Evolved Face-QR Code - Generation 1")
    plt.axis('off')
    plt.show()
    
    # Run evolution cycles
    for gen in range(2, generations + 1):
        print(f"\n[Generation {gen}] Simulating authentication and evolution...")
        
        # Simulate authentication (with random success to drive evolution)
        import random
        success = random.choice([True, False, True])  # Bias toward success
        similarity = evolution_ext.similarity_threshold + (0.1 if success else -0.1)
        
        print(f"Simulated authentication {'successful' if success else 'failed'} with similarity {similarity:.4f}")
        
        # Evolve based on simulated authentication
        evolution_ext.evolve(authentication_success=success, similarity_score=similarity)
        
        # Generate new QR code
        print(f"Generating new evolved QR code for generation {gen}...")
        qr_img, qr_path = evolution_ext.generate_evolved_qr(face_image_path)
        
        if not qr_path:
            print(f"Error: Failed to generate QR code for generation {gen}")
            continue
        
        # Display the QR code
        plt.figure(figsize=(8, 8))
        plt.imshow(qr_img, cmap='gray')
        plt.title(f"Evolved Face-QR Code - Generation {gen}")
        plt.axis('off')
        plt.show()
    
    # Visualize evolution history
    print("\nVisualizing evolution history...")
    evolution_ext.visualize_evolution()
    
    # Visualize authentication history
    print("\nVisualizing authentication history...")
    evolution_ext.visualize_authentication_history()
    
    print(f"\n{'='*60}")
    print(f"EVOLUTION DEMONSTRATION COMPLETE")
    print(f"{'='*60}\n")
    
    return True

def run_live_evolution(face_image_path=None):
    """
    Run live evolution with camera authentication.
    
    Args:
        face_image_path: Optional path to face image for initial QR generation
    """
    print(f"\n{'='*60}")
    print(f"FACE-QR LIVE EVOLUTION WITH CAMERA")
    print(f"{'='*60}\n")
    
    # Apply patches
    patch_camera_extension()
    
    # Create evolution extension
    evolution_ext = FaceQREvolutionExtension()
    
    # If face image provided, generate initial QR
    qr_path = None
    if face_image_path:
        print("\nGenerating initial evolved QR code...")
        _, qr_path = evolution_ext.generate_evolved_qr(face_image_path)
    
    # Run authentication with evolution
    if qr_path:
        print(f"\nStarting camera authentication with evolved QR code...")
        evolution_ext.authenticate_with_evolution(qr_code_path=qr_path)
    else:
        print("\nError: No QR code available for authentication")
        return False
    
    # Visualize evolution
    print("\nVisualizing evolution history...")
    evolution_ext.visualize_evolution()
    
    print(f"\n{'='*60}")
    print(f"LIVE EVOLUTION COMPLETE")
    print(f"{'='*60}\n")
    
    return True

def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Test Face-QR Evolution")
    parser.add_argument("--face", required=True, help="Path to face image")
    parser.add_argument("--demo", action="store_true", help="Run evolution demonstration")
    parser.add_argument("--live", action="store_true", help="Run live evolution with camera")
    parser.add_argument("--generations", type=int, default=3, help="Number of generations for demo")
    args = parser.parse_args()
    
    # Check if face image exists
    if not os.path.exists(args.face):
        print(f"Error: Face image not found at {args.face}")
        return 1
    
    # Run requested mode
    if args.demo:
        run_evolution_demo(args.face, args.generations)
    elif args.live:
        run_live_evolution(args.face)
    else:
        print("Please specify either --demo or --live mode")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
