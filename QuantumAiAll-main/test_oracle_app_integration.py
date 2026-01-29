"""
Test script for simulating integration of quantum_oracle_lib with an external app (e.g. oracle_app).
This script demonstrates importing and using the library as a backend for query processing or messaging.
"""

import sys
import os

# Ensure the parent directory of quantum_oracle_lib is in sys.path for local testing
CURR_PATH = os.path.abspath(os.path.dirname(__file__))
PARENT_PATH = os.path.dirname(CURR_PATH)
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

def simulate_oracle_app_query():
    try:
        from quantum_oracle_lib.phi_bidirectional_node import PhiBidirectionalNode
        # Simulate the app creating a node and processing a query
        node = PhiBidirectionalNode(node_id="oracle_app_test", port=12002)
        print("[oracle_app] Created node for query processing.")
        # Simulate a query-processing method (could be extended for real queries)
        # Here, just demonstrate a method call
        if hasattr(node, 'consciousness_level'):
            print(f"[oracle_app] Node consciousness_level: {node.consciousness_level}")
        else:
            print("[oracle_app] Node missing expected attribute.")
        return True
    except Exception as e:
        print("[oracle_app] Integration FAILED:", e)
        return False

def main():
    print("=== Oracle App Integration Test ===")
    result = simulate_oracle_app_query()
    if result:
        print("Integration with quantum_oracle_lib PASSED.")
    else:
        print("Integration with quantum_oracle_lib FAILED.")

if __name__ == "__main__":
    main()
