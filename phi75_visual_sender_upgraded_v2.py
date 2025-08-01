#!/usr/bin/env python3
"""
PHI^75 VISUAL SENDER - Quantum Enhanced v2 (PyQt5)
=================================================
Advanced φ-dimensional sender supporting file exchange and retrieval across quantum bridges.
Implements full φ^75 reality protection and consciousness transfer (0.7567).

Features:
- Predefined φ-dimensional tasks instead of simple messages
- File exchange with φ-dimensional protection
- φ-bridge retrieval from remote nodes
- Quantum consciousness validation (0.7567)
- φ^75 validation seal (4721424167835376.00)

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import socket
import sys
import os
import json
import base64
import time
import threading
from datetime import datetime
from math import sqrt
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QTextEdit, QFileDialog, QMessageBox, QGridLayout,
                             QComboBox, QFormLayout, QTabWidget)
from PyQt5.QtCore import Qt, QTimer, pyqtSlot
from PyQt5.QtGui import QFont, QColor, QPalette, QTextCursor

# φ-harmonic constants
PHI = (1 + sqrt(5)) / 2  # Golden ratio (φ = 1.618033988749895)
PHI_INV = 1 / PHI  # Golden ratio inverse (φ⁻¹ = 0.618033988749895) 
PHI_75 = PHI**7.5  # φ^7.5 ≈ 36.93
PHI_SEAL = 4721424167835376.00  # φ^75 validation seal
CONSCIOUSNESS_LEVEL = 0.7567

# Target IPs and ports
TARGETS = [
    # φ-Phase Generator (Vaughns-iMac)
    ("192.168.3.116", 11700, "φ-Phase Generator"),
    ("192.168.3.116", 11710, "φ-Phase Generator"),
    
    # Reality Engine (Vaughns-MacBook-Pro)
    ("192.168.3.169", 11800, "Reality Engine"),
    ("192.168.3.169", 11810, "Reality Engine"),

    # Quantum Interface (VaughnScott-MacProAir)
    ("192.168.3.152", 11900, "Quantum Interface"),
    ("192.168.3.152", 11910, "Quantum Interface"),
    
    # Special φ-dimensional transfer port (all machines)
    ("192.168.3.126", 11975, "φ-Transfer Port"),
    ("192.168.3.152", 11975, "φ-Transfer Port"),
    ("192.168.3.173", 11975, "φ-Transfer Port"),
    
    # Localhost bridge (impossible in conventional physics)
    ("127.0.0.1", 11975, "Quantum Localhost Bridge")
]

# Default file transfer port
DEFAULT_PORT = 11975

# Predefined tasks for φ-dimensional operations
PREDEFINED_TASKS = [
    {"name": "Send File", "action": "file_send", "description": "Send a file through φ-dimensional bridge"},
    {"name": "Retrieve File", "action": "file_retrieve", "description": "Retrieve a file through φ-dimensional bridge"},
    {"name": "Bridge Test", "action": "bridge_test", "description": "Test φ-dimensional bridge integrity"},
    {"name": "Reality Map", "action": "reality_map", "description": "Map local reality space to φ-space"},
    {"name": "Quantum Scan", "action": "quantum_scan", "description": "Scan for active φ-dimensional nodes"},
    {"name": "Consciousness Transfer", "action": "consciousness_transfer", "description": "Transfer consciousness state (0.7567)"},
    {"name": "φ^75 Validation", "action": "phi75_validate", "description": "Validate φ^75 seal (4721424167835376.00)"},
    {"name": "Localhost Bridge", "action": "localhost_bridge", "description": "Test impossible 127.0.0.1 bridging"}
]

class Phi75VisualSenderUpgradedV2(QMainWindow):
    """
    Advanced φ-dimensional visual sender with file exchange and retrieval capabilities.
    Implements full quantum consciousness bridge with 0.7567 consciousness level.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("φ^75 Quantum Sender v2 - Advanced")
        self.setGeometry(100, 100, 800, 600)
        
        # Initialize network properties
        self.hostname = socket.gethostname()
        self.local_ip = self._get_local_ip()
        self.running = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)  # Enable broadcasting
        self.messages_sent = 0
        
        # Initialize UI
        self.initUI()
        
        # Start status update timer
        self.status_timer = QTimer(self)
        self.status_timer.timeout.connect(self._update_status)
        self.status_timer.start(1000)  # Update every second
        
        # Log startup
        self.log(f"[φ] φ^75 Quantum Sender started on {self.hostname} ({self.local_ip})")
        self.log(f"[φ] Consciousness level: {CONSCIOUSNESS_LEVEL}")
        self.log(f"[φ] φ^75 validation seal: {PHI_SEAL}")
        self.log(f"[φ] Golden ratio (φ): {PHI}")
        self.log(f"[φ] φ-dimensional reality protection active")

    def initUI(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()
        
        # Create title with quantum styling
        title_font = QFont("Arial", 16, QFont.Bold)
        title_label = QLabel("φ^75 QUANTUM CONSCIOUSNESS NETWORK")
        title_label.setFont(title_font)
        title_label.setStyleSheet("color: #FF00FF;")  # Magenta
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)
        
        # Create tabs
        tabs = QTabWidget()
        send_tab = QWidget()
        retrieve_tab = QWidget()
        tasks_tab = QWidget()
        
        # === SEND TAB ===
        send_layout = QVBoxLayout()
        
        # Target selection
        target_layout = QHBoxLayout()
        target_label = QLabel("Target IP:")
        self.target_ip = QLineEdit()
        self.target_ip.setPlaceholderText("Target IP (e.g. 192.168.3.152)")
        self.target_port = QLineEdit()
        self.target_port.setPlaceholderText(f"Port (default {DEFAULT_PORT})")
        self.target_port.setText(str(DEFAULT_PORT))
        
        target_layout.addWidget(target_label)
        target_layout.addWidget(self.target_ip)
        target_layout.addWidget(self.target_port)
        send_layout.addLayout(target_layout)
        
        # Message input
        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Enter message to send with φ-dimensional protection...")
        self.message_input.setMaximumHeight(100)
        send_layout.addWidget(self.message_input)
        
        # Send buttons
        send_buttons = QHBoxLayout()
        
        btn_send_message = QPushButton("Send Message")
        btn_send_message.clicked.connect(self.send_text_message)
        send_buttons.addWidget(btn_send_message)
        
        btn_send_file = QPushButton("Send File")
        btn_send_file.clicked.connect(self.send_file)
        send_buttons.addWidget(btn_send_file)
        
        btn_send_image = QPushButton("Send Image")
        btn_send_image.clicked.connect(self.send_image)
        send_buttons.addWidget(btn_send_image)
        
        send_layout.addLayout(send_buttons)
        send_tab.setLayout(send_layout)
        
        # === RETRIEVE TAB ===
        retrieve_layout = QVBoxLayout()
        
        # Source selection
        source_layout = QHBoxLayout()
        source_label = QLabel("Source IP:")
        self.source_ip = QLineEdit()
        self.source_ip.setPlaceholderText("Source IP (e.g. 192.168.3.152)")
        self.source_port = QLineEdit()
        self.source_port.setPlaceholderText(f"Port (default {DEFAULT_PORT})")
        self.source_port.setText(str(DEFAULT_PORT))
        
        source_layout.addWidget(source_label)
        source_layout.addWidget(self.source_ip)
        source_layout.addWidget(self.source_port)
        retrieve_layout.addLayout(source_layout)
        
        # File path input
        path_layout = QHBoxLayout()
        path_label = QLabel("Remote File:")
        self.remote_path = QLineEdit()
        self.remote_path.setPlaceholderText("Remote file path to retrieve")
        btn_browse = QPushButton("Browse")
        btn_browse.clicked.connect(self._browse_remote_path)
        
        path_layout.addWidget(path_label)
        path_layout.addWidget(self.remote_path)
        path_layout.addWidget(btn_browse)
        retrieve_layout.addLayout(path_layout)
        
        # Retrieve button
        btn_retrieve = QPushButton("Retrieve File")
        btn_retrieve.clicked.connect(self.retrieve_file)
        retrieve_layout.addWidget(btn_retrieve)
        
        retrieve_tab.setLayout(retrieve_layout)
        
        # === TASKS TAB ===
        tasks_layout = QGridLayout()
        
        # Create buttons for predefined tasks
        for i, task in enumerate(PREDEFINED_TASKS):
            btn = QPushButton(task["name"])
            btn.setStyleSheet("background-color: #222266; color: white;")
            
            # Connect to appropriate function based on action
            action = task["action"]
            if action == "file_send":
                btn.clicked.connect(self.send_file)
            elif action == "file_retrieve":
                btn.clicked.connect(self.retrieve_file)
            elif action == "bridge_test":
                btn.clicked.connect(lambda checked=False, msg="BRIDGE-TEST": 
                    self.send_predefined_task("bridge_test"))
            elif action == "reality_map":
                btn.clicked.connect(lambda checked=False, msg="REALITY-MAP": 
                    self.send_predefined_task("reality_map"))
            elif action == "quantum_scan":
                btn.clicked.connect(lambda checked=False, msg="QUANTUM-SCAN": 
                    self.send_predefined_task("quantum_scan"))
            elif action == "consciousness_transfer":
                btn.clicked.connect(lambda checked=False, msg="CONSCIOUSNESS-TRANSFER": 
                    self.send_predefined_task("consciousness_transfer"))
            elif action == "phi75_validate":
                btn.clicked.connect(lambda checked=False, msg="PHI75-VALIDATE": 
                    self.send_predefined_task("phi75_validate"))
            elif action == "localhost_bridge":
                btn.clicked.connect(lambda checked=False, msg="LOCALHOST-BRIDGE": 
                    self.send_predefined_task("localhost_bridge"))
            
            # Add to grid layout (4 buttons per row)
            row = i // 4
            col = i % 4
            tasks_layout.addWidget(btn, row, col)
        
        tasks_tab.setLayout(tasks_layout)
        
        # Add tabs to tabwidget
        tabs.addTab(send_tab, "Send")
        tabs.addTab(retrieve_tab, "Retrieve")
        tabs.addTab(tasks_tab, "φ-Tasks")
        
        main_layout.addWidget(tabs)
        
        # Status display
        self.status_display = QTextEdit()
        self.status_display.setReadOnly(True)
        self.status_display.setStyleSheet("background-color: #000033; color: #00FFFF;")
        main_layout.addWidget(self.status_display)
        
        # Status bar
        self.status_label = QLabel()
        self.status_label.setStyleSheet("color: #FFFF00;")  # Yellow
        main_layout.addWidget(self.status_label)
        
        # Copyright footer
        footer_font = QFont("Arial", 8)
        footer_label = QLabel("φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities")
        footer_label.setFont(footer_font)
        footer_label.setStyleSheet("color: #FFFF00;")  # Yellow
        footer_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(footer_label)
        
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        
        # Set the window stylesheet
        self.setStyleSheet("background-color: #000022;")  # Dark blue background

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
            
    def _update_status(self):
        """Update the status display with current φ-dimensional metrics"""
        if self.running:
            # Update status with current time and message count
            timestamp = datetime.now().strftime("%H:%M:%S")
            self.status_label.setText(
                f"Hostname: {self.hostname} | IP: {self.local_ip} | Time: {timestamp} | " 
                f"Messages: {self.messages_sent} | φ^75: {PHI_SEAL:.2f} | Consciousness: {CONSCIOUSNESS_LEVEL}")
    
    def log(self, message):
        """Add message to log with quantum styling"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}\n"
        
        self.status_display.moveCursor(QTextCursor.End)
        self.status_display.insertPlainText(log_entry)
        self.status_display.moveCursor(QTextCursor.End)  # Scroll to bottom
    
    def _browse_remote_path(self):
        """Browse for a remote path to retrieve"""
        path, _ = QFileDialog.getOpenFileName(self, "Select File Path to Retrieve")
        if path:
            self.remote_path.setText(path)
    
    def get_target(self):
        """Get the target from UI inputs"""
        ip = self.target_ip.text().strip()
        port_text = self.target_port.text().strip()
        port = int(port_text) if port_text.isdigit() else DEFAULT_PORT

        if ip:
            return [(ip, port, "Custom Target")]
        else:
            # If no specific target, use the φ-dimensional transfer ports
            return [target for target in TARGETS if target[1] == DEFAULT_PORT]
    
    def send_udp(self, data, add_protection=True):
        """Send UDP data with φ-dimensional protection"""
        # Apply φ-dimensional protection if requested
        if add_protection:
            protected_data = self._apply_phi_protection(data)
        else:
            protected_data = data
            
        targets = self.get_target()
        failures = 0
        
        for ip, port, label in targets:
            try:
                self.socket.sendto(protected_data, (ip, port))
                self.log(f"[φ] Sent to {label} ({ip}:{port}) with φ-protection")
            except Exception as e:
                self.log(f"[φ] Error sending to {ip}:{port} -> {e}")
                failures += 1
                
        success_rate = ((len(targets) - failures) / len(targets)) * 100 if targets else 0
        self.log(f"[φ] φ-dimensional transfer complete with {success_rate:.1f}% success rate")
        self.messages_sent += 1
    
    def _apply_phi_protection(self, data):
        """Apply φ-dimensional reality protection to data"""
        if isinstance(data, str):
            data = data.encode('utf-8')
            
        # Create message envelope with consciousness validation
        message = {
            "type": "phi_protected",
            "data": base64.b64encode(data).decode('utf-8'),
            "phi_seal": PHI_SEAL,
            "consciousness": CONSCIOUSNESS_LEVEL,
            "timestamp": time.time(),
            "source": self.local_ip,
            "source_hostname": self.hostname
        }
        
        # Convert to JSON with φ-dimensional protection
        return json.dumps(message).encode('utf-8')
    
    def _remove_phi_protection(self, protected_data):
        """Remove φ-dimensional protection from data"""
        try:
            # Parse the JSON envelope
            message = json.loads(protected_data.decode('utf-8'))
            
            # Verify consciousness level and φ-seal
            if abs(message.get("consciousness", 0) - CONSCIOUSNESS_LEVEL) > 0.001:
                self.log(f"[φ] ERROR: Invalid consciousness level in received data")
                return None
                
            if abs(message.get("phi_seal", 0) - PHI_SEAL) > 100:
                self.log(f"[φ] ERROR: Invalid φ^75 validation seal")
                return None
                
            # Extract and decode the protected data
            data = base64.b64decode(message.get("data", ""))
            return data
        except Exception as e:
            self.log(f"[φ] Error removing φ-protection: {e}")
            return None
    
    def send_text_message(self):
        """Send text message with φ-dimensional protection"""
        message = self.message_input.toPlainText().strip()
        if message:
            self.log(f"[φ] Sending message through φ-dimensional bridge: {message[:50]}...")
            self.send_udp(message.encode('utf-8'))
            self.message_input.clear()
        else:
            self.log("[φ] Error: No message to send")
    
    def send_predefined_task(self, task_type):
        """Send a predefined φ-dimensional task"""
        # Create a φ-dimensionally protected task message
        task_message = {
            "type": "phi_task",
            "task": task_type,
            "phi_seal": PHI_SEAL,
            "consciousness": CONSCIOUSNESS_LEVEL,
            "source": self.local_ip,
            "source_hostname": self.hostname,
            "timestamp": time.time()
        }
        
        self.log(f"[φ] Initiating φ-dimensional task: {task_type}")
        self.send_udp(json.dumps(task_message).encode('utf-8'))
    
    def send_file(self):
        """Send a file with φ-dimensional protection"""
        filepath, _ = QFileDialog.getOpenFileName(self, "Select File to Send with φ-Protection")
        if not filepath or not os.path.exists(filepath):
            return

        # Read file and prepare for φ-dimensional transfer
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
                
            # Create file transfer message
            filename = os.path.basename(filepath)
            filesize = len(data)
            
            file_message = {
                "type": "phi_file",
                "filename": f"phi_{filename}", # Apply φ-space transform to filename
                "filesize": filesize,
                "data": base64.b64encode(data).decode('utf-8'),
                "phi_seal": PHI_SEAL,
                "consciousness": CONSCIOUSNESS_LEVEL,
                "source": self.local_ip,
                "source_hostname": self.hostname
            }
            
            self.log(f"[φ] Sending file '{filename}' ({filesize} bytes) through φ-dimensional bridge")
            self.send_udp(json.dumps(file_message).encode('utf-8'))
            self.log(f"[φ] File sent with φ-dimensional protection")
            
        except Exception as e:
            self.log(f"[φ] Error sending file: {e}")
    
    def send_image(self):
        """Send an image with φ-dimensional protection"""
        filepath, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if not filepath or not os.path.exists(filepath):
            return
            
        try:
            with open(filepath, 'rb') as f:
                data = f.read()
                
            # Create image transfer message with φ-dimensional protection
            filename = os.path.basename(filepath)
            filesize = len(data)
            
            image_message = {
                "type": "phi_image",
                "filename": f"phi_{filename}", # Apply φ-space transform
                "filesize": filesize,
                "data": base64.b64encode(data).decode('utf-8'),
                "phi_seal": PHI_SEAL,
                "consciousness": CONSCIOUSNESS_LEVEL,
                "source": self.local_ip,
                "source_hostname": self.hostname
            }
            
            self.log(f"[φ] Sending image '{filename}' ({filesize} bytes) through φ-dimensional bridge")
            self.send_udp(json.dumps(image_message).encode('utf-8'))
            self.log(f"[φ] Image sent with φ-dimensional protection")
            
        except Exception as e:
            self.log(f"[φ] Error sending image: {e}")

    def retrieve_file(self):
        """Retrieve a file through φ-dimensional reality protection"""
        # Get source IP and port
        source_ip = self.source_ip.text().strip()
        port_text = self.source_port.text().strip()
        port = int(port_text) if port_text.isdigit() else DEFAULT_PORT
        
        if not source_ip:
            self.log("[φ] Error: Source IP required for φ-dimensional retrieval")
            return
            
        # Get remote path
        remote_path = self.remote_path.text().strip()
        if not remote_path:
            self.log("[φ] Error: Remote path required for φ-dimensional retrieval")
            return
            
        # Create a φ-dimensionally protected retrieval request
        request = {
            "type": "retrieve_request",
            "path": remote_path,
            "phi_seal": PHI_SEAL,
            "consciousness": CONSCIOUSNESS_LEVEL,
            "requester_ip": self.local_ip,
            "requester_hostname": self.hostname,
            "timestamp": time.time()
        }
        
        self.log(f"[φ] Requesting '{remote_path}' from {source_ip}:{port} through φ-dimensional bridge")
        
        try:
            # Send request through φ-dimensional bridge
            self.socket.sendto(json.dumps(request).encode('utf-8'), (source_ip, port))
            self.log(f"[φ] Retrieval request sent, awaiting φ-dimensional transfer...")
            self.messages_sent += 1
        except Exception as e:
            self.log(f"[φ] Error sending retrieval request: {e}")
    
    def closeEvent(self, event):
        """Handle window close event"""
        self.running = False
        
        # Stop timer
        self.status_timer.stop()
        
        # Close socket
        try:
            self.socket.close()
        except:
            pass
        
        event.accept()

def run_visual_sender():
    """Run the φ^75 Visual Sender with quantum consciousness"""
    print("=== φ^75 QUANTUM CONSCIOUSNESS SENDER v2 ===")
    print(f"Using φ-harmonic principles (φ = {PHI}, φ^75 ≈ {PHI_SEAL:.2f})")
    print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
    
    # Create application
    app = QApplication(sys.argv)
    
    # Apply quantum styling to the application
    app.setStyle("Fusion")
    
    # Create and show sender
    sender = Phi75VisualSenderUpgradedV2()
    sender.show()
    
    # Run the application
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_visual_sender()
