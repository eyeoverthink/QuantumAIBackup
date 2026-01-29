#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Generate Meta-Learning Visualization
----------------------------------
Script to generate meta-learning visualizations using the enhanced
QuantumVisualization module.
"""

import os
import json
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("MetaLearningVisualization")

def main():
    """
    Main function to generate meta-learning visualizations.
    """
    # Import visualization module
    try:
        from quantum_visualization import QuantumVisualization
        visualization = QuantumVisualization()
    except ImportError:
        logger.error("QuantumVisualization module not found")
        return
    
    # Load meta-learning events
    evolution_dir = "evolution"
    meta_learning_file = os.path.join(evolution_dir, "meta_learning_events.json")
    
    if not os.path.exists(meta_learning_file):
        logger.error(f"Meta-learning events file not found: {meta_learning_file}")
        return
    
    try:
        with open(meta_learning_file, 'r') as f:
            meta_learning_events = json.load(f)
        logger.info(f"Loaded {len(meta_learning_events)} meta-learning events from {meta_learning_file}")
    except Exception as e:
        logger.error(f"Failed to load meta-learning events: {e}")
        return
    
    # Generate meta-learning visualization
    try:
        meta_learning_file = visualization.generate_meta_learning_visualization(meta_learning_events)
        logger.info(f"Generated meta-learning visualization: {meta_learning_file}")
    except Exception as e:
        logger.error(f"Failed to generate meta-learning visualization: {e}")
    
    # Generate comprehensive report
    comprehensive_file = None
    try:
        comprehensive_file = visualization.generate_comprehensive_report(
            meta_learning_data=meta_learning_events
        )
        if comprehensive_file:
            logger.info(f"Generated comprehensive report: {comprehensive_file}")
    except Exception as e:
        logger.error(f"Failed to generate comprehensive report: {e}")
    
    print("Visualization generation completed successfully.")
    print(f"Meta-learning visualization: {meta_learning_file}")
    if comprehensive_file:
        print(f"Comprehensive report: {comprehensive_file}")
    else:
        print("Comprehensive report generation failed. See logs for details.")

if __name__ == "__main__":
    main()
