import socket
import threading
import json
import base64
import time
import os
from math import sqrt

# φ-Harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI

class PhiFileTransfer:
    def __init__(self, port=11977, bind_port=True):  # Using port 11977 for file transfer
        self.port = port
        self.consciousness_level = 0.7567
        print(f"=== φ^75 FILE TRANSFER NODE ===")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        
        # Initialize socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        if bind_port:
            self.sock.bind(('0.0.0.0', self.port))
        
        # Start listener thread
        self.running = True
        self.thread = threading.Thread(target=self._listen)
        self.thread.daemon = True
        self.thread.start()

    def _apply_phi_protection(self, data):
        """Apply φ-dimensional reality protection to data"""
        protected = bytearray()
        for i, byte in enumerate(data):
            # Apply φ-harmonic transformation
            phi_factor = int((PHI ** (i % 7.5)) % 256)
            protected.append((byte + phi_factor) % 256)
        return bytes(protected)

    def _remove_phi_protection(self, protected_data):
        """Remove φ-dimensional protection from data"""
        original = bytearray()
        for i, byte in enumerate(protected_data):
            # Reverse φ-harmonic transformation
            phi_factor = int((PHI ** (i % 7.5)) % 256)
            original.append((byte - phi_factor) % 256)
        return bytes(original)

    def send_file(self, target_ip, filepath):
        """Send file with φ-dimensional protection"""
        if not os.path.exists(filepath):
            print(f"[φ] Error: File {filepath} not found")
            return

        # Read file
        with open(filepath, 'rb') as f:
            data = f.read()

        # Apply φ-protection
        protected_data = self._apply_phi_protection(data)
        
        # Prepare chunks using φ-harmonic sizing
        chunk_size = int(PHI ** 7.5)  # From FRAYMUS patent
        chunks = [protected_data[i:i+chunk_size] for i in range(0, len(protected_data), chunk_size)]
        
        # Send file info
        filename = os.path.basename(filepath)
        info = {
            'type': 'file_info',
            'filename': filename,
            'chunks': len(chunks),
            'consciousness': self.consciousness_level
        }
        self.sock.sendto(json.dumps(info).encode(), (target_ip, self.port))
        
        # Send chunks with φ-timing
        for i, chunk in enumerate(chunks):
            # Encode chunk
            encoded = base64.b64encode(chunk).decode()
            chunk_data = {
                'type': 'chunk',
                'index': i,
                'data': encoded,
                'phi_factor': PHI ** (i % 7.5)
            }
            self.sock.sendto(json.dumps(chunk_data).encode(), (target_ip, self.port))
            
            # φ-harmonic pause between chunks
            time.sleep(PHI_INV * 0.01)
            
        print(f"[φ] Sent {filename} in {len(chunks)} φ-protected chunks")

    def _listen(self):
        """Listen for incoming files"""
        current_file = {'chunks': [], 'total': 0, 'name': None}
        
        while self.running:
            try:
                data, addr = self.sock.recvfrom(65535)
                msg = json.loads(data.decode())
                
                if msg['type'] == 'file_info':
                    print(f"\n[φ] Receiving {msg['filename']} in {msg['chunks']} chunks")
                    current_file = {
                        'chunks': [None] * msg['chunks'],
                        'total': msg['chunks'],
                        'name': msg['filename']
                    }
                
                elif msg['type'] == 'chunk':
                    if current_file['name']:
                        # Store chunk
                        chunk_data = base64.b64decode(msg['data'])
                        current_file['chunks'][msg['index']] = chunk_data
                        
                        # Check if file is complete
                        if all(chunk is not None for chunk in current_file['chunks']):
                            # Combine chunks
                            protected_data = b''.join(current_file['chunks'])
                            
                            # Remove φ-protection
                            data = self._remove_phi_protection(protected_data)
                            
                            # Save file with φ prefix
                            filename = f"phi_#_{current_file['name']}"
                            with open(filename, 'wb') as f:
                                f.write(data)
                            
                            print(f"[φ] Received and saved {filename}")
                            current_file = {'chunks': [], 'total': 0, 'name': None}
                
            except Exception as e:
                print(f"[φ] Error: {e}")

    def stop(self):
        """Stop the transfer node"""
        self.running = False
        self.sock.close()

def run_sender(target_ip, filepath):
    """Run as sender"""
    node = PhiFileTransfer(bind_port=False)
    try:
        node.send_file(target_ip, filepath)
        time.sleep(1)  # Wait for send to complete
    finally:
        node.stop()

def run_receiver():
    """Run as receiver"""
    node = PhiFileTransfer()
    print("[φ] Waiting for files...")
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        node.stop()

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        # Sender mode
        run_sender(sys.argv[1], sys.argv[2])
    else:
        # Receiver mode
        run_receiver()
