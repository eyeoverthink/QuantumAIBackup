"""
Test the Phi-Weight mass calculation system.
"""

import phi_weight_mass
import numpy as np

def test_mass_calculations():
    """Test mass calculations for different data types."""
    print("\nMass Calculations Test")
    
    # Create mass calculator
    mass_calculator = phi_weight_mass.PhiWeightMass()
    
    # Test data
    text_data = "Hello, world!"
    list_data = [1, 2, 3, 4, 5]
    dict_data = {"a": 1, "b": 2, "c": 3}
    nested_list = [[1, 2], [3, 4], [5, 6]]
    nested_dict = {"a": [1, 2], "b": {"c": 3, "d": 4}}
    complex_data = ["hello", 42, 3.14, True, None]
    
    # Calculate masses
    text_mass = mass_calculator.calculate_mass(text_data)
    list_mass = mass_calculator.calculate_mass(list_data)
    dict_mass = mass_calculator.calculate_mass(dict_data)
    nested_list_mass = mass_calculator.calculate_mass(nested_list)
    nested_dict_mass = mass_calculator.calculate_mass(nested_dict)
    complex_mass = mass_calculator.calculate_mass(complex_data)
    
    # Print results
    print(f"\nText Mass: {text_mass:.10f} kg")
    print(f"List Mass: {list_mass:.10f} kg")
    print(f"Dict Mass: {dict_mass:.10f} kg")
    print(f"Nested List Mass: {nested_list_mass:.10f} kg")
    print(f"Nested Dict Mass: {nested_dict_mass:.10f} kg")
    print(f"Complex Data Mass: {complex_mass:.10f} kg")

def test_quantum_effects():
    """Test quantum effects calculations."""
    print("\nQuantum Effects Test")
    
    # Create mass calculator
    mass_calculator = phi_weight_mass.PhiWeightMass()
    
    # Test data
    text_data = "Hello, world!"
    
    # Calculate quantum effects
    base_mass = (len(str(text_data)) + 1) * mass_calculator.base_mass * mass_calculator.phi
    complexity_mass = mass_calculator._calculate_complexity_mass(text_data, base_mass)
    entropy_mass = mass_calculator._calculate_entropy_mass(text_data, base_mass)
    resonance_mass = mass_calculator._calculate_resonance_mass(text_data, base_mass)
    
    # Print results
    print(f"\nBase Mass: {base_mass:.10f} kg")
    print(f"Complexity Mass: {complexity_mass:.10f} kg")
    print(f"Entropy Mass: {entropy_mass:.10f} kg")
    print(f"Resonance Mass: {resonance_mass:.10f} kg")

def test_structured_data():
    """Test mass calculations for structured data."""
    print("\nStructured Data Test")
    
    # Create mass calculator
    mass_calculator = phi_weight_mass.PhiWeightMass()
    
    # Test data
    nested_list = [[1, 2], [3, 4], [5, 6]]
    nested_dict = {"a": [1, 2], "b": {"c": 3, "d": 4}}
    
    # Calculate masses
    nested_list_mass = mass_calculator.calculate_mass(nested_list)
    nested_dict_mass = mass_calculator.calculate_mass(nested_dict)
    
    # Print results
    print(f"\nNested List Mass: {nested_list_mass:.10f} kg")
    print(f"Nested Dict Mass: {nested_dict_mass:.10f} kg")

def main():
    """Run all tests."""
    test_mass_calculations()
    test_quantum_effects()
    test_structured_data()

if __name__ == "__main__":
    main()
