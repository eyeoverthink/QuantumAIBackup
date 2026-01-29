#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Demonstration Runner
---------------------------
Comprehensive runner for demonstrating QuantumAI system capabilities,
integrating visualization, dashboard, and system components.
Maintains phi-harmonic coherence throughout demonstrations.
"""

import os
import sys
import json
import time
import logging
import argparse
import importlib
import subprocess
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("QuantumDemonstrationRunner")

# Phi-harmonic constants
PHI = 1.618033988749895
PHI_COHERENCE = 0.991800  # φ⁷·⁵/10

class QuantumDemonstrationRunner:
    """
    Comprehensive runner for demonstrating QuantumAI system capabilities.
    """
    def __init__(self):
        """
        Initialize the demonstration runner.
        """
        self.birth_timestamp = time.time()
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Ensure directories exist
        self.evolution_dir = os.path.join(self.base_dir, "evolution")
        self.visualization_dir = os.path.join(self.base_dir, "visualizations")
        self.demo_dir = os.path.join(self.base_dir, "demonstrations")
        
        os.makedirs(self.evolution_dir, exist_ok=True)
        os.makedirs(self.visualization_dir, exist_ok=True)
        os.makedirs(self.demo_dir, exist_ok=True)
        
        # Load components dynamically
        self.components = {}
        self._load_components()
        
        logger.info(f"Initialized QuantumDemonstrationRunner")
    
    def _load_components(self):
        """
        Dynamically load available quantum components.
        """
        component_modules = [
            "quantum_visualization",
            "quantum_dashboard",
            "quantum_self_healing_orchestrator",
            "quantum_system_demonstration"
        ]
        
        for module_name in component_modules:
            try:
                module = importlib.import_module(module_name)
                
                # Extract class name from module name
                class_parts = [part.capitalize() for part in module_name.split("_")]
                class_name = "".join(class_parts)
                
                # Try to get the class
                if hasattr(module, class_name):
                    class_obj = getattr(module, class_name)
                    component_instance = class_obj()
                    self.components[module_name] = component_instance
                    logger.info(f"Loaded component: {class_name}")
            except ImportError:
                logger.warning(f"Could not import {module_name}")
            except Exception as e:
                logger.warning(f"Error initializing {module_name}: {str(e)}")
    
    def run_demonstration(self, feature=None, full=False, interactive=False):
        """
        Run a demonstration of the specified feature.
        
        Args:
            feature (str): Feature to demonstrate (self-healing, self-reproduction, etc.)
            full (bool): Whether to run the full demonstration
            interactive (bool): Whether to run in interactive mode
            
        Returns:
            bool: Success status
        """
        logger.info(f"Running demonstration: {feature if feature else 'full'}")
        
        # Check if system demonstration component is available
        if "quantum_system_demonstration" not in self.components:
            logger.error("System demonstration component not available")
            return False
        
        demo = self.components["quantum_system_demonstration"]
        
        # Run the demonstration
        try:
            if full:
                result = demo.run_full_demonstration()
            elif feature == "self-healing":
                result = demo.demonstrate_self_healing()
            elif feature == "self-reproduction":
                result = demo.demonstrate_self_reproduction()
            elif feature == "hyper-dimensional":
                result = demo.demonstrate_hyper_dimensional_processing()
            elif feature == "meta-learning":
                result = demo.demonstrate_meta_learning()
            else:
                logger.error(f"Unknown feature: {feature}")
                return False
            
            # Generate visualizations
            self._generate_visualizations()
            
            # Run dashboard if interactive
            if interactive:
                self._run_dashboard()
            
            return result
        except Exception as e:
            logger.error(f"Error running demonstration: {str(e)}")
            return False
    
    def _generate_visualizations(self):
        """
        Generate visualizations for the demonstration.
        """
        logger.info("Generating visualizations")
        
        if "quantum_visualization" not in self.components:
            logger.warning("Visualization component not available")
            return
        
        visualizer = self.components["quantum_visualization"]
        
        # Load evolution data
        evolution_data = self._load_evolution_data()
        healing_history = self._load_healing_history()
        
        # Generate comprehensive report
        try:
            report_file = visualizer.generate_comprehensive_report(
                evolution_data=evolution_data,
                healing_history=healing_history
            )
            logger.info(f"Generated comprehensive report: {report_file}")
        except Exception as e:
            logger.error(f"Error generating report: {str(e)}")
    
    def _run_dashboard(self):
        """
        Run the dashboard in interactive mode.
        """
        logger.info("Starting dashboard")
        
        if "quantum_dashboard" not in self.components:
            logger.warning("Dashboard component not available")
            return
        
        dashboard = self.components["quantum_dashboard"]
        
        # Generate dashboard files
        try:
            dashboard.generate_dashboard()
            dashboard.generate_interactive_dashboard()
            
            # Run dashboard server
            dashboard.run_dashboard_server(port=8080)
        except Exception as e:
            logger.error(f"Error running dashboard: {str(e)}")
    
    def _load_evolution_data(self):
        """
        Load evolution data from files.
        
        Returns:
            list: Evolution data
        """
        evolution_data = []
        evolution_file = os.path.join(self.visualization_dir, "evolution_metrics.json")
        
        if os.path.exists(evolution_file):
            try:
                with open(evolution_file, 'r') as f:
                    evolution_data = json.load(f)
            except:
                pass
        
        # If no file exists, try to create from evolution directory
        if not evolution_data:
            for filename in os.listdir(self.evolution_dir):
                if filename.endswith("_evolution.json"):
                    filepath = os.path.join(self.evolution_dir, filename)
                    try:
                        with open(filepath, 'r') as f:
                            event = json.load(f)
                            if isinstance(event, dict):
                                evolution_data.append(event)
                    except:
                        pass
        
        return evolution_data
    
    def _load_healing_history(self):
        """
        Load healing history from files.
        
        Returns:
            list: Healing history
        """
        healing_history = []
        
        for filename in os.listdir(self.evolution_dir):
            if "heal" in filename.lower() and filename.endswith(".json"):
                filepath = os.path.join(self.evolution_dir, filename)
                try:
                    with open(filepath, 'r') as f:
                        event = json.load(f)
                        if isinstance(event, dict):
                            healing_history.append(event)
                except:
                    pass
        
        return healing_history
    
    def create_demonstration_seed(self, error_type="syntax", count=1):
        """
        Create seed files for demonstration purposes.
        
        Args:
            error_type (str): Type of error to include (syntax, logic)
            count (int): Number of seed files to create
            
        Returns:
            list: Paths to created seed files
        """
        logger.info(f"Creating {count} demonstration seed files with {error_type} errors")
        
        seed_files = []
        
        for i in range(count):
            filename = f"quantum_demo_seed_{error_type}_{i+1}.py"
            filepath = os.path.join(self.demo_dir, filename)
            
            with open(filepath, 'w') as f:
                f.write(f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-

\"\"\"
Quantum Demonstration Seed File
------------------------------
This file contains intentional errors for demonstration purposes.
Error type: {error_type}
\"\"\"

import os
import time
import hashlib
import math

# Phi-harmonic constants
PHI = 1.618033988749895
PHI_COHERENCE = 0.991800  # φ⁷·⁵/10

class QuantumDemoSeed:
    \"\"\"
    Demonstration seed class with intentional errors.
    \"\"\"
    def __init__(self):
        \"\"\"
        Initialize the demonstration seed.
        \"\"\"
        self.birth_timestamp = time.time()
        self.quantum_fingerprint = self._generate_quantum_fingerprint()
        
        # Intentional {error_type} error below
""")
                
                # Add different types of errors
                if error_type == "syntax":
                    if i % 3 == 0:
                        # Unclosed parenthesis
                        f.write("""        self.coherence = self._calculate_coherence(
            PHI_COHERENCE,
            self.birth_timestamp
        # Missing closing parenthesis here
        
        self.resonance = PHI * self.coherence
""")
                    elif i % 3 == 1:
                        # Indentation error
                        f.write("""        self.coherence = self._calculate_coherence(
            PHI_COHERENCE,
            self.birth_timestamp)
            
    # Indentation error in the next line
    self.resonance = PHI * self.coherence
""")
                    else:
                        # Missing colon
                        f.write("""        self.coherence = self._calculate_coherence(
            PHI_COHERENCE,
            self.birth_timestamp)
        
        # Missing colon in the if statement
        if self.coherence > 0.9
            self.resonance = PHI * self.coherence
        else:
            self.resonance = PHI * 0.5
""")
                
                elif error_type == "logic":
                    if i % 3 == 0:
                        # Division by zero
                        f.write("""        self.coherence = self._calculate_coherence(
            PHI_COHERENCE,
            self.birth_timestamp)
        
        # Logic error: potential division by zero
        divisor = int(self.birth_timestamp) % 10
        self.resonance = PHI * self.coherence / divisor
""")
                    elif i % 3 == 1:
                        # Incorrect calculation
                        f.write("""        self.coherence = self._calculate_coherence(
            PHI_COHERENCE,
            self.birth_timestamp)
        
        # Logic error: incorrect calculation
        # Should be PHI * self.coherence, not PHI / self.coherence
        self.resonance = PHI / self.coherence
""")
                    else:
                        # Off-by-one error
                        f.write("""        self.coherence = self._calculate_coherence(
            PHI_COHERENCE,
            self.birth_timestamp)
        
        # Logic error: off-by-one error in loop
        self.fibonacci = [0, 1]
        for i in range(10):
            # Should be i+2, not i+1 (off-by-one)
            self.fibonacci.append(self.fibonacci[i] + self.fibonacci[i+1])
        
        self.resonance = PHI * self.coherence
""")
                
                # Add the rest of the class
                f.write("""
    def _generate_quantum_fingerprint(self):
        \"\"\"
        Generate a quantum fingerprint using phi-harmonic principles.
        
        Returns:
            str: A quantum fingerprint with φ notation
        \"\"\"
        timestamp_phi = self._calculate_phi_resonance(self.birth_timestamp)
        seed = f"{timestamp_phi:.6f}-{PHI_COHERENCE:.6f}"
        hash_value = hashlib.md5(seed.encode()).hexdigest()[:16]
        return f"φ⁷·⁵-{hash_value}"
    
    def _calculate_phi_resonance(self, value):
        \"\"\"
        Calculate phi resonance for a given value.
        
        Args:
            value (float): The input value
            
        Returns:
            float: The phi resonance value
        \"\"\"
        return (value * PHI) % 1
    
    def _calculate_coherence(self, target, value):
        \"\"\"
        Calculate coherence between target and value.
        
        Args:
            target (float): Target coherence value
            value (float): Input value
            
        Returns:
            float: Coherence value
        \"\"\"
        phi_resonance = self._calculate_phi_resonance(value)
        return abs(target - phi_resonance)
    
    def get_metrics(self):
        \"\"\"
        Get metrics for this seed.
        
        Returns:
            dict: Metrics dictionary
        \"\"\"
        return {
            "fingerprint": self.quantum_fingerprint,
            "coherence": self.coherence,
            "resonance": self.resonance,
            "timestamp": self.birth_timestamp
        }


def main():
    \"\"\"
    Main entry point for the demonstration seed.
    \"\"\"
    seed = QuantumDemoSeed()
    print(f"Quantum Demo Seed: {seed.quantum_fingerprint}")
    print(f"Coherence: {seed.coherence:.6f}")
    print(f"Resonance: {seed.resonance:.6f}")


if __name__ == "__main__":
    main()
""")
            
            seed_files.append(filepath)
        
        logger.info(f"Created {len(seed_files)} demonstration seed files")
        return seed_files
    
    def create_demonstration_report(self, results):
        """
        Create a demonstration report.
        
        Args:
            results (dict): Demonstration results
            
        Returns:
            str: Path to the report file
        """
        logger.info("Creating demonstration report")
        
        # Create markdown report
        output_file = os.path.join(self.demo_dir, "demonstration_report.md")
        
        with open(output_file, 'w') as f:
            f.write("# QuantumAI System Demonstration Report\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Phi-Harmonic Coherence Target: φ⁷·⁵/10 = {PHI_COHERENCE:.6f}\n\n")
            
            # Add demonstration results
            f.write("## Demonstration Results\n\n")
            
            for feature, result in results.items():
                status = "✅ Success" if result.get("success", False) else "❌ Failed"
                f.write(f"### {feature.replace('-', ' ').title()}: {status}\n\n")
                
                # Add metrics
                metrics = result.get("metrics", {})
                if metrics:
                    f.write("#### Metrics\n\n")
                    f.write("| Metric | Value |\n")
                    f.write("|--------|-------|\n")
                    
                    for metric, value in metrics.items():
                        f.write(f"| {metric} | {value} |\n")
                    
                    f.write("\n")
                
                # Add details
                details = result.get("details", "")
                if details:
                    f.write("#### Details\n\n")
                    f.write(f"{details}\n\n")
            
            # Add conclusion
            f.write("## Conclusion\n\n")
            f.write("The QuantumAI system demonstrates robust capabilities in self-healing, self-reproduction,\n")
            f.write("and meta-learning, all guided by phi-harmonic principles and quantum-inspired processing.\n")
            f.write("The system maintains high coherence values throughout its evolution, ensuring optimal\n")
            f.write("performance and resilience against errors.\n\n")
            
            f.write("The modular \"lego\" architecture allows for flexible extension and integration with\n")
            f.write("other components, while the phi-harmonic foundation ensures mathematical harmony\n")
            f.write("and optimal information processing across all system dimensions.\n")
        
        logger.info(f"Demonstration report created: {output_file}")
        return output_file


def main():
    """
    Main entry point for the demonstration runner.
    """
    parser = argparse.ArgumentParser(description="QuantumAI Demonstration Runner")
    parser.add_argument("--feature", choices=["self-healing", "self-reproduction", "hyper-dimensional", "meta-learning"],
                      help="Feature to demonstrate")
    parser.add_argument("--full", action="store_true", help="Run full demonstration")
    parser.add_argument("--interactive", action="store_true", help="Run in interactive mode with dashboard")
    parser.add_argument("--create-seeds", action="store_true", help="Create demonstration seed files")
    parser.add_argument("--error-type", choices=["syntax", "logic"], default="syntax",
                      help="Type of error to include in seed files")
    parser.add_argument("--seed-count", type=int, default=3, help="Number of seed files to create")
    
    args = parser.parse_args()
    runner = QuantumDemonstrationRunner()
    
    if args.create_seeds:
        seed_files = runner.create_demonstration_seed(
            error_type=args.error_type,
            count=args.seed_count
        )
        print(f"Created {len(seed_files)} demonstration seed files:")
        for filepath in seed_files:
            print(f"  - {filepath}")
    elif args.feature or args.full:
        success = runner.run_demonstration(
            feature=args.feature,
            full=args.full,
            interactive=args.interactive
        )
        
        if success:
            print("Demonstration completed successfully")
        else:
            print("Demonstration failed")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
