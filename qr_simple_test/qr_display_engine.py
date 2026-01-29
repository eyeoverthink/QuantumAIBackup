#!/usr/bin/env python3
"""
QR Display Engine - Part of Animated QR Flipbook Execution System
By Vaughn Scott

Displays a sequence of QR codes at an optimal frame rate for camera capture.
Implements phi-harmonic timing for optimal visual communication.
"""

import os
import sys
import time
import math
import glob
import pygame
import argparse
from PIL import Image

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

class QRDisplayEngine:
    """
    Displays a sequence of QR codes with phi-harmonic timing.
    """
    
    def __init__(self, sequence_dir="qr_sequence", frame_rate=10, fullscreen=False):
        """
        Initialize the QR Display Engine.
        
        Args:
            sequence_dir: Directory containing QR code sequence images
            frame_rate: Base frame rate for display (frames per second)
            fullscreen: Whether to display in fullscreen mode
        """
        self.sequence_dir = sequence_dir
        self.base_frame_rate = frame_rate
        self.fullscreen = fullscreen
        self.frame_paths = []
        self.current_frame = 0
        
        # Initialize pygame
        pygame.init()
        pygame.display.set_caption("QR Flipbook Display - By Vaughn Scott")
        
        # Get screen info
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        
        # Set up display
        if fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((800, 800))
            
        # Load sequence
        self.load_sequence()
        
        # Calculate phi-harmonic frame timings
        self.frame_timings = self.calculate_frame_timings()
    
    def load_sequence(self):
        """Load QR code sequence from directory."""
        # Check if directory exists
        if not os.path.exists(self.sequence_dir):
            print(f"Error: Sequence directory '{self.sequence_dir}' not found.")
            sys.exit(1)
        
        # Get all PNG files in directory
        self.frame_paths = sorted(glob.glob(os.path.join(self.sequence_dir, "qr_frame_*.png")))
        
        if not self.frame_paths:
            print(f"Error: No QR frames found in '{self.sequence_dir}'.")
            sys.exit(1)
            
        print(f"Loaded {len(self.frame_paths)} QR frames from {self.sequence_dir}")
    
    def calculate_frame_timings(self):
        """
        Calculate phi-harmonic timing for each frame.
        
        Returns:
            List of frame durations in milliseconds
        """
        base_duration = 1000.0 / self.base_frame_rate  # ms
        timings = []
        
        for i in range(len(self.frame_paths)):
            # Apply phi-harmonic variation to timing
            # This creates a natural rhythm based on the golden ratio
            phase = (i * PHI) % (2 * math.pi)
            variation = 0.2 * math.sin(phase)  # ±20% variation
            
            # Calculate frame duration with phi-harmonic variation
            duration = base_duration * (1.0 + variation)
            
            # Every PHI frames, add a slightly longer pause for processing
            if i % int(PHI * 5) == 0 and i > 0:
                duration *= PHI  # Longer pause at phi-harmonic intervals
                
            timings.append(duration)
        
        return timings
    
    def display_frame(self, frame_index):
        """
        Display a single QR frame.
        
        Args:
            frame_index: Index of frame to display
        """
        # Load image with PIL
        image = Image.open(self.frame_paths[frame_index])
        
        # Convert to pygame surface
        mode = image.mode
        size = image.size
        data = image.tobytes()
        
        py_image = pygame.image.fromstring(data, size, mode)
        
        # Scale to fit screen while maintaining aspect ratio
        img_width, img_height = size
        
        # Get display size
        display_width, display_height = self.screen.get_size()
        
        # Calculate scaling factor
        scale = min(display_width / img_width, display_height / img_height) * 0.9
        
        # Calculate new dimensions
        new_width = int(img_width * scale)
        new_height = int(img_height * scale)
        
        # Scale image
        py_image = pygame.transform.scale(py_image, (new_width, new_height))
        
        # Calculate position (center of screen)
        x = (display_width - new_width) // 2
        y = (display_height - new_height) // 2
        
        # Fill screen with white
        self.screen.fill((255, 255, 255))
        
        # Draw image
        self.screen.blit(py_image, (x, y))
        
        # Add frame info
        font = pygame.font.SysFont('Arial', 24)
        frame_text = font.render(f"Frame: {frame_index + 1}/{len(self.frame_paths)}", True, (0, 0, 0))
        self.screen.blit(frame_text, (10, 10))
        
        # Update display
        pygame.display.flip()
    
    def run_sequence(self, loop=True, response_mode=False):
        """
        Run the QR code sequence animation.
        
        Args:
            loop: Whether to loop the sequence
            response_mode: Whether to wait for QR response after sequence
        """
        running = True
        clock = pygame.time.Clock()
        
        print("Starting QR Flipbook animation...")
        print("Press ESC to exit, SPACE to pause/resume")
        
        paused = False
        start_time = time.time()
        
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_SPACE:
                        paused = not paused
                        if paused:
                            print("Animation paused. Press SPACE to resume.")
                        else:
                            print("Animation resumed.")
            
            if not paused:
                # Display current frame
                self.display_frame(self.current_frame)
                
                # Wait for frame duration
                frame_duration = self.frame_timings[self.current_frame]
                pygame.time.delay(int(frame_duration))
                
                # Move to next frame
                self.current_frame += 1
                
                # Handle end of sequence
                if self.current_frame >= len(self.frame_paths):
                    if loop:
                        self.current_frame = 0
                        print("Sequence loop complete, restarting...")
                    elif response_mode:
                        print("Sequence complete. Waiting for QR response...")
                        # TODO: Implement QR response capture
                        time.sleep(5)  # Wait for demonstration
                        running = False
                    else:
                        running = False
            
            # Maintain reasonable CPU usage
            clock.tick(60)
        
        end_time = time.time()
        duration = end_time - start_time
        
        print(f"QR Flipbook animation finished.")
        print(f"Displayed {len(self.frame_paths)} frames in {duration:.2f} seconds")
        print(f"Average frame rate: {len(self.frame_paths) / duration:.2f} fps")
        
        pygame.quit()

def main():
    """Main function to run the QR Display Engine."""
    parser = argparse.ArgumentParser(description="QR Flipbook Display Engine")
    parser.add_argument("--dir", default="qr_sequence", help="Directory containing QR sequence")
    parser.add_argument("--rate", type=float, default=5, help="Base frame rate (fps)")
    parser.add_argument("--fullscreen", action="store_true", help="Run in fullscreen mode")
    parser.add_argument("--loop", action="store_true", help="Loop the sequence")
    parser.add_argument("--response", action="store_true", help="Wait for QR response")
    
    args = parser.parse_args()
    
    # Create and run display engine
    engine = QRDisplayEngine(
        sequence_dir=args.dir,
        frame_rate=args.rate,
        fullscreen=args.fullscreen
    )
    
    engine.run_sequence(loop=args.loop, response_mode=args.response)

if __name__ == "__main__":
    print("QR Display Engine - By Vaughn Scott")
    main()
