#!/usr/bin/env python3
"""
φ-Harmonic Node Patch
Fixes acknowledgment loops in phi_bidirectional_node.py
"""

import os
import re
import sys

def patch_bidirectional_node():
    """Patch the bidirectional node to prevent acknowledgment loops"""
    node_file = "../phi_bidirectional_node.py"
    if not os.path.exists(node_file):
        node_file = "phi_bidirectional_node.py"
        if not os.path.exists(node_file):
            print("[φ] Error: Could not find phi_bidirectional_node.py")
            return False
    
    print(f"[φ] Found node file: {node_file}")
    
    # Read the file
    with open(node_file, "r") as f:
        content = f.read()
    
    # Look for the acknowledgment check pattern
    ack_pattern = r"if not (\w+)\.startswith\(\"Acknowledgment Received:\"\):"
    
    # Check if the file already contains the fix
    if "and \"Acknowledgment Received:\" not in" in content:
        print("[φ] Node already patched to prevent acknowledgment loops")
        return True
    
    # Apply the patch
    patched_content = re.sub(
        ack_pattern,
        r"if not \1.startswith(\"Acknowledgment Received:\") and \"Acknowledgment Received:\" not in \1:",
        content
    )
    
    # Check if the pattern was found and replaced
    if patched_content == content:
        print("[φ] Error: Could not find acknowledgment pattern to patch")
        return False
    
    # Write the patched file
    with open(node_file, "w") as f:
        f.write(patched_content)
    
    print("[φ] Successfully patched node to prevent acknowledgment loops")
    print("[φ] Please restart the node for changes to take effect")
    return True

if __name__ == "__main__":
    success = patch_bidirectional_node()
    sys.exit(0 if success else 1)
