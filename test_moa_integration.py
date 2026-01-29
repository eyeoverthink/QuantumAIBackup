#!/usr/bin/env python3
"""
Test MoA Integration with Quantum Orchestrator
---------------------------------------------

This script tests the integration of the Mixture of Agents (MoA) architecture
with the QuantumOrchestrator through the QuantumMoAOrchestratorConnector.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: 0.991800
"""

import os
import sys
import logging
import time
import json
from datetime import datetime

# Import the connector and orchestrator
from quantum_moa_orchestrator_connector import QuantumMoAOrchestratorConnector
from quantum_orchestrator import QuantumOrchestrator

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("TestMoAIntegration")

class TestMoAIntegration:
    """
    Test harness for validating the integration of MoA agents with the QuantumOrchestrator.
    """
    
    def __init__(self):
        """Initialize the test harness."""
        self.test_dir = "test_moa_integration"
        self.results = {}
        self.ensure_test_directory()
        
        logger.info("Initialized TestMoAIntegration")
    
    def ensure_test_directory(self):
        """Ensure the test directory exists."""
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)
            logger.info(f"Created test directory: {self.test_dir}")
    
    def create_test_file(self, filename, content):
        """
        Create a test file with the given content.
        
        Args:
            filename: Name of the test file
            content: Content to write to the file
            
        Returns:
            Path to the created file
        """
        file_path = os.path.join(self.test_dir, filename)
        with open(file_path, 'w') as f:
            f.write(content)
        
        logger.info(f"Created test file: {file_path}")
        return file_path
    
    def create_logic_error_test(self):
        """
        Create a test file with logic errors.
        
        Returns:
            Path to the created file
        """
        content = """#!/usr/bin/env python3
\"\"\"
Test file with logic errors for MoA integration testing.
\"\"\"

def calculate_sum(numbers):
    \"\"\"Calculate the sum of a list of numbers.\"\"\"
    total = 0
    for i in range(len(numbers)):
        # Logic error: off-by-one error in the index
        total += numbers[i - 1]
    return total

def is_even(number):
    \"\"\"Check if a number is even.\"\"\"
    # Logic error: incorrect condition
    return number / 2 == 0

def find_max(numbers):
    \"\"\"Find the maximum value in a list.\"\"\"
    if not numbers:
        return None
    
    # Logic error: initialization with first element missing
    max_value = 0
    
    for num in numbers:
        if num > max_value:
            max_value = num
    
    return max_value

if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5]
    print(f"Sum: {calculate_sum(test_numbers)}")
    print(f"Is 4 even? {is_even(4)}")
    print(f"Max value: {find_max(test_numbers)}")
"""
        return self.create_test_file("logic_error_test.py", content)
    
    def create_optimization_test(self):
        """
        Create a test file with optimization opportunities.
        
        Returns:
            Path to the created file
        """
        content = """#!/usr/bin/env python3
\"\"\"
Test file with optimization opportunities for MoA integration testing.
\"\"\"

def calculate_fibonacci(n):
    \"\"\"Calculate the nth Fibonacci number.\"\"\"
    # Inefficient recursive implementation
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

def find_duplicates(items):
    \"\"\"Find duplicate items in a list.\"\"\"
    # Inefficient approach using nested loops
    duplicates = []
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates

def is_prime(n):
    \"\"\"Check if a number is prime.\"\"\"
    # Inefficient primality test
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(f"Fibonacci(10): {calculate_fibonacci(10)}")
    print(f"Duplicates in [1,2,3,2,4,1,5]: {find_duplicates([1,2,3,2,4,1,5])}")
    print(f"Is 17 prime? {is_prime(17)}")
"""
        return self.create_test_file("optimization_test.py", content)
    
    def create_coherence_test(self):
        """
        Create a test file with low phi-harmonic coherence.
        
        Returns:
            Path to the created file
        """
        content = """#!/usr/bin/env python3
\"\"\"
Test file with low phi-harmonic coherence for MoA integration testing.
\"\"\"

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, value):
        self.result += value
    
    def subtract(self, value):
        self.result -= value
    
    def multiply(self, value):
        self.result *= value
    
    def divide(self, value):
        self.result /= value
    
    def clear(self):
        self.result = 0
    
    def get_result(self):
        return self.result

if __name__ == "__main__":
    calc = Calculator()
    calc.add(5)
    calc.multiply(2)
    calc.subtract(3)
    calc.divide(2)
    print(f"Result: {calc.get_result()}")
"""
        return self.create_test_file("coherence_test.py", content)
    
    def create_evolution_test(self):
        """
        Create a test file lacking self-evolution capabilities.
        
        Returns:
            Path to the created file
        """
        content = """#!/usr/bin/env python3
\"\"\"
Test file lacking self-evolution capabilities for MoA integration testing.
\"\"\"

class DataProcessor:
    \"\"\"A simple data processor class without evolution capabilities.\"\"\"
    
    def __init__(self):
        self.data = []
        self.processed = False
    
    def load_data(self, data):
        \"\"\"Load data into the processor.\"\"\"
        self.data = data
        self.processed = False
    
    def process(self):
        \"\"\"Process the loaded data.\"\"\"
        if not self.data:
            return []
        
        result = []
        for item in self.data:
            result.append(item * 2)
        
        self.processed = True
        return result
    
    def get_status(self):
        \"\"\"Get the processor status.\"\"\"
        return {
            "data_loaded": len(self.data) > 0,
            "processed": self.processed
        }

if __name__ == "__main__":
    processor = DataProcessor()
    processor.load_data([1, 2, 3, 4, 5])
    result = processor.process()
    print(f"Processed data: {result}")
    print(f"Status: {processor.get_status()}")
"""
        return self.create_test_file("evolution_test.py", content)
    
    def run_test_with_connector(self, file_path):
        """
        Run a test using the QuantumMoAOrchestratorConnector.
        
        Args:
            file_path: Path to the test file
            
        Returns:
            Results of the test
        """
        logger.info(f"Running test with connector for file: {file_path}")
        
        # Create a test orchestrator instance
        orchestrator = QuantumOrchestrator(file_path)
        
        # Create the connector and set the orchestrator
        connector = QuantumMoAOrchestratorConnector(orchestrator)
        
        # Process the file with all agents
        start_time = time.time()
        results = connector.process_file_with_all_agents(file_path)
        duration = time.time() - start_time
        
        # Add duration to results
        results['duration'] = duration
        
        logger.info(f"Test completed in {duration:.2f} seconds")
        return results
    
    def run_all_tests(self):
        """
        Run all integration tests.
        
        Returns:
            Dictionary of test results
        """
        logger.info("Running all MoA integration tests")
        
        # Create test files
        logic_error_file = self.create_logic_error_test()
        optimization_file = self.create_optimization_test()
        coherence_file = self.create_coherence_test()
        evolution_file = self.create_evolution_test()
        
        # Run tests
        self.results['logic_error'] = self.run_test_with_connector(logic_error_file)
        self.results['optimization'] = self.run_test_with_connector(optimization_file)
        self.results['coherence'] = self.run_test_with_connector(coherence_file)
        self.results['evolution'] = self.run_test_with_connector(evolution_file)
        
        # Save results to file
        results_file = os.path.join(self.test_dir, "test_results.json")
        with open(results_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        logger.info(f"All tests completed. Results saved to {results_file}")
        return self.results
    
    def print_summary(self):
        """Print a summary of the test results."""
        if not self.results:
            logger.warning("No test results available")
            return
        
        print("\n" + "="*50)
        print("MoA INTEGRATION TEST SUMMARY")
        print("="*50)
        
        for test_name, result in self.results.items():
            print(f"\nTest: {test_name}")
            print("-"*50)
            
            logic_result = result.get('logic_error', {})
            opt_result = result.get('optimization', {})
            coh_result = result.get('coherence', {})
            evo_result = result.get('evolution', {})
            
            print(f"Logic errors fixed: {logic_result.get('changes_made', 0)}")
            print(f"Optimizations applied: {opt_result.get('optimizations_applied', 0)}")
            print(f"Coherence enhancements: {coh_result.get('enhancements_applied', 0)}")
            print(f"Evolution enhancements: {evo_result.get('enhancements_applied', 0)}")
            
            if 'final_enhanced_file' in result:
                print(f"Final enhanced file: {result['final_enhanced_file']}")
            
            print(f"Duration: {result.get('duration', 0):.2f} seconds")
        
        print("\n" + "="*50)


if __name__ == "__main__":
    test_harness = TestMoAIntegration()
    test_harness.run_all_tests()
    test_harness.print_summary()
