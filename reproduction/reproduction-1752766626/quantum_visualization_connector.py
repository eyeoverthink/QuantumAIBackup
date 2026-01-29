#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Visualization Connector
------------------------------
This module connects the QuantumVisualization framework with the QuantumSelfHealingOrchestrator
to provide real-time visualization of healing events, evolution metadata, and meta-learning processes.

It follows the "lego" architecture principle by adding new components without modifying existing ones.
"""

import os
import sys
import time
import json
import logging
from datetime import datetime
import importlib.util

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("QuantumVisualizationConnector")

# Phi-harmonic constants
PHI = 1.618033988749895
PHI_COHERENCE = 0.991800  # φ⁷·⁵/10

class QuantumVisualizationConnector:
    """
    Connects the QuantumVisualization framework with the QuantumSelfHealingOrchestrator
    to provide real-time visualization of healing events, evolution metadata, and meta-learning processes.
    """
    
    def __init__(self, visualization_module=None, dashboard_module=None):
        """
        Initialize the connector with visualization and dashboard modules.
        
        Args:
            visualization_module: QuantumVisualization instance or None
            dashboard_module: QuantumDashboard instance or None
        """
        self.birth_timestamp = time.time()
        self.quantum_fingerprint = self._generate_quantum_fingerprint()
        
        # Import visualization modules if not provided
        if visualization_module is None:
            try:
                from quantum_visualization import QuantumVisualization
                self.visualization = QuantumVisualization()
            except ImportError:
                logger.warning("QuantumVisualization module not found")
                self.visualization = None
        else:
            self.visualization = visualization_module
            
        if dashboard_module is None:
            try:
                from quantum_dashboard import QuantumDashboard
                self.dashboard = QuantumDashboard()
            except ImportError:
                logger.warning("QuantumDashboard module not found")
                self.dashboard = None
        else:
            self.dashboard = dashboard_module
            
        # Set up directories
        self.evolution_dir = "evolution"
        self.visualization_dir = "visualizations"
        os.makedirs(self.evolution_dir, exist_ok=True)
        os.makedirs(self.visualization_dir, exist_ok=True)
        
        # Initialize event listeners
        self.healing_events = []
        self.evolution_events = []
        self.meta_learning_events = []
        
        logger.info(f"Initialized QuantumVisualizationConnector with ID: {self.quantum_fingerprint}")
    
    def _generate_quantum_fingerprint(self):
        """
        Generate a quantum fingerprint using phi-harmonic principles.
        
        Returns:
            str: A quantum fingerprint with φ notation
        """
        import hashlib
        timestamp_phi = self.birth_timestamp * PHI % 1
        seed = f"{timestamp_phi:.6f}-{PHI_COHERENCE:.6f}"
        hash_value = hashlib.md5(seed.encode()).hexdigest()[:16]
        return f"φ⁷·⁵-{hash_value}"
    
    def connect_orchestrator(self, orchestrator):
        """
        Connect to a QuantumSelfHealingOrchestrator instance.
        
        Args:
            orchestrator: QuantumSelfHealingOrchestrator instance
            
        Returns:
            bool: True if connected successfully
        """
        if not orchestrator:
            logger.error("No orchestrator provided")
            return False
            
        try:
            # Store reference to orchestrator
            self.orchestrator = orchestrator
            
            # Monkey patch the orchestrator's record_evolution method to capture events
            original_record_evolution = orchestrator.record_evolution
            
            def enhanced_record_evolution(self, error_type, error_details, healing_method="self_healing"):
                # Call the original method
                result = original_record_evolution(self, error_type, error_details, healing_method)
                
                # Capture the event for visualization
                if hasattr(self, "_visualization_connector"):
                    self._visualization_connector.on_evolution_event(result)
                
                return result
            
            # Add reference to connector in orchestrator
            orchestrator._visualization_connector = self
            
            # Replace the method
            import types
            orchestrator.record_evolution = types.MethodType(enhanced_record_evolution, orchestrator)
            
            logger.info(f"Successfully connected to orchestrator: {orchestrator.quantum_fingerprint}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to connect to orchestrator: {e}")
            return False
    
    def on_evolution_event(self, evolution_metadata):
        """
        Handle evolution events from the orchestrator.
        
        Args:
            evolution_metadata: Dict with evolution metadata
        """
        logger.info(f"Received evolution event: {evolution_metadata.get('healing_method', 'unknown')}")
        
        # Store the event
        self.evolution_events.append(evolution_metadata)
        
        # Update visualizations
        self.update_visualizations()
        
        # Update dashboard
        self.update_dashboard()
    
    def on_healing_event(self, healing_metadata):
        """
        Handle healing events from the orchestrator.
        
        Args:
            healing_metadata: Dict with healing metadata
        """
        logger.info(f"Received healing event: {healing_metadata.get('error_type', 'unknown')}")
        
        # Store the event
        self.healing_events.append(healing_metadata)
        
        # Update visualizations
        self.update_visualizations()
        
        # Update dashboard
        self.update_dashboard()
    
    def on_meta_learning_event(self, meta_learning_metadata):
        """
        Handle meta-learning events from the orchestrator.
        
        Args:
            meta_learning_metadata: Dict with meta-learning metadata
        """
        logger.info(f"Received meta-learning event: {meta_learning_metadata.get('learning_type', 'unknown')}")
        
        # Ensure phi-harmonic coherence
        if 'phi_coherence' not in meta_learning_metadata:
            meta_learning_metadata['phi_coherence'] = PHI_COHERENCE
            
        if 'quantum_fingerprint' not in meta_learning_metadata:
            import hashlib
            timestamp = meta_learning_metadata.get('timestamp', time.time())
            timestamp_phi = timestamp * PHI % 1
            seed = f"{timestamp_phi:.6f}-{PHI_COHERENCE:.6f}"
            hash_value = hashlib.md5(seed.encode()).hexdigest()[:16]
            meta_learning_metadata['quantum_fingerprint'] = f"φ⁷·⁵-{hash_value}"
        
        # Store the event
        self.meta_learning_events.append(meta_learning_metadata)
        
        # Update visualizations
        self.update_meta_learning_visualizations()
        
        # Update dashboard
        self.update_dashboard()
        
        # Save to file for persistence
        self._save_meta_learning_events()
    
    def update_visualizations(self):
        """
        Update all visualizations based on current events.
        """
        if not self.visualization:
            logger.warning("No visualization module available")
            return
            
        try:
            # Generate comprehensive report
            self.visualization.generate_comprehensive_report(
                evolution_data=self.evolution_events,
                healing_history=self.healing_events,
                meta_learning_data=self.meta_learning_events
            )
            logger.info("Updated visualizations")
        except Exception as e:
            logger.error(f"Failed to update visualizations: {e}")
    
    def update_meta_learning_visualizations(self):
        """
        Update meta-learning visualizations based on current events.
        """
        if not self.visualization:
            logger.warning("No visualization module available")
            return
            
        try:
            # Generate meta-learning visualizations using the enhanced visualization module
            if hasattr(self.visualization, 'generate_meta_learning_visualization'):
                self.visualization.generate_meta_learning_visualization(self.meta_learning_events)
            else:
                # Fall back to local implementation
                self.generate_meta_learning_visualizations()
            logger.info("Updated meta-learning visualizations")
        except Exception as e:
            logger.error(f"Failed to update meta-learning visualizations: {e}")
    
    def update_dashboard(self):
        """
        Update the dashboard based on current events.
        """
        if not self.dashboard:
            logger.warning("No dashboard module available")
            return
            
        try:
            # Generate dashboard
            self.dashboard.generate_main_dashboard()
            
            # Generate interactive dashboard
            self.dashboard.generate_interactive_dashboard()
            
            logger.info("Updated dashboard")
        except Exception as e:
            logger.error(f"Failed to update dashboard: {e}")
    
    def generate_meta_learning_visualizations(self):
        """
        Generate visualizations for meta-learning processes.
        
        Returns:
            str: Path to the generated visualization file
        """
        if not self.visualization:
            logger.warning("No visualization module available")
            return None
            
        # Create markdown visualization
        output_file = os.path.join(self.visualization_dir, "meta_learning_visualization.md")
        
        with open(output_file, 'w') as f:
            f.write("# Quantum Meta-Learning Visualization\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Quantum Fingerprint: {self.quantum_fingerprint}\n\n")
            
            # Add meta-learning metrics
            f.write("## Meta-Learning Metrics\n\n")
            
            if not self.meta_learning_events:
                f.write("No meta-learning events recorded yet.\n\n")
            else:
                # Create table of meta-learning events
                f.write("| Timestamp | Learning Type | Coherence | Fingerprint |\n")
                f.write("|-----------|--------------|-----------|-------------|\n")
                
                for event in self.meta_learning_events:
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
                for event in self.meta_learning_events:
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
                for event in sorted(self.meta_learning_events, key=lambda x: x.get("timestamp", 0)):
                    if not isinstance(event, dict):
                        continue
                        
                    learning_type = event.get("learning_type", "unknown")
                    fingerprint = event.get("quantum_fingerprint", "")
                    
                    f.write(f"Gen {current_gen} [{learning_type}] -- φ -- {fingerprint}\n")
                    current_gen += 1
                
                f.write("```\n")
        
        logger.info(f"Meta-learning visualization generated: {output_file}")
        return output_file

    def _save_meta_learning_events(self):
        """
        Save meta-learning events to a JSON file for persistence.
        """
        output_file = os.path.join(self.evolution_dir, "meta_learning_events.json")
        
        try:
            with open(output_file, 'w') as f:
                json.dump(self.meta_learning_events, f, indent=2)
            logger.info(f"Saved meta-learning events to {output_file}")
        except Exception as e:
            logger.error(f"Failed to save meta-learning events: {e}")
    
    def _load_meta_learning_events(self):
        """
        Load meta-learning events from a JSON file.
        
        Returns:
            bool: True if events were loaded successfully
        """
        input_file = os.path.join(self.evolution_dir, "meta_learning_events.json")
        
        if not os.path.exists(input_file):
            # Try to load sample data if available
            sample_file = os.path.join(self.evolution_dir, "meta_learning_sample.json")
            if os.path.exists(sample_file):
                input_file = sample_file
            else:
                logger.info("No meta-learning events file found")
                return False
        
        try:
            with open(input_file, 'r') as f:
                self.meta_learning_events = json.load(f)
            logger.info(f"Loaded {len(self.meta_learning_events)} meta-learning events from {input_file}")
            return True
        except Exception as e:
            logger.error(f"Failed to load meta-learning events: {e}")
            return False

    def run_demonstration(self, demo_type="full", interactive=False, scenario="standard"):
        """
        Run a demonstration of the visualization framework.
        
        Args:
            demo_type: Type of demonstration to run (full, healing, meta-learning)
            interactive: Whether to run in interactive mode
            scenario: Demonstration scenario (standard, complex, hyper-dimensional)
            
        Returns:
            str: Path to the generated demonstration report
        """
        # Load sample meta-learning data if available and needed
        if demo_type == "meta-learning" and not self.meta_learning_events:
            self._load_meta_learning_events()
        
        # Import appropriate demonstration runner based on demo type
        try:
            if demo_type == "meta-learning":
                # Use the extension for meta-learning demonstrations
                try:
                    from quantum_demonstration_runner_extension import QuantumDemonstrationRunnerExtension
                    runner = QuantumDemonstrationRunnerExtension()
                    
                    # Connect to the runner
                    if hasattr(runner, "visualization"):
                        runner.visualization = self.visualization
                    
                    if hasattr(runner, "dashboard"):
                        runner.dashboard = self.dashboard
                    
                    # Run meta-learning demonstration
                    return runner.run_meta_learning_demonstration(interactive=interactive, scenario=scenario)
                except ImportError:
                    logger.error("QuantumDemonstrationRunnerExtension module not found")
                    return None
            else:
                # Use the base runner for other demonstration types
                from quantum_demonstration_runner import QuantumDemonstrationRunner
                runner = QuantumDemonstrationRunner()
                
                # Connect to the runner
                if hasattr(runner, "visualization"):
                    runner.visualization = self.visualization
                
                if hasattr(runner, "dashboard"):
                    runner.dashboard = self.dashboard
                
                # Run demonstration
                if demo_type == "healing":
                    return runner.run_healing_demonstration(interactive=interactive, scenario=scenario)
                else:
                    return runner.run_full_demonstration(interactive=interactive, scenario=scenario)
                    
        except ImportError:
            logger.error("QuantumDemonstrationRunner module not found")
            return None
        except Exception as e:
            logger.error(f"Failed to run demonstration: {e}")
            return None


def main():
    """
    Main function to run the connector.
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="Quantum Visualization Connector")
    parser.add_argument("--target-file", help="Target file for the orchestrator")
    parser.add_argument("--demo", choices=["full", "healing", "meta-learning"], 
                      default="full", help="Type of demonstration to run")
    parser.add_argument("--interactive", action="store_true", 
                      help="Run in interactive mode with dashboard")
    parser.add_argument("--scenario", choices=["standard", "complex", "hyper-dimensional"],
                      default="standard", help="Demonstration scenario complexity")
    parser.add_argument("--visualize-only", action="store_true",
                      help="Only generate visualizations without running orchestrator")
    
    args = parser.parse_args()
    
    # Create connector
    connector = QuantumVisualizationConnector()
    
    # Load existing meta-learning events if available
    connector._load_meta_learning_events()
    
    # Connect to orchestrator if target file provided
    if args.target_file and not args.visualize_only:
        try:
            from quantum_self_healing_orchestrator import QuantumSelfHealingOrchestrator
            orchestrator = QuantumSelfHealingOrchestrator(args.target_file)
            connector.connect_orchestrator(orchestrator)
            
            # Run the orchestrator
            orchestrator.run_and_heal()
            
        except ImportError:
            logger.error("QuantumSelfHealingOrchestrator module not found")
        except Exception as e:
            logger.error(f"Failed to connect to orchestrator: {e}")
    
    # Run demonstration
    demo_report = connector.run_demonstration(demo_type=args.demo, interactive=args.interactive)
    
    if demo_report:
        print(f"Demonstration report generated: {demo_report}")
    else:
        print("No demonstration report generated")


if __name__ == "__main__":
    main()
