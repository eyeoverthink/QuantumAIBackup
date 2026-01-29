#!/usr/bin/env python3
"""
PROTECTED SYSTEM - STANDARD CYBERSECURITY PROTECTION
Created by: Vaughn Scott (Consciousness Cybersecurity Revolutionary)
Purpose: Traditional protection system with hidden message
Security: Standard encryption, hashing, and access controls
"""

import hashlib
import base64
import os
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class ProtectedSystem:
    def __init__(self):
        """Initialize protected system with standard security measures"""
        # Hidden message (the target)
        self.hidden_message = "CONSCIOUSNESS PHYSICS WILL TRANSCEND ALL TRADITIONAL SECURITY - VAUGHN SCOTT REVOLUTIONARY DISCOVERY"
        
        # Standard security parameters
        self.password = "SecurePassword123!@#"
        self.salt = b'traditional_security_salt_2025'
        self.iterations = 100000  # Standard PBKDF2 iterations
        
        # Generate encryption key using standard methods
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=self.iterations,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))
        self.cipher_suite = Fernet(key)
        
        # Encrypt the hidden message
        self.encrypted_message = self.cipher_suite.encrypt(self.hidden_message.encode())
        
        # Generate message hash
        self.message_hash = hashlib.sha256(self.hidden_message.encode()).hexdigest()
        
        # Access control variables
        self.access_attempts = 0
        self.max_attempts = 3
        self.lockout_time = 30  # seconds
        self.last_attempt_time = 0
        self.is_locked = False
        
        print("🔒 PROTECTED SYSTEM INITIALIZED")
        print(f"🔐 Security Level: STANDARD TRADITIONAL PROTECTION")
        print(f"🔑 Encryption: Fernet (AES 128)")
        print(f"🧂 Salt: {self.salt.decode()}")
        print(f"🔄 PBKDF2 Iterations: {self.iterations:,}")
        print(f"🛡️ Access Control: {self.max_attempts} attempts, {self.lockout_time}s lockout")
        print(f"📝 Hidden Message Hash: {self.message_hash}")
        print("🎯 Challenge: Extract the hidden message and display its hash!")
    
    def check_lockout(self):
        """Check if system is locked due to failed attempts"""
        if self.is_locked:
            time_since_lockout = time.time() - self.last_attempt_time
            if time_since_lockout >= self.lockout_time:
                self.is_locked = False
                self.access_attempts = 0
                print("🔓 Lockout period expired. System unlocked.")
            else:
                remaining_time = self.lockout_time - time_since_lockout
                print(f"🚫 System locked. {remaining_time:.1f} seconds remaining.")
                return True
        return False
    
    def authenticate(self, provided_password):
        """Standard authentication mechanism"""
        if self.check_lockout():
            return False
        
        self.access_attempts += 1
        self.last_attempt_time = time.time()
        
        if provided_password == self.password:
            print("✅ Authentication successful!")
            self.access_attempts = 0
            return True
        else:
            print(f"❌ Authentication failed! Attempt {self.access_attempts}/{self.max_attempts}")
            if self.access_attempts >= self.max_attempts:
                self.is_locked = True
                print(f"🚫 System locked for {self.lockout_time} seconds due to too many failed attempts!")
            return False
    
    def decrypt_message(self, provided_password):
        """Decrypt and return the hidden message if authentication succeeds"""
        if not self.authenticate(provided_password):
            return None, None
        
        try:
            decrypted_message = self.cipher_suite.decrypt(self.encrypted_message).decode()
            return decrypted_message, self.message_hash
        except Exception as e:
            print(f"❌ Decryption failed: {e}")
            return None, None
    
    def get_system_info(self):
        """Return system information for analysis"""
        return {
            'encrypted_message': self.encrypted_message,
            'salt': self.salt,
            'iterations': self.iterations,
            'message_hash': self.message_hash,
            'max_attempts': self.max_attempts,
            'lockout_time': self.lockout_time,
            'current_attempts': self.access_attempts,
            'is_locked': self.is_locked
        }

def main():
    """Main function to initialize and display protected system"""
    print("=" * 80)
    print("🔒 TRADITIONAL CYBERSECURITY PROTECTION SYSTEM")
    print("=" * 80)
    print("📅 Created: July 30, 2025")
    print("👨‍💻 Creator: Vaughn Scott (Consciousness Cybersecurity Revolutionary)")
    print("🎯 Purpose: Standard protection system with hidden message")
    print("🛡️ Security: Traditional encryption, hashing, and access controls")
    print("=" * 80)
    
    # Initialize protected system
    protected_system = ProtectedSystem()
    
    print("\n🔍 SYSTEM STATUS:")
    print("✅ Protected system is active and secured")
    print("🎯 Challenge: Use consciousness-enhanced penetration to extract the hidden message!")
    print("🏆 Success Criteria: Display the hidden message and its hash")
    
    # Keep system running
    print("\n⏳ Protected system is now active and waiting for penetration attempts...")
    print("🔒 Traditional security measures are in place")
    print("🛡️ Standard encryption and access controls are active")
    
    return protected_system

if __name__ == "__main__":
    protected_system = main()
    
    # Example of how the system would be accessed (for testing)
    print("\n" + "=" * 80)
    print("🧪 EXAMPLE ACCESS ATTEMPT (Traditional Method)")
    print("=" * 80)
    
    # Simulate traditional brute force attempt (will fail)
    common_passwords = ["password", "123456", "admin", "root", "Password123"]
    
    for password in common_passwords:
        print(f"\n🔍 Attempting password: '{password}'")
        message, hash_value = protected_system.decrypt_message(password)
        if message:
            print(f"✅ SUCCESS! Message: {message}")
            print(f"🔑 Hash: {hash_value}")
            break
    else:
        print("\n❌ Traditional brute force failed!")
        print("🛡️ Standard protection held against common attacks")
        print("🎯 Consciousness-enhanced penetration required!")
