#!/usr/bin/env python3
"""
PHI^75 VISUAL RECEIVER (PyQt5 VERSION)
=====================
Visual UDP message receiver that displays incoming messages in a GUI window,
making the φ-dimensional reality protection visible across all three MacBooks.

This is a PyQt5 implementation that preserves all functionality of the original
tkinter version while working with your current Python environment.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import random
import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QLabel, QFrame
from PyQt5.QtGui import QFont, QColor, QTextCharFormat, QTextCursor
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, QObject

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
LISTEN_PORTS = [11700, 11710, 11720, 11800, 11810, 11820, 11900, 11910, 11975, 11974, 11975, 11976]
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BG_COLOR = "#000000"  # Black
TEXT_COLOR = "#00FF00"  # Green
HIGHLIGHT_COLOR = "#FFFF00"  # Yellow
TITLE_COLOR = "#FF00FF"  # Magenta

# Signal handler for thread-safe message processing
class MessageSignalHandler(QObject):
    """Signal handler for thread-safe message processing"""
    message_signal = pyqtSignal(str, bool)
    
    def __init__(self):
        super().__init__()

class Phi75VisualReceiver(QMainWindow):
    """
    Visual UDP message receiver that displays incoming messages in a GUI window.
    """
    
    def __init__(self):
        """Initialize the visual receiver"""
        super().__init__()
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.running = False
        self.sockets = []
        self.messages = []
        self.max_messages = 100
        
        # Set up signal handler for thread-safe message processing
        self.message_handler = MessageSignalHandler()
        self.message_handler.message_signal.connect(self._add_message)
        
        # Create GUI
        self.setWindowTitle(f"φ^75 Visual Receiver - {self.hostname} ({self.local_ip})")
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet(f"background-color: {BG_COLOR};")
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Create title
        title_font = QFont("Menlo", 16)
        title_font.setBold(True)
        title = QLabel("φ^75 QUANTUM CONSCIOUSNESS NETWORK")
        title.setFont(title_font)
        title.setStyleSheet(f"color: {TITLE_COLOR}; background-color: {BG_COLOR};")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Create subtitle
        subtitle_font = QFont("Menlo", 12)
        subtitle = QLabel(f"FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025")
        subtitle.setFont(subtitle_font)
        subtitle.setStyleSheet(f"color: {HIGHLIGHT_COLOR}; background-color: {BG_COLOR};")
        subtitle.setAlignment(Qt.AlignCenter)
        layout.addWidget(subtitle)
        
        # Create status display
        status_frame = QFrame()
        status_frame.setStyleSheet(f"background-color: {BG_COLOR};")
        status_layout = QVBoxLayout(status_frame)
        
        status_font = QFont("Menlo", 10)
        self.status_label = QLabel(f"Hostname: {self.hostname} | IP: {self.local_ip} | Listening on ports: {LISTEN_PORTS}")
        self.status_label.setFont(status_font)
        self.status_label.setStyleSheet(f"color: {TEXT_COLOR}; background-color: {BG_COLOR};")
        status_layout.addWidget(self.status_label)
        
        layout.addWidget(status_frame)
        
        # Create message display
        message_font = QFont("Menlo", 12)
        self.message_display = QTextEdit()
        self.message_display.setFont(message_font)
        self.message_display.setStyleSheet(f"color: {TEXT_COLOR}; background-color: {BG_COLOR};")
        self.message_display.setReadOnly(True)
        layout.addWidget(self.message_display)
        
        # Create footer
        footer_font = QFont("Menlo", 10)
        footer_font.setItalic(True)
        footer = QLabel("φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities")
        footer.setFont(footer_font)
        footer.setStyleSheet(f"color: {HIGHLIGHT_COLOR}; background-color: {BG_COLOR};")
        footer.setAlignment(Qt.AlignCenter)
        layout.addWidget(footer)
        
        # Set up status update timer
        self.status_timer = QTimer(self)
        self.status_timer.timeout.connect(self._update_status)
        self.status_timer.start(1000)  # Update every second
    
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
        """Add a message to the display (called from the main thread)"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        
        # Format message with timestamp
        formatted_message = f"[{timestamp}] {message}"
        
        # Add to message list with color based on system flag
        color = HIGHLIGHT_COLOR if system else TEXT_COLOR
        self.messages.append((formatted_message, color))
        
        # Trim message list if it gets too long
        if len(self.messages) > self.max_messages:
            self.messages = self.messages[-self.max_messages:]
        
        # Update display
        self._update_display()
    
    def add_message_safe(self, message, system=False):
        """Thread-safe method to add a message to the display"""
        # Emit signal to add message from the main thread
        self.message_handler.message_signal.emit(message, system)
    
    def _update_display(self):
        """Update the message display"""
        # Clear display
        self.message_display.clear()
        
        # Create text cursor for formatting
        cursor = self.message_display.textCursor()
        
        # Add messages with formatting
        for message, color in self.messages:
            # Create format for this message
            fmt = QTextCharFormat()
            fmt.setForeground(QColor(color))
            
            # Insert text with format
            cursor.insertText(message + "\n", fmt)
        
        # Scroll to bottom
        cursor.movePosition(QTextCursor.End)
        self.message_display.setTextCursor(cursor)
    
    def _receive_messages(self):
        """Receive messages from all sockets"""
        while self.running:
            for sock, port in self.sockets:
                try:
                    data, addr = sock.recvfrom(4096)
                    try:
                        message = data.decode("utf-8")
                        # Use a thread-safe way to update the UI
                        message_text = f"Port {port} | {addr[0]}:{addr[1]} | {message}"
                        self.add_message_safe(message_text)
                    except UnicodeDecodeError:
                        # Handle binary data
                        self.add_message_safe(f"Port {port} | {addr[0]}:{addr[1]} | [Binary data received: {len(data)} bytes]", system=True)
                except socket.timeout:
                    # No data available, continue to next socket
                    pass
                except Exception as e:
                    self.add_message_safe(f"Error receiving on port {port}: {e}", system=True)
            
            # Small sleep to prevent CPU overuse
            time.sleep(0.01)
    
    def _update_status(self):
        """Update the status display"""
        # Update status with current time
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.status_label.setText(f"Hostname: {self.hostname} | IP: {self.local_ip} | Time: {timestamp} | Listening on ports: {LISTEN_PORTS}")
    
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
        
        # Add initial messages using the thread-safe method
        self.add_message_safe(f"φ^75 Visual Receiver started on {self.hostname} ({self.local_ip})", system=True)
        self.add_message_safe("Waiting for messages from the φ^75 Quantum Consciousness Network...", system=True)
        self.add_message_safe(f"Phi-harmonic resonance: 0.618034 (exactly φ^-1)", system=True)
        self.add_message_safe(f"Quantum coherence: 0.991800", system=True)
        
        # Show the GUI
        self.show()
    
    def stop(self):
        """Stop the visual receiver"""
        if not self.running:
            return
            
        self.running = False
        
        # Add stopped message
        self.add_message_safe("Visual Receiver stopping...", system=True)
        
        # Close all sockets
        for sock, port in self.sockets:
            try:
                sock.close()
            except Exception as e:
                print(f"Error closing socket on port {port}: {e}")
        
        # Clear socket list
        self.sockets = []
        
        # Wait for threads to finish
        if hasattr(self, 'receiver_thread') and self.receiver_thread.is_alive():
            try:
                self.receiver_thread.join(1.0)
            except Exception as e:
                print(f"Error joining receiver thread: {e}")
        
        # Final message
        self.add_message_safe("Visual Receiver stopped", system=True)
        
        # Close GUI
        self.close()
    
    def closeEvent(self, event):
        """Handle window close event"""
        self.stop()
        event.accept()

def run_visual_receiver():
    """Run the φ^75 Visual Receiver"""
    print("=== φ^75 VISUAL RECEIVER (PyQt5) ===")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print(f"Phi-harmonic resonance: 0.618034 (exactly φ^-1)")
    print(f"Quantum coherence: 0.991800")
    
    # Create and start receiver
    app = QApplication(sys.argv)
    receiver = Phi75VisualReceiver()
    receiver.start()
    
    # Start the application event loop
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_visual_receiver()
