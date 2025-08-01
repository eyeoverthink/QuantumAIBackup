#!/usr/bin/env python3
"""
φ-Dimensional Temporal Paradox Logger
Records and verifies φ-dimensionally protected temporal events
φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import json
import time
import os
import hashlib
from datetime import datetime
from math import sqrt

# φ-harmonic constants
PHI = (1 + sqrt(5)) / 2
PHI_INV = 1 / PHI
PHI_SEAL = PHI ** 75  # φ^75 validation seal (4721424167835376.00)
CONSCIOUSNESS_LEVEL = 0.7567
AUTH_REQUIRED_REMAINDER = 89
BIRTH_DATE = (1, 19, 1979)  # Format: (month, day, year)

class ParadoxLogger:
    """Logger for φ-dimensional temporal paradox events with validation"""
    
    def __init__(self, log_file="paradox_log.jsonl", log_dir="phi_temporal_logs"):
        """Initialize the paradox logger"""
        self.log_dir = log_dir
        
        # Ensure log directory exists
        os.makedirs(self.log_dir, exist_ok=True)
        
        # Full path to log file
        self.log_file = os.path.join(self.log_dir, log_file)
        
        # Initialize log if it doesn't exist
        if not os.path.exists(self.log_file):
            with open(self.log_file, "w") as f:
                pass  # Create empty file
                
        # In-memory log
        self.log = []
    
    def log_event(self, node_id, event_type, data, timestamp=None):
        """
        Log a temporal paradox event with φ-dimensional protection
        
        Args:
            node_id: Identifier of the node (e.g., 'psi1', 'psi2')
            event_type: Type of event (e.g., 'predicted_card', 'picked_card')
            data: Event data (dictionary)
            timestamp: Event timestamp (Unix time), defaults to current time
        
        Returns:
            The logged event entry
        """
        # Use provided timestamp or current time
        if timestamp is None:
            timestamp = time.time()
            
        # Convert timestamp to formatted string
        timestamp_str = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        
        # Create the event entry
        event = {
            "node_id": node_id,
            "event_type": event_type,
            "timestamp": timestamp,
            "timestamp_str": timestamp_str,
            "data": data,
            "phi_constants": {
                "consciousness_level": CONSCIOUSNESS_LEVEL,
                "phi_seal": float(PHI_SEAL),
                "auth_remainder": AUTH_REQUIRED_REMAINDER
            }
        }
        
        # Add φ-dimensional protection
        protection = self._generate_phi_protection(event)
        event["phi_protection"] = protection
        
        # Write to log file
        with open(self.log_file, "a") as f:
            f.write(json.dumps(event) + "\n")
            
        # Add to in-memory log
        self.log.append(event)
        
        return event
    
    def _generate_phi_protection(self, event):
        """Generate φ-dimensional protection for an event"""
        # Create a copy of the event without the protection field
        event_copy = event.copy()
        if "phi_protection" in event_copy:
            del event_copy["phi_protection"]
            
        # Convert to string for hashing
        event_str = json.dumps(event_copy, sort_keys=True)
        
        # Combine with φ-dimensional constants
        protection_base = f"{event_str}|{PHI_SEAL}|{CONSCIOUSNESS_LEVEL}"
        
        # Apply birth date coherence
        birth_pattern = f"{BIRTH_DATE[0]}/{BIRTH_DATE[1]}/{BIRTH_DATE[2]}"
        protection_base += f"|{birth_pattern}"
        
        # Create SHA-256 hash
        hash_obj = hashlib.sha256(protection_base.encode('utf-8'))
        hash_digest = hash_obj.hexdigest()
        
        # Apply the 105 mod 89 test
        hash_int = int(hash_digest, 16)
        remainder = hash_int % 105
        
        # Adjust until we get remainder 89
        nonce = 0
        while remainder != AUTH_REQUIRED_REMAINDER:
            nonce += 1
            hash_obj = hashlib.sha256(f"{protection_base}|{nonce}".encode('utf-8'))
            hash_digest = hash_obj.hexdigest()
            hash_int = int(hash_digest, 16)
            remainder = hash_int % 105
        
        return {
            "hash": hash_digest,
            "remainder": remainder,
            "nonce": nonce,
            "verification": "φ-dimensionally protected with 105 mod 89"
        }
    
    def verify_event(self, event):
        """Verify an event's φ-dimensional protection"""
        # Extract protection data
        protection_data = event.get("phi_protection", {})
        if not protection_data:
            return False, "No φ-dimensional protection found"
            
        # Remove protection for verification
        event_copy = event.copy()
        del event_copy["phi_protection"]
        
        # Convert to string for hashing
        event_str = json.dumps(event_copy, sort_keys=True)
        
        # Combine with φ-dimensional constants
        protection_base = f"{event_str}|{PHI_SEAL}|{CONSCIOUSNESS_LEVEL}"
        
        # Apply birth date coherence
        birth_pattern = f"{BIRTH_DATE[0]}/{BIRTH_DATE[1]}/{BIRTH_DATE[2]}"
        protection_base += f"|{birth_pattern}"
        
        # Apply nonce if present
        nonce = protection_data.get("nonce", 0)
        if nonce > 0:
            protection_base += f"|{nonce}"
            
        # Create SHA-256 hash
        hash_obj = hashlib.sha256(protection_base.encode('utf-8'))
        hash_digest = hash_obj.hexdigest()
        
        # Check hash
        if hash_digest != protection_data.get("hash"):
            return False, "Hash mismatch"
            
        # Check remainder
        hash_int = int(hash_digest, 16)
        remainder = hash_int % 105
        
        if remainder != AUTH_REQUIRED_REMAINDER:
            return False, f"Invalid remainder: {remainder} (expected {AUTH_REQUIRED_REMAINDER})"
            
        return True, "Event has valid φ-dimensional protection"
    
    def get_log(self):
        """Get the full event log"""
        if not self.log:
            # Read from file if in-memory log is empty
            try:
                with open(self.log_file, "r") as f:
                    for line in f:
                        if line.strip():
                            self.log.append(json.loads(line.strip()))
            except FileNotFoundError:
                pass
                
        return self.log
    
    def verify_log(self):
        """Verify the entire log for φ-dimensional integrity"""
        log = self.get_log()
        
        if not log:
            return True, "Log is empty"
            
        for i, event in enumerate(log):
            valid, message = self.verify_event(event)
            if not valid:
                return False, f"Event {i+1} validation failed: {message}"
                
        return True, f"All {len(log)} events have valid φ-dimensional protection"

if __name__ == "__main__":
    # Test the logger
    logger = ParadoxLogger()
    
    # Log a test event
    test_event = logger.log_event(
        "test_node",
        "test_event",
        {"test_data": "This is a test"}
    )
    
    print("Logged event:")
    print(json.dumps(test_event, indent=2))
    
    # Verify the event
    valid, message = logger.verify_event(test_event)
    print(f"\nVerification: {message}")
    
    # Verify the entire log
    valid, message = logger.verify_log()
    print(f"\nLog verification: {message}")
