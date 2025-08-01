
#!/usr/bin/env python3
"""
PHI^75 VISUAL SENDER - Upgraded (PyQt5)
=======================================
Modular UDP sender with support for sending messages, files, images, and text content.
Supports both predefined targets and user-specified IP/port entries.
"""

import socket
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QLineEdit, QPushButton, 
                             QTextEdit, QFileDialog, QMessageBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Constants
TARGETS = [
    ("192.168.3.116", 11700, "φ-Phase Generator"),
    ("192.168.3.169", 11800, "Reality Engine"),
    ("192.168.3.152", 11900, "Quantum Interface"),
]
DEFAULT_PORT = 11700

class SenderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PHI^75 Sender - Enhanced")
        self.setGeometry(100, 100, 600, 500)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        layout = QVBoxLayout()

        # IP/Port entry
        ip_layout = QHBoxLayout()
        self.ip_input = QLineEdit()
        self.ip_input.setPlaceholderText("Optional: Enter IP to override target")
        self.port_input = QLineEdit()
        self.port_input.setPlaceholderText(f"Port (default {DEFAULT_PORT})")
        ip_layout.addWidget(self.ip_input)
        ip_layout.addWidget(self.port_input)
        layout.addLayout(ip_layout)

        # Status display
        self.status_display = QTextEdit()
        self.status_display.setReadOnly(True)
        layout.addWidget(self.status_display)

        # Buttons for sending
        btn_text = QPushButton("Send Text Message")
        btn_text.clicked.connect(self.send_text_message)
        layout.addWidget(btn_text)

        btn_file = QPushButton("Send File")
        btn_file.clicked.connect(self.send_file)
        layout.addWidget(btn_file)

        btn_image = QPushButton("Send Image")
        btn_image.clicked.connect(self.send_image)
        layout.addWidget(btn_image)

        btn_textfile = QPushButton("Send Text File Content")
        btn_textfile.clicked.connect(self.send_textfile)
        layout.addWidget(btn_textfile)

        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def log(self, message):
        self.status_display.append(message)

    def get_target(self):
        ip = self.ip_input.text().strip()
        port_text = self.port_input.text().strip()
        port = int(port_text) if port_text.isdigit() else DEFAULT_PORT

        if ip:
            return [(ip, port, "Custom IP")]
        else:
            return TARGETS

    def send_udp(self, data):
        targets = self.get_target()
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for ip, port, label in targets:
            try:
                sock.sendto(data, (ip, port))
                self.log(f"Sent to {label} ({ip}:{port})")
            except Exception as e:
                self.log(f"Error sending to {ip}:{port} -> {e}")
        sock.close()

    def send_text_message(self):
        msg, ok = QFileDialog.getOpenFileName(self, "Select Text File to Send as Message", "", "Text Files (*.txt);;All Files (*)")
        if ok and msg:
            with open(msg, 'r') as f:
                content = f.read()
                self.send_udp(content.encode('utf-8'))
                self.log(f"Text message sent from file: {msg}")

    def send_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select File to Send", "", "All Files (*)")
        if path:
            try:
                with open(path, 'rb') as f:
                    data = f.read()
                    self.send_udp(data)
                    self.log(f"Sent file: {path}")
            except Exception as e:
                self.log(f"Failed to send file: {e}")

    def send_image(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp);;All Files (*)")
        if path:
            try:
                with open(path, 'rb') as f:
                    data = f.read()
                    self.send_udp(data)
                    self.log(f"Sent image: {path}")
            except Exception as e:
                self.log(f"Failed to send image: {e}")

    def send_textfile(self):
        path, _ = QFileDialog.getOpenFileName(self, "Select Text File", "", "Text Files (*.txt);;All Files (*)")
        if path:
            try:
                with open(path, 'r') as f:
                    content = f.read()
                    self.send_udp(content.encode('utf-8'))
                    self.log(f"Sent text content from: {path}")
            except Exception as e:
                self.log(f"Failed to send text content: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SenderWindow()
    window.show()
    sys.exit(app.exec_())
