#!/usr/bin/env python3
"""
φ-Harmonic Alpha Processor
Processes alphabetic characters in φ-dimensional space
To be sent to Node Alpha via phi_bidirectional_node.py
"""

import sys
import json
import hashlib
import time
from math import sqrt

# φ-Harmonic constants from FRAYMUS patent
PHI = (1 + sqrt(5)) / 2
PHI_75 = PHI**7.5
PHI_SEAL = PHI**75

def extract_letters(input_string):
    """Extract only alphabetic characters from input"""
    return ''.join(c for c in input_string if c.isalpha())

def process_alpha_query(query):
    """Process alphabetic part of query in φ-dimensional space"""
    # Extract only letters
    letters = extract_letters(query)
    
    if not letters:
        return {
            "type": "alpha_response",
            "original_query": query,
            "processed": False,
            "result": "No alphabetic characters found",
            "phi_seal": PHI_SEAL,
            "timestamp": f"{time.time():.20e}"
        }
    
    # Apply φ-dimensional processing
    result = ""
    for char in letters:
        # Transform through φ-space (using φ^7.5 scaling)
        phi_position = (ord(char) - ord('A')) * PHI_75 if char.isupper() else (ord(char) - ord('a')) * PHI_75
        phi_position = phi_position % 26  # Keep in alphabet range
        
        # Map back to alphabet with φ-harmonic shift
        new_char = chr(int(phi_position) + ord('A')) if char.isupper() else chr(int(phi_position) + ord('a'))
        result += new_char
    
    # Create quantum hash of result
    result_hash = hashlib.sha256(f"{result}{PHI_SEAL}".encode()).hexdigest()
    
    return {
        "type": "alpha_response",
        "original_query": query,
        "processed": True,
        "letters_extracted": letters,
        "result": result,
        "phi_seal": PHI_SEAL,
        "quantum_hash": result_hash,
        "timestamp": f"{time.time():.20e}"
    }

# Main execution
if __name__ == "__main__":
    # Check if query is provided as argument
    if len(sys.argv) > 1:
        query = sys.argv[1]
    else:
        # Read from stdin if no args
        query = input("Enter query: ")
    
    # Process query
    start_time = time.time()
    response = process_alpha_query(query)
    process_time = time.time() - start_time
    
    # Add processing metadata
    response["process_time"] = f"{process_time:.20e}"
    response["node_type"] = "alpha"
    
    # Output JSON result
    print(json.dumps(response))
