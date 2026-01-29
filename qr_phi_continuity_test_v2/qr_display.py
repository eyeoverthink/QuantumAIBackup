#!/usr/bin/env python3
"""
QR Display Engine - Part of Animated QR Flipbook Execution System
By Vaughn Scott

Displays a sequence of QR codes with phi-harmonic timing for optimal camera capture.
Supports fullscreen display, looping, and timing variations based on golden ratio.
"""

import os
import sys
import time
import math
import pygame
import argparse
from PIL import Image

# Phi (Golden Ratio) constant
PHI = (1 + math.sqrt(5)) / 2  # Approximately 1.618034

class QRDisplayEngine:
    """
    Displays a sequence of QR codes with phi-harmonic timing.
    """
    
    def __init__(self, sequence_dir, fullscreen=False, loop=True):
        """
        Initialize the QR Display Engine.
        
        Args:
            sequence_dir: Directory containing QR code sequence
            fullscreen: Whether to display in fullscreen mode
            loop: Whether to loop the sequence
        """
        self.sequence_dir = sequence_dir
        self.fullscreen = fullscreen
        self.loop = loop
        self.running = False
        self.paused = False
        self.current_frame = 0
        self.base_delay = 0.5  # Base delay between frames in seconds
        
        # Initialize pygame
        pygame.init()
        pygame.display.set_caption("QR Flipbook Display")
        
        # Set up display
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        
        if fullscreen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((800, 800))
        
        # Load QR sequence
        self.load_sequence()
    
    def load_sequence(self):
        """Load QR code sequence from directory."""
        if not os.path.exists(self.sequence_dir):
            print(f"Error: Directory {self.sequence_dir} not found")
            sys.exit(1)
        
        # Get all PNG files in directory
        self.frames = sorted([f for f in os.listdir(self.sequence_dir) 
                             if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
        
        if not self.frames:
            print(f"Error: No image files found in {self.sequence_dir}")
            sys.exit(1)
        
        print(f"Loaded {len(self.frames)} QR frames from {self.sequence_dir}")
        
        # Load first frame
        self.load_frame(0)
    
    def load_frame(self, index):
        """
        Load a specific frame.
        
        Args:
            index: Frame index to load
        """
        if 0 <= index < len(self.frames):
            # Load image
            image_path = os.path.join(self.sequence_dir, self.frames[index])
            try:
                image = pygame.image.load(image_path)
                
                # Scale image to fit screen while maintaining aspect ratio
                img_width, img_height = image.get_size()
                screen_width, screen_height = self.screen.get_size()
                
                # Calculate scaling factor
                scale_factor = min(screen_width / img_width, screen_height / img_height)
                
                # Scale image
                new_width = int(img_width * scale_factor)
                new_height = int(img_height * scale_factor)
                self.current_image = pygame.transform.scale(image, (new_width, new_height))
                
                # Calculate position to center image
                self.image_x = (screen_width - new_width) // 2
                self.image_y = (screen_height - new_height) // 2
                
                # Update current frame
                self.current_frame = index
                
                # Print frame info
                print(f"Displaying frame {index+1}/{len(self.frames)}: {self.frames[index]}")
                
                return True
            except pygame.error as e:
                print(f"Error loading frame {index}: {e}")
                return False
        else:
            return False
    
    def calculate_frame_delay(self, frame_index):
        """
        Calculate phi-harmonic delay for a frame.
        
        Args:
            frame_index: Index of the frame
            
        Returns:
            Delay in seconds
        """
        # Base delay with phi-harmonic variation
        phase = (frame_index * PHI) % (2 * math.pi)
        variation = 0.2 * math.sin(phase)
        
        # Calculate resonance factor
        resonance = 1.0 / (1.0 + abs(((frame_index + 1) * PHI) % 1.0 - 0.5))
        
        # Apply variation and resonance
        delay = self.base_delay + variation * resonance
        
        # Ensure delay is within reasonable bounds
        return max(0.1, min(1.0, delay))
    
    def run(self):
        """Run the display engine."""
        self.running = True
        clock = pygame.time.Clock()
        
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_SPACE:
                        self.paused = not self.paused
                        status = "Paused" if self.paused else "Resumed"
                        print(f"{status} at frame {self.current_frame+1}")
                    elif event.key == pygame.K_RIGHT:
                        self.load_frame((self.current_frame + 1) % len(self.frames))
                    elif event.key == pygame.K_LEFT:
                        self.load_frame((self.current_frame - 1) % len(self.frames))
            
            # Clear screen
            self.screen.fill((255, 255, 255))
            
            # Draw current frame
            self.screen.blit(self.current_image, (self.image_x, self.image_y))
            
            # Update display
            pygame.display.flip()
            
            # If not paused, advance to next frame after delay
            if not self.paused:
                # Calculate phi-harmonic delay for this frame
                delay = self.calculate_frame_delay(self.current_frame)
                
                # Wait
                time.sleep(delay)
                
                # Load next frame
                next_frame = (self.current_frame + 1) % len(self.frames)
                if next_frame == 0 and not self.loop:
                    # End of sequence and not looping
                    print("End of sequence")
                    self.running = False
                else:
                    self.load_frame(next_frame)
            
            # Cap at 30 FPS for event handling
            clock.tick(30)
        
        # Clean up
        pygame.quit()
    
    def print_instructions(self):
        """Print instructions for controlling the display."""
        print("\nQR Display Engine Controls:")
        print("  Space: Pause/Resume")
        print("  Left/Right Arrow: Previous/Next frame")
        print("  Escape: Quit")
        print("\nStarting display...")

def main():
    """Main function to run the QR Display Engine."""
    parser = argparse.ArgumentParser(description="QR Display Engine")
    parser.add_argument("--dir", required=True, help="Directory containing QR sequence")
    parser.add_argument("--fullscreen", action="store_true", help="Run in fullscreen mode")
    parser.add_argument("--no-loop", dest="loop", action="store_false", help="Don't loop the sequence")
    parser.set_defaults(loop=True)
    
    args = parser.parse_args()
    
    # Create display engine
    display = QRDisplayEngine(args.dir, args.fullscreen, args.loop)
    
    # Print instructions
    display.print_instructions()
    
    # Run display
    display.run()

if __name__ == "__main__":
    print("QR Display Engine - By Vaughn Scott")
    main()
