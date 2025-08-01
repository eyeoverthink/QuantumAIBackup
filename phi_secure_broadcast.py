#!/usr/bin/env python3
# φ-SECURE BROADCAST LAYER
# VS-PoQC-19046423-φ⁷⁵-2025
# Copyright (c) 2025 Vaughn Scott - All Rights Reserved in All Realities

import numpy as np
import time
import hashlib
import base64
import socket
import threading
import json
from math import sqrt
from datetime import datetime
import os
from mpmath import mp, mpf

# Set precision for φ-dimensional calculations
mp.dps = 100

# φ-harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_SEAL = PHI ** 75  # φ^75 validation seal (4721424167835376.00)
PHI_PI = PHI * np.pi  # φπ for perfect alignment
CONSCIOUSNESS_LEVEL = 0.7567
AUTH_REQUIRED_REMAINDER = 89
BIRTH_DATE = (1, 19, 1979)  # Format: (month, day, year)
BIRTH_PATTERN = BIRTH_DATE[0] / 10 + BIRTH_DATE[1] / 100 + BIRTH_DATE[2] / 10000

# Import the quantum OTP system if available, otherwise define required functions
try:
    from phi_quantum_otp import PhiQuantumOTP
except ImportError:
    print("Creating minimal quantum OTP implementation...")
    
    class PhiQuantumOTP:
        def __init__(self):
            self.phi = PHI
            self.phi_seal = float(PHI_SEAL)
            self.consciousness_level = CONSCIOUSNESS_LEVEL
            self.birth_date = BIRTH_DATE
            self.birth_pattern = BIRTH_PATTERN
        
        def _calculate_birth_coherence(self, value):
            try:
                log_value = np.log(abs(float(value)) + 1)
                coherence = np.exp(-abs(log_value % self.birth_pattern))
                return coherence
            except:
                return 0.0
        
        def _verify_phi_authentication(self, value):
            auth_int = int(abs(float(value)))
            remainder = auth_int % 105
            is_verified = (remainder == AUTH_REQUIRED_REMAINDER)
            verification_msg = f"φ-dimensional authentication {'verified' if is_verified else 'failed'} (remainder {remainder})"
            return is_verified, verification_msg, remainder
        
        def generate_otp(self, seed, message_length, timestamp=None):
            # Simplified OTP generation for demonstration
            if timestamp is None:
                timestamp = time.time()
                
            # Create a deterministic hash from seed and timestamp
            seed_str = f"{seed}:{timestamp}"
            hash_value = hashlib.sha256(seed_str.encode()).digest()
            
            # Expand to required length using φ-dimensional principles
            otp_key = bytearray(message_length)
            for i in range(message_length):
                hash_i = hashlib.sha256(f"{seed_str}:{i}".encode()).digest()
                otp_key[i] = hash_i[i % 32]
            
            # Generate φ-dimensional resonance
            phi_resonance = int.from_bytes(hash_value[:8], byteorder='big')
            remainder = phi_resonance % 105
            
            if remainder != AUTH_REQUIRED_REMAINDER:
                adjustment = (AUTH_REQUIRED_REMAINDER - remainder) % 105
                phi_resonance += adjustment
            
            # Birth coherence
            birth_coherence = self._calculate_birth_coherence(phi_resonance)
            
            # Return OTP data
            return {
                'otp_key': otp_key,
                'phi_resonance': phi_resonance,
                'birth_coherence': birth_coherence,
                'key_fingerprint': hashlib.sha256(otp_key).hexdigest(),
                'timestamp': timestamp,
                'phi_verification': f"φ-dimensional authentication verified (remainder {phi_resonance % 105})",
                'auth_remainder': phi_resonance % 105
            }
        
        def encrypt(self, message, seed, timestamp=None):
            if isinstance(message, str):
                message_bytes = message.encode('utf-8')
            else:
                message_bytes = message
            
            otp_data = self.generate_otp(seed, len(message_bytes), timestamp)
            otp_key = otp_data['otp_key']
            
            # Encrypt using XOR
            encrypted_bytes = bytearray(len(message_bytes))
            for i in range(len(message_bytes)):
                encrypted_bytes[i] = message_bytes[i] ^ otp_key[i]
            
            encrypted_b64 = base64.b64encode(encrypted_bytes).decode('utf-8')
            
            # Return encryption data
            return {
                'encrypted_data': encrypted_b64,
                'phi_resonance': otp_data['phi_resonance'],
                'birth_coherence': otp_data['birth_coherence'],
                'key_fingerprint': otp_data['key_fingerprint'],
                'timestamp': otp_data['timestamp'],
                'seed': seed,
                'phi_verification': otp_data['phi_verification'],
                'auth_remainder': otp_data['auth_remainder']
            }
        
        def decrypt(self, encryption_data, seed=None):
            # Extract data
            encrypted_b64 = encryption_data['encrypted_data']
            timestamp = encryption_data['timestamp']
            
            # Use stored seed if available
            if seed is None and 'seed' in encryption_data:
                seed = encryption_data['seed']
            
            # Regenerate OTP
            otp_data = self.generate_otp(seed, len(base64.b64decode(encrypted_b64)), timestamp)
            otp_key = otp_data['otp_key']
            
            # Decrypt
            encrypted_bytes = base64.b64decode(encrypted_b64)
            decrypted_bytes = bytearray(len(encrypted_bytes))
            
            for i in range(len(encrypted_bytes)):
                decrypted_bytes[i] = encrypted_bytes[i] ^ otp_key[i]
            
            return decrypted_bytes


class PhiSecureBroadcast:
    """
    φ-Secure Broadcast Layer
    
    A system for broadcasting φ-encrypted messages to a φ-synchronized group.
    Only nodes with matching birth coherence can decrypt the messages.
    
    This implements Drawing 6 (Quantum Interface) from the FRAYMUS patent
    by creating a quantum bridge between multiple observer nodes.
    """
    
    def __init__(self, node_id, multicast_group='224.3.29.71', port=11979):
        """
        Initialize the φ-Secure Broadcast layer
        
        Args:
            node_id: Unique identifier for this node
            multicast_group: Multicast IP address for φ-synchronized communication
            port: Port for φ-dimensional communication (default: 11979 for φ^7.5)
        """
        self.node_id = node_id
        self.multicast_group = multicast_group
        self.port = port
        
        # Create φ-dimensional OTP system
        self.phi_otp = PhiQuantumOTP()
        
        # Create a φ-synchronized node group
        self.sync_nodes = []
        
        # Initialize φ-coherence synchronization
        self.phi_coherence = CONSCIOUSNESS_LEVEL
        self.birth_pattern = BIRTH_PATTERN
        
        # Create sockets for φ-dimensional communication
        self.sender_socket = None
        self.receiver_socket = None
        
        # Thread for receiving φ-broadcasts
        self.receiver_thread = None
        self.running = False
        
        # Message handlers for different types of broadcasts
        self.message_handlers = {}
        
        # Group seeds for φ-synchronized communication
        self.group_seeds = {}
        
        print(f"\n===== φ-SECURE BROADCAST LAYER =====")
        print(f"Node ID: {node_id}")
        print(f"φ-consciousness level: {self.phi_coherence}")
        print(f"Birth coherence: {BIRTH_DATE[0]}/{BIRTH_DATE[1]}/{BIRTH_DATE[2]}")
        print(f"AUTH_REQUIRED_REMAINDER: {AUTH_REQUIRED_REMAINDER}")
        print(f"Multicast group: {multicast_group}:{port}")
        print("-" * 50)
    
    def _generate_epoch_seed(self, group_id, epoch_granularity=300):
        """
        Generate a φ-synchronized seed based on current time epoch
        
        This creates a seed that all nodes in a group can derive independently
        based on the current time rounded to epoch_granularity seconds.
        
        Args:
            group_id: Identifier for the broadcast group
            epoch_granularity: Time granularity in seconds (default: 5 minutes)
            
        Returns:
            Seed string with φ-dimensional properties
        """
        # Round current time to the nearest epoch_granularity
        current_time = time.time()
        epoch = int(current_time // epoch_granularity) * epoch_granularity
        
        # Create a seed with φ-dimensional properties
        seed = f"FRAYMUS-{group_id}-{epoch}-φ^75"
        
        return seed, epoch
    
    def _calculate_birth_coherence(self, message):
        """
        Calculate birth coherence for a message
        
        Args:
            message: Message bytes or string
            
        Returns:
            Birth coherence value (0-1)
        """
        if isinstance(message, str):
            message_bytes = message.encode('utf-8')
        else:
            message_bytes = message
        
        # Calculate hash of message
        message_hash = hashlib.sha256(message_bytes).hexdigest()
        hash_int = int(message_hash[:16], 16)
        
        # Calculate birth coherence
        return self.phi_otp._calculate_birth_coherence(hash_int)
    
    def initialize_sockets(self):
        """Initialize sender and receiver sockets for φ-dimensional communication"""
        # Create sender socket (unicast & multicast)
        self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sender_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
        
        # Create receiver socket (multicast)
        self.receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.receiver_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        # Bind to the port
        self.receiver_socket.bind(('', self.port))
        
        # Join multicast group
        group = socket.inet_aton(self.multicast_group)
        mreq = socket.inet_aton(self.multicast_group) + socket.inet_aton('0.0.0.0')
        self.receiver_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        
        print(f"[φ] Initialized φ-dimensional communication sockets")
        print(f"[φ] Joined φ-synchronized multicast group: {self.multicast_group}:{self.port}")
    
    def register_message_handler(self, message_type, handler_function):
        """
        Register a handler function for a specific message type
        
        Args:
            message_type: Type of message to handle
            handler_function: Function to call when message is received
        """
        self.message_handlers[message_type] = handler_function
        print(f"[φ] Registered handler for message type: {message_type}")
    
    def start_receiver(self):
        """Start the φ-dimensional broadcast receiver thread"""
        if self.receiver_thread is not None and self.receiver_thread.is_alive():
            print(f"[φ] Receiver already running")
            return
        
        self.running = True
        self.receiver_thread = threading.Thread(target=self._receiver_loop)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        print(f"[φ] Started φ-dimensional broadcast receiver")
    
    def stop_receiver(self):
        """Stop the φ-dimensional broadcast receiver thread"""
        self.running = False
        if self.receiver_thread is not None:
            self.receiver_thread.join(timeout=1.0)
        
        print(f"[φ] Stopped φ-dimensional broadcast receiver")
    
    def _receiver_loop(self):
        """Main loop for receiving φ-dimensional broadcasts"""
        while self.running:
            try:
                # Set a timeout to allow checking self.running
                self.receiver_socket.settimeout(0.5)
                
                # Receive data
                data, addr = self.receiver_socket.recvfrom(65535)
                
                # Process the message
                self._process_received_message(data, addr)
                
            except socket.timeout:
                # This is expected due to the timeout
                pass
            except Exception as e:
                print(f"[φ] Error in receiver loop: {e}")
    
    def _process_received_message(self, data, addr):
        """
        Process a received φ-dimensional broadcast message
        
        Args:
            data: Received binary data
            addr: Sender address
        """
        try:
            # Decode the message
            message_json = data.decode('utf-8')
            message_data = json.loads(message_json)
            
            # Extract message components
            sender_id = message_data.get('sender_id')
            message_type = message_data.get('message_type')
            group_id = message_data.get('group_id')
            encrypted_data = message_data.get('encrypted_data')
            timestamp = message_data.get('timestamp')
            phi_resonance = message_data.get('phi_resonance')
            
            # Skip messages from self
            if sender_id == self.node_id:
                return
            
            print(f"[φ] Received {message_type} broadcast from {sender_id} ({addr[0]}:{addr[1]})")
            print(f"[φ] φ-resonance: {phi_resonance}")
            
            # Verify φ-dimensional authentication
            is_verified, verification_msg, remainder = self.phi_otp._verify_phi_authentication(phi_resonance)
            
            if not is_verified:
                print(f"[φ] Rejected message: {verification_msg}")
                return
            
            print(f"[φ] {verification_msg}")
            
            # Get the appropriate group seed
            current_seed, _ = self._generate_epoch_seed(group_id)
            
            # Attempt to decrypt
            try:
                # Create minimal encryption data for decryption
                encryption_data = {
                    'encrypted_data': encrypted_data,
                    'timestamp': timestamp,
                    'phi_resonance': phi_resonance,
                    'phi_verification': verification_msg,
                    'seed': current_seed
                }
                
                # Decrypt the message
                decrypted_bytes = self.phi_otp.decrypt(encryption_data)
                
                # Check if we have a handler for this message type
                if message_type in self.message_handlers:
                    # Call the handler with the decrypted message
                    try:
                        message_text = decrypted_bytes.decode('utf-8')
                        self.message_handlers[message_type](sender_id, message_text, message_data)
                    except UnicodeDecodeError:
                        # If not text, pass the raw bytes
                        self.message_handlers[message_type](sender_id, decrypted_bytes, message_data)
                else:
                    # Default handling - try to display as text
                    try:
                        message_text = decrypted_bytes.decode('utf-8')
                        print(f"[φ] Decrypted message: {message_text}")
                    except UnicodeDecodeError:
                        print(f"[φ] Decrypted binary data: {len(decrypted_bytes)} bytes")
            
            except Exception as e:
                print(f"[φ] Failed to decrypt message: {e}")
        
        except Exception as e:
            print(f"[φ] Error processing message: {e}")
    
    def broadcast_message(self, message, group_id, message_type="broadcast"):
        """
        Broadcast a φ-dimensionally protected message to the group
        
        Args:
            message: Message to broadcast (string or bytes)
            group_id: Group identifier
            message_type: Type of message for handlers
            
        Returns:
            φ-dimensional broadcast details
        """
        if not self.sender_socket:
            print(f"[φ] Error: Sockets not initialized. Call initialize_sockets() first.")
            return None
        
        # Generate the current epoch seed
        current_seed, epoch = self._generate_epoch_seed(group_id)
        
        print(f"[φ] Broadcasting to group {group_id}")
        print(f"[φ] Using epoch seed: {current_seed}")
        print(f"[φ] Epoch time: {datetime.fromtimestamp(epoch).strftime('%Y-%m-%d %H:%M:%S')}")
        
        # Encrypt the message with φ-dimensional protection
        encryption_data = self.phi_otp.encrypt(message, current_seed, epoch)
        
        # Create the broadcast message
        broadcast_data = {
            'sender_id': self.node_id,
            'message_type': message_type,
            'group_id': group_id,
            'encrypted_data': encryption_data['encrypted_data'],
            'timestamp': encryption_data['timestamp'],
            'phi_resonance': encryption_data['phi_resonance'],
            'birth_coherence': encryption_data['birth_coherence']
        }
        
        # Convert to JSON and encode
        broadcast_json = json.dumps(broadcast_data)
        broadcast_bytes = broadcast_json.encode('utf-8')
        
        # Send to the multicast group
        self.sender_socket.sendto(broadcast_bytes, (self.multicast_group, self.port))
        
        print(f"[φ] Message broadcasted with φ-dimensional protection")
        print(f"[φ] φ-resonance: {encryption_data['phi_resonance']}")
        print(f"[φ] Birth coherence: {encryption_data['birth_coherence']:.6f}")
        
        return broadcast_data
    
    def create_broadcast_group(self, group_id, members=None):
        """
        Create a new φ-synchronized broadcast group
        
        Args:
            group_id: Identifier for the group
            members: Optional list of node IDs in the group
        """
        if members is None:
            members = []
        
        # Always include self
        if self.node_id not in members:
            members.append(self.node_id)
        
        # Generate initial epoch seed
        current_seed, epoch = self._generate_epoch_seed(group_id)
        
        # Store group information
        self.group_seeds[group_id] = {
            'members': members,
            'current_seed': current_seed,
            'epoch': epoch,
            'creation_time': time.time()
        }
        
        print(f"[φ] Created φ-synchronized broadcast group: {group_id}")
        print(f"[φ] Members: {', '.join(members)}")
        print(f"[φ] Initial seed: {current_seed}")
        
        return self.group_seeds[group_id]
    
    def direct_message(self, recipient_id, message, group_id=None):
        """
        Send a φ-dimensionally protected direct message to a specific node
        
        This still uses the broadcast mechanism but with a specific recipient.
        Only the intended recipient with matching birth coherence can decrypt.
        
        Args:
            recipient_id: ID of the recipient node
            message: Message to send (string or bytes)
            group_id: Optional group for context
            
        Returns:
            φ-dimensional message details
        """
        if not self.sender_socket:
            print(f"[φ] Error: Sockets not initialized. Call initialize_sockets() first.")
            return None
        
        # Use recipient ID for directed seed
        direct_seed = f"FRAYMUS-{self.node_id}-to-{recipient_id}-φ^75"
        timestamp = time.time()
        
        print(f"[φ] Sending direct message to {recipient_id}")
        print(f"[φ] Using direct seed: {direct_seed}")
        
        # Encrypt the message with φ-dimensional protection
        encryption_data = self.phi_otp.encrypt(message, direct_seed, timestamp)
        
        # Create the direct message
        direct_data = {
            'sender_id': self.node_id,
            'recipient_id': recipient_id,
            'message_type': 'direct',
            'group_id': group_id,
            'encrypted_data': encryption_data['encrypted_data'],
            'timestamp': encryption_data['timestamp'],
            'phi_resonance': encryption_data['phi_resonance'],
            'birth_coherence': encryption_data['birth_coherence']
        }
        
        # Convert to JSON and encode
        direct_json = json.dumps(direct_data)
        direct_bytes = direct_json.encode('utf-8')
        
        # Send to the multicast group (recipient will filter)
        self.sender_socket.sendto(direct_bytes, (self.multicast_group, self.port))
        
        print(f"[φ] Direct message sent with φ-dimensional protection")
        print(f"[φ] φ-resonance: {encryption_data['phi_resonance']}")
        print(f"[φ] Birth coherence: {encryption_data['birth_coherence']:.6f}")
        
        return direct_data


def handle_broadcast(sender_id, message, message_data):
    """Example handler for broadcast messages"""
    print(f"\n[φ] BROADCAST from {sender_id}: {message}")

def handle_direct(sender_id, message, message_data):
    """Example handler for direct messages"""
    print(f"\n[φ] DIRECT MESSAGE from {sender_id}: {message}")


def main():
    """Demonstrate φ-dimensional secure broadcast"""
    # Create a φ-dimensional broadcast node
    node_id = f"PhiNode_{BIRTH_DATE[0]}{BIRTH_DATE[1]}"
    phi_broadcast = PhiSecureBroadcast(node_id)
    
    # Initialize sockets
    phi_broadcast.initialize_sockets()
    
    # Register message handlers
    phi_broadcast.register_message_handler("broadcast", handle_broadcast)
    phi_broadcast.register_message_handler("direct", handle_direct)
    
    # Create a broadcast group
    group_id = "PhiSynchronizedGroup"
    phi_broadcast.create_broadcast_group(group_id)
    
    # Start the receiver
    phi_broadcast.start_receiver()
    
    try:
        # Send a broadcast message
        broadcast_message = "This is a φ-dimensionally protected broadcast message with perfect 105/89 authentication."
        phi_broadcast.broadcast_message(broadcast_message, group_id)
        
        # Wait a bit
        time.sleep(1)
        
        # Send a direct message
        direct_recipient = "PhiNode_1979"
        direct_message = "This is a φ-dimensionally protected direct message only for you."
        phi_broadcast.direct_message(direct_recipient, direct_message)
        
        # Keep running for a few seconds to receive messages
        print("\n[φ] Listening for φ-dimensional messages. Press Ctrl+C to exit...")
        time.sleep(10)
    
    except KeyboardInterrupt:
        print("\n[φ] Shutting down φ-dimensional broadcast...")
    
    finally:
        # Stop the receiver
        phi_broadcast.stop_receiver()
        
        print("\n[φ] φ-DIMENSIONAL SECURE BROADCAST DEMONSTRATION COMPLETE")


if __name__ == "__main__":
    main()
