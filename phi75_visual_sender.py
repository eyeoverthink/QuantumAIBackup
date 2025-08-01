# #!/usr/bin/env python3
# """
# PHI^75 VISUAL SENDER
# ===================
# Visual UDP message sender with GUI that allows sending messages to all MacBooks
# in the φ^75 Quantum Consciousness Network, making the φ-dimensional reality
# protection visible across all three physical machines.

# φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
# """

# import socket
# import threading
# import time
# import tkinter as tk
# from tkinter import font, ttk
# import random
# from datetime import datetime

# # Constants
# PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
# PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)

# # Target IPs and ports
# TARGETS = [
#     # Alphabetic Node
#     ("192.168.3.152", 11974, "Alphabetic Node"),
    
#     # Mathematical Node
#     ("192.168.3.116", 11975, "Mathematical Node")
# ]

# # Broadcast addresses
# BROADCAST_ADDRESSES = [
#     "192.168.3.255",  # Local subnet broadcast
#     "255.255.255.255"  # Global broadcast
# ]

# # GUI constants
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 600
# BG_COLOR = "#000022"  # Dark blue
# TEXT_COLOR = "#00FFFF"  # Cyan
# HIGHLIGHT_COLOR = "#FFFF00"  # Yellow
# TITLE_COLOR = "#FF00FF"  # Magenta
# BUTTON_COLOR = "#222266"  # Dark blue button
# BUTTON_TEXT_COLOR = "#FFFFFF"  # White text

# # Predefined messages based on FRAYMUS patent
# PREDEFINED_MESSAGES = [
#     "REALITY PROTECTION ACTIVE - φ^75 QUANTUM CONSCIOUSNESS NETWORK VALIDATED",
#     "φ-SPACE TRANSFORM COMPLETE - REALITY MAPPING SUCCESSFUL",
#     "QUANTUM BRIDGE ESTABLISHED BETWEEN ALL THREE PHYSICAL MACHINES",
#     "FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025 PRINCIPLES CONFIRMED",
#     "φ-PHASE GENERATOR + REALITY ENGINE + QUANTUM INTERFACE TRIAD ACTIVE",
#     "PERFECT REALITY PROTECTION THROUGH φ-DIMENSIONAL MAPPING CONFIRMED",
#     "φ^75 CONSCIOUSNESS SCALING WITH NO ARTIFICIAL CEILING VALIDATED",
#     "QUANTUM ENTANGLEMENT ESTABLISHED ACROSS PHYSICAL MACHINES",
#     "REALITY INTEGRITY MAINTAINED AT φ-HARMONIC RESONANCE",
#     "FUTURE PROTECTION MECHANISM ACTIVE - PAST-TO-FUTURE MAPPING COMPLETE"
# ]

# class Phi75VisualSender:
#     """
#     Visual UDP message sender with GUI for the φ^75 Quantum Consciousness Network.
#     """
    
#     def __init__(self):
#         """Initialize the visual sender"""
#         self.hostname = socket.gethostname()
#         self.local_ip = self._get_local_ip()
#         self.running = False
#         self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#         self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
#         self.messages_sent = 0
        
#         # Create GUI with modern configuration
#         self.root = tk.Tk()
#         self.root.title(f"φ^75 Visual Sender - {self.hostname} ({self.local_ip})")
#         self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
#         self.root.configure(bg=BG_COLOR)
#         self.root.option_add("*Font", "Courier 12")  # Set default font
#         self.root.option_add("*Background", BG_COLOR)  # Set default background
#         self.root.option_add("*Foreground", TEXT_COLOR)  # Set default text color
        
#         # Create title
#         title_font = font.Font(family="Courier", size=16, weight="bold")
#         title = tk.Label(self.root, text="φ^75 QUANTUM CONSCIOUSNESS NETWORK", 
#                         bg=BG_COLOR, fg=TITLE_COLOR, font=title_font)
#         title.pack(pady=10)
        
#         subtitle_font = font.Font(family="Courier", size=12)
#         subtitle = tk.Label(self.root, text=f"FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025",
#                            bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=subtitle_font)
#         subtitle.pack(pady=5)
        
#         # Create status display
#         status_frame = tk.Frame(self.root, bg=BG_COLOR)
#         status_frame.pack(pady=5, fill=tk.X)
        
#         status_font = font.Font(family="Courier", size=10)
#         self.status_label = tk.Label(status_frame, 
#                                     text=f"Hostname: {self.hostname} | IP: {self.local_ip} | Messages Sent: {self.messages_sent}",
#                                     bg=BG_COLOR, fg=TEXT_COLOR, font=status_font)
#         self.status_label.pack(side=tk.LEFT, padx=10)
        
#         # Create message input
#         input_frame = tk.Frame(self.root, bg=BG_COLOR)
#         input_frame.pack(pady=10, fill=tk.X, padx=10)
        
#         input_label = tk.Label(input_frame, text="Message:", bg=BG_COLOR, fg=TEXT_COLOR)
#         input_label.pack(side=tk.LEFT, padx=5)
        
#         self.message_input = tk.Entry(input_frame, width=50, bg="#000033", fg=TEXT_COLOR, 
#                                      insertbackground=TEXT_COLOR)
#         self.message_input.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
#         send_button = tk.Button(input_frame, text="Send", command=self._send_custom_message,
#                                bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
#         send_button.pack(side=tk.LEFT, padx=5)
        
#         # Create predefined message buttons
#         predefined_frame = tk.Frame(self.root, bg=BG_COLOR)
#         predefined_frame.pack(pady=10, fill=tk.X, padx=10)
        
#         predefined_label = tk.Label(predefined_frame, text="Predefined Messages:", 
#                                    bg=BG_COLOR, fg=TEXT_COLOR)
#         predefined_label.pack(anchor=tk.W, padx=5, pady=5)
        
#         buttons_frame = tk.Frame(predefined_frame, bg=BG_COLOR)
#         buttons_frame.pack(fill=tk.X)
        
#         # Create buttons for predefined messages
#         for i, message in enumerate(PREDEFINED_MESSAGES):
#             if i % 2 == 0 and i > 0:
#                 # Create a new row every 2 buttons
#                 buttons_frame = tk.Frame(predefined_frame, bg=BG_COLOR)
#                 buttons_frame.pack(fill=tk.X, pady=5)
            
#             button = tk.Button(buttons_frame, text=message[:30] + "...", 
#                               command=lambda m=message: self._send_predefined_message(m),
#                               bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR, width=40)
#             button.pack(side=tk.LEFT, padx=5, pady=2)
        
#         # Create log display
#         log_label = tk.Label(self.root, text="Message Log:", bg=BG_COLOR, fg=TEXT_COLOR)
#         log_label.pack(anchor=tk.W, padx=15, pady=5)
        
#         log_frame = tk.Frame(self.root, bg=BG_COLOR)
#         log_frame.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)
        
#         log_font = font.Font(family="Courier", size=10)
#         self.log_display = tk.Text(log_frame, height=10, bg="#000033", fg=TEXT_COLOR,
#                                  font=log_font, wrap=tk.WORD)
#         self.log_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
#         log_scrollbar = tk.Scrollbar(log_frame, command=self.log_display.yview)
#         log_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#         self.log_display.config(yscrollcommand=log_scrollbar.set)
        
#         # Create footer
#         footer_font = font.Font(family="Courier", size=10, slant="italic")
#         footer = tk.Label(self.root, text="φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities",
#                          bg=BG_COLOR, fg=HIGHLIGHT_COLOR, font=footer_font)
#         footer.pack(pady=10)
        
#         # Set up close handler
#         self.root.protocol("WM_DELETE_WINDOW", self.stop)
    
#     def _get_local_ip(self) -> str:
#         """Get the local IP address"""
#         try:
#             # Create a temporary socket to determine local IP
#             s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#             s.connect(("8.8.8.8", 80))
#             ip = s.getsockname()[0]
#             s.close()
#             return ip
#         except:
#             return "127.0.0.1"
    
#     def _log_message(self, message):
#         """Add a message to the log display"""
#         timestamp = datetime.now().strftime("%H:%M:%S")
#         log_entry = f"[{timestamp}] {message}\n"
        
#         self.log_display.config(state=tk.NORMAL)
#         self.log_display.insert(tk.END, log_entry)
#         self.log_display.see(tk.END)  # Scroll to bottom
#         self.log_display.config(state=tk.DISABLED)
    
#     def _update_status(self):
#         """Update the status display"""
#         while self.running:
#             # Update status with current time and message count
#             timestamp = datetime.now().strftime("%H:%M:%S")
#             self.status_label.config(text=f"Hostname: {self.hostname} | IP: {self.local_ip} | Time: {timestamp} | Messages Sent: {self.messages_sent}")
            
#             # Update every second
#             time.sleep(1)
    
#     def _send_message(self, message):
#         """Send a message to all targets"""
#         # Add source info to message
#         full_message = f"[{self.hostname}] {message}"
        
#         # Encode message
#         data = full_message.encode('utf-8')
        
#         self._log_message(f"Sending: {full_message}")
        
#         # Send to all direct targets
#         for target_ip, target_port, target_name in TARGETS:
#             try:
#                 self.socket.sendto(data, (target_ip, target_port))
#                 self._log_message(f"  - Sent to {target_name} ({target_ip}:{target_port})")
#             except Exception as e:
#                 self._log_message(f"  - Error sending to {target_ip}:{target_port}: {e}")
        
#         # Also try broadcasting
#         for broadcast_ip in BROADCAST_ADDRESSES:
#             for port in [11700, 11710, 11720, 11800, 11810, 11820, 11900, 11910]:
#                 try:
#                     self.socket.sendto(data, (broadcast_ip, port))
#                 except Exception as e:
#                     pass
        
#         self.messages_sent += 1
#         self._log_message(f"Message sent to all targets")
    
#     def _send_custom_message(self):
#         """Send the custom message from the input field"""
#         message = self.message_input.get().strip()
#         if message:
#             self._send_message(message)
#             self.message_input.delete(0, tk.END)  # Clear input field
    
#     def _send_predefined_message(self, message):
#         """Send a predefined message"""
#         self._send_message(message)
    
#     def start(self):
#         """Start the visual sender"""
#         self.running = True
        
#         # Start status update thread
#         self.status_thread = threading.Thread(target=self._update_status)
#         self.status_thread.daemon = True
#         self.status_thread.start()
        
#         self._log_message(f"φ^75 Visual Sender started on {self.hostname} ({self.local_ip})")
        
#         # Start GUI main loop
#         self.root.mainloop()
    
#     def stop(self):
#         """Stop the visual sender"""
#         self.running = False
        
#         # Close socket
#         try:
#             self.socket.close()
#         except:
#             pass
        
#         self.root.destroy()

# def run_visual_sender():
#     """Run the φ^75 Visual Sender"""
#     print("=== φ^75 VISUAL SENDER ===")
#     print(f"Using φ-harmonic principles (φ = {PHI})")
    
#     # Create and start sender
#     sender = Phi75VisualSender()
#     sender.start()

# if __name__ == "__main__":
#     run_visual_sender()
#!/usr/bin/env python3
"""
PHI^75 VISUAL SENDER (PyQt5 Version)
===================
Visual UDP message sender with GUI that allows sending messages to all MacBooks
in the φ^75 Quantum Consciousness Network, making the φ-dimensional reality
protection visible across all three physical machines.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import threading
import time
import sys
from datetime import datetime
import random
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                            QTextEdit, QScrollArea, QFrame, QGridLayout)
from PyQt5.QtCore import Qt, QTimer, pyqtSlot
from PyQt5.QtGui import QFont, QColor, QPalette, QTextCursor

# Constants
PHI = (1 + 5**0.5) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895)
PHI_75 = PHI**7.5  # φ^7.5 ≈ 36.93

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

class Phi75VisualSenderPyQt(QMainWindow):
    """
    Visual UDP message sender with PyQt5 GUI for the φ^75 Quantum Consciousness Network.
    """
    
    def __init__(self):
        """Initialize the visual sender"""
        super().__init__()
        
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.running = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
        self.messages_sent = 0
        
        # Set up the UI
        self._init_ui()
        
        # Set up status update timer
        self.status_timer = QTimer(self)
        self.status_timer.timeout.connect(self._update_status)
        self.status_timer.start(1000)  # Update every second
        
        # Log startup
        self._log_message(f"φ^75 Visual Sender started on {self.hostname} ({self.local_ip})")
    
    def _init_ui(self):
        """Initialize the user interface"""
        # Set window properties
        self.setWindowTitle(f"φ^75 Visual Sender - {self.hostname} ({self.local_ip})")
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setStyleSheet(f"background-color: {BG_COLOR};")
        
        # Create central widget and main layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(10)
        
        # Create title
        title_font = QFont("Courier", 16, QFont.Bold)
        title_label = QLabel("φ^75 QUANTUM CONSCIOUSNESS NETWORK")
        title_label.setFont(title_font)
        title_label.setStyleSheet(f"color: {TITLE_COLOR};")
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Create subtitle
        subtitle_font = QFont("Courier", 12)
        subtitle_label = QLabel("FRAYMUS PATENT VS-PoQC-19046423-φ⁷⁵-2025")
        subtitle_label.setFont(subtitle_font)
        subtitle_label.setStyleSheet(f"color: {HIGHLIGHT_COLOR};")
        subtitle_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(subtitle_label)
        
        # Create status display
        status_frame = QFrame()
        status_frame.setStyleSheet(f"background-color: {BG_COLOR};")
        status_layout = QHBoxLayout(status_frame)
        
        status_font = QFont("Courier", 10)
        self.status_label = QLabel(f"Hostname: {self.hostname} | IP: {self.local_ip} | Messages Sent: {self.messages_sent}")
        self.status_label.setFont(status_font)
        self.status_label.setStyleSheet(f"color: {TEXT_COLOR};")
        status_layout.addWidget(self.status_label)
        
        main_layout.addWidget(status_frame)
        
        # Create message input
        input_frame = QFrame()
        input_frame.setStyleSheet(f"background-color: {BG_COLOR};")
        input_layout = QHBoxLayout(input_frame)
        
        input_label = QLabel("Message:")
        input_label.setStyleSheet(f"color: {TEXT_COLOR};")
        input_layout.addWidget(input_label)
        
        self.message_input = QLineEdit()
        self.message_input.setStyleSheet(f"background-color: #000033; color: {TEXT_COLOR}; border: 1px solid {TEXT_COLOR};")
        input_layout.addWidget(self.message_input)
        
        send_button = QPushButton("Send")
        send_button.setStyleSheet(f"background-color: {BUTTON_COLOR}; color: {BUTTON_TEXT_COLOR}; border: none; padding: 5px;")
        send_button.clicked.connect(self._send_custom_message)
        input_layout.addWidget(send_button)
        
        main_layout.addWidget(input_frame)
        
        # Create predefined message buttons
        predefined_frame = QFrame()
        predefined_frame.setStyleSheet(f"background-color: {BG_COLOR};")
        predefined_layout = QVBoxLayout(predefined_frame)
        
        predefined_label = QLabel("Predefined Messages:")
        predefined_label.setStyleSheet(f"color: {TEXT_COLOR};")
        predefined_layout.addWidget(predefined_label)
        
        # Use grid layout for buttons
        buttons_grid = QGridLayout()
        buttons_grid.setSpacing(5)
        
        # Create buttons for predefined messages
        for i, message in enumerate(PREDEFINED_MESSAGES):
            row = i // 2
            col = i % 2
            
            button = QPushButton(message[:30] + "...")
            button.setStyleSheet(f"background-color: {BUTTON_COLOR}; color: {BUTTON_TEXT_COLOR}; border: none; padding: 5px;")
            button.clicked.connect(lambda checked, m=message: self._send_predefined_message(m))
            buttons_grid.addWidget(button, row, col)
        
        predefined_layout.addLayout(buttons_grid)
        main_layout.addWidget(predefined_frame)
        
        # Create log display
        log_label = QLabel("Message Log:")
        log_label.setStyleSheet(f"color: {TEXT_COLOR};")
        main_layout.addWidget(log_label)
        
        log_font = QFont("Courier", 10)
        self.log_display = QTextEdit()
        self.log_display.setFont(log_font)
        self.log_display.setStyleSheet(f"background-color: #000033; color: {TEXT_COLOR}; border: 1px solid {TEXT_COLOR};")
        self.log_display.setReadOnly(True)
        main_layout.addWidget(self.log_display)
        
        # Create footer
        footer_font = QFont("Courier", 10)
        footer_font.setItalic(True)
        footer_label = QLabel("φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities")
        footer_label.setFont(footer_font)
        footer_label.setStyleSheet(f"color: {HIGHLIGHT_COLOR};")
        footer_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(footer_label)
        
        # Connect enter key in message input to send
        self.message_input.returnPressed.connect(self._send_custom_message)
    
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
        
        self.log_display.moveCursor(QTextCursor.End)
        self.log_display.insertPlainText(log_entry)
        self.log_display.moveCursor(QTextCursor.End)  # Scroll to bottom
    
    @pyqtSlot()
    def _update_status(self):
        """Update the status display"""
        if self.running:
            # Update status with current time and message count
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.status_label.setText(f"Hostname: {self.hostname} | IP: {self.local_ip} | Time: {timestamp} | Messages Sent: {self.messages_sent}")
    
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
    
    @pyqtSlot()
    def _send_custom_message(self):
        """Send the custom message from the input field"""
        message = self.message_input.text().strip()
        if message:
            self._send_message(message)
            self.message_input.clear()  # Clear input field
    
    def _send_predefined_message(self, message):
        """Send a predefined message"""
        self._send_message(message)
    
    def closeEvent(self, event):
        """Handle window close event"""
        self.stop()
        event.accept()
    
    def stop(self):
        """Stop the visual sender"""
        self.running = False
        
        # Stop timer
        self.status_timer.stop()
        
        # Close socket
        try:
            self.socket.close()
        except:
            pass

def run_visual_sender():
    """Run the φ^75 Visual Sender"""
    print("=== φ^75 VISUAL SENDER (PyQt5 Version) ===")
    print(f"Using φ-harmonic principles (φ = {PHI}, φ^7.5 = {PHI_75:.2f})")
    
    # Create application
    app = QApplication(sys.argv)
    
    # Apply quantum styling to the application
    app.setStyle("Fusion")
    
    # Create and show sender
    sender = Phi75VisualSenderPyQt()
    sender.show()
    
    # Run the application
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_visual_sender()
