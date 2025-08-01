#!/usr/bin/env python3
"""
PHI^75 CONSOLE RECEIVER
=====================
Console-based UDP message receiver that displays incoming messages in the terminal,
making the φ-dimensional reality protection visible across all three MacBooks.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
from datetime import datetime
import sys
import os

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
LISTEN_PORTS = [11700, 11710, 11720, 11800, 11810, 11820, 11900, 11910]

# ANSI Colors for terminal
class Colors:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    
    # Background colors
    BG_BLACK = "\033[40m"
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"

class Phi75ConsoleReceiver:
    """
    Console-based UDP message receiver that displays incoming messages in the terminal.
    """
    
    def __init__(self):
        """Initialize the console receiver"""
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.running = False
        self.sockets = []
        self.messages = []
        self.max_messages = 100
        
        # Clear terminal
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Print header
        print(f"{Colors.MAGENTA}{Colors.BOLD}=== φ^75 QUANTUM CONSCIOUSNESS NETWORK ==={Colors.RESET}")
        print(f"{Colors.YELLOW}FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025{Colors.RESET}")
        print(f"{Colors.CYAN}Hostname: {self.hostname} | IP: {self.local_ip}{Colors.RESET}")
        print(f"{Colors.CYAN}Listening on ports: {LISTEN_PORTS}{Colors.RESET}")
        print(f"{Colors.CYAN}Using φ-harmonic principles (φ = {PHI}){Colors.RESET}")
        print(f"{Colors.CYAN}Phi-harmonic resonance: {PHI_INV:.6f} (exactly φ^-1){Colors.RESET}")
        print(f"{Colors.CYAN}Quantum coherence: 0.991800{Colors.RESET}")
        print(f"{Colors.MAGENTA}{Colors.BOLD}----------------------------------------{Colors.RESET}")
    
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
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        
        if system:
            if error:
                prefix = f"[{Colors.RED}SYSTEM ERROR {timestamp}{Colors.RESET}] "
                print(f"{prefix}{message}")
            else:
                prefix = f"[{Colors.BLUE}SYSTEM {timestamp}{Colors.RESET}] "
                print(f"{prefix}{message}")
        else:
            prefix = f"[{Colors.GREEN}{timestamp}{Colors.RESET}] "
            print(f"{prefix}{Colors.BOLD}{message}{Colors.RESET}")
            
            # Add a visual separator for φ-dimensional reality protection messages
            if "REALITY PROTECTION" in message or "φ-SPACE" in message or "QUANTUM" in message:
                print(f"{Colors.MAGENTA}φ{'~' * 50}φ{Colors.RESET}")
    
    def _receive_messages(self):
        """Receive messages from all sockets"""
        while self.running:
            for sock, port in self.sockets:
                try:
                    data, addr = sock.recvfrom(4096)
                    message = data.decode('utf-8')
                    self._add_message(f"[Port {port}] [From {addr[0]}] {message}")
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
            sys.stdout.write(f"\r[{Colors.CYAN}STATUS {timestamp}{Colors.RESET}] Listening on ports: {LISTEN_PORTS}")
            sys.stdout.flush()
            
            # Update every second
            time.sleep(1)
    
    def start(self):
        """Start the console receiver"""
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
        
        self._add_message(f"φ^75 Console Receiver started on {self.hostname} ({self.local_ip})", system=True)
        self._add_message("Waiting for messages from the φ^75 Quantum Consciousness Network...", system=True)
        
        # Wait for keyboard interrupt
        try:
            while self.running:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self):
        """Stop the console receiver"""
        self.running = False
        
        # Close all sockets
        for sock, port in self.sockets:
            try:
                sock.close()
            except:
                pass
        
        self._add_message("Console Receiver stopped", system=True)
        
        # Wait for threads to finish
        if hasattr(self, 'receiver_thread') and self.receiver_thread.is_alive():
            self.receiver_thread.join(1.0)
        if hasattr(self, 'status_thread') and self.status_thread.is_alive():
            self.status_thread.join(1.0)

def run_console_receiver():
    """Run the φ^75 Console Receiver"""
    print("=== φ^75 CONSOLE RECEIVER ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    
    # Create and start receiver
    receiver = Phi75ConsoleReceiver()
    receiver.start()

if __name__ == "__main__":
    run_console_receiver()
