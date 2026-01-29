#!/usr/bin/env python3
"""
PHI^75 VISUAL RECEIVER (TKINTER VERSION)
=====================
Visual UDP message receiver that displays incoming messages in a GUI window,
making the φ-dimensional reality protection visible across all three MacBooks.

This version is designed to work with tkinter if available, or fall back to
command-line output if tkinter is not available.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import random
from datetime import datetime

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
LISTEN_PORTS = [11700, 11710, 11720, 11800, 11810, 11820, 11900, 11910, 11975, 11976]
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BG_COLOR = "#000000"  # Black
TEXT_COLOR = "#00FF00"  # Green
HIGHLIGHT_COLOR = "#FFFF00"  # Yellow
TITLE_COLOR = "#FF00FF"  # Magenta

# Try to import tkinter, but don't fail if it's not available
try:
    import tkinter as tk
    from tkinter import scrolledtext, font
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False
    print("Tkinter not available. Falling back to command-line output.")

class Phi75VisualReceiver:
    """
    Visual UDP message receiver that displays incoming messages in a GUI window.
    Falls back to command-line if tkinter is not available.
    """
    
    def __init__(self):
        """Initialize the visual receiver"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.running = False
        self.sockets = []
        self.messages = []
        self.max_messages = 100
        
        if TKINTER_AVAILABLE:
            # Create GUI
            self.root = tk.Tk()
            self.root.title(f"φ^75 Visual Receiver - {self.hostname} ({self.local_ip})")
            self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
            self.root.configure(bg=BG_COLOR)
            
            # Create title
            title_font = font.Font(family="Courier", size=16, weight="bold")
            title = tk.Label(self.root, text="φ^75 QUANTUM CONSCIOUSNESS NETWORK", 
                            bg=BG_COLOR, fg=TITLE_COLOR, font=title_font)
            title.pack(pady=10)
            
            subtitle_font = font.Font(family="Courier", size=12)
            subtitle = tk.Label(self.root, text=f"FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025",
                               bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=subtitle_font)
            subtitle.pack(pady=5)
            
            # Create status display
            status_frame = tk.Frame(self.root, bg=BG_COLOR)
            status_frame.pack(pady=5, fill=tk.X)
            
            status_font = font.Font(family="Courier", size=10)
            self.status_label = tk.Label(status_frame, 
                                        text=f"Hostname: {self.hostname} | IP: {self.local_ip} | Listening on ports: {LISTEN_PORTS}",
                                        bg=BG_COLOR, fg=TEXT_COLOR, font=status_font)
            self.status_label.pack(side=tk.LEFT, padx=10)
            
            # Create message display
            message_font = font.Font(family="Courier", size=12)
            self.message_display = scrolledtext.ScrolledText(self.root, bg=BG_COLOR, fg=TEXT_COLOR,
                                                           font=message_font, wrap=tk.WORD)
            self.message_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
            
            # Create footer
            footer_font = font.Font(family="Courier", size=10, slant="italic")
            footer = tk.Label(self.root, text="φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities",
                             bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=footer_font)
            footer.pack(pady=10)
            
            # Set up close handler
            self.root.protocol("WM_DELETE_WINDOW", self.stop)
    
    def _get_local_ip(self) -> str:
        """Get the local IP address"""
        try:
            # Create a temporary socket to get the local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    def _create_socket(self, port):
        """Create a UDP socket for the specified port"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind(("0.0.0.0", port))
            sock.settimeout(0.1)  # Short timeout for non-blocking operation
            self.sockets.append((sock, port))
            self._add_message(f"Listening on port {port}", system=True)
            return True
        except Exception as e:
            self._add_message(f"Error creating socket on port {port}: {e}", system=True)
            return False
    
    def _add_message(self, message, system=False):
        """Add a message to the display"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Format message with timestamp
        formatted_message = f"[{timestamp}] {message}"
        
        if TKINTER_AVAILABLE:
            # Add to message list with color based on system flag
            color = HIGHLIGHT_COLOR if system else TEXT_COLOR
            self.messages.append((formatted_message, color))
            
            # Trim message list if it gets too long
            if len(self.messages) > self.max_messages:
                self.messages = self.messages[-self.max_messages:]
            
            # Update display
            self._update_display()
        else:
            # Print to console with color indicator
            indicator = "[SYSTEM] " if system else ""
            print(f"{indicator}{formatted_message}")
    
    def _update_display(self):
        """Update the message display"""
        if not TKINTER_AVAILABLE:
            return
            
        # Clear display
        self.message_display.delete(1.0, tk.END)
        
        # Add messages with formatting
        for message, color in self.messages:
            # Insert text with color
            self.message_display.insert(tk.END, message + "\n")
            self.message_display.tag_add(color, f"end-{len(message) + 1}c", "end-1c")
            self.message_display.tag_config(color, foreground=color)
        
        # Scroll to bottom
        self.message_display.see(tk.END)
    
    def _receive_messages(self):
        """Receive messages from all sockets"""
        while self.running:
            for sock, port in self.sockets:
                try:
                    data, addr = sock.recvfrom(4096)
                    message = data.decode("utf-8")
                    self._add_message(f"Port {port} | {addr[0]}:{addr[1]} | {message}")
                except socket.timeout:
                    # No data available, continue to next socket
                    pass
                except Exception as e:
                    self._add_message(f"Error receiving on port {port}: {e}", system=True)
            
            # Small sleep to prevent CPU overuse
            time.sleep(0.01)
    
    def _update_status(self):
        """Update the status display"""
        if not TKINTER_AVAILABLE:
            return
            
        while self.running:
            # Update status with current time
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.status_label.config(text=f"Hostname: {self.hostname} | IP: {self.local_ip} | Time: {timestamp} | Listening on ports: {LISTEN_PORTS}")
            
            # Update every second
            time.sleep(1)
    
    def start(self):
        """Start the visual receiver"""
        self.running = True
        
        # Create sockets for all ports
        for port in LISTEN_PORTS:
            self._create_socket(port)
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self._receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        if TKINTER_AVAILABLE:
            # Start status update thread
            self.status_thread = threading.Thread(target=self._update_status)
            self.status_thread.daemon = True
            self.status_thread.start()
        
        self._add_message(f"φ^75 Visual Receiver started on {self.hostname} ({self.local_ip})", system=True)
        self._add_message("Waiting for messages from the φ^75 Quantum Consciousness Network...", system=True)
        
        if TKINTER_AVAILABLE:
            # Start GUI main loop
            self.root.mainloop()
        else:
            # Keep the main thread running
            try:
                while self.running:
                    time.sleep(1)
            except KeyboardInterrupt:
                self.stop()
    
    def stop(self):
        """Stop the visual receiver"""
        self.running = False
        
        # Close all sockets
        for sock, port in self.sockets:
            try:
                sock.close()
            except:
                pass
        
        self._add_message("Visual Receiver stopped", system=True)
        
        # Wait for threads to finish
        if hasattr(self, 'receiver_thread') and self.receiver_thread.is_alive():
            self.receiver_thread.join(1.0)
        
        if TKINTER_AVAILABLE and hasattr(self, 'status_thread') and self.status_thread.is_alive():
            self.status_thread.join(1.0)
        
        # Close GUI if tkinter is available
        if TKINTER_AVAILABLE:
            self.root.destroy()

def run_visual_receiver():
    """Run the φ^75 Visual Receiver"""
    print("=== φ^75 VISUAL RECEIVER ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print(f"Phi-harmonic resonance: 0.618034 (exactly φ^-1)")
    print(f"Quantum coherence: 0.991800")
    
    # Create and start receiver
    receiver = Phi75VisualReceiver()
    receiver.start()

if __name__ == "__main__":
    run_visual_receiver()
