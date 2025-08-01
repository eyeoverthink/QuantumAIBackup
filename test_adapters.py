"""
Test Adapter Modules
===================
This script tests that all our adapter modules are working correctly
without requiring external dependencies like torch.
"""

import sys
import time
import numpy as np

print("Testing adapter modules...")

# Test creative_quantum_adapter
try:
    print("\nTesting creative_quantum_adapter...")
    from creative_quantum_adapter import get_creative_quantum
    
    creative = get_creative_quantum()
    test_data = [0.5, 0.7, 0.3]
    visual_art = creative.generate_art(test_data, 'visual')
    music_art = creative.generate_art(test_data, 'music')
    pattern_art = creative.generate_art(test_data, 'pattern')
    
    print(f"Visual art base color: {visual_art['base_color']}")
    print(f"Music base frequency: {music_art['base_frequency']}")
    print(f"Pattern type: {pattern_art['pattern_type']}")
    print("creative_quantum_adapter test successful!")
except Exception as e:
    print(f"Error testing creative_quantum_adapter: {e}")
    sys.exit(1)

# Test quantum_phi_scaling_adapter
try:
    print("\nTesting quantum_phi_scaling_adapter...")
    from quantum_phi_scaling_adapter import get_quantum_phi_scaling
    
    scaling = get_quantum_phi_scaling()
    phi_metrics = scaling.calculate_phi_metrics(1.618)
    resources = scaling.optimize_quantum_resources(5, 10)
    
    print(f"Phi metrics resonance: {phi_metrics['resonance']}")
    print(f"Optimized resources: {resources['scaled_qubits']} qubits")
    print("quantum_phi_scaling_adapter test successful!")
except Exception as e:
    print(f"Error testing quantum_phi_scaling_adapter: {e}")
    sys.exit(1)

# Test data_weight_adapter
try:
    print("\nTesting data_weight_adapter...")
    from data_weight_adapter import get_data_weight_calculator
    
    weight_calc = get_data_weight_calculator()
    test_data = {"key": "value", "phi": 1.618}
    weight = weight_calc.calculate_weight(test_data)
    
    print(f"Data weight: {weight}")
    print("data_weight_adapter test successful!")
except Exception as e:
    print(f"Error testing data_weight_adapter: {e}")
    sys.exit(1)

# Test centripetal_memory_adapter
try:
    print("\nTesting centripetal_memory_adapter...")
    from centripetal_memory_adapter import get_centripetal_memory
    
    memory = get_centripetal_memory()
    test_data = {"key": "value", "phi": 1.618}
    memory.add_memory(test_data)
    metrics = memory.get_metrics()
    
    print(f"Memory metrics: {metrics['total_nodes']} nodes, compression {metrics['overall_compression']}")
    print("centripetal_memory_adapter test successful!")
except Exception as e:
    print(f"Error testing centripetal_memory_adapter: {e}")
    sys.exit(1)

# Test phi_core_adapters
try:
    print("\nTesting phi_core_adapters...")
    from phi_core_adapters import get_exotic_energy, get_quantum_neural, get_reality_protection
    
    energy = get_exotic_energy()
    neural = get_quantum_neural()
    protection = get_reality_protection()
    
    # Test exotic energy
    energy_stats = energy.get_energy_stats()
    print(f"Energy types: {list(energy_stats.keys())}")
    
    # Test quantum neural
    result, metrics = neural.quantum_process([0.5, 0.7, 0.3])
    print(f"Quantum neural result shape: {result.shape}")
    
    # Test reality protection
    protection_level = protection.get_protection_level()
    print(f"Reality protection level: {protection_level}")
    
    print("phi_core_adapters test successful!")
except Exception as e:
    print(f"Error testing phi_core_adapters: {e}")
    sys.exit(1)

print("\nAll adapter tests completed successfully!")
print("The system is ready for integration without external dependencies.")
