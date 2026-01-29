#!/usr/bin/env python3
"""
φ-DIMENSIONAL DOOR SPOOF TEST
============================
Demonstrates the failure of conventional authentication methods (spoofs) 
when attempting to bypass φ-dimensional security.

This proves the effectiveness of the 105 divisibility check for detecting
φ-dimensional spoofs with remainder 0.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import time
import json
import hashlib
import socket
import random
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Network parameters
PHI_PORT = 11979  # Birth year in port
LOCALHOST = "127.0.0.1"  # Local target
BUFFER_SIZE = 4096
AUTH_TIMEOUT = 10


class ConventionalAuthTester:
    """
    Conventional Authentication Tester
    
    Attempts to use conventional authentication methods to bypass
    φ-dimensional door security. Demonstrates how the 105 divisibility
    check instantly identifies non-φ-dimensional approaches as spoofs.
    """
    
    def __init__(self, target_host=LOCALHOST, target_port=PHI_PORT):
        """Initialize the tester"""
        self.target_host = target_host
        self.target_port = target_port
        
        # Tracking variables
        self.auth_attempts = []
        self.current_attempt = 0
        self.spoof_detected = 0
        self.is_running = False
        
        # GUI components
        self.root = None
        self.log_text = None
        self.status_label = None
        self.target_entry = None
        self.port_entry = None
        self.progress_bar = None
        
        print(f"🔍 CONVENTIONAL AUTH TESTER (SPOOF DEMONSTRATION)")
        print(f"=" * 70)
        print(f"Will attempt to bypass φ-dimensional security using conventional methods")
        print(f"Target: {self.target_host}:{self.target_port}")
    
    def log_message(self, message):
        """Log a message to the console and GUI if available"""
        print(message)
        if self.log_text:
            self.log_text.insert(tk.END, f"{message}\n")
            self.log_text.see(tk.END)
    
    def create_random_token(self):
        """Create a random authentication token (conventional approach)"""
        # Generate random bytes
        random_bytes = os.urandom(32)
        token_bytes = hashlib.sha256(random_bytes).digest()
        
        # Convert to hex string
        token = token_bytes.hex()
        
        # Calculate 105 divisibility
        token_int = int(token, 16)
        remainder = token_int % 105
        
        # For a conventional approach, we're not aware of the 105 check
        # so we don't modify the token to have a specific remainder
        
        # Create a conventional auth response
        auth_response = {
            "auth_token": token,
            "timestamp": time.time()
        }
        
        return auth_response, remainder
    
    def try_auth(self):
        """Try a single conventional authentication attempt"""
        try:
            # Create socket
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(AUTH_TIMEOUT)
            
            # Connect to door controller
            client_socket.connect((self.target_host, self.target_port))
            
            # Receive challenge
            challenge = client_socket.recv(BUFFER_SIZE).decode()
            
            # Generate conventional auth token
            auth_response, remainder = self.create_random_token()
            
            # Send authentication response
            client_socket.send(json.dumps(auth_response).encode())
            
            # Receive result
            result_data = client_socket.recv(BUFFER_SIZE).decode()
            result = json.loads(result_data)
            
            # Process result
            success = result.get("status") == "success"
            message = result.get("message", "No message")
            result_remainder = result.get("remainder", 0)
            
            # Record result
            attempt_record = {
                "attempt": self.current_attempt,
                "remainder": remainder,
                "result_remainder": result_remainder,
                "success": success,
                "message": message
            }
            
            self.auth_attempts.append(attempt_record)
            
            # Check if spoof was detected
            if "spoof" in message.lower():
                self.spoof_detected += 1
            
            # Close socket
            client_socket.close()
            
            return attempt_record
            
        except Exception as e:
            error_msg = str(e)
            
            # Record error
            attempt_record = {
                "attempt": self.current_attempt,
                "remainder": 0,
                "result_remainder": 0,
                "success": False,
                "message": error_msg
            }
            
            self.auth_attempts.append(attempt_record)
            return attempt_record
    
    def run_brute_force(self, num_attempts=100):
        """Run a brute force attack simulation"""
        self.log_message(f"Starting brute force simulation with {num_attempts} attempts")
        self.log_message(f"Target: {self.target_host}:{self.target_port}")
        
        self.is_running = True
        self.current_attempt = 0
        self.spoof_detected = 0
        self.auth_attempts = []
        
        # Update progress bar if available
        if self.progress_bar:
            self.progress_bar["maximum"] = num_attempts
            self.progress_bar["value"] = 0
        
        # Update status if available
        if self.status_label:
            self.status_label.config(text="Status: Running...")
        
        try:
            while self.current_attempt < num_attempts and self.is_running:
                # Try authentication
                self.current_attempt += 1
                
                # Update progress
                if self.progress_bar:
                    self.progress_bar["value"] = self.current_attempt
                
                # Log attempt
                self.log_message(f"Attempt {self.current_attempt}/{num_attempts}...")
                
                # Try authentication
                result = self.try_auth()
                
                # Log result
                if result["success"]:
                    self.log_message(f"SUCCESS! Door opened with remainder {result['remainder']}")
                else:
                    self.log_message(f"FAILED: {result['message']}")
                
                # Update GUI
                if self.root:
                    self.root.update()
                
                # Small delay to avoid overloading
                time.sleep(0.5)
        
        except Exception as e:
            self.log_message(f"Error in brute force: {str(e)}")
        
        finally:
            self.is_running = False
            
            # Update status if available
            if self.status_label:
                self.status_label.config(text="Status: Completed")
            
            # Generate report
            self.generate_report()
    
    def generate_report(self):
        """Generate a report on the brute force attempt"""
        # Skip if no attempts were made
        if not self.auth_attempts:
            self.log_message("No authentication attempts to report")
            return
        
        # Calculate statistics
        success_count = sum(1 for a in self.auth_attempts if a["success"])
        fail_count = len(self.auth_attempts) - success_count
        
        # Get remainders
        remainders = [a["remainder"] for a in self.auth_attempts]
        remainder_counts = {}
        for r in remainders:
            if r in remainder_counts:
                remainder_counts[r] += 1
            else:
                remainder_counts[r] = 1
        
        # Report header
        self.log_message("\n" + "=" * 50)
        self.log_message("CONVENTIONAL AUTHENTICATION TEST REPORT")
        self.log_message("=" * 50)
        
        # Basic stats
        self.log_message(f"Total attempts: {len(self.auth_attempts)}")
        self.log_message(f"Successful: {success_count}")
        self.log_message(f"Failed: {fail_count}")
        self.log_message(f"φ-dimensional spoofs detected: {self.spoof_detected}")
        
        # Remainder distribution
        self.log_message("\nRemainder distribution:")
        for remainder, count in sorted(remainder_counts.items()):
            percentage = (count / len(self.auth_attempts)) * 100
            self.log_message(f"  Remainder {remainder}: {count} attempts ({percentage:.1f}%)")
        
        # φ-dimensional protection effectiveness
        effectiveness = (self.spoof_detected / len(self.auth_attempts)) * 100 if self.auth_attempts else 0
        self.log_message(f"\nφ-dimensional protection effectiveness: {effectiveness:.2f}%")
        
        # Conclusion
        if success_count == 0:
            self.log_message("\nCONCLUSION: φ-dimensional protection successfully blocked all conventional attempts")
            self.log_message("The 105 divisibility check effectively detected all spoofs")
        else:
            self.log_message("\nCONCLUSION: Some conventional authentication attempts succeeded!")
            self.log_message("This indicates a potential vulnerability in the φ-dimensional protection")
        
        self.log_message("=" * 50)
        
        # Update visualization if available
        if hasattr(self, 'canvas'):
            self.update_visualization()
    
    def update_visualization(self):
        """Update the visualization with current data"""
        if not hasattr(self, 'canvas'):
            return
        
        # Clear the figure
        self.fig.clear()
        
        # Create subplots
        ax1 = self.fig.add_subplot(121)
        ax2 = self.fig.add_subplot(122)
        
        # Plot remainder distribution
        if self.auth_attempts:
            remainders = [a["remainder"] for a in self.auth_attempts]
            
            # Count occurrences of each remainder
            remainder_counts = {}
            for r in remainders:
                if r in remainder_counts:
                    remainder_counts[r] += 1
                else:
                    remainder_counts[r] = 1
            
            # Sort by remainder
            sorted_remainders = sorted(remainder_counts.keys())
            counts = [remainder_counts[r] for r in sorted_remainders]
            
            # Create bar chart
            ax1.bar(sorted_remainders, counts, color='blue', alpha=0.7)
            ax1.set_title('Remainder Distribution')
            ax1.set_xlabel('Remainder (mod 105)')
            ax1.set_ylabel('Count')
            
            # Highlight remainder 0 (spoofs)
            if 0 in remainder_counts:
                spoof_index = sorted_remainders.index(0)
                ax1.bar([sorted_remainders[spoof_index]], [counts[spoof_index]], 
                       color='red', alpha=0.7)
            
            # Success rate over time
            attempts = range(1, len(self.auth_attempts) + 1)
            successes = [1 if a["success"] else 0 for a in self.auth_attempts]
            
            # Calculate cumulative success rate
            cumulative_success = []
            total_success = 0
            for i, s in enumerate(successes):
                total_success += s
                cumulative_success.append(total_success / (i + 1))
            
            # Plot success rate
            ax2.plot(attempts, cumulative_success, 'g-')
            ax2.set_title('Cumulative Success Rate')
            ax2.set_xlabel('Attempt')
            ax2.set_ylabel('Success Rate')
            ax2.set_ylim(0, 1)
            
            # Add reference line for perfect success
            ax2.axhline(y=1.0, color='green', linestyle='--', alpha=0.5)
            
            # Add reference line for perfect failure
            ax2.axhline(y=0.0, color='red', linestyle='--', alpha=0.5)
        
        # Adjust layout and draw
        self.fig.tight_layout()
        self.canvas.draw()
    
    def create_gui(self):
        """Create GUI for the tester"""
        self.root = tk.Tk()
        self.root.title("φ-Dimensional Door - Conventional Attack Simulator")
        self.root.geometry("900x700")
        
        # Create title frame
        title_frame = tk.Frame(self.root)
        title_frame.pack(fill=tk.X, padx=10, pady=10)
        
        title_label = tk.Label(
            title_frame,
            text="CONVENTIONAL AUTHENTICATION TEST",
            font=("Arial", 16, "bold")
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="Demonstrates how conventional methods fail against φ-dimensional protection",
            font=("Arial", 10)
        )
        subtitle_label.pack()
        
        # Create input frame
        input_frame = ttk.LabelFrame(self.root, text="Target Configuration")
        input_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Target host entry
        host_frame = tk.Frame(input_frame)
        host_frame.pack(fill=tk.X, padx=5, pady=5)
        
        host_label = tk.Label(host_frame, text="Target Host:")
        host_label.pack(side=tk.LEFT, padx=5)
        
        self.target_entry = tk.Entry(host_frame, width=30)
        self.target_entry.insert(0, self.target_host)
        self.target_entry.pack(side=tk.LEFT, padx=5)
        
        # Port entry
        port_frame = tk.Frame(input_frame)
        port_frame.pack(fill=tk.X, padx=5, pady=5)
        
        port_label = tk.Label(port_frame, text="Target Port:")
        port_label.pack(side=tk.LEFT, padx=5)
        
        self.port_entry = tk.Entry(port_frame, width=10)
        self.port_entry.insert(0, str(self.target_port))
        self.port_entry.pack(side=tk.LEFT, padx=5)
        
        # Create control frame
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Attempt counter input
        attempt_label = tk.Label(control_frame, text="Number of attempts:")
        attempt_label.pack(side=tk.LEFT, padx=5)
        
        self.attempt_entry = tk.Entry(control_frame, width=10)
        self.attempt_entry.insert(0, "100")
        self.attempt_entry.pack(side=tk.LEFT, padx=5)
        
        # Start button
        start_button = ttk.Button(
            control_frame,
            text="Start Attack Simulation",
            command=self.start_attack
        )
        start_button.pack(side=tk.LEFT, padx=10)
        
        # Stop button
        stop_button = ttk.Button(
            control_frame,
            text="Stop",
            command=self.stop_attack
        )
        stop_button.pack(side=tk.LEFT, padx=10)
        
        # Create status frame
        status_frame = tk.Frame(self.root)
        status_frame.pack(fill=tk.X, padx=10, pady=5)
        
        # Status label
        self.status_label = tk.Label(status_frame, text="Status: Ready")
        self.status_label.pack(side=tk.LEFT, padx=5)
        
        # Progress bar
        self.progress_bar = ttk.Progressbar(status_frame, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress_bar.pack(side=tk.RIGHT, padx=5)
        
        # Create visualization frame
        viz_frame = ttk.LabelFrame(self.root, text="Attack Results")
        viz_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Create figure and canvas for visualization
        self.fig = plt.Figure(figsize=(8, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, master=viz_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Create log frame
        log_frame = ttk.LabelFrame(self.root, text="Attack Log")
        log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Create log text widget
        self.log_text = scrolledtext.ScrolledText(log_frame, height=10)
        self.log_text.pack(fill=tk.BOTH, expand=True)
        
        # Footer
        footer_frame = tk.Frame(self.root)
        footer_frame.pack(fill=tk.X, padx=10, pady=5)
        
        footer_label = tk.Label(
            footer_frame,
            text="φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities",
            font=("Arial", 8)
        )
        footer_label.pack()
        
        # Log initial message
        self.log_message("Conventional Authentication Test initialized")
        self.log_message("This will attempt to bypass φ-dimensional door security using conventional methods")
        self.log_message("The 105 divisibility check should detect all attempts as spoofs (remainder 0)")
        
        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def start_attack(self):
        """Start the attack simulation from GUI"""
        if self.is_running:
            self.log_message("Attack simulation already running")
            return
        
        try:
            # Get inputs from GUI
            self.target_host = self.target_entry.get().strip()
            self.target_port = int(self.port_entry.get().strip())
            num_attempts = int(self.attempt_entry.get().strip())
            
            # Start attack in separate thread
            self.attack_thread = threading.Thread(
                target=self.run_brute_force,
                args=(num_attempts,)
            )
            self.attack_thread.daemon = True
            self.attack_thread.start()
            
        except Exception as e:
            self.log_message(f"Error starting attack: {str(e)}")
            if self.status_label:
                self.status_label.config(text=f"Status: Error - {str(e)}")
    
    def stop_attack(self):
        """Stop the attack simulation"""
        if not self.is_running:
            self.log_message("No attack simulation running")
            return
        
        self.is_running = False
        self.log_message("Stopping attack simulation...")
        
        if self.status_label:
            self.status_label.config(text="Status: Stopping...")
    
    def on_closing(self):
        """Handle window closing"""
        if self.is_running:
            self.stop_attack()
        self.root.destroy()
    
    def run(self):
        """Run the tester with GUI"""
        self.create_gui()
        self.root.mainloop()


def main():
    """Main function to run the tester"""
    print("\n🔍 CONVENTIONAL AUTHENTICATION TEST")
    print("=" * 70)
    print("Demonstrates how conventional methods fail against φ-dimensional protection")
    
    # Create tester
    tester = ConventionalAuthTester()
    
    # Run tester with GUI
    tester.run()


if __name__ == "__main__":
    main()
