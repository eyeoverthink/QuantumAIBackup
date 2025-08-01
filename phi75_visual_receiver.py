#!/usr/bin/env python3
"""
PHI^75 VISUAL RECEIVER
=====================
Visual UDP message receiver that displays incoming messages in a GUI window,
making the φ-dimensional reality protection visible across all three MacBooks.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import tkinter as tk
from tkinter import scrolledtext, font
import random
from datetime import datetime

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
LISTEN_PORTS = [11700, 11710, 11720, 11800, 11810, 11820, 11900, 11910]
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BG_COLOR = "#000000"  # Black
TEXT_COLOR = "#00FF00"  # Green
HIGHLIGHT_COLOR = "#FFFF00"  # Yellow
TITLE_COLOR = "#FF00FF"  # Magenta

class Phi75VisualReceiver:
    """
    Visual UDP message receiver that displays incoming messages in a GUI window.
    """
    
    def __init__(self):
        """Initialize the visual receiver"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.running = False
        self.sockets = []
        self.messages = []
        self.max_messages = 100
        
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
            # Create a temporary socket to determine local IP
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
            sock.settimeout(0.5)  # Set timeout for non-blocking operation
            self.sockets.append((sock, port))
            self._add_message(f"Socket created on port {port}", system=True)
        except Exception as e:
            self._add_message(f"Error creating socket on port {port}: {e}", system=True, error=True)
    
    def _add_message(self, message, system=False, error=False):
        """Add a message to the display"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        if system:
            if error:
                prefix = f"[SYSTEM ERROR {timestamp}] "
                color = "#FF0000"  # Red
            else:
                prefix = f"[SYSTEM {timestamp}] "
                color = "#AAAAAA"  # Gray
        else:
            prefix = f"[{timestamp}] "
            color = TEXT_COLOR
        
        full_message = f"{prefix}{message}\n"
        self.messages.append((full_message, color))
        
        # Limit number of messages
        if len(self.messages) > self.max_messages:
            self.messages.pop(0)
        
        # Update display
        self._update_display()
    
    def _update_display(self):
        """Update the message display"""
        self.message_display.config(state=tk.NORMAL)
        self.message_display.delete(1.0, tk.END)
        
        for message, color in self.messages:
            self.message_display.insert(tk.END, message)
            # Get the line number of the inserted text
            line_start = self.message_display.index(f"end-1c linestart")
            line_end = self.message_display.index(f"end-1c")
            self.message_display.tag_add(f"color_{color}", line_start, line_end)
            self.message_display.tag_config(f"color_{color}", foreground=color)
        
        self.message_display.config(state=tk.DISABLED)
        self.message_display.see(tk.END)  # Scroll to bottom
    
    def _receive_messages(self):
        """Receive messages from all sockets"""
        while self.running:
            for sock, port in self.sockets:
                try:
                    data, addr = sock.recvfrom(4096)
                    message = data.decode('utf-8')
                    self._add_message(f"[Port {port}] {message}")
                except socket.timeout:
                    # No message received, continue
                    pass
                except Exception as e:
                    self._add_message(f"Error receiving on port {port}: {e}", system=True, error=True)
            
            # Small delay to prevent CPU hogging
            time.sleep(0.01)
    
    def _update_status(self):
        """Update the status display"""
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
        
        # Start status update thread
        self.status_thread = threading.Thread(target=self._update_status)
        self.status_thread.daemon = True
        self.status_thread.start()
        
        self._add_message(f"φ^75 Visual Receiver started on {self.hostname} ({self.local_ip})", system=True)
        self._add_message("Waiting for messages from the φ^75 Quantum Consciousness Network...", system=True)
        
        # Start GUI main loop
        self.root.mainloop()
    
    def stop(self):
        """Stop the visual receiver"""
        self.running = False
        
        # Close all sockets
        for sock, port in self.sockets:
            try:
                sock.close()
            except:
                pass
        
        self.root.destroy()

def run_visual_receiver():
    """Run the φ^75 Visual Receiver"""
    print("=== φ^75 VISUAL RECEIVER ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    
    # Create and start receiver
    receiver = Phi75VisualReceiver()
    receiver.start()

if __name__ == "__main__":
    run_visual_receiver()
