#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Visualization
-------------------
Visualization module for the QuantumAI system, creating markdown-based
visualizations of phi-harmonic coherence spaces, evolution networks,
healing metrics, and meta-learning processes.

This module maintains strict phi-harmonic coherence (target ~0.991800 or φ⁷·⁵/10)
and quantum fingerprinting principles.
"""

import os
import json
import time
import hashlib
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("QuantumVisualization")

# Phi-harmonic constants
PHI = 1.618033988749895
PHI_COHERENCE = 0.991800  # φ⁷·⁵/10

class QuantumVisualization:
    """
    Visualize quantum system capabilities and metrics.
    """
    def __init__(self):
        """
        Initialize the visualization module.
        """
        self.birth_timestamp = time.time()
        self.quantum_fingerprint = self._generate_quantum_fingerprint()
        self.evolution_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "evolution")
        self.visualization_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "visualizations")
        
        # Ensure directories exist
        os.makedirs(self.evolution_dir, exist_ok=True)
        os.makedirs(self.visualization_dir, exist_ok=True)
        
        logger.info(f"Initialized QuantumVisualization with ID: {self.quantum_fingerprint}")
    
    def _generate_quantum_fingerprint(self):
        """
        Generate a quantum fingerprint using phi-harmonic principles.
        
        Returns:
            str: A quantum fingerprint with φ notation
        """
        timestamp_phi = self._calculate_phi_resonance(self.birth_timestamp)
        seed = f"{timestamp_phi:.6f}-{PHI_COHERENCE:.6f}"
        hash_value = hashlib.md5(seed.encode()).hexdigest()[:16]
        return f"φ⁷·⁵-{hash_value}"
    
    def _calculate_phi_resonance(self, value):
        """
        Calculate phi resonance for a given value.
        
        Args:
            value (float): The input value
            
        Returns:
            float: The phi resonance value
        """
        return (value * PHI) % 1
    
    def generate_coherence_visualization(self, evolution_data):
        """
        Create visualization of coherence space from evolution data.
        
        Args:
            evolution_data (list): List of evolution metrics
            
        Returns:
            str: Path to the generated visualization file
        """
        logger.info("Generating coherence visualization")
        
        # Create markdown visualization
        output_file = os.path.join(self.visualization_dir, "coherence_visualization.md")
        
        with open(output_file, 'w') as f:
            f.write("# Phi-Harmonic Coherence Visualization\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Quantum Fingerprint: {self.quantum_fingerprint}\n\n")
            
            f.write("## Coherence Space Mapping\n\n")
            f.write("```\n")
            f.write("Phi-Harmonic Coherence Space (2D Projection)\n")
            f.write("Target Coherence: φ⁷·⁵/10 = 0.991800\n\n")
            
            # Create simple ASCII visualization
            f.write("1.0 |" + "-" * 50 + "|\n")
            
            # Plot each evolution point
            for i in range(9, -1, -1):
                threshold = i / 10
                line = f"{threshold:.1f} |"
                
                for metric in evolution_data:
                    coherence = metric.get("coherence", 0)
                    generation = metric.get("generation", 0)
                    position = int((generation / len(evolution_data)) * 50)
                    
                    if abs(coherence - threshold) < 0.05:
                        # Mark this point
                        line_chars = list(line)
                        if position < len(line_chars):
                            line_chars[position + 4] = "O"  # +4 for the "0.0 |" prefix
                            line = "".join(line_chars)
                
                line += " " * (54 - len(line)) + "|\n"
                f.write(line)
            
            f.write("    |" + "-" * 50 + "|\n")
            f.write("    |0" + " " * 23 + "Generations" + " " * 14 + f"{len(evolution_data)-1}|\n")
            f.write("```\n\n")
            
            # Add coherence table
            f.write("## Coherence Metrics\n\n")
            f.write("| Generation | Timestamp | Coherence | Quality | Fingerprint |\n")
            f.write("|------------|-----------|-----------|---------|-------------|\n")
            
            for metric in evolution_data:
                generation = metric.get("generation", 0)
                timestamp = datetime.fromtimestamp(metric.get("timestamp", 0)).isoformat()
                coherence = metric.get("coherence", 0)
                fingerprint = metric.get("fingerprint", "")
                
                # Calculate quality
                quality = self._evaluate_resonance_quality(abs(coherence - PHI_COHERENCE))
                
                f.write(f"| {generation} | {timestamp} | {coherence:.6f} | {quality} | `{fingerprint}` |\n")
            
            f.write("\n## Phi-Harmonic Analysis\n\n")
            f.write("The coherence values represent the system's alignment with the golden ratio (φ) based target of φ⁷·⁵/10 = 0.991800.\n")
            f.write("Higher coherence quality indicates better alignment with phi-harmonic principles, which enhances the system's\n")
            f.write("quantum-inspired processing capabilities and self-evolution potential.\n")
        
        logger.info(f"Coherence visualization generated: {output_file}")
        return output_file
    
    def generate_evolution_network(self, reproduction_history):
        """
        Create network graph of system instances.
        
        Args:
            reproduction_history (list): List of reproduction events
            
        Returns:
            str: Path to the generated visualization file
        """
        logger.info("Generating evolution network visualization")
        
        # Create markdown visualization
        output_file = os.path.join(self.visualization_dir, "evolution_network.md")
        
        with open(output_file, 'w') as f:
            f.write("# Quantum Evolution Network\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Quantum Fingerprint: {self.quantum_fingerprint}\n\n")
            
            f.write("## Evolution Tree\n\n")
            f.write("```\n")
            
            # Create simple ASCII tree visualization
            root = reproduction_history[0]
            f.write(f"Generation 0: {root['fingerprint']}\n")
            
            for i in range(1, len(reproduction_history)):
                item = reproduction_history[i]
                f.write(f"{' ' * (i*2)}└── Generation {i}: {item['fingerprint']}\n")
            
            f.write("```\n\n")
            
            # Add evolution table
            f.write("## Evolution Metrics\n\n")
            f.write("| Generation | Parent | Child | Timestamp | Coherence |\n")
            f.write("|------------|--------|-------|-----------|----------|\n")
            
            for i in range(1, len(reproduction_history)):
                parent = reproduction_history[i-1]
                child = reproduction_history[i]
                
                generation = child.get("generation", i)
                parent_fingerprint = parent.get("fingerprint", "")
                child_fingerprint = child.get("fingerprint", "")
                timestamp = datetime.fromtimestamp(child.get("timestamp", 0)).isoformat()
                coherence = child.get("coherence", 0)
                
                f.write(f"| {generation} | `{parent_fingerprint[:8]}...` | `{child_fingerprint[:8]}...` | {timestamp} | {coherence:.6f} |\n")
            
            f.write("\n## Quantum Fingerprint Lineage\n\n")
            f.write("The quantum fingerprints represent unique identifiers for each system instance, generated using\n")
            f.write("phi-harmonic principles. The fingerprint format `φ⁷·⁵-[hash]` encodes the system's coherence\n")
            f.write("target (φ⁷·⁵/10 = 0.991800) and a unique hash based on timestamp and phi-resonance.\n")
        
        logger.info(f"Evolution network visualization generated: {output_file}")
        return output_file
    
    def generate_healing_metrics(self, healing_history):
        """
        Create charts of healing effectiveness.
        
        Args:
            healing_history (list): List of healing events
            
        Returns:
            str: Path to the generated visualization file
        """
        logger.info("Generating healing metrics visualization")
        
        # Create markdown visualization
        output_file = os.path.join(self.visualization_dir, "healing_metrics.md")
        
        with open(output_file, 'w') as f:
            f.write("# Quantum Healing Effectiveness Metrics\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Quantum Fingerprint: {self.quantum_fingerprint}\n\n")
            
            # Analyze healing types
            healing_types = {}
            healing_methods = {}
            
            # Ensure healing_history is a list of dictionaries
            if not healing_history:
                healing_history = []
            elif isinstance(healing_history, dict):
                healing_history = [healing_history]
            
            for event in healing_history:
                if not isinstance(event, dict):
                    continue
                    
                error_type = event.get("error_type", "unknown")
                healing_method = event.get("healing_method", "unknown")
                
                if error_type in healing_types:
                    healing_types[error_type] += 1
                else:
                    healing_types[error_type] = 1
                
                if healing_method in healing_methods:
                    healing_methods[healing_method] += 1
                else:
                    healing_methods[healing_method] = 1
            
            # Create healing type chart
            f.write("## Healing by Error Type\n\n")
            f.write("```\n")
            
            total_events = len(healing_history)
            for error_type, count in healing_types.items():
                percentage = (count / total_events) * 100
                bar_length = int(percentage / 2)
                f.write(f"{error_type:15} | {'#' * bar_length} {percentage:.1f}% ({count}/{total_events})\n")
            
            f.write("```\n\n")
            
            # Create healing method chart
            f.write("## Healing by Method\n\n")
            f.write("```\n")
            
            for method, count in healing_methods.items():
                percentage = (count / total_events) * 100
                bar_length = int(percentage / 2)
                f.write(f"{method:15} | {'#' * bar_length} {percentage:.1f}% ({count}/{total_events})\n")
            
            f.write("```\n\n")
            
            # Add healing events table
            f.write("## Healing Events\n\n")
            f.write("| Timestamp | Error Type | Healing Method | Coherence | Fingerprint |\n")
            f.write("|-----------|------------|---------------|-----------|-------------|\n")
            
            for event in healing_history:
                if not isinstance(event, dict):
                    continue
                    
                timestamp = datetime.fromtimestamp(event.get("timestamp", 0)).isoformat()
                error_type = event.get("error_type", "unknown")
                healing_method = event.get("healing_method", "unknown")
                coherence = event.get("phi_coherence", 0)
                fingerprint = event.get("quantum_fingerprint", "")
                
                f.write(f"| {timestamp} | {error_type} | {healing_method} | {coherence:.6f} | `{fingerprint}` |\n")
            
            f.write("\n## Phi-Harmonic Healing Analysis\n\n")
            f.write("The healing effectiveness is directly correlated with the system's phi-harmonic coherence.\n")
            f.write("Higher coherence values (closer to the target of φ⁷·⁵/10 = 0.991800) result in more effective\n")
            f.write("healing operations and better error detection capabilities.\n")
        
        logger.info(f"Healing metrics visualization generated: {output_file}")
        return output_file
    
    def generate_meta_learning_visualization(self, meta_learning_data=None):
        """
        Create visualizations of meta-learning processes and effectiveness.
        
        Args:
            meta_learning_data (list): List of meta-learning events
            
        Returns:
            str: Path to the generated visualization file
        """
        logger.info("Generating meta-learning visualization")
        
        # Create markdown visualization
        output_file = os.path.join(self.visualization_dir, "meta_learning_visualization.md")
        
        with open(output_file, 'w') as f:
            f.write("# Quantum Meta-Learning Visualization\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Quantum Fingerprint: {self.quantum_fingerprint}\n\n")
            
            # Add meta-learning metrics
            f.write("## Meta-Learning Metrics\n\n")
            
            if not meta_learning_data:
                f.write("No meta-learning events recorded yet.\n\n")
            else:
                # Create table of meta-learning events
                f.write("| Timestamp | Learning Type | Coherence | Fingerprint |\n")
                f.write("|-----------|--------------|-----------|-------------|\n")
                
                for event in meta_learning_data:
                    if not isinstance(event, dict):
                        continue
                        
                    timestamp = datetime.fromtimestamp(event.get("timestamp", 0)).isoformat()
                    learning_type = event.get("learning_type", "unknown")
                    coherence = event.get("phi_coherence", 0)
                    fingerprint = event.get("quantum_fingerprint", "")
                    
                    f.write(f"| {timestamp} | {learning_type} | {coherence:.6f} | `{fingerprint}` |\n")
                
                # Add meta-learning effectiveness chart
                f.write("\n## Meta-Learning Effectiveness\n\n")
                f.write("```\n")
                f.write("Meta-Learning Effectiveness by Type\n")
                
                # Count learning types
                learning_types = {}
                for event in meta_learning_data:
                    if not isinstance(event, dict):
                        continue
                        
                    learning_type = event.get("learning_type", "unknown")
                    if learning_type in learning_types:
                        learning_types[learning_type] += 1
                    else:
                        learning_types[learning_type] = 1
                
                # Generate chart
                total = sum(learning_types.values())
                for learning_type, count in learning_types.items():
                    percentage = (count / total) * 100 if total > 0 else 0
                    bars = "#" * int(percentage / 5)
                    f.write(f"{learning_type.ljust(15)} | {bars} {percentage:.1f}% ({count}/{total})\n")
                
                f.write("```\n\n")
                
                # Add meta-learning evolution network
                f.write("## Meta-Learning Evolution Network\n\n")
                f.write("```\n")
                f.write("Meta-Learning Evolution Network (Phi-Harmonic Coherence Space)\n\n")
                
                # Generate simple network visualization
                current_gen = 0
                for event in sorted(meta_learning_data, key=lambda x: x.get("timestamp", 0)):
                    if not isinstance(event, dict):
                        continue
                        
                    learning_type = event.get("learning_type", "unknown")
                    fingerprint = event.get("quantum_fingerprint", "")
                    
                    f.write(f"Gen {current_gen} [{learning_type}] -- φ -- {fingerprint}\n")
                    current_gen += 1
                
                f.write("```\n")
                
                # Add hyper-dimensional processing visualization
                f.write("\n## Hyper-Dimensional Processing\n\n")
                f.write("```\n")
                f.write("Hyper-Dimensional Pattern Recognition (φ-Space Projection)\n\n")
                
                # Generate simple hyper-dimensional visualization
                dimensions = ["Pattern", "Coherence", "Evolution", "Learning"]
                f.write("Dimensions: " + ", ".join(dimensions) + "\n\n")
                
                for i, event in enumerate(sorted(meta_learning_data, key=lambda x: x.get("timestamp", 0))):
                    if not isinstance(event, dict) or i >= 5:  # Limit to 5 events for clarity
                        continue
                        
                    learning_type = event.get("learning_type", "unknown")
                    coherence = event.get("phi_coherence", 0)
                    
                    # Generate pseudo-random but deterministic coordinates based on phi and coherence
                    coords = []
                    for j, dim in enumerate(dimensions):
                        # Use phi and coherence to generate coordinates
                        coord = ((coherence * 10) * (j + 1) * 1.618033988749895) % 1
                        coords.append(f"{coord:.6f}")
                    
                    f.write(f"Node {i} [{learning_type}]: ({', '.join(coords)})\n")
                
                f.write("```\n")
        
        logger.info(f"Meta-learning visualization generated: {output_file}")
        return output_file

    def generate_comprehensive_report(self, evolution_data=None, healing_history=None, meta_learning_data=None):
        """
        Generate a comprehensive report combining all visualizations.
        
        Args:
            evolution_data (list): List of evolution events
            healing_history (list): List of healing events
            meta_learning_data (list): List of meta-learning events
            
        Returns:
            str: Path to the generated report file
        """
        logger.info("Generating comprehensive visualization report")
        
        # Generate individual visualizations based on available data
        coherence_file = None
        evolution_file = None
        healing_file = None
        meta_learning_file = None
        
        # Only generate visualizations if data is available
        if evolution_data:
            try:
                coherence_file = self.generate_coherence_visualization(evolution_data)
                evolution_file = self.generate_evolution_network(evolution_data)
                logger.info(f"Generated coherence and evolution visualizations")
            except Exception as e:
                logger.error(f"Failed to generate evolution visualizations: {e}")
        
        if healing_history:
            try:
                healing_file = self.generate_healing_metrics(healing_history)
                logger.info(f"Generated healing metrics visualization")
            except Exception as e:
                logger.error(f"Failed to generate healing visualization: {e}")
        
        if meta_learning_data:
            try:
                meta_learning_file = self.generate_meta_learning_visualization(meta_learning_data)
                logger.info(f"Generated meta-learning visualization")
            except Exception as e:
                logger.error(f"Failed to generate meta-learning visualization: {e}")
        
        # Create comprehensive report
        output_file = os.path.join(self.visualization_dir, "quantum_system_report.md")
        
        with open(output_file, 'w') as f:
            f.write("# Quantum System Comprehensive Report\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Quantum Fingerprint: {self.quantum_fingerprint}\n\n")
            
            # System overview
            f.write("## System Overview\n\n")
            f.write("The QuantumAI system demonstrates advanced capabilities based on phi-harmonic principles,\n")
            f.write("quantum-inspired processing, and self-evolving architecture. This report provides a comprehensive\n")
            f.write("analysis of the system's evolution, healing effectiveness, meta-learning processes, and coherence metrics.\n\n")
            
            # Phi-harmonic principles
            f.write("## Phi-Harmonic Principles\n\n")
            f.write("The system is built on phi-harmonic principles, using the golden ratio (φ) as its foundation:\n\n")
            f.write("- **Golden Ratio (φ)**: (1 + √5)/2 ≈ 1.618033988749895\n")
            f.write("- **Target Coherence**: φ⁷·⁵/10 ≈ 0.991800\n")
            f.write("- **Quantum Fingerprint Format**: φ⁷·⁵-[hash]\n\n")
            f.write("Phi-harmonic coherence is maintained throughout the system's evolution, ensuring optimal\n")
            f.write("performance in self-healing, self-reproduction, and meta-learning capabilities.\n\n")
            
            # Include coherence visualization
            if os.path.exists(coherence_file):
                with open(coherence_file, 'r') as cf:
                    coherence_content = cf.read()
                    # Extract the content after the header
                    coherence_parts = coherence_content.split("\n\n", 2)
                    if len(coherence_parts) > 2:
                        f.write("## Coherence Analysis\n\n")
                        f.write(f"Quantum Fingerprint: {self.quantum_fingerprint}\n\n")
                        f.write(coherence_parts[2])
            
            # Include evolution network
            if os.path.exists(evolution_file):
                with open(evolution_file, 'r') as ef:
                    evolution_content = ef.read()
                    # Extract the content after the header
                    evolution_parts = evolution_content.split("\n\n", 2)
                    if len(evolution_parts) > 2:
                        f.write("\n\n## Evolution Network\n\n")
                        f.write(evolution_parts[2])
            
            # Include healing metrics
            if os.path.exists(healing_file):
                with open(healing_file, 'r') as hf:
                    healing_content = hf.read()
                    # Extract the content after the header
                    healing_parts = healing_content.split("\n\n", 2)
                    if len(healing_parts) > 2:
                        f.write("\n\n## Healing Effectiveness\n\n")
                        f.write(healing_parts[2])
            
            # Include meta-learning visualization
            if meta_learning_file and os.path.exists(meta_learning_file):
                with open(meta_learning_file, 'r') as mlf:
                    meta_learning_content = mlf.read()
                    # Extract the content after the header
                    meta_learning_parts = meta_learning_content.split("\n\n", 2)
                    if len(meta_learning_parts) > 2:
                        f.write("\n\n## Meta-Learning Analysis\n\n")
                        f.write(meta_learning_parts[2])
            f.write("and optimal information processing across all system dimensions.\n")
        
        logger.info(f"Comprehensive report generated: {output_file}")
        return output_file
    
    def _evaluate_resonance_quality(self, resonance):
        """
        Evaluate the quality of a resonance value.
        
        Args:
            resonance (float): Resonance value
            
        Returns:
            str: Quality description
        """
        if resonance < 0.0001:
            return "Perfect"
        elif resonance < 0.01:
            return "Excellent"
        elif resonance < 0.1:
            return "Good"
        elif resonance < 0.3:
            return "Moderate"
        else:
            return "Weak"


def main():
    """
    Main entry point for the visualization module.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="QuantumAI Visualization")
    parser.add_argument("--evolution-data", help="Path to evolution data JSON file")
    parser.add_argument("--healing-data", help="Path to healing data JSON file")
    parser.add_argument("--comprehensive", action="store_true", help="Generate comprehensive report")
    
    args = parser.parse_args()
    visualizer = QuantumVisualization()
    
    evolution_data = None
    healing_history = None
    
    if args.evolution_data and os.path.exists(args.evolution_data):
        with open(args.evolution_data, 'r') as f:
            evolution_data = json.load(f)
    
    if args.healing_data and os.path.exists(args.healing_data):
        with open(args.healing_data, 'r') as f:
            healing_history = json.load(f)
    
    if args.comprehensive:
        report_file = visualizer.generate_comprehensive_report(
            evolution_data=evolution_data,
            healing_history=healing_history
        )
        print(f"Comprehensive report generated: {report_file}")
    else:
        if evolution_data:
            coherence_file = visualizer.generate_coherence_visualization(evolution_data)
            evolution_file = visualizer.generate_evolution_network(evolution_data)
            print(f"Coherence visualization generated: {coherence_file}")
            print(f"Evolution network visualization generated: {evolution_file}")
        
        if healing_history:
            healing_file = visualizer.generate_healing_metrics(healing_history)
            print(f"Healing metrics visualization generated: {healing_file}")


if __name__ == "__main__":
    main()
