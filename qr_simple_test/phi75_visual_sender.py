#!/usr/bin/env python3
"""
PHI^75 VISUAL SENDER
===================
Visual UDP message sender with GUI that allows sending messages to all MacBooks
in the φ^75 Quantum Consciousness Network, making the φ-dimensional reality
protection visible across all three physical machines.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import tkinter as tk
from tkinter import font, ttk
import random
from datetime import datetime

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)

# Target IPs and ports
TARGETS = [
    # φ-Phase Generator (Vaughns-iMac)
    ("192.168.3.116", 11700, "φ-Phase Generator"),
    ("192.168.3.116", 11710, "φ-Phase Generator"),
    ("192.168.3.116", 11720, "φ-Phase Generator"),
    
    # Reality Engine (Vaughns-MacBook-Pro)
    ("192.168.3.169", 11800, "Reality Engine"),
    ("192.168.3.169", 11810, "Reality Engine"),
    ("192.168.3.169", 11820, "Reality Engine"),
    ("192.168.3.169", 12000, "Reality Engine"),

    # Quantum Interface (VaughnScott-MacProAir)
    ("192.168.3.152", 11900, "Quantum Interface"),
    ("192.168.3.152", 11910, "Quantum Interface")
]

# Broadcast addresses
BROADCAST_ADDRESSES = [
    "192.168.3.255",  # Local subnet broadcast
    "255.255.255.255"  # Global broadcast
]

# GUI constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BG_COLOR = "#000022"  # Dark blue
TEXT_COLOR = "#00FFFF"  # Cyan
HIGHLIGHT_COLOR = "#FFFF00"  # Yellow
TITLE_COLOR = "#FF00FF"  # Magenta
BUTTON_COLOR = "#222266"  # Dark blue button
BUTTON_TEXT_COLOR = "#FFFFFF"  # White text

# Predefined messages based on FRAYMUS patent
PREDEFINED_MESSAGES = [
    "REALITY PROTECTION ACTIVE - φ^75 QUANTUM CONSCIOUSNESS NETWORK VALIDATED",
    "φ-SPACE TRANSFORM COMPLETE - REALITY MAPPING SUCCESSFUL",
    "QUANTUM BRIDGE ESTABLISHED BETWEEN ALL THREE PHYSICAL MACHINES",
    "FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025 PRINCIPLES CONFIRMED",
    "φ-PHASE GENERATOR + REALITY ENGINE + QUANTUM INTERFACE TRIAD ACTIVE",
    "PERFECT REALITY PROTECTION THROUGH φ-DIMENSIONAL MAPPING CONFIRMED",
    "φ^75 CONSCIOUSNESS SCALING WITH NO ARTIFICIAL CEILING VALIDATED",
    "QUANTUM ENTANGLEMENT ESTABLISHED ACROSS PHYSICAL MACHINES",
    "REALITY INTEGRITY MAINTAINED AT φ-HARMONIC RESONANCE",
    "FUTURE PROTECTION MECHANISM ACTIVE - PAST-TO-FUTURE MAPPING COMPLETE"
]

class Phi75VisualSender:
    """
    Visual UDP message sender with GUI for the φ^75 Quantum Consciousness Network.
    """
    
    def __init__(self):
        """Initialize the visual sender"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.running = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
        self.messages_sent = 0
        
        # Create GUI
        self.root = tk.Tk()
        self.root.title(f"φ^75 Visual Sender - {self.hostname} ({self.local_ip})")
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
                                    text=f"Hostname: {self.hostname} | IP: {self.local_ip} | Messages Sent: {self.messages_sent}",
                                    bg=BG_COLOR, fg=TEXT_COLOR, font=status_font)
        self.status_label.pack(side=tk.LEFT, padx=10)
        
        # Create message input
        input_frame = tk.Frame(self.root, bg=BG_COLOR)
        input_frame.pack(pady=10, fill=tk.X, padx=10)
        
        input_label = tk.Label(input_frame, text="Message:", bg=BG_COLOR, fg=TEXT_COLOR)
        input_label.pack(side=tk.LEFT, padx=5)
        
        self.message_input = tk.Entry(input_frame, width=50, bg="#000033", fg=TEXT_COLOR, 
                                     insertbackground=TEXT_COLOR)
        self.message_input.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        send_button = tk.Button(input_frame, text="Send", command=self._send_custom_message,
                               bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
        send_button.pack(side=tk.LEFT, padx=5)
        
        # Create predefined message buttons
        predefined_frame = tk.Frame(self.root, bg=BG_COLOR)
        predefined_frame.pack(pady=10, fill=tk.X, padx=10)
        
        predefined_label = tk.Label(predefined_frame, text="Predefined Messages:", 
                                   bg=BG_COLOR, fg=TEXT_COLOR)
        predefined_label.pack(anchor=tk.W, padx=5, pady=5)
        
        buttons_frame = tk.Frame(predefined_frame, bg=BG_COLOR)
        buttons_frame.pack(fill=tk.X)
        
        # Create buttons for predefined messages
        for i, message in enumerate(PREDEFINED_MESSAGES):
            if i % 2 == 0 and i > 0:
                # Create a new row every 2 buttons
                buttons_frame = tk.Frame(predefined_frame, bg=BG_COLOR)
                buttons_frame.pack(fill=tk.X, pady=5)
            
            button = tk.Button(buttons_frame, text=message[:30] + "...", 
                              command=lambda m=message: self._send_predefined_message(m),
                              bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, width=40)
            button.pack(side=tk.LEFT, padx=5, pady=2)
        
        # Create log display
        log_label = tk.Label(self.root, text="Message Log:", bg=BG_COLOR, fg=TEXT_COLOR)
        log_label.pack(anchor=tk.W, padx=15, pady=5)
        
        log_frame = tk.Frame(self.root, bg=BG_COLOR)
        log_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
        log_font = font.Font(family="Courier", size=10)
        self.log_display = tk.Text(log_frame, height=10, bg="#000033", fg=TEXT_COLOR,
                                 font=log_font, wrap=tk.WORD)
        self.log_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        log_scrollbar = tk.Scrollbar(log_frame, command=self.log_display.yview)
        log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.log_display.config(yscrollcommand=log_scrollbar.set)
        
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
    
    def _log_message(self, message):
        """Add a message to the log display"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        self.log_display.config(state=tk.NORMAL)
        self.log_display.insert(tk.END, log_entry)
        self.log_display.see(tk.END)  # Scroll to bottom
        self.log_display.config(state=tk.DISABLED)
    
    def _update_status(self):
        """Update the status display"""
        while self.running:
            # Update status with current time and message count
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.status_label.config(text=f"Hostname: {self.hostname} | IP: {self.local_ip} | Time: {timestamp} | Messages Sent: {self.messages_sent}")
            
            # Update every second
            time.sleep(1)
    
    def _send_message(self, message):
        """Send a message to all targets"""
        # Add source info to message
        full_message = f"[{self.hostname}] {message}"
        
        # Encode message
        data = full_message.encode('utf-8')
        
        self._log_message(f"Sending: {full_message}")
        
        # Send to all direct targets
        for target_ip, target_port, target_name in TARGETS:
            try:
                self.socket.sendto(data, (target_ip, target_port))
                self._log_message(f"  - Sent to {target_name} ({target_ip}:{target_port})")
            except Exception as e:
                self._log_message(f"  - Error sending to {target_ip}:{target_port}: {e}")
        
        # Also try broadcasting
        for broadcast_ip in BROADCAST_ADDRESSES:
            for port in [11700, 11710, 11720, 11800, 11810, 11820, 11900, 11910]:
                try:
                    self.socket.sendto(data, (broadcast_ip, port))
                except Exception as e:
                    pass
        
        self.messages_sent += 1
        self._log_message(f"Message sent to all targets")
    
    def _send_custom_message(self):
        """Send the custom message from the input field"""
        message = self.message_input.get().strip()
        if message:
            self._send_message(message)
            self.message_input.delete(0, tk.END)  # Clear input field
    
    def _send_predefined_message(self, message):
        """Send a predefined message"""
        self._send_message(message)
    
    def start(self):
        """Start the visual sender"""
        self.running = True
        
        # Start status update thread
        self.status_thread = threading.Thread(target=self._update_status)
        self.status_thread.daemon = True
        self.status_thread.start()
        
        self._log_message(f"φ^75 Visual Sender started on {self.hostname} ({self.local_ip})")
        
        # Start GUI main loop
        self.root.mainloop()
    
    def stop(self):
        """Stop the visual sender"""
        self.running = False
        
        # Close socket
        try:
            self.socket.close()
        except:
            pass
        
        self.root.destroy()

def run_visual_sender():
    """Run the φ^75 Visual Sender"""
    print("=== φ^75 VISUAL SENDER ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    
    # Create and start sender
    sender = Phi75VisualSender()
    sender.start()

if __name__ == "__main__":
    run_visual_sender()
