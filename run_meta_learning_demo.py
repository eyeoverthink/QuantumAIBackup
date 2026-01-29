#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Meta-Learning Demonstration Runner
---------------------------------
Script to run meta-learning demonstrations with the QuantumVisualizationConnector
and QuantumDemonstrationRunnerExtension.

This script provides a clean interface for running different types of meta-learning
demonstrations with proper error handling and visualization generation.
"""

import os
import sys
import time
import logging
import argparse
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("MetaLearningDemo")

def run_meta_learning_demo(scenario="standard", interactive=False, visualization_only=False):
    """
    Run a meta-learning demonstration with proper error handling.
    
    Args:
        scenario: Demonstration scenario (standard, complex, hyper-dimensional)
        interactive: Whether to run in interactive mode
        visualization_only: Whether to only generate visualizations without running a full demo
        
    Returns:
        bool: True if demonstration was successful
    """
    try:
        # Import required modules
        from quantum_visualization import QuantumVisualization
        from quantum_dashboard import QuantumDashboard
        from quantum_visualization_connector import QuantumVisualizationConnector
        from quantum_demonstration_runner_extension import QuantumDemonstrationRunnerExtension
        
        # Initialize components
        visualization = QuantumVisualization()
        dashboard = QuantumDashboard()
        connector = QuantumVisualizationConnector(
            visualization_module=visualization,
            dashboard_module=dashboard
        )
        
        # Run demonstration
        if visualization_only:
            # Load meta-learning events and generate visualizations only
            connector._load_meta_learning_events()
            meta_learning_file = visualization.generate_meta_learning_visualization(connector.meta_learning_events)
            logger.info(f"Generated meta-learning visualization: {meta_learning_file}")
            
            # Try to generate comprehensive report with meta-learning data only
            try:
                report_file = visualization.generate_comprehensive_report(
                    meta_learning_data=connector.meta_learning_events
                )
                if report_file:
                    logger.info(f"Generated comprehensive report: {report_file}")
            except Exception as e:
                logger.error(f"Failed to generate comprehensive report: {e}")
                
            return True
        else:
            # Run full demonstration with runner extension
            runner = QuantumDemonstrationRunnerExtension(
                visualization=visualization,
                dashboard=dashboard
            )
            
            # Run meta-learning demonstration
            output_file = runner.run_meta_learning_demonstration(
                scenario=scenario,
                interactive=interactive
            )
            
            if output_file:
                logger.info(f"Meta-learning demonstration completed: {output_file}")
                return True
            else:
                logger.error("Failed to generate demonstration report")
                return False
                
    except ImportError as e:
        logger.error(f"Failed to import required modules: {e}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error running meta-learning demonstration: {e}")
        return False

def main():
    """
    Main function to parse arguments and run the demonstration.
    """
    parser = argparse.ArgumentParser(description="Meta-Learning Demonstration Runner")
    parser.add_argument("--scenario", choices=["standard", "complex", "hyper-dimensional"], 
                      default="standard", help="Demonstration scenario")
    parser.add_argument("--interactive", action="store_true", 
                      help="Run in interactive mode with dashboard")
    parser.add_argument("--visualization-only", action="store_true",
                      help="Only generate visualizations without running a full demo")
    
    args = parser.parse_args()
    
    # Run the demonstration
    success = run_meta_learning_demo(
        scenario=args.scenario,
        interactive=args.interactive,
        visualization_only=args.visualization_only
    )
    
    # Exit with appropriate status code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
