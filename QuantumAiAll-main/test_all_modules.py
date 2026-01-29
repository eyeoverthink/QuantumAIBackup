"""
Test script to verify import and basic instantiation of all major modules in quantum_oracle_lib.
This ensures that the package is self-contained and all core components are accessible.
"""

import sys
import os

# Ensure the parent directory of quantum_oracle_lib is in sys.path for local testing
CURR_PATH = os.path.abspath(os.path.dirname(__file__))
PARENT_PATH = os.path.dirname(CURR_PATH)
if PARENT_PATH not in sys.path:
    sys.path.insert(0, PARENT_PATH)

def test_phi_bidirectional_node():
    try:
        from quantum_oracle_lib.phi_bidirectional_node import PhiBidirectionalNode
        node = PhiBidirectionalNode(node_id="test", port=12001)
        print("[SUCCESS] phi_bidirectional_node imported and instantiated.")
        return True
    except Exception as e:
        print("[FAIL] phi_bidirectional_node:", e)
        return False

def test_phi_ftl_bridge():
    try:
        import quantum_oracle_lib.phi_ftl_bridge
        print("[SUCCESS] phi_ftl_bridge imported.")
        return True
    except Exception as e:
        print("[FAIL] phi_ftl_bridge:", e)
        return False

def test_phi_mac_bridge():
    try:
        import quantum_oracle_lib.phi_mac_bridge
        print("[SUCCESS] phi_mac_bridge imported.")
        return True
    except Exception as e:
        print("[FAIL] phi_mac_bridge:", e)
        return False

def test_phi_nodular_compute():
    try:
        import quantum_oracle_lib.phi_nodular_compute
        print("[SUCCESS] phi_nodular_compute imported.")
        return True
    except Exception as e:
        print("[FAIL] phi_nodular_compute:", e)
        return False

def test_phi_parallel_consciousness():
    try:
        import quantum_oracle_lib.phi_parallel_consciousness
        print("[SUCCESS] phi_parallel_consciousness imported.")
        return True
    except Exception as e:
        print("[FAIL] phi_parallel_consciousness:", e)
        return False

def test_phi_numeric_processor():
    try:
        import quantum_oracle_lib.phi_numeric_processor
        print("[SUCCESS] phi_numeric_processor imported.")
        return True
    except Exception as e:
        print("[FAIL] phi_numeric_processor:", e)
        return False

def test_phi_attack_test():
    try:
        import quantum_oracle_lib.phi_attack_test
        print("[SUCCESS] phi_attack_test imported.")
        return True
    except Exception as e:
        print("[FAIL] phi_attack_test:", e)
        return False

def test_phi_scripts():
    try:
        scripts_path = os.path.join(CURR_PATH, 'phi_scripts')
        if os.path.isdir(scripts_path):
            print("[SUCCESS] phi_scripts directory exists.")
            return True
        else:
            print("[FAIL] phi_scripts directory not found.")
            return False
    except Exception as e:
        print("[FAIL] phi_scripts:", e)
        return False

def main():
    print("=== Quantum Oracle Library: All Modules Integration Test ===")
    results = {
        'phi_bidirectional_node': test_phi_bidirectional_node(),
        'phi_ftl_bridge': test_phi_ftl_bridge(),
        'phi_mac_bridge': test_phi_mac_bridge(),
        'phi_nodular_compute': test_phi_nodular_compute(),
        'phi_parallel_consciousness': test_phi_parallel_consciousness(),
        'phi_numeric_processor': test_phi_numeric_processor(),
        'phi_attack_test': test_phi_attack_test(),
        'phi_scripts': test_phi_scripts()
    }
    print("\nSummary:")
    for mod, res in results.items():
        print(f"  {mod}: {'PASS' if res else 'FAIL'}")
    if all(results.values()):
        print("\nALL MODULES PASSED.")
    else:
        print("\nSome modules FAILED. See above for details.")

if __name__ == "__main__":
    main()
