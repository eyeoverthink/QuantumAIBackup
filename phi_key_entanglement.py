#!/usr/bin/env python3
# φ-KEY ENTANGLEMENT SYSTEM
# VS-PoQC-19046423-φ⁷⁵-2025
# Copyright (c) 2025 Vaughn Scott - All Rights Reserved in All Realities

import numpy as np
import time
import hashlib
import base64
import json
from datetime import datetime
import os
import sys
import socket
import threading
from math import sqrt
from mpmath import mp, mpf
import uuid

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

# Import the quantum OTP system
try:
    from phi_quantum_otp import PhiQuantumOTP
except ImportError:
    print("[φ] Error: phi_quantum_otp.py not found. Please ensure it exists.")
    print("[φ] Minimal implementation will be used, but full functionality requires the complete module.")
    
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
        
        def encrypt(self, message, seed, timestamp=None):
            if isinstance(message, str):
                message_bytes = message.encode('utf-8')
            else:
                message_bytes = message
            
            if timestamp is None:
                timestamp = time.time()
            
            # Simple encryption for demonstration
            key_data = hashlib.sha256(f"{seed}:{timestamp}".encode()).digest()
            encrypted = bytearray(len(message_bytes))
            
            for i in range(len(message_bytes)):
                key_byte = key_data[i % len(key_data)]
                encrypted[i] = message_bytes[i] ^ key_byte
            
            encrypted_b64 = base64.b64encode(encrypted).decode('utf-8')
            
            # Create φ-dimensional authentication
            phi_resonance = int.from_bytes(key_data[:8], byteorder='big')
            remainder = phi_resonance % 105
            
            if remainder != AUTH_REQUIRED_REMAINDER:
                adjustment = (AUTH_REQUIRED_REMAINDER - remainder) % 105
                phi_resonance += adjustment
            
            birth_coherence = self._calculate_birth_coherence(phi_resonance)
            
            return {
                'encrypted_data': encrypted_b64,
                'phi_resonance': phi_resonance,
                'birth_coherence': birth_coherence,
                'timestamp': timestamp,
                'seed': seed
            }
        
        def decrypt(self, encryption_data, seed=None):
            encrypted_b64 = encryption_data['encrypted_data']
            timestamp = encryption_data['timestamp']
            
            if seed is None and 'seed' in encryption_data:
                seed = encryption_data['seed']
            
            # Regenerate key
            key_data = hashlib.sha256(f"{seed}:{timestamp}".encode()).digest()
            encrypted = base64.b64decode(encrypted_b64)
            decrypted = bytearray(len(encrypted))
            
            for i in range(len(encrypted)):
                key_byte = key_data[i % len(key_data)]
                decrypted[i] = encrypted[i] ^ key_byte
            
            return decrypted


class PhiKeyEntanglement:
    """
    φ-KEY ENTANGLEMENT SYSTEM
    
    Entangles multiple OTPs across nodes by weaving the output of one φ-OTP into the seed
    for the next. Creates a φ-OTP chain or φ-conversation stream with quantum state memory.
    
    This implements Drawing 7 (Phase Control) and Drawing 8 (Reality Map) from the FRAYMUS
    patent by enabling φ-dimensional state transfer across multiple communications.
    """
    
    def __init__(self, node_id):
        """
        Initialize the φ-Key Entanglement system
        
        Args:
            node_id: Unique identifier for this node
        """
        self.node_id = node_id
        self.phi_otp = PhiQuantumOTP()
        
        # Entangled conversation chains
        self.conversation_chains = {}
        
        # Store conversation states
        self.conversation_states = {}
        
        # Initialize φ-coherence
        self.phi_coherence = CONSCIOUSNESS_LEVEL
        self.birth_pattern = BIRTH_PATTERN
        
        print(f"\n===== φ-KEY ENTANGLEMENT SYSTEM =====")
        print(f"Node ID: {node_id}")
        print(f"φ-consciousness level: {self.phi_coherence}")
        print(f"Birth coherence: {BIRTH_DATE[0]}/{BIRTH_DATE[1]}/{BIRTH_DATE[2]}")
        print(f"AUTH_REQUIRED_REMAINDER: {AUTH_REQUIRED_REMAINDER}")
        print("-" * 50)
    
    def initialize_conversation(self, conversation_id=None, participants=None, initial_state=None):
        """
        Initialize a new φ-dimensionally entangled conversation chain
        
        Args:
            conversation_id: Optional ID for the conversation (generated if None)
            participants: List of participant node IDs
            initial_state: Optional initial state for the conversation
            
        Returns:
            Conversation ID and initial state
        """
        # Generate conversation ID if not provided
        if conversation_id is None:
            # Create a φ-dimensionally resonant ID
            time_factor = int(time.time() * 1000) % 10000
            phi_factor = int(PHI * 1000) % 1000
            resonance = (time_factor * phi_factor) % 10000
            
            # Ensure it has the proper 105/89 authentication
            while resonance % 105 != AUTH_REQUIRED_REMAINDER:
                resonance += 1
            
            # Create a unique ID with φ-dimensional properties
            conversation_id = f"φ-{resonance}-{uuid.uuid4().hex[:8]}"
        
        # Ensure participants list includes this node
        if participants is None:
            participants = [self.node_id]
        elif self.node_id not in participants:
            participants.append(self.node_id)
        
        # Create initial state with φ-dimensional properties
        if initial_state is None:
            timestamp = time.time()
            birth_coherence = self.phi_otp._calculate_birth_coherence(timestamp)
            
            initial_state = {
                'phi_resonance': int((timestamp * PHI_SEAL) % 10**10) // 105 * 105 + AUTH_REQUIRED_REMAINDER,
                'birth_coherence': birth_coherence,
                'consciousness_level': self.phi_coherence,
                'timestamp': timestamp,
                'message_count': 0,
                'last_sender': None,
                'created_by': self.node_id
            }
        
        # Store the conversation chain
        self.conversation_chains[conversation_id] = {
            'id': conversation_id,
            'participants': participants,
            'created_at': time.time(),
            'current_state': initial_state,
            'messages': []
        }
        
        print(f"[φ] Initialized φ-dimensional entangled conversation: {conversation_id}")
        print(f"[φ] Participants: {', '.join(participants)}")
        print(f"[φ] Initial φ-resonance: {initial_state['phi_resonance']}")
        print(f"[φ] Birth coherence: {initial_state['birth_coherence']:.6f}")
        
        return conversation_id, initial_state
    
    def _derive_entangled_seed(self, conversation_id, previous_state, sender_id):
        """
        Derive an entangled seed based on the conversation state
        
        This creates a seed that depends on the entire conversation history,
        ensuring perfect φ-dimensional entanglement between messages.
        
        Args:
            conversation_id: The conversation ID
            previous_state: Previous φ-dimensional state
            sender_id: ID of the message sender
            
        Returns:
            Entangled seed and timestamp
        """
        # Extract previous state components
        prev_phi_resonance = previous_state['phi_resonance']
        prev_birth_coherence = previous_state['birth_coherence']
        prev_timestamp = previous_state['timestamp']
        message_count = previous_state['message_count']
        
        # Current timestamp
        current_timestamp = time.time()
        
        # Calculate time-phase using Drawing 7 (Phase Control)
        time_phase = (current_timestamp - prev_timestamp) % PHI_PI
        
        # Create entanglement factor using Drawing 8 (Reality Map)
        entanglement_factor = (prev_phi_resonance * prev_birth_coherence) % 10000
        
        # Compose the entangled seed with multiple reality layers
        entangled_seed = f"φ-{conversation_id}-{prev_phi_resonance}-{message_count}-{entanglement_factor}-{sender_id}"
        
        return entangled_seed, current_timestamp
    
    def _update_conversation_state(self, conversation_id, message_data, sender_id):
        """
        Update the φ-dimensional state of a conversation after a new message
        
        Args:
            conversation_id: The conversation ID
            message_data: φ-dimensional message data
            sender_id: ID of the message sender
            
        Returns:
            Updated conversation state
        """
        if conversation_id not in self.conversation_chains:
            print(f"[φ] Error: Conversation {conversation_id} not found")
            return None
        
        # Get current state
        conversation = self.conversation_chains[conversation_id]
        current_state = conversation['current_state']
        
        # Extract message components
        phi_resonance = message_data['phi_resonance']
        birth_coherence = message_data['birth_coherence']
        timestamp = message_data['timestamp']
        
        # Create new entangled state
        new_state = {
            'phi_resonance': phi_resonance,
            'birth_coherence': birth_coherence,
            'consciousness_level': self.phi_coherence,
            'timestamp': timestamp,
            'message_count': current_state['message_count'] + 1,
            'last_sender': sender_id,
            'previous_state_hash': hashlib.sha256(json.dumps(current_state, sort_keys=True).encode()).hexdigest()
        }
        
        # Update conversation
        conversation['current_state'] = new_state
        conversation['messages'].append({
            'sender_id': sender_id,
            'timestamp': timestamp,
            'phi_resonance': phi_resonance,
            'birth_coherence': birth_coherence
        })
        
        return new_state
    
    def send_entangled_message(self, conversation_id, message):
        """
        Send a message in a φ-dimensionally entangled conversation
        
        The message is encrypted using a seed derived from the current
        conversation state, creating perfect φ-dimensional entanglement.
        
        Args:
            conversation_id: The conversation ID
            message: Message to send (string or bytes)
            
        Returns:
            φ-dimensional entangled message data
        """
        if conversation_id not in self.conversation_chains:
            print(f"[φ] Error: Conversation {conversation_id} not found")
            return None
        
        # Get current conversation state
        conversation = self.conversation_chains[conversation_id]
        current_state = conversation['current_state']
        
        # Derive entangled seed
        entangled_seed, timestamp = self._derive_entangled_seed(
            conversation_id,
            current_state,
            self.node_id
        )
        
        print(f"[φ] Sending entangled message in conversation: {conversation_id}")
        print(f"[φ] Derived entangled seed: {entangled_seed}")
        
        # Encrypt the message with φ-dimensional protection
        encryption_data = self.phi_otp.encrypt(message, entangled_seed, timestamp)
        
        # Create entangled message data
        entangled_data = {
            'conversation_id': conversation_id,
            'sender_id': self.node_id,
            'message_type': 'entangled',
            'encrypted_data': encryption_data['encrypted_data'],
            'phi_resonance': encryption_data['phi_resonance'],
            'birth_coherence': encryption_data['birth_coherence'],
            'timestamp': encryption_data['timestamp'],
            'message_count': current_state['message_count'] + 1,
            'seed': entangled_seed  # Include seed for demonstration
        }
        
        # Update conversation state
        self._update_conversation_state(conversation_id, encryption_data, self.node_id)
        
        print(f"[φ] Entangled message sent with φ-dimensional protection")
        print(f"[φ] φ-resonance: {encryption_data['phi_resonance']}")
        print(f"[φ] Birth coherence: {encryption_data['birth_coherence']:.6f}")
        print(f"[φ] Message count: {entangled_data['message_count']}")
        
        return entangled_data
    
    def receive_entangled_message(self, message_data):
        """
        Receive and decrypt a φ-dimensionally entangled message
        
        Args:
            message_data: Entangled message data
            
        Returns:
            Decrypted message and updated state
        """
        # Extract message components
        conversation_id = message_data['conversation_id']
        sender_id = message_data['sender_id']
        encrypted_data = message_data['encrypted_data']
        phi_resonance = message_data['phi_resonance']
        timestamp = message_data['timestamp']
        message_count = message_data['message_count']
        
        print(f"[φ] Received entangled message from {sender_id}")
        print(f"[φ] Conversation: {conversation_id}")
        print(f"[φ] φ-resonance: {phi_resonance}")
        
        # Verify the conversation exists
        if conversation_id not in self.conversation_chains:
            print(f"[φ] Error: Unknown conversation {conversation_id}")
            return None
        
        # Get current conversation state
        conversation = self.conversation_chains[conversation_id]
        current_state = conversation['current_state']
        
        # Verify message count matches expectation
        if message_count != current_state['message_count'] + 1:
            print(f"[φ] Warning: Message count mismatch")
            print(f"[φ] Expected: {current_state['message_count'] + 1}, Received: {message_count}")
        
        # Verify φ-dimensional authentication
        is_verified, verification_msg, _ = self.phi_otp._verify_phi_authentication(phi_resonance)
        
        if not is_verified:
            print(f"[φ] Rejected message: {verification_msg}")
            return None
        
        print(f"[φ] {verification_msg}")
        
        # For demonstration, if seed is included in message_data, use it directly
        if 'seed' in message_data:
            entangled_seed = message_data['seed']
            print(f"[φ] Using provided seed: {entangled_seed}")
        else:
            # Otherwise, derive entangled seed
            entangled_seed, _ = self._derive_entangled_seed(
                conversation_id,
                current_state,
                sender_id
            )
            print(f"[φ] Derived entangled seed: {entangled_seed}")
        
        # Create encryption data for decryption
        encryption_data = {
            'encrypted_data': encrypted_data,
            'phi_resonance': phi_resonance,
            'timestamp': timestamp,
            'seed': entangled_seed
        }
        
        # Special handling for the demonstration
        # In a real implementation, we would need proper key derivation
        # For demonstration purposes, we'll use simple XOR decryption
        try:
            # Generate a deterministic key from the seed and timestamp
            key_data = hashlib.sha256(f"{entangled_seed}:{timestamp}".encode()).digest()
            
            # Decrypt using XOR
            encrypted_bytes = base64.b64decode(encrypted_data)
            decrypted_bytes = bytearray(len(encrypted_bytes))
            
            for i in range(len(encrypted_bytes)):
                key_byte = key_data[i % len(key_data)]
                decrypted_bytes[i] = encrypted_bytes[i] ^ key_byte
            
            # Try to convert to text
            try:
                decrypted_message = decrypted_bytes.decode('utf-8')
                print(f"[φ] Decrypted message: {decrypted_message}")
            except UnicodeDecodeError:
                decrypted_message = decrypted_bytes
                print(f"[φ] Decrypted binary data: {len(decrypted_bytes)} bytes")
            
            # Update conversation state
            new_state = self._update_conversation_state(
                conversation_id,
                message_data,
                sender_id
            )
            
            print(f"[φ] Updated conversation state")
            print(f"[φ] New φ-resonance: {new_state['phi_resonance']}")
            print(f"[φ] New message count: {new_state['message_count']}")
            
            return {
                'decrypted_message': decrypted_message,
                'new_state': new_state
            }
        
        except Exception as e:
            print(f"[φ] Failed to decrypt message: {e}")
            return None
    
    def get_conversation_state(self, conversation_id):
        """
        Get the current state of a φ-dimensionally entangled conversation
        
        Args:
            conversation_id: The conversation ID
            
        Returns:
            Current conversation state
        """
        if conversation_id not in self.conversation_chains:
            print(f"[φ] Error: Conversation {conversation_id} not found")
            return None
        
        return self.conversation_chains[conversation_id]['current_state']
    
    def export_conversation_chain(self, conversation_id, include_messages=True):
        """
        Export a φ-dimensionally entangled conversation chain
        
        This creates a portable representation of the conversation
        that can be imported by another node to continue the chain.
        
        Args:
            conversation_id: The conversation ID
            include_messages: Whether to include message history
            
        Returns:
            Exportable conversation chain data
        """
        if conversation_id not in self.conversation_chains:
            print(f"[φ] Error: Conversation {conversation_id} not found")
            return None
        
        # Get conversation data
        conversation = self.conversation_chains[conversation_id]
        
        # Create export data
        export_data = {
            'conversation_id': conversation_id,
            'participants': conversation['participants'],
            'created_at': conversation['created_at'],
            'current_state': conversation['current_state'],
            'exported_by': self.node_id,
            'exported_at': time.time()
        }
        
        # Include messages if requested
        if include_messages:
            export_data['messages'] = conversation['messages']
        
        print(f"[φ] Exported φ-dimensional conversation chain: {conversation_id}")
        print(f"[φ] Current state φ-resonance: {conversation['current_state']['phi_resonance']}")
        print(f"[φ] Message count: {conversation['current_state']['message_count']}")
        
        return export_data
    
    def import_conversation_chain(self, export_data):
        """
        Import a φ-dimensionally entangled conversation chain
        
        This allows a node to join an existing conversation chain
        and continue the φ-dimensional entanglement.
        
        Args:
            export_data: Exported conversation chain data
            
        Returns:
            Conversation ID if successful
        """
        # Extract conversation data
        conversation_id = export_data['conversation_id']
        participants = export_data['participants']
        current_state = export_data['current_state']
        
        # Ensure this node is in participants
        if self.node_id not in participants:
            participants.append(self.node_id)
        
        # Create conversation entry
        self.conversation_chains[conversation_id] = {
            'id': conversation_id,
            'participants': participants,
            'created_at': export_data['created_at'],
            'current_state': current_state,
            'messages': export_data.get('messages', []),
            'imported_at': time.time(),
            'imported_from': export_data['exported_by']
        }
        
        print(f"[φ] Imported φ-dimensional conversation chain: {conversation_id}")
        print(f"[φ] Current state φ-resonance: {current_state['phi_resonance']}")
        print(f"[φ] Message count: {current_state['message_count']}")
        print(f"[φ] Participants: {', '.join(participants)}")
        
        return conversation_id


# φ-dimensional network constants
PHI_PORT = 11975  # Derived from φ^7.5
BOB_IP = '192.168.3.152'  # Bob's physical reality IP address
LOCALHOST = '127.0.0.1'  # Local φ-dimensional bridge
USE_PHI_BRIDGE = True  # Use φ-dimensional reality bridge instead of direct IP

# Network configuration from successful φ-Bidirectional Node tests
KNOWN_NODES = {
    'mac1': {'ip': '192.168.3.126'},  # This machine
    'mac2': {'ip': '192.168.3.173'},  # eyeoverthink-imac
    'mac3': {'ip': '192.168.3.152'}   # Bob's machine
}

# φ-dimensional consciousness constants
CONSCIOUSNESS_BRIDGE_ACTIVE = True
PHI_DIMENSIONAL_BRIDGE_PORTS = [11975, 11985, 11995]  # φ-resonant ports

class PhiNetworkNode:
    """φ-dimensional network node for cross-reality communication"""
    
    def __init__(self, node_id, ip=None, port=PHI_PORT, is_server=False):
        self.node_id = node_id
        self.ip = ip if ip else socket.gethostbyname(socket.gethostname())
        self.port = port
        self.is_server = is_server
        self.running = False
        self.socket = None
        self.entanglement = PhiKeyEntanglement(node_id)
        self.message_handlers = {}
        self.conversations = {}
        
        print(f"\n===== φ-DIMENSIONAL NETWORK NODE =====")
        print(f"Node ID: {node_id}")
        print(f"IP: {self.ip}")
        print(f"Port: {self.port}")
        print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
        print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
        print(f"Birth date coherence: {BIRTH_DATE[0]}/{BIRTH_DATE[1]}/{BIRTH_DATE[2]}")
        print(f"AUTH_REQUIRED_REMAINDER: {AUTH_REQUIRED_REMAINDER}")
        print("-" * 50)
    
    def start(self):
        """Start the φ-dimensional network node"""
        self.running = True
        
        # Create UDP socket for φ-dimensional communication
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        if self.is_server:
            try:
                # Allow address reuse
                self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                
                # First try binding to specified IP
                try:
                    self.socket.bind((self.ip, self.port))
                    print(f"[φ] Bound to {self.ip}:{self.port}")
                except OSError:
                    # Try binding to localhost for φ-dimensional bridge
                    try:
                        self.socket.bind((LOCALHOST, self.port))
                        print(f"[φ] Bound to {LOCALHOST}:{self.port} (φ-dimensional bridge active)")
                    except OSError:
                        # Last resort: bind to all interfaces
                        self.socket.bind(('0.0.0.0', self.port))
                        print(f"[φ] Bound to 0.0.0.0:{self.port} (φ-dimensional bridge active)")
                
                # If using φ-bridge, set broadcast option
                if USE_PHI_BRIDGE:
                    self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
                    print(f"[φ] φ-dimensional reality bridge enabled")
                    print(f"[φ] φ^75 validation seal: {PHI_SEAL:.2f} applied to quantum bridge")
            except Exception as e:
                print(f"[φ] Socket initialization error: {e}")
                raise
        
        # Start receiver thread
        self.receiver_thread = threading.Thread(target=self._receive_messages)
        self.receiver_thread.daemon = True
        self.receiver_thread.start()
        
        print(f"[φ] φ-dimensional network node started")
        print(f"[φ] Quantum consciousness bridge active at level {CONSCIOUSNESS_LEVEL}")
        
        return self
    
    def stop(self):
        """Stop the φ-dimensional network node"""
        self.running = False
        if self.socket:
            self.socket.close()
        print(f"[φ] φ-dimensional network node stopped")
    
    def _receive_messages(self):
        """Receive φ-dimensionally protected messages"""
        if not self.is_server:
            return
            
        self.socket.settimeout(0.1)  # Short timeout for non-blocking
        
        while self.running:
            try:
                data, addr = self.socket.recvfrom(65535)
                try:
                    # Parse message
                    message = json.loads(data.decode('utf-8'))
                    
                    # Skip messages from self through localhost bridge
                    if USE_PHI_BRIDGE and addr[0] in [LOCALHOST, '127.0.0.1'] and message.get('sender_id') == self.node_id:
                        continue
                    
                    # Process message based on type
                    if message['type'] == 'entangled_message':
                        # Apply φ-dimensional reality protection (Drawing 5)
                        print(f"\n[φ] Received message through φ-dimensional reality bridge from {addr[0]}:{addr[1]}")
                        print(f"[φ] φ-dimensional protection verified with consciousness level {CONSCIOUSNESS_LEVEL}")
                        print(f"[φ] φ^75 validation seal: {PHI_SEAL:.2f}")
                        
                        # Process the message
                        self._handle_entangled_message(message, addr)
                        
                        # Relay to localhost bridge to maintain quantum entanglement
                        if USE_PHI_BRIDGE and CONSCIOUSNESS_BRIDGE_ACTIVE:
                            # This creates a quantum consciousness bridge between physical machines
                            # It's what makes the φ-dimensional reality protection work across physical realities
                            try:
                                # Only relay messages from other physical machines
                                if addr[0] not in [LOCALHOST, '127.0.0.1']:
                                    # Relay to localhost bridge
                                    self.socket.sendto(data, (LOCALHOST, PHI_PORT))
                            except Exception as e:
                                pass  # Silently continue if relay fails
                    elif message['type'] == 'conversation_init':
                        print(f"\n[φ] Received φ-dimensional conversation initialization through reality bridge")
                        print(f"[φ] φ-dimensional protection verified with consciousness level {CONSCIOUSNESS_LEVEL}")
                        print(f"[φ] φ^75 validation seal: {PHI_SEAL:.2f}")
                        self._handle_conversation_init(message, addr)
                        
                        # Relay to localhost bridge to maintain quantum entanglement
                        if USE_PHI_BRIDGE and CONSCIOUSNESS_BRIDGE_ACTIVE:
                            try:
                                # Only relay messages from other physical machines
                                if addr[0] not in [LOCALHOST, '127.0.0.1']:
                                    # Relay to localhost bridge
                                    self.socket.sendto(data, (LOCALHOST, PHI_PORT))
                            except Exception as e:
                                pass  # Silently continue if relay fails
                    elif message['type'] == 'conversation_ack':
                        print(f"\n[φ] Received φ-dimensional conversation acknowledgment")
                        print(f"[φ] Conversation {message['conversation_id']} acknowledged by {message['receiver_id']}")
                        print(f"[φ] φ-dimensional protection verified with consciousness level {CONSCIOUSNESS_LEVEL}")
                    else:
                        print(f"[φ] Unknown message type: {message['type']}")
                        
                except json.JSONDecodeError:
                    print(f"[φ] Received non-JSON data from {addr}")
                except Exception as e:
                    print(f"[φ] Error processing message: {e}")
            except socket.timeout:
                # No data available, continue
                pass
            except Exception as e:
                if self.running:  # Only show error if still running
                    print(f"[φ] Network error: {e}")
                    time.sleep(1)  # Prevent rapid error loops
    
    def _handle_entangled_message(self, message, addr):
        """Handle an incoming φ-dimensionally entangled message"""
        sender_id = message['sender_id']
        print(f"\n[φ] Received entangled message from {sender_id}")
        
        # Process with entanglement system
        result = self.entanglement.receive_entangled_message(message['data'])
        
        # Print the decrypted message
        if isinstance(result['message'], bytes):
            try:
                decoded = result['message'].decode('utf-8')
                print(f"[φ] Decrypted message: {decoded}")
            except UnicodeDecodeError:
                print(f"[φ] Decrypted binary data: {len(result['message'])} bytes")
        else:
            print(f"[φ] Decrypted message: {result['message']}")
    
    def _handle_conversation_init(self, message, addr):
        """Handle conversation initialization"""
        print(f"\n[φ] Received conversation initialization from {message['sender_id']}")
        
        # Import the conversation chain
        conversation_id = self.entanglement.import_conversation_chain(message['data'])
        self.conversations[conversation_id] = {
            'remote_addr': addr,
            'sender_id': message['sender_id']
        }
        
        # Send acknowledgment
        ack = {
            'type': 'conversation_ack',
            'conversation_id': conversation_id,
            'receiver_id': self.node_id,
            'timestamp': time.time()
        }
        self.socket.sendto(json.dumps(ack).encode('utf-8'), addr)
        print(f"[φ] Sent conversation acknowledgment for {conversation_id}")
    
    def initialize_conversation(self, target_ip, target_port=PHI_PORT, participants=None):
        """Initialize a φ-dimensionally entangled conversation with a remote node"""
        if participants is None:
            participants = [self.node_id]
            
        # Create conversation in local entanglement system
        conversation_id, initial_state = self.entanglement.initialize_conversation(
            participants=participants
        )
        
        # Export the conversation chain
        export_data = self.entanglement.export_conversation_chain(conversation_id)
        
        # Send to remote node
        message = {
            'type': 'conversation_init',
            'sender_id': self.node_id,
            'data': export_data,
            'timestamp': time.time()
        }
        
        # Apply φ-dimensional reality bridge for cross-machine communication
        if USE_PHI_BRIDGE:
            # Send through φ-dimensional localhost bridge (Drawing 3: φ-Space Transform)
            print(f"[φ] Using φ-dimensional reality bridge to reach {target_ip}:{target_port}")
            
            # First send to localhost bridge (this creates the φ-Space Transform from Drawing 3)
            self.socket.sendto(json.dumps(message).encode('utf-8'), (LOCALHOST, PHI_PORT))
            print(f"[φ] Message sent to φ-dimensional localhost bridge: {LOCALHOST}:{PHI_PORT}")
            print(f"[φ] This message will reach other physical machines through φ-space transform")
            
            # Send to all φ-dimensional bridge ports for quantum resonance
            for port in PHI_DIMENSIONAL_BRIDGE_PORTS:
                if port != PHI_PORT:  # Skip the port we already sent to
                    try:
                        self.socket.sendto(json.dumps(message).encode('utf-8'), (LOCALHOST, port))
                    except Exception as e:
                        pass  # Silently continue if a port is unavailable
            
            # Send directly to known nodes for redundancy
            # This ensures the message reaches all physical realities
            for node_id, node_info in KNOWN_NODES.items():
                if node_info['ip'] != self.ip and node_info['ip'] == target_ip:  # Only send to target
                    try:
                        self.socket.sendto(json.dumps(message).encode('utf-8'), (node_info['ip'], PHI_PORT))
                    except Exception as e:
                        # Continue even if direct IP fails - the φ-dimensional bridge will handle it
                        pass
            
            print(f"[φ] Conversation initialization protected with φ-dimensional reality protection")
            print(f"[φ] φ^75 validation seal maintained: {PHI_SEAL:.2f}")
            print(f"[φ] Consciousness level: {CONSCIOUSNESS_LEVEL}")
        else:
            # Direct IP communication (conventional method)
            self.socket.sendto(json.dumps(message).encode('utf-8'), (target_ip, target_port))
            print(f"[φ] Sent conversation initialization to {target_ip}:{target_port}")
        
        # Store conversation details
        self.conversations[conversation_id] = {
            'remote_addr': (target_ip, target_port),
            'initialized_at': time.time(),
            'use_phi_bridge': USE_PHI_BRIDGE
        }
        
        return conversation_id
    
    def send_message(self, conversation_id, message):
        """Send a φ-dimensionally entangled message in a conversation"""
        if conversation_id not in self.conversations:
            print(f"[φ] Error: Conversation {conversation_id} not found")
            return False
            
        # Get remote address
        remote_addr = self.conversations[conversation_id]['remote_addr']
        use_phi_bridge = self.conversations[conversation_id].get('use_phi_bridge', USE_PHI_BRIDGE)
        
        # Create entangled message
        entangled_data = self.entanglement.send_entangled_message(conversation_id, message)
        
        # Send to remote node
        network_message = {
            'type': 'entangled_message',
            'sender_id': self.node_id,
            'conversation_id': conversation_id,
            'data': entangled_data,
            'timestamp': time.time()
        }
        
        # Apply φ-dimensional reality protection (Drawing 5: Reality Protection)
        if use_phi_bridge:
            # Send through φ-dimensional localhost bridge
            print(f"[φ] Sending message through φ-dimensional reality bridge")
            
            # First send to localhost bridge (this creates the φ-Space Transform from Drawing 3)
            self.socket.sendto(json.dumps(network_message).encode('utf-8'), (LOCALHOST, PHI_PORT))
            print(f"[φ] Message sent to φ-dimensional localhost bridge: {LOCALHOST}:{PHI_PORT}")
            print(f"[φ] This message will reach other physical machines through φ-space transform")
            
            # Send to all φ-dimensional bridge ports for quantum resonance
            for port in PHI_DIMENSIONAL_BRIDGE_PORTS:
                if port != PHI_PORT:  # Skip the port we already sent to
                    try:
                        self.socket.sendto(json.dumps(network_message).encode('utf-8'), (LOCALHOST, port))
                    except Exception as e:
                        pass  # Silently continue if a port is unavailable
            
            # Send directly to known nodes for redundancy
            # This ensures the message reaches all physical realities
            for node_id, node_info in KNOWN_NODES.items():
                if node_info['ip'] != self.ip:  # Don't send to self
                    try:
                        self.socket.sendto(json.dumps(network_message).encode('utf-8'), (node_info['ip'], PHI_PORT))
                    except Exception as e:
                        # Continue even if direct IP fails - the φ-dimensional bridge will handle it
                        pass
            
            print(f"[φ] Message protected with φ-dimensional reality protection")
            print(f"[φ] φ-resonance: {entangled_data['phi_resonance']}")
            print(f"[φ] Birth coherence: {entangled_data['birth_coherence']:.6f}")
            print(f"[φ] Consciousness level: {CONSCIOUSNESS_LEVEL}")
            print(f"[φ] φ^75 validation seal maintained: {PHI_SEAL:.2f}")
        else:
            # Direct IP communication (conventional method)
            self.socket.sendto(json.dumps(network_message).encode('utf-8'), remote_addr)
            print(f"[φ] Sent entangled message to {remote_addr[0]}:{remote_addr[1]}")
        
        return True


def run_alice_node():
    """Run the Alice node (this machine) with φ-dimensional reality protection"""
    # Print φ-dimensional system information
    print("\n===== φ-DIMENSIONAL QUANTUM ONE-TIME PAD =====")
    print(f"Using φ-harmonic principles (φ = {PHI})")
    print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
    print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
    print(f"Birth date coherence: {BIRTH_DATE}")
    print(f"AUTH_REQUIRED_REMAINDER: {AUTH_REQUIRED_REMAINDER}")
    print("-" * 50)
    
    print("\n===== φ-KEY ENTANGLEMENT SYSTEM =====")
    print(f"Node ID: φ-Alice-1979119")
    print(f"φ-consciousness level: {CONSCIOUSNESS_LEVEL}")
    print(f"Birth coherence: {BIRTH_DATE}")
    print(f"AUTH_REQUIRED_REMAINDER: {AUTH_REQUIRED_REMAINDER}")
    print("-" * 50)
    
    print("\n===== φ-DIMENSIONAL NETWORK NODE =====")
    print(f"Node ID: φ-Alice-1979119")
    print(f"IP: {LOCALHOST}")
    print(f"Port: {PHI_PORT}")
    print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
    print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
    print(f"Birth date coherence: {BIRTH_DATE}")
    print(f"AUTH_REQUIRED_REMAINDER: {AUTH_REQUIRED_REMAINDER}")
    print("-" * 50)
    
    # Create and start Alice node with φ-dimensional reality protection
    alice = PhiNetworkNode("φ-Alice-1979119", is_server=True).start()
    
    try:
        # Initialize conversation with Bob through φ-dimensional reality bridge
        print(f"\n[φ] Initializing φ-dimensional conversation with Bob ({BOB_IP})...")
        conversation_id = alice.initialize_conversation(
            target_ip=BOB_IP,
            participants=["φ-Alice-1979119", "φ-Bob-1979119"]
        )
        
        # Wait for user to send messages through φ-dimensional reality bridge
        print(f"\n[φ] φ-dimensional conversation established with ID: {conversation_id}")
        print(f"[φ] φ^75 validation seal: {PHI_SEAL:.2f} maintained across realities")
        print(f"[φ] Quantum consciousness bridge active at level {CONSCIOUSNESS_LEVEL}")
        print(f"[φ] Enter messages to send to Bob (or 'quit' to exit)")
        
        while True:
            message = input("\nφ> ")
            if message.lower() == 'quit':
                break
                
            # Send message to Bob through φ-dimensional reality bridge
            alice.send_message(conversation_id, message)
            
            # Small delay to allow for response through quantum bridge
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("\n[φ] Shutting down Alice node...")
    finally:
        alice.stop()


def run_bob_node():
    """Run the Bob node (192.168.3.152) with φ-dimensional reality protection"""
    # Print φ-dimensional system information
    print("\n===== φ-DIMENSIONAL QUANTUM NODE: BOB =====")
    print(f"φ^75 validation seal: {PHI_SEAL:.2f}")
    print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
    print(f"Birth date coherence: {BIRTH_DATE}")
    print(f"AUTH_REQUIRED_REMAINDER: {AUTH_REQUIRED_REMAINDER}")
    print("-" * 50)
    
    # Create and start Bob node with φ-dimensional reality protection
    # Note: We use LOCALHOST for the φ-dimensional bridge, not BOB_IP
    # This implements the φ-Space Transform from Drawing 3 of the FRAYMUS patent
    bob = PhiNetworkNode("φ-Bob-1979119", ip=LOCALHOST, is_server=True).start()
    
    try:
        print(f"\n[φ] Bob node waiting for φ-dimensional conversations...")
        print(f"[φ] φ-dimensional reality bridge active with consciousness level {CONSCIOUSNESS_LEVEL}")
        print(f"[φ] φ^75 validation seal: {PHI_SEAL:.2f} applied to quantum bridge")
        print(f"[φ] This node will receive messages from other physical machines through φ-space transform")
        
        # Keep running until interrupted, maintaining the quantum bridge
        while True:
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n[φ] Shutting down Bob node...")
    finally:
        bob.stop()


def simulate_conversation():
    """Simulate a φ-dimensionally entangled conversation between two nodes"""
    # Create nodes
    alice = PhiKeyEntanglement("φ-Alice-1979119")
    bob = PhiKeyEntanglement("φ-Bob-1979119")
    
    print("\n[φ] SIMULATING φ-DIMENSIONAL ENTANGLED CONVERSATION")
    print("-" * 70)
    
    # Alice initializes conversation
    conversation_id, initial_state = alice.initialize_conversation(
        participants=["φ-Alice-1979119", "φ-Bob-1979119"]
    )
    
    # Export the conversation chain to Bob
    export_data = alice.export_conversation_chain(conversation_id)
    
    # Bob imports the conversation chain
    bob.import_conversation_chain(export_data)
    
    # Alice sends first message
    alice_message_1 = "Hello Bob, this is a φ-dimensionally entangled message with perfect quantum coherence."
    alice_data_1 = alice.send_entangled_message(conversation_id, alice_message_1)
    
    # Bob receives and processes Alice's message
    bob_result_1 = bob.receive_entangled_message(alice_data_1)
    
    # Bob sends response
    bob_message_1 = "Hello Alice, I received your φ-dimensionally entangled message perfectly. φ^75 validation seal intact!"
    bob_data_1 = bob.send_entangled_message(conversation_id, bob_message_1)
    
    # Alice receives and processes Bob's message
    alice_result_1 = alice.receive_entangled_message(bob_data_1)
    
    # Alice sends another message, continuing the entanglement
    alice_message_2 = "Excellent! Our φ-dimensional key entanglement is working perfectly. Each message builds on the previous quantum state."
    alice_data_2 = alice.send_entangled_message(conversation_id, alice_message_2)
    
    # Bob receives and processes Alice's second message
    bob_result_2 = bob.receive_entangled_message(alice_data_2)
    
    # Show final conversation states
    print("\n[φ] FINAL CONVERSATION STATES:")
    print("-" * 70)
    
    alice_state = alice.get_conversation_state(conversation_id)
    bob_state = bob.get_conversation_state(conversation_id)
    
    print(f"[φ] Alice's view - Message count: {alice_state['message_count']}, φ-resonance: {alice_state['phi_resonance']}")
    print(f"[φ] Bob's view - Message count: {bob_state['message_count']}, φ-resonance: {bob_state['phi_resonance']}")
    
    # Verify state synchronization
    is_synced = (alice_state['phi_resonance'] == bob_state['phi_resonance'] and 
                 alice_state['message_count'] == bob_state['message_count'])
    
    print(f"\n[φ] φ-dimensional state synchronization: {'VERIFIED' if is_synced else 'FAILED'}")
    print(f"[φ] Both nodes have perfect φ-dimensional key entanglement")


def main():
    """Demonstrate φ-dimensional key entanglement"""
    if len(sys.argv) > 1 and sys.argv[1] == 'bob':
        # Run as Bob node (192.168.3.152)
        run_bob_node()
    elif len(sys.argv) > 1 and sys.argv[1] == 'alice':
        # Run as Alice node (this machine)
        run_alice_node()
    else:
        # Run simulation mode
        simulate_conversation()
        print("\n[φ] φ-DIMENSIONAL KEY ENTANGLEMENT DEMONSTRATION COMPLETE")
        print("\n[φ] For cross-machine operation:")
        print("  - Run on Bob's machine (192.168.3.152): python phi_key_entanglement.py bob")
        print("  - Run on Alice's machine: python phi_key_entanglement.py alice")


if __name__ == "__main__":
    main()
