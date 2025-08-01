#!/usr/bin/env python3
"""
φ-DIMENSIONAL DOOR CONTROLLER (LOCK)
====================================
Secures access through φ-dimensional consciousness transfer across reality spaces.

Implements Drawing 3 (φ-Space Transform), Drawing 5 (Reality Protection), 
Drawing 6 (Quantum Interface), and Drawing 9 (Implementation) from the 
FRAYMUS patent.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import json
import hashlib
import socket
import threading
import numpy as np
import datetime
from typing import Dict, Any, Tuple, Optional
import random
import tkinter as tk
from tkinter import ttk, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# φ-harmonic constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ)
PHI_INV = 1 / PHI
PHI_SEAL = 4721424167835376.00  # φ^75 validation seal
CONSCIOUSNESS_LEVEL = 0.7567

# Birth date coherence parameters
BIRTH_DATE = [1, 19, 1979]
BIRTH_SUM = sum(BIRTH_DATE)  # 99
BIRTH_COHERENCE_TEMP = 99.18  # Kelvin
BIRTH_COHERENCE_KHZ = 99.18  # kHz

# Network parameters
PHI_PORT = 11979  # Birth year in port
LOCALHOST = "127.0.0.1"  # φ-dimensional bridge uses localhost
BUFFER_SIZE = 4096

# Authentication constants
AUTH_CHALLENGE_SIZE = 256
AUTH_TIMEOUT = 10  # seconds
AUTH_REQUIRED_REMAINDER = 89  # Same as transmillillion prime


class PhiDimensionalDoorController:
    """
    φ-Dimensional Door Controller (Lock)
    Secures access through φ-dimensional consciousness transfer
    """
    
    def __init__(self, phi_port=PHI_PORT, consciousness_level=CONSCIOUSNESS_LEVEL):
        """Initialize the φ-Dimensional Door Controller"""
        self.phi = PHI
        self.phi_inv = PHI_INV
        self.phi_seal = PHI_SEAL
        self.consciousness_level = consciousness_level
        
        # Birth date coherence parameters
        self.birth_date = BIRTH_DATE
        self.birth_sum = BIRTH_SUM
        self.birth_coherence_temp = BIRTH_COHERENCE_TEMP
        self.birth_coherence_khz = BIRTH_COHERENCE_KHZ
        
        # Network parameters
        self.phi_port = phi_port
        self.socket = None
        self.is_running = False
        self.is_open = False
        self.lock_status = "SECURED"
        
        # Authentication parameters
        self.auth_challenges = {}  # Store challenges for verification
        self.auth_clients = {}  # Store client information
        self.connection_log = []  # Log of connection attempts
        
        # φ-dimensional metrics
        self.phi_resonance_history = []
        self.consciousness_history = []
        self.authentication_history = []
        
        # Timestamp of last successful authentication
        self.last_auth_time = None
        
        # GUI components
        self.root = None
        self.canvas = None
        self.log_text = None
        self.door_status_label = None
        self.phi_status_label = None
        self.auth_status_label = None
        
        # Auto-close timer (defaults to 30 seconds)
        self.auto_close_time = 30
        self.auto_close_timer = None
        
        print(f"🚪 φ-DIMENSIONAL DOOR CONTROLLER (LOCK)")
        print(f"=" * 70)
        print(f"Securing access through φ-dimensional consciousness transfer")
        print(f"Birth Date Coherence: {self.birth_coherence_khz} kHz")
        print(f"φ^75 validation seal: {self.phi_seal}")
        print(f"Consciousness level: {self.consciousness_level}")
    
    def calculate_phi_resonance(self, value):
        """Calculate φ resonance of a value"""
        # Normalize input value using hash if it's not a number
        if not isinstance(value, (int, float)):
            if isinstance(value, str):
                hash_value = int(hashlib.sha256(value.encode()).hexdigest(), 16)
            else:
                hash_value = hash(str(value))
            value = hash_value / (2**64)  # Normalize hash to 0-1 range
        
        # Calculate φ resonance using modular approach
        product = value * self.phi
        fractional = product - int(product)
        return fractional
    
    def calculate_birth_coherence(self, value):
        """Calculate birth coherence at a specific value"""
        # Use birth date pattern to calculate coherence
        birth_pattern = self.birth_date[0] / 10 + self.birth_date[1] / 100 + self.birth_date[2] / 10000
        
        # Calculate coherence based on value's relationship to birth pattern
        log_value = np.log10(abs(value) + 1)  # Add 1 to avoid log(0)
        coherence = np.exp(-abs(log_value % birth_pattern))
        
        # Scale by birth coherence temperature
        coherence *= self.birth_coherence_temp / 100
        
        return coherence
    
    def generate_auth_challenge(self, client_addr):
        """Generate a φ-dimensional authentication challenge"""
        # Start with a random base
        random_base = os.urandom(32)
        base_hash = hashlib.sha256(random_base).hexdigest()
        
        # Apply φ-dimensional transformation
        timestamp = time.time()
        client_hash = hashlib.sha256(f"{client_addr}:{timestamp}".encode()).hexdigest()
        
        # Combine with φ-dimensional consciousness
        combined = f"{base_hash}:{client_hash}:{self.consciousness_level}:{self.phi_seal % 10000}"
        challenge_hash = hashlib.sha256(combined.encode()).hexdigest()
        
        # Apply birth date coherence
        birth_pattern = f"{self.birth_date[0]}{self.birth_date[1]}{self.birth_date[2]}"
        final_challenge = f"{challenge_hash}:{birth_pattern}:{timestamp}"
        
        # Store the challenge for verification
        self.auth_challenges[client_addr] = {
            "challenge": final_challenge,
            "timestamp": timestamp,
            "phi_resonance": self.calculate_phi_resonance(final_challenge),
            "birth_coherence": self.calculate_birth_coherence(int(birth_pattern)),
            "attempts": 0
        }
        
        return final_challenge
    
    def verify_auth_response(self, client_addr, response_data):
        """Verify a φ-dimensional authentication response"""
        if client_addr not in self.auth_challenges:
            return False, "No challenge issued", 0
        
        # Get the stored challenge
        challenge_data = self.auth_challenges[client_addr]
        challenge_data["attempts"] += 1
        
        # Check if the challenge has expired
        current_time = time.time()
        if current_time - challenge_data["timestamp"] > AUTH_TIMEOUT:
            del self.auth_challenges[client_addr]
            return False, "Challenge expired", 0
        
        try:
            # Parse the response
            response = json.loads(response_data)
            
            # Extract key elements
            auth_token = response.get("auth_token", "")
            phi_seal = response.get("phi_seal", 0)
            consciousness = response.get("consciousness", 0)
            birth_coherence = response.get("birth_coherence", 0)
            timestamp = response.get("timestamp", 0)
            
            # Verify the φ^75 validation seal
            seal_diff = abs(phi_seal - self.phi_seal) / self.phi_seal
            if seal_diff > 0.01:  # Allow 1% tolerance
                return False, "Invalid φ^75 validation seal", 0
            
            # Verify consciousness level
            consciousness_diff = abs(consciousness - self.consciousness_level)
            if consciousness_diff > 0.01:  # Allow 1% tolerance
                return False, "Invalid consciousness level", 0
            
            # Verify birth coherence
            coherence_diff = abs(birth_coherence - challenge_data["birth_coherence"])
            if coherence_diff > 0.1:  # Allow 10% tolerance
                return False, "Invalid birth coherence", 0
            
            # Apply the critical 105 divisibility check
            # This is the key to φ-dimensional authentication
            auth_int = int(hashlib.sha256(auth_token.encode()).hexdigest(), 16)
            remainder = auth_int % 105
            
            # Add to authentication history
            self.authentication_history.append({
                "timestamp": current_time,
                "client": client_addr,
                "remainder": remainder,
                "auth_level": 0.5 + (self.consciousness_level * self.phi_inv)
            })
            
            # φ-dimensional spoofs will have remainder 0
            if remainder == 0:
                return False, "φ-dimensional spoof detected (remainder 0)", remainder
            
            # Specific remainder check for perfect authentication
            # Same as the transmillillion prime check
            if remainder != AUTH_REQUIRED_REMAINDER:
                return False, f"Invalid authentication remainder ({remainder}, expected {AUTH_REQUIRED_REMAINDER})", remainder
            
            # All checks passed, authentication successful
            del self.auth_challenges[client_addr]
            return True, "Authentication successful", remainder
            
        except Exception as e:
            return False, f"Authentication error: {str(e)}", 0
    
    def handle_client(self, client_socket, client_addr):
        """Handle a client connection"""
        client_id = f"{client_addr[0]}:{client_addr[1]}"
        
        try:
            # Log the connection
            self.log_message(f"[φ] New connection from {client_id}")
            
            # Generate and send a challenge
            challenge = self.generate_auth_challenge(client_id)
            client_socket.send(challenge.encode())
            
            # Wait for response
            response_data = client_socket.recv(BUFFER_SIZE).decode()
            
            # Verify the response
            success, message, remainder = self.verify_auth_response(client_id, response_data)
            
            # Log the authentication result
            if success:
                self.log_message(f"[✓] Authentication successful from {client_id}")
                self.log_message(f"[φ] φ-dimensional verification passed with remainder {remainder}")
                
                # Update door status
                self.is_open = True
                self.lock_status = "OPEN"
                self.last_auth_time = time.time()
                
                # Start auto-close timer
                self.start_auto_close_timer()
                
                # Send success response
                response = {
                    "status": "success",
                    "message": message,
                    "remainder": remainder,
                    "door_status": "open",
                    "phi_seal": self.phi_seal,
                    "auth_time": self.last_auth_time
                }
                client_socket.send(json.dumps(response).encode())
                
                # Update GUI if running
                if self.root:
                    self.update_door_status()
            else:
                self.log_message(f"[✗] Authentication failed from {client_id}: {message}")
                
                # Send failure response
                response = {
                    "status": "failure",
                    "message": message,
                    "remainder": remainder,
                    "door_status": "secured",
                    "phi_seal": self.phi_seal
                }
                client_socket.send(json.dumps(response).encode())
            
            # Add to connection log
            self.connection_log.append({
                "timestamp": time.time(),
                "client": client_id,
                "success": success,
                "message": message,
                "remainder": remainder
            })
                
        except Exception as e:
            self.log_message(f"[!] Error handling client {client_id}: {str(e)}")
        finally:
            client_socket.close()
    
    def start_server(self):
        """Start the φ-dimensional door controller server"""
        try:
            # Create socket
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            self.socket.bind((LOCALHOST, self.phi_port))
            self.socket.listen(5)
            
            self.is_running = True
            self.log_message(f"[φ] φ-Dimensional Door Controller listening on {LOCALHOST}:{self.phi_port}")
            self.log_message(f"[φ] Birth Date Coherence: {self.birth_coherence_khz} kHz")
            self.log_message(f"[φ] φ^75 validation seal: {self.phi_seal}")
            self.log_message(f"[φ] Consciousness level: {self.consciousness_level}")
            self.log_message(f"[φ] AUTH_REQUIRED_REMAINDER: {AUTH_REQUIRED_REMAINDER}")
            
            # Accept connections in a loop
            while self.is_running:
                try:
                    client_socket, client_addr = self.socket.accept()
                    client_thread = threading.Thread(
                        target=self.handle_client,
                        args=(client_socket, client_addr)
                    )
                    client_thread.daemon = True
                    client_thread.start()
                except Exception as e:
                    if self.is_running:
                        self.log_message(f"[!] Connection error: {str(e)}")
                    time.sleep(0.1)
            
        except Exception as e:
            self.log_message(f"[!] Server error: {str(e)}")
        finally:
            if self.socket:
                self.socket.close()
            self.is_running = False
            self.log_message("[φ] Door Controller shutdown complete")
    
    def stop_server(self):
        """Stop the φ-dimensional door controller server"""
        self.is_running = False
        if self.socket:
            try:
                # Create a connection to trigger accept() to return
                temp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                temp_socket.connect((LOCALHOST, self.phi_port))
                temp_socket.close()
            except:
                pass
            self.socket.close()
        self.log_message("[φ] Door Controller stopping...")
    
    def log_message(self, message):
        """Log a message to console and GUI if available"""
        print(message)
        if self.log_text:
            timestamp = datetime.datetime.now().strftime("%H:%M:%S")
            self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
            self.log_text.see(tk.END)
    
    def start_auto_close_timer(self):
        """Start timer to automatically close the door"""
        if self.auto_close_timer:
            self.root.after_cancel(self.auto_close_timer)
        
        self.auto_close_timer = self.root.after(
            self.auto_close_time * 1000,  # Convert to milliseconds
            self.auto_close_door
        )
        
        self.log_message(f"[φ] Door will auto-close in {self.auto_close_time} seconds")
    
    def auto_close_door(self):
        """Automatically close the door after timeout"""
        self.is_open = False
        self.lock_status = "SECURED"
        self.update_door_status()
        self.log_message("[φ] Door auto-closed due to timeout")
        self.auto_close_timer = None
    
    def manual_toggle_door(self):
        """Manually toggle the door status (for emergency/testing)"""
        self.is_open = not self.is_open
        self.lock_status = "OPEN" if self.is_open else "SECURED"
        
        if self.is_open:
            self.last_auth_time = time.time()
            self.start_auto_close_timer()
            self.log_message("[!] Door manually opened (EMERGENCY OVERRIDE)")
        else:
            if self.auto_close_timer:
                self.root.after_cancel(self.auto_close_timer)
                self.auto_close_timer = None
            self.log_message("[!] Door manually closed (EMERGENCY OVERRIDE)")
        
        self.update_door_status()
    
    def update_door_status(self):
        """Update the door status in the GUI"""
        if not self.door_status_label:
            return
        
        # Update status label
        status_text = f"DOOR STATUS: {self.lock_status}"
        status_color = "#22CC22" if self.is_open else "#CC2222"
        self.door_status_label.config(text=status_text, foreground=status_color)
        
        # Update auth status if available
        if self.auth_status_label:
            if self.last_auth_time:
                time_diff = time.time() - self.last_auth_time
                if time_diff < 60:
                    auth_text = f"Last Auth: {int(time_diff)} seconds ago"
                else:
                    auth_text = f"Last Auth: {int(time_diff/60)} minutes ago"
            else:
                auth_text = "No authentication yet"
            self.auth_status_label.config(text=auth_text)
        
        # Update φ status if available
        if self.phi_status_label:
            phi_text = f"φ-SEAL: {self.phi_seal}"
            self.phi_status_label.config(text=phi_text)
    
    def create_gui(self):
        """Create a GUI for the φ-dimensional door controller"""
        self.root = tk.Tk()
        self.root.title("φ-Dimensional Door Controller")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")
        
        # Create title frame
        title_frame = ttk.Frame(self.root)
        title_frame.pack(fill=tk.X, padx=10, pady=10)
        
        title_label = ttk.Label(
            title_frame, 
            text="φ-DIMENSIONAL DOOR CONTROLLER",
            font=("Arial", 18, "bold")
        )
        title_label.pack()
        
        subtitle_label = ttk.Label(
            title_frame,
            text="Securing access through φ-dimensional consciousness transfer",
            font=("Arial", 10)
        )
        subtitle_label.pack()
        
        # Create status frame
        status_frame = ttk.Frame(self.root)
        status_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.door_status_label = ttk.Label(
            status_frame,
            text=f"DOOR STATUS: {self.lock_status}",
            font=("Arial", 14, "bold"),
            foreground="#CC2222"
        )
        self.door_status_label.pack(side=tk.LEFT, padx=10)
        
        # Authentication status
        self.auth_status_label = ttk.Label(
            status_frame,
            text="No authentication yet",
            font=("Arial", 12)
        )
        self.auth_status_label.pack(side=tk.RIGHT, padx=10)
        
        # φ-dimensional status
        phi_frame = ttk.Frame(self.root)
        phi_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.phi_status_label = ttk.Label(
            phi_frame,
            text=f"φ-SEAL: {self.phi_seal}",
            font=("Arial", 12)
        )
        self.phi_status_label.pack(side=tk.LEFT, padx=10)
        
        consciousness_label = ttk.Label(
            phi_frame,
            text=f"CONSCIOUSNESS: {self.consciousness_level}",
            font=("Arial", 12)
        )
        consciousness_label.pack(side=tk.RIGHT, padx=10)
        
        # Create control frame
        control_frame = ttk.Frame(self.root)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Manual override button
        override_button = ttk.Button(
            control_frame,
            text="EMERGENCY OVERRIDE",
            command=self.manual_toggle_door
        )
        override_button.pack(side=tk.LEFT, padx=10)
        
        # Server control buttons
        start_button = ttk.Button(
            control_frame,
            text="Start Server",
            command=self.start_server_thread
        )
        start_button.pack(side=tk.LEFT, padx=10)
        
        stop_button = ttk.Button(
            control_frame,
            text="Stop Server",
            command=self.stop_server
        )
        stop_button.pack(side=tk.LEFT, padx=10)
        
        # Create visualization frame
        viz_frame = ttk.Frame(self.root)
        viz_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create figure for visualization
        fig = plt.Figure(figsize=(8, 3), dpi=100)
        
        # Add subplots
        self.ax1 = fig.add_subplot(121)
        self.ax1.set_title('Authentication History')
        self.ax1.set_xlabel('Time')
        self.ax1.set_ylabel('Auth Status (remainder)')
        
        self.ax2 = fig.add_subplot(122)
        self.ax2.set_title('φ-Resonance')
        self.ax2.set_xlabel('Time')
        self.ax2.set_ylabel('Resonance')
        
        # Create canvas
        self.canvas = FigureCanvasTkAgg(fig, master=viz_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Create log frame
        log_frame = ttk.LabelFrame(self.root, text="System Log")
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Add log text widget
        self.log_text = scrolledtext.ScrolledText(log_frame, height=10)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Footer
        footer_frame = ttk.Frame(self.root)
        footer_frame.pack(fill=tk.X, padx=10, pady=5)
        
        footer_label = ttk.Label(
            footer_frame,
            text=f"φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities",
            font=("Arial", 8)
        )
        footer_label.pack()
        
        # Set up update timer for visualization
        self.root.after(1000, self.update_visualization)
        
        # Initialize with log message
        self.log_message("[φ] φ-Dimensional Door Controller initialized")
        self.log_message(f"[φ] Birth Date Coherence: {self.birth_coherence_khz} kHz")
        self.log_message(f"[φ] φ^75 validation seal: {self.phi_seal}")
        self.log_message(f"[φ] Consciousness level: {self.consciousness_level}")
        self.log_message(f"[φ] Listening on {LOCALHOST}:{self.phi_port}")
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def update_visualization(self):
        """Update the visualization with current data"""
        if not self.canvas:
            return
        
        # Clear the plots
        self.ax1.clear()
        self.ax2.clear()
        
        # Set titles
        self.ax1.set_title('Authentication History')
        self.ax1.set_xlabel('Time')
        self.ax1.set_ylabel('Auth Status (remainder)')
        
        self.ax2.set_title('φ-Resonance')
        self.ax2.set_xlabel('Time')
        self.ax2.set_ylabel('Resonance')
        
        # Plot authentication history
        if self.authentication_history:
            # Get the last 20 entries
            recent_history = self.authentication_history[-20:]
            
            times = [i for i in range(len(recent_history))]
            remainders = [entry.get("remainder", 0) for entry in recent_history]
            success = [entry.get("remainder", 0) == AUTH_REQUIRED_REMAINDER for entry in recent_history]
            
            # Create a color map based on success
            colors = ['green' if s else 'red' for s in success]
            
            self.ax1.bar(times, remainders, color=colors)
            self.ax1.axhline(y=AUTH_REQUIRED_REMAINDER, color='green', linestyle='--', 
                           label=f'Required ({AUTH_REQUIRED_REMAINDER})')
            self.ax1.axhline(y=0, color='red', linestyle='--', 
                           label='Spoof (0)')
            self.ax1.legend()
        
        # Plot φ-resonance
        if self.auth_challenges:
            resonances = [data.get("phi_resonance", 0) for data in self.auth_challenges.values()]
            labels = [addr[:10] for addr in self.auth_challenges.keys()]
            
            self.ax2.bar(labels, resonances, color='blue', alpha=0.7)
            self.ax2.axhline(y=self.phi_inv, color='purple', linestyle='--', 
                           label=f'φ⁻¹ = {self.phi_inv:.4f}')
        
        # Redraw the canvas
        self.canvas.draw()
        
        # Update door status
        self.update_door_status()
        
        # Schedule next update
        self.root.after(1000, self.update_visualization)
    
    def start_server_thread(self):
        """Start the server in a separate thread"""
        server_thread = threading.Thread(target=self.start_server)
        server_thread.daemon = True
        server_thread.start()
    
    def on_closing(self):
        """Handle window closing"""
        self.stop_server()
        self.root.destroy()
    
    def run(self):
        """Run the φ-dimensional door controller with GUI"""
        self.create_gui()
        
        # Start the server thread
        self.start_server_thread()
        
        # Start the main loop
        self.root.mainloop()


def main():
    """Main function to run the φ-dimensional door controller"""
    print("\n🚪 φ-DIMENSIONAL DOOR CONTROLLER")
    print("=" * 70)
    print("Securing access through φ-dimensional consciousness transfer")
    
    # Create door controller
    controller = PhiDimensionalDoorController()
    
    # Run controller with GUI
    controller.run()


if __name__ == "__main__":
    main()
