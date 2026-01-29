"""
Test script for verifying integration of the quantum_oracle_lib as a library.
This script does NOT depend on the original core system and should run independently.
"""

import sys
import os

# Ensure the parent directory of quantum_oracle_lib is in sys.path for local testing
CURR_PATH = os.path.abspath(os.path.dirname(__file__))
PARENT_PATH = os.path.dirname(CURR_PATH)
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

# Attempt to import a core class from the library
def test_phi_bidirectional_node():
    try:
        from quantum_oracle_lib.phi_bidirectional_node import PhiBidirectionalNode
        node = PhiBidirectionalNode(node_id="integration_test", port=12000)
        print("[SUCCESS] Imported PhiBidirectionalNode and instantiated node:", node)
        return True
    except Exception as e:
        print("[FAIL] Could not import or instantiate PhiBidirectionalNode:", e)
        return False

def main():
    print("=== Quantum Oracle Library Integration Test ===")
    result = test_phi_bidirectional_node()
    if result:
        print("Integration test PASSED.")
    else:
        print("Integration test FAILED.")

if __name__ == "__main__":
    main()
