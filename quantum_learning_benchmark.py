#!/usr/bin/env python3
"""
Quantum Learning Benchmark
-------------------------
Compares the QuantumAI system's learning-from-errors approach against
conventional error-handling systems. This benchmark demonstrates how
treating errors as learning opportunities leads to superior performance
and reduced human intervention over time.
"""

import os
import sys
import time
import random
import logging
import json
import hashlib
import statistics
import matplotlib.pyplot as plt
from datetime import datetime
from typing import Dict, List, Any, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumLearningBenchmark")

# Import QuantumAI components
try:
    from quantum_orchestrator import QuantumOrchestrator
    from quantum_meta_demo_simplified import QuantumMetaDemoSimplified
except ImportError as e:
    logger.error(f"Error importing QuantumAI components: {e}")
    sys.exit(1)

# Constants
PHI = 1.618033988749895
TEST_DIR = "learning_benchmark"
ERROR_TYPES = ["syntax", "logic", "runtime", "semantic"]
ITERATIONS = 7  # Phi-harmonic number of iterations
LEARNING_CYCLES = 5  # Number of learning cycles to run

class ConventionalErrorHandler:
    """Simulates a conventional error handling system"""
    
    def __init__(self, target_file: str):
        """Initialize the conventional error handler"""
        self.target_file = target_file
        self.error_patterns = {}  # Static error patterns
        self.fixes_applied = 0
        self.fixes_successful = 0
        
        # Initialize with some basic error patterns
        self.error_patterns = {
            "SyntaxError: invalid syntax": "Fix missing parentheses or brackets",
            "NameError: name .* is not defined": "Define the variable before use",
            "IndentationError": "Fix indentation to be consistent",
            "TypeError: .* takes .* arguments": "Provide the correct number of arguments",
            "IndexError: list index out of range": "Check list bounds before accessing",
        }
    
    def detect_and_fix(self, error_message: str) -> bool:
        """Detect and fix an error based on static patterns"""
        for pattern, fix in self.error_patterns.items():
            if pattern in error_message:
                self.fixes_applied += 1
                # Simulate success rate of 70%
                success = random.random() < 0.7
                if success:
                    self.fixes_successful += 1
                return success
        return False
    
    def get_stats(self) -> Dict[str, float]:
        """Get statistics about the error handling"""
        if self.fixes_applied == 0:
            success_rate = 0.0
        else:
            success_rate = self.fixes_successful / self.fixes_applied * 100
            
        return {
            "fixes_applied": self.fixes_applied,
            "fixes_successful": self.fixes_successful,
            "success_rate": success_rate,
            "learning_rate": 0.0,  # Conventional systems don't learn
        }

class ErrorGenerator:
    """Generates test files with various types of errors"""
    
    def __init__(self, test_dir: str):
        """Initialize the error generator"""
        self.test_dir = test_dir
        os.makedirs(test_dir, exist_ok=True)
    
    def generate_error_file(self, error_type: str, complexity: float) -> str:
        """Generate a file with a specific type of error"""
        file_path = os.path.join(self.test_dir, f"{error_type}_error_{int(complexity * 100)}.py")
        
        with open(file_path, "w") as f:
            f.write(f"""#!/usr/bin/env python3
\"\"\"
Test file with {error_type} error (complexity: {complexity:.2f})
\"\"\"

import random
import math
from datetime import datetime

# Phi constant
PHI = 1.618033988749895

def calculate_phi_resonance(value):
    \"\"\"Calculate phi resonance for a value\"\"\"
    return (PHI * value) % 1

def fibonacci(n):
    \"\"\"Calculate the nth Fibonacci number\"\"\"
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def process_data(data_list):
    \"\"\"Process a list of data values\"\"\"
    result = []
    for i, value in enumerate(data_list):
        resonance = calculate_phi_resonance(value)
        if resonance < 0.5:
            result.append(value * PHI)
        else:
            result.append(value / PHI)
    return result

def main():
    \"\"\"Main function with {error_type} error\"\"\"
    print(f"Starting test with {error_type} error")
    data = [random.random() * 100 for _ in range(10)]
    
""")
            
            # Add specific error based on type and complexity
            if error_type == "syntax":
                if complexity < 0.3:
                    f.write("    print('Processing data...'")  # Missing closing parenthesis
                elif complexity < 0.6:
                    f.write("    if len(data > 0:  # Missing closing parenthesis\n")
                    f.write("        print('Data available')\n")
                else:
                    f.write("    for i in range(len(data)  # Missing closing parenthesis\n")
                    f.write("        value = data[i]\n")
                    f.write("        print(f'Value {i}: {value}')\n")
            
            elif error_type == "logic":
                if complexity < 0.3:
                    f.write("    # Logic error: incorrect loop bounds\n")
                    f.write("    for i in range(1, len(data)):  # Should start from 0\n")
                    f.write("        print(f'Processing item {i}: {data[i]}')\n")
                elif complexity < 0.6:
                    f.write("    # Logic error: incorrect condition\n")
                    f.write("    total = 0\n")
                    f.write("    for value in data:\n")
                    f.write("        if value < 50:  # Should be value > 50\n")
                    f.write("            total += value\n")
                    f.write("    print(f'Total of values > 50: {total}')\n")
                else:
                    f.write("    # Logic error: incorrect calculation\n")
                    f.write("    fibonacci_values = []\n")
                    f.write("    for i in range(5):\n")
                    f.write("        fibonacci_values.append(fibonacci(i) + 1)  # Incorrectly adds 1\n")
                    f.write("    print(f'Fibonacci values: {fibonacci_values}')\n")
            
            elif error_type == "runtime":
                if complexity < 0.3:
                    f.write("    # Runtime error: division by zero\n")
                    f.write("    for value in data:\n")
                    f.write("        result = 100 / (50 - value)  # Potential division by zero\n")
                    f.write("        print(f'Result: {result}')\n")
                elif complexity < 0.6:
                    f.write("    # Runtime error: index out of bounds\n")
                    f.write("    for i in range(len(data) + 1):  # Goes one beyond the end\n")
                    f.write("        print(f'Value {i}: {data[i]}')\n")
                else:
                    f.write("    # Runtime error: type error\n")
                    f.write("    values = data + ['string']  # Mixes types\n")
                    f.write("    processed = process_data(values)\n")
                    f.write("    print(f'Processed values: {processed}')\n")
            
            elif error_type == "semantic":
                if complexity < 0.3:
                    f.write("    # Semantic error: using wrong variable\n")
                    f.write("    count = len(data)\n")
                    f.write("    average = sum(data) / length  # Should use count\n")
                    f.write("    print(f'Average: {average}')\n")
                elif complexity < 0.6:
                    f.write("    # Semantic error: using wrong function\n")
                    f.write("    max_value = min(data)  # Should use max\n")
                    f.write("    print(f'Maximum value: {max_value}')\n")
                else:
                    f.write("    # Semantic error: complex logical mistake\n")
                    f.write("    even_count = 0\n")
                    f.write("    odd_count = 0\n")
                    f.write("    for value in data:\n")
                    f.write("        if int(value) % 2 == 0:\n")
                    f.write("            odd_count += 1  # Should increment even_count\n")
                    f.write("        else:\n")
                    f.write("            even_count += 1  # Should increment odd_count\n")
                    f.write("    print(f'Even values: {even_count}, Odd values: {odd_count}')\n")
            
            # Close the main function and add the entry point
            f.write("\nif __name__ == '__main__':\n")
            f.write("    main()\n")
        
        return file_path

class LearningBenchmark:
    """Benchmark comparing QuantumAI learning vs conventional error handling"""
    
    def __init__(self):
        """Initialize the learning benchmark"""
        self.test_dir = TEST_DIR
        os.makedirs(self.test_dir, exist_ok=True)
        
        self.error_generator = ErrorGenerator(self.test_dir)
        self.results = {
            "quantum": {cycle: {} for cycle in range(1, LEARNING_CYCLES + 1)},
            "conventional": {cycle: {} for cycle in range(1, LEARNING_CYCLES + 1)}
        }
        
        self.test_files = []
        
    def generate_test_suite(self):
        """Generate a suite of test files with various errors"""
        logger.info("Generating test suite...")
        
        for error_type in ERROR_TYPES:
            for i in range(ITERATIONS):
                # Use phi-harmonic complexity scaling
                complexity = ((PHI * i) % 1)
                file_path = self.error_generator.generate_error_file(error_type, complexity)
                self.test_files.append(file_path)
                logger.info(f"Generated test file: {file_path}")
        
        logger.info(f"Generated {len(self.test_files)} test files")
    
    def run_quantum_test(self, file_path: str, cycle: int) -> Dict[str, Any]:
        """Run a test using the QuantumAI system"""
        start_time = time.time()
        
        # Create a new orchestrator for this test
        orchestrator = QuantumOrchestrator(file_path)
        
        # Run and heal the file
        orchestrator.run_and_heal(max_attempts=3)
        
        # Check if the file runs successfully after healing
        import subprocess
        import sys
        result = subprocess.run(
            [sys.executable, file_path],
            capture_output=True, text=True
        )
        
        success = result.returncode == 0
        duration = time.time() - start_time
        
        # Get quantum fingerprint and phi-resonance
        meta_demo = QuantumMetaDemoSimplified()
        with open(file_path, 'r') as f:
            content = f.read()
        
        analysis = meta_demo.analyze_function(content, "main")
        phi_resonance = analysis.get("phi_resonance", 0.0)
        
        return {
            "success": success,
            "duration": duration,
            "phi_resonance": phi_resonance,
            "error_output": result.stderr if not success else ""
        }
    
    def run_conventional_test(self, file_path: str, cycle: int) -> Dict[str, Any]:
        """Run a test using a conventional error handling system"""
        start_time = time.time()
        
        # Create a conventional error handler
        handler = ConventionalErrorHandler(file_path)
        
        # Try to run the file and handle errors
        import subprocess
        import sys
        
        for attempt in range(3):  # Max 3 attempts
            result = subprocess.run(
                [sys.executable, file_path],
                capture_output=True, text=True
            )
            
            if result.returncode == 0:
                break
                
            # Try to fix the error
            fixed = handler.detect_and_fix(result.stderr)
            if not fixed:
                break
        
        success = result.returncode == 0
        duration = time.time() - start_time
        
        # Get handler stats
        stats = handler.get_stats()
        
        return {
            "success": success,
            "duration": duration,
            "stats": stats,
            "error_output": result.stderr if not success else ""
        }
    
    def run_benchmark_cycle(self, cycle: int):
        """Run a complete benchmark cycle"""
        logger.info(f"Running benchmark cycle {cycle}...")
        
        quantum_successes = 0
        conventional_successes = 0
        quantum_durations = []
        conventional_durations = []
        
        for file_path in self.test_files:
            # Run quantum test
            logger.info(f"Running quantum test on {os.path.basename(file_path)}")
            quantum_result = self.run_quantum_test(file_path, cycle)
            quantum_durations.append(quantum_result["duration"])
            if quantum_result["success"]:
                quantum_successes += 1
            
            # Run conventional test
            logger.info(f"Running conventional test on {os.path.basename(file_path)}")
            conventional_result = self.run_conventional_test(file_path, cycle)
            conventional_durations.append(conventional_result["duration"])
            if conventional_result["success"]:
                conventional_successes += 1
            
            # Store detailed results
            file_name = os.path.basename(file_path)
            self.results["quantum"][cycle][file_name] = quantum_result
            self.results["conventional"][cycle][file_name] = conventional_result
        
        # Calculate cycle statistics
        quantum_success_rate = quantum_successes / len(self.test_files) * 100
        conventional_success_rate = conventional_successes / len(self.test_files) * 100
        
        quantum_avg_duration = statistics.mean(quantum_durations)
        conventional_avg_duration = statistics.mean(conventional_durations)
        
        # Store cycle summary
        self.results["quantum"][cycle]["summary"] = {
            "success_rate": quantum_success_rate,
            "avg_duration": quantum_avg_duration,
            "total_files": len(self.test_files),
            "successful_files": quantum_successes
        }
        
        self.results["conventional"][cycle]["summary"] = {
            "success_rate": conventional_success_rate,
            "avg_duration": conventional_avg_duration,
            "total_files": len(self.test_files),
            "successful_files": conventional_successes
        }
        
        logger.info(f"Cycle {cycle} complete")
        logger.info(f"Quantum success rate: {quantum_success_rate:.2f}%")
        logger.info(f"Conventional success rate: {conventional_success_rate:.2f}%")
    
    def run_full_benchmark(self):
        """Run the full benchmark with multiple learning cycles"""
        logger.info("Starting full benchmark...")
        
        # Generate test suite
        self.generate_test_suite()
        
        # Run benchmark cycles
        for cycle in range(1, LEARNING_CYCLES + 1):
            self.run_benchmark_cycle(cycle)
        
        # Save results
        self.save_results()
        
        # Generate visualizations
        self.generate_visualizations()
        
        logger.info("Benchmark complete")
    
    def save_results(self):
        """Save benchmark results to a file"""
        results_file = os.path.join(self.test_dir, "benchmark_results.json")
        with open(results_file, 'w') as f:
            json.dump(self.results, f, indent=2)
        
        logger.info(f"Results saved to {results_file}")
    
    def generate_visualizations(self):
        """Generate visualizations of benchmark results"""
        # Extract data for plotting
        cycles = list(range(1, LEARNING_CYCLES + 1))
        
        quantum_success_rates = [self.results["quantum"][cycle]["summary"]["success_rate"] for cycle in cycles]
        conventional_success_rates = [self.results["conventional"][cycle]["summary"]["success_rate"] for cycle in cycles]
        
        quantum_durations = [self.results["quantum"][cycle]["summary"]["avg_duration"] for cycle in cycles]
        conventional_durations = [self.results["conventional"][cycle]["summary"]["avg_duration"] for cycle in cycles]
        
        # Create success rate plot
        plt.figure(figsize=(10, 6))
        plt.plot(cycles, quantum_success_rates, 'b-', marker='o', label='QuantumAI')
        plt.plot(cycles, conventional_success_rates, 'r-', marker='x', label='Conventional')
        plt.xlabel('Learning Cycle')
        plt.ylabel('Success Rate (%)')
        plt.title('Error Correction Success Rate by Learning Cycle')
        plt.legend()
        plt.grid(True)
        success_plot_file = os.path.join(self.test_dir, "success_rates.png")
        plt.savefig(success_plot_file)
        
        # Create duration plot
        plt.figure(figsize=(10, 6))
        plt.plot(cycles, quantum_durations, 'b-', marker='o', label='QuantumAI')
        plt.plot(cycles, conventional_durations, 'r-', marker='x', label='Conventional')
        plt.xlabel('Learning Cycle')
        plt.ylabel('Average Duration (seconds)')
        plt.title('Error Correction Duration by Learning Cycle')
        plt.legend()
        plt.grid(True)
        duration_plot_file = os.path.join(self.test_dir, "durations.png")
        plt.savefig(duration_plot_file)
        
        logger.info(f"Visualizations saved to {self.test_dir}")
    
    def print_summary(self):
        """Print a summary of the benchmark results"""
        print("\n" + "="*80)
        print(" QUANTUM LEARNING BENCHMARK RESULTS ")
        print("="*80)
        
        # Calculate improvement rates
        quantum_first_success = self.results["quantum"][1]["summary"]["success_rate"]
        quantum_last_success = self.results["quantum"][LEARNING_CYCLES]["summary"]["success_rate"]
        quantum_improvement = quantum_last_success - quantum_first_success
        
        conventional_first_success = self.results["conventional"][1]["summary"]["success_rate"]
        conventional_last_success = self.results["conventional"][LEARNING_CYCLES]["summary"]["success_rate"]
        conventional_improvement = conventional_last_success - conventional_first_success
        
        quantum_first_duration = self.results["quantum"][1]["summary"]["avg_duration"]
        quantum_last_duration = self.results["quantum"][LEARNING_CYCLES]["summary"]["avg_duration"]
        quantum_speedup = (quantum_first_duration - quantum_last_duration) / quantum_first_duration * 100
        
        conventional_first_duration = self.results["conventional"][1]["summary"]["avg_duration"]
        conventional_last_duration = self.results["conventional"][LEARNING_CYCLES]["summary"]["avg_duration"]
        conventional_speedup = (conventional_first_duration - conventional_last_duration) / conventional_first_duration * 100
        
        print("\nSuccess Rate Improvement:")
        print(f"  QuantumAI: {quantum_improvement:.2f}% ({quantum_first_success:.2f}% → {quantum_last_success:.2f}%)")
        print(f"  Conventional: {conventional_improvement:.2f}% ({conventional_first_success:.2f}% → {conventional_last_success:.2f}%)")
        
        print("\nPerformance Improvement:")
        print(f"  QuantumAI: {quantum_speedup:.2f}% faster ({quantum_first_duration:.4f}s → {quantum_last_duration:.4f}s)")
        print(f"  Conventional: {conventional_speedup:.2f}% faster ({conventional_first_duration:.4f}s → {conventional_last_duration:.4f}s)")
        
        print("\nLearning Effectiveness:")
        learning_advantage = quantum_improvement - conventional_improvement
        print(f"  QuantumAI learning advantage: {learning_advantage:.2f}%")
        
        print("\nCONCLUSION:")
        if quantum_improvement > conventional_improvement:
            print("  🌟 QuantumAI demonstrates superior learning from errors")
            print(f"  {learning_advantage:.2f}% greater improvement in success rate")
            print("  Errors are successfully converted into learning opportunities")
        else:
            print("  ⚠️ Conventional system showed better improvement")
            print(f"  {-learning_advantage:.2f}% greater improvement in success rate")
        
        print("="*80)
        print(f"Detailed results and visualizations available in the '{self.test_dir}' directory")
        print("="*80)

def run_learning_benchmark():
    """Run the quantum learning benchmark"""
    benchmark = LearningBenchmark()
    benchmark.run_full_benchmark()
    benchmark.print_summary()

if __name__ == "__main__":
    # Check if matplotlib is available
    try:
        import matplotlib
    except ImportError:
        print("Warning: matplotlib not found. Visualizations will not be generated.")
        print("Install matplotlib with: pip install matplotlib")
    
    run_learning_benchmark()
