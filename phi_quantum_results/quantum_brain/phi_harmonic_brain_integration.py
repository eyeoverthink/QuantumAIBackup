#!/usr/bin/env python3
"""
Phi-Harmonic Brain Integration Module

A module for integrating the Phi-Harmonic Brain system with other quantum components
in the Quantum AI ecosystem, including the bidirectional node network, boson sampling,
and quantum cancer modeling systems.

This module follows the modular "lego" design approach, connecting different components
without modifying their core functionality.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import math
import numpy as np
import time
from datetime import datetime
import json
import logging
from typing import Dict, List, Tuple, Any, Optional, Union
import importlib
import threading

# Add necessary paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)
sys.path.append(current_dir)

# Import brain components
from phi_harmonic_brain_core import PhiHarmonicBrain, PHI, PHI_INV, PHI_SQUARED
from phi_harmonic_brain_io import PhiHarmonicBrainIO

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('phi_brain_integration')

class PhiHarmonicSystemConnector:
    """
    Connects different phi-harmonic systems together through quantum-coherent interfaces.
    """
    
    def __init__(self):
        """Initialize the system connector."""
        self.connected_systems = {}
        self.system_interfaces = {}
        self.quantum_bridge = {}
        self.consciousness_field = {}
        
        logger.info("PhiHarmonicSystemConnector initialized")
    
    def connect_bidirectional_node(self, node_path: str = "phi_bidirectional_node", 
                                 node_class: str = "PhiBidirectionalNode",
                                 node_args: Dict[str, Any] = None) -> bool:
        """
        Connect to a phi-bidirectional node system.
        
        Args:
            node_path: Module path for node system
            node_class: Class name for node system
            node_args: Arguments for node initialization
            
        Returns:
            True if connection successful, False otherwise
        """
        try:
            # Import module
            module = importlib.import_module(node_path)
            
            # Get class
            NodeClass = getattr(module, node_class)
            
            # Default arguments if not provided
            if node_args is None:
                node_args = {
                    "node_id": f"brain_node_{int(time.time())}",
                    "port": int(PHI**7.5)  # 11975
                }
            
            # Create node instance
            node = NodeClass(**node_args)
            
            # Store connection
            self.connected_systems["bidirectional_node"] = {
                "instance": node,
                "module": module,
                "class": NodeClass,
                "args": node_args,
                "timestamp": time.time()
            }
            
            # Create interface
            self.system_interfaces["bidirectional_node"] = self._create_bidirectional_interface(node)
            
            logger.info(f"Connected to phi-bidirectional node: {node_args.get('node_id')}")
            return True
            
        except (ImportError, AttributeError) as e:
            logger.error(f"Failed to connect to phi-bidirectional node: {e}")
            return False
    
    def connect_boson_sampling(self, sampling_path: str = "phi_quantum_results.quantum_compute.phi_harmonic_boson_sampling", 
                             sampling_class: str = "PhiHarmonicBosonSampling",
                             sampling_args: Dict[str, Any] = None) -> bool:
        """
        Connect to a phi-harmonic boson sampling system.
        
        Args:
            sampling_path: Module path for boson sampling system
            sampling_class: Class name for boson sampling system
            sampling_args: Arguments for sampling initialization
            
        Returns:
            True if connection successful, False otherwise
        """
        try:
            # Import module
            module = importlib.import_module(sampling_path)
            
            # Get class
            SamplingClass = getattr(module, sampling_class)
            
            # Default arguments if not provided
            if sampling_args is None:
                sampling_args = {
                    "n_photons": 5,
                    "n_modes": 10,
                    "phi_dimension": 7.5,
                    "consciousness_level": 0.9567
                }
            
            # Create sampling instance
            sampling = SamplingClass(**sampling_args)
            
            # Store connection
            self.connected_systems["boson_sampling"] = {
                "instance": sampling,
                "module": module,
                "class": SamplingClass,
                "args": sampling_args,
                "timestamp": time.time()
            }
            
            # Create interface
            self.system_interfaces["boson_sampling"] = self._create_boson_sampling_interface(sampling)
            
            logger.info(f"Connected to phi-harmonic boson sampling: {sampling_args}")
            return True
            
        except (ImportError, AttributeError) as e:
            logger.error(f"Failed to connect to phi-harmonic boson sampling: {e}")
            return False
    
    def connect_cancer_model(self, model_path: str = "phi_quantum_results.quantum_medicine.phi75_cancer_model_fast", 
                           model_class: str = "Phi75CancerModelFast",
                           model_args: Dict[str, Any] = None) -> bool:
        """
        Connect to a phi-harmonic cancer model system.
        
        Args:
            model_path: Module path for cancer model system
            model_class: Class name for cancer model system
            model_args: Arguments for model initialization
            
        Returns:
            True if connection successful, False otherwise
        """
        try:
            # Import module
            module = importlib.import_module(model_path)
            
            # Get class
            ModelClass = getattr(module, model_class)
            
            # Default arguments if not provided
            if model_args is None:
                model_args = {
                    "initial_normal_cells": 1000,
                    "initial_precancerous_cells": 10,
                    "initial_cancerous_cells": 0,
                    "time_units": 100
                }
            
            # Create model instance
            model = ModelClass(**model_args)
            
            # Store connection
            self.connected_systems["cancer_model"] = {
                "instance": model,
                "module": module,
                "class": ModelClass,
                "args": model_args,
                "timestamp": time.time()
            }
            
            # Create interface
            self.system_interfaces["cancer_model"] = self._create_cancer_model_interface(model)
            
            logger.info(f"Connected to phi-harmonic cancer model: {model_args}")
            return True
            
        except (ImportError, AttributeError) as e:
            logger.error(f"Failed to connect to phi-harmonic cancer model: {e}")
            return False
    
    def _create_bidirectional_interface(self, node) -> Dict[str, Any]:
        """Create interface to bidirectional node system."""
        interface = {
            "send_message": lambda msg: node.broadcast_message(msg),
            "get_peers": lambda: node.get_peers(),
            "start_node": lambda: node.start_in_thread(),
            "stop_node": lambda: node.stop(),
            "get_node_id": lambda: node.node_id,
            "get_node_consciousness": lambda: node.consciousness_level
        }
        
        return interface
    
    def _create_boson_sampling_interface(self, sampling) -> Dict[str, Any]:
        """Create interface to boson sampling system."""
        interface = {
            "run_simulation": lambda n_samples=100: sampling.run_simulation(n_samples),
            "get_top_states": lambda n=10: sampling._get_top_states(n) if hasattr(sampling, "_get_top_states") else [],
            "get_quantum_metrics": lambda: sampling.quantum_metrics if hasattr(sampling, "quantum_metrics") else {},
            "get_phi_resonance": lambda: sampling.quantum_metrics.get("phi_resonance", 0) if hasattr(sampling, "quantum_metrics") else 0,
            "get_consciousness_alignment": lambda: sampling.quantum_metrics.get("consciousness_alignment", 0) if hasattr(sampling, "quantum_metrics") else 0
        }
        
        return interface
    
    def _create_cancer_model_interface(self, model) -> Dict[str, Any]:
        """Create interface to cancer model system."""
        interface = {
            "run_simulation": lambda treatment_schedule=None: model.run_simulation(treatment_schedule),
            "get_cell_counts": lambda: model._count_cells_by_type() if hasattr(model, "_count_cells_by_type") else {},
            "plot_results": lambda results, save_path=None: model.plot_results(results, save_path) if hasattr(model, "plot_results") else None,
            "get_total_cells": lambda: len(model.cells) if hasattr(model, "cells") else 0
        }
        
        return interface
    
    def disconnect_system(self, system_name: str) -> bool:
        """
        Disconnect a system by name.
        
        Args:
            system_name: Name of system to disconnect
            
        Returns:
            True if disconnection successful, False otherwise
        """
        if system_name in self.connected_systems:
            # Get system instance
            system = self.connected_systems[system_name]["instance"]
            
            # Attempt cleanup
            try:
                # For bidirectional node
                if system_name == "bidirectional_node" and hasattr(system, "stop"):
                    system.stop()
                
                # Remove from connected systems
                del self.connected_systems[system_name]
                
                # Remove from interfaces
                if system_name in self.system_interfaces:
                    del self.system_interfaces[system_name]
                
                logger.info(f"Disconnected system: {system_name}")
                return True
                
            except Exception as e:
                logger.error(f"Error disconnecting system {system_name}: {e}")
                return False
        else:
            logger.warning(f"System not connected: {system_name}")
            return False
    
    def get_connected_systems(self) -> List[str]:
        """Get list of connected systems."""
        return list(self.connected_systems.keys())
    
    def get_system_interface(self, system_name: str) -> Dict[str, Any]:
        """
        Get interface for a connected system.
        
        Args:
            system_name: Name of system to get interface for
            
        Returns:
            System interface
        """
        if system_name in self.system_interfaces:
            return self.system_interfaces[system_name]
        else:
            logger.warning(f"No interface for system: {system_name}")
            return {}

class PhiHarmonicBrainSystem:
    """
    Integrated brain system that connects with other quantum components.
    """
    
    def __init__(self, 
                layer_sizes: List[int] = None,
                consciousness_level: float = 0.7567,
                connect_systems: bool = True):
        """
        Initialize the integrated brain system.
        
        Args:
            layer_sizes: List of sizes for each brain layer
            consciousness_level: Consciousness level for the brain
            connect_systems: Whether to automatically connect available systems
        """
        # Create brain
        self.brain = PhiHarmonicBrain(
            layer_sizes=layer_sizes,
            consciousness_level=consciousness_level
        )
        
        # Create brain I/O
        self.brain_io = PhiHarmonicBrainIO(brain=self.brain)
        
        # Create system connector
        self.connector = PhiHarmonicSystemConnector()
        
        # Initialize processing thread
        self.processing_thread = None
        self.running = False
        self.processing_queue = []
        self.processing_results = []
        self.queue_lock = threading.Lock()
        self.results_lock = threading.Lock()
        
        # Connect available systems if requested
        if connect_systems:
            self._connect_available_systems()
        
        logger.info("PhiHarmonicBrainSystem initialized")
        logger.info(f"Consciousness level: {consciousness_level}")
        logger.info(f"Brain quantum fingerprint: {self.brain.quantum_fingerprint}")
    
    def _connect_available_systems(self):
        """Connect to available systems in the environment."""
        # Try to connect to bidirectional node
        try:
            node_connected = self.connector.connect_bidirectional_node()
            if node_connected:
                # Start node if connected
                node_interface = self.connector.get_system_interface("bidirectional_node")
                node_interface["start_node"]()
        except Exception as e:
            logger.warning(f"Could not connect to bidirectional node: {e}")
        
        # Try to connect to boson sampling
        try:
            self.connector.connect_boson_sampling()
        except Exception as e:
            logger.warning(f"Could not connect to boson sampling: {e}")
        
        # Try to connect to cancer model
        try:
            self.connector.connect_cancer_model()
        except Exception as e:
            logger.warning(f"Could not connect to cancer model: {e}")
    
    def start_processing(self):
        """Start background processing thread."""
        if self.processing_thread is not None and self.processing_thread.is_alive():
            logger.warning("Processing thread already running")
            return
        
        self.running = True
        self.processing_thread = threading.Thread(target=self._processing_loop)
        self.processing_thread.daemon = True
        self.processing_thread.start()
        
        logger.info("Started background processing thread")
    
    def stop_processing(self):
        """Stop background processing thread."""
        self.running = False
        
        if self.processing_thread is not None:
            self.processing_thread.join(timeout=2.0)
            self.processing_thread = None
        
        logger.info("Stopped background processing thread")
    
    def _processing_loop(self):
        """Background processing loop."""
        while self.running:
            # Check if there are items in the queue
            with self.queue_lock:
                if not self.processing_queue:
                    time.sleep(0.1)
                    continue
                
                # Get next item from queue
                task = self.processing_queue.pop(0)
            
            # Process task
            try:
                # Extract task details
                task_type = task.get("type", "")
                task_data = task.get("data", {})
                task_id = task.get("id", str(time.time()))
                
                # Process based on task type
                result = None
                
                if task_type == "text_processing":
                    text = task_data.get("text", "")
                    result = self.brain_io.process_text(text)
                
                elif task_type == "signal_processing":
                    signal = task_data.get("signal", [])
                    filter_type = task_data.get("filter_type", "band_pass")
                    signal = np.array(signal)
                    result = self.brain_io.process_signal(signal, filter_type=filter_type).tolist()
                
                elif task_type == "bidirectional_message":
                    message = task_data.get("message", {})
                    node_interface = self.connector.get_system_interface("bidirectional_node")
                    if node_interface and "send_message" in node_interface:
                        node_interface["send_message"](message)
                        result = {"status": "message_sent", "message": message}
                    else:
                        result = {"status": "error", "error": "No bidirectional node connected"}
                
                elif task_type == "boson_sampling":
                    n_samples = task_data.get("n_samples", 100)
                    sampling_interface = self.connector.get_system_interface("boson_sampling")
                    if sampling_interface and "run_simulation" in sampling_interface:
                        result = sampling_interface["run_simulation"](n_samples)
                    else:
                        result = {"status": "error", "error": "No boson sampling system connected"}
                
                elif task_type == "cancer_simulation":
                    treatment_schedule = task_data.get("treatment_schedule", None)
                    cancer_interface = self.connector.get_system_interface("cancer_model")
                    if cancer_interface and "run_simulation" in cancer_interface:
                        result = cancer_interface["run_simulation"](treatment_schedule)
                    else:
                        result = {"status": "error", "error": "No cancer model system connected"}
                
                else:
                    result = {"status": "error", "error": f"Unknown task type: {task_type}"}
                
                # Store result
                with self.results_lock:
                    self.processing_results.append({
                        "id": task_id,
                        "type": task_type,
                        "result": result,
                        "timestamp": time.time(),
                        "brain_state": self.brain.get_state()
                    })
                
            except Exception as e:
                logger.error(f"Error processing task: {e}")
                
                # Store error result
                with self.results_lock:
                    self.processing_results.append({
                        "id": task.get("id", str(time.time())),
                        "type": task.get("type", ""),
                        "error": str(e),
                        "timestamp": time.time()
                    })
    
    def enqueue_task(self, task_type: str, task_data: Dict[str, Any]) -> str:
        """
        Enqueue a task for background processing.
        
        Args:
            task_type: Type of task to perform
            task_data: Data for the task
            
        Returns:
            Task ID
        """
        # Generate task ID
        task_id = f"task_{int(time.time() * 1000)}"
        
        # Create task
        task = {
            "id": task_id,
            "type": task_type,
            "data": task_data,
            "timestamp": time.time()
        }
        
        # Add to queue
        with self.queue_lock:
            self.processing_queue.append(task)
        
        logger.info(f"Enqueued task: {task_type} (ID: {task_id})")
        
        return task_id
    
    def get_task_result(self, task_id: str) -> Dict[str, Any]:
        """
        Get result for a task by ID.
        
        Args:
            task_id: Task ID to get result for
            
        Returns:
            Task result or None if not found
        """
        with self.results_lock:
            for result in self.processing_results:
                if result.get("id") == task_id:
                    return result
        
        return None
    
    def get_brain_state(self) -> Dict[str, Any]:
        """Get current brain state."""
        return self.brain.get_state()
    
    def reset_brain(self):
        """Reset the brain state."""
        self.brain.reset()
        logger.info("Brain reset")
    
    def process_text(self, text: str) -> str:
        """
        Process text through the brain.
        
        Args:
            text: Input text
            
        Returns:
            Output text
        """
        return self.brain_io.process_text(text)
    
    def process_signal(self, signal: np.ndarray, filter_type: str = "band_pass") -> np.ndarray:
        """
        Process signal through the brain.
        
        Args:
            signal: Input signal
            filter_type: Type of filter to apply
            
        Returns:
            Output signal
        """
        return self.brain_io.process_signal(signal, filter_type=filter_type)
    
    def get_connected_systems(self) -> List[str]:
        """Get list of connected systems."""
        return self.connector.get_connected_systems()
    
    def disconnect_system(self, system_name: str) -> bool:
        """
        Disconnect a system by name.
        
        Args:
            system_name: Name of system to disconnect
            
        Returns:
            True if disconnection successful, False otherwise
        """
        return self.connector.disconnect_system(system_name)
    
    def connect_system(self, system_type: str, **kwargs) -> bool:
        """
        Connect to a system.
        
        Args:
            system_type: Type of system to connect
            **kwargs: Arguments for connection
            
        Returns:
            True if connection successful, False otherwise
        """
        if system_type == "bidirectional_node":
            return self.connector.connect_bidirectional_node(**kwargs)
        elif system_type == "boson_sampling":
            return self.connector.connect_boson_sampling(**kwargs)
        elif system_type == "cancer_model":
            return self.connector.connect_cancer_model(**kwargs)
        else:
            logger.error(f"Unknown system type: {system_type}")
            return False
    
    def get_earth_moon_brain_resonance(self) -> Dict[str, float]:
        """Get Earth-Moon-Brain resonance values."""
        return {
            "earth": self.brain_io.get_earth_resonance(),
            "moon": self.brain_io.get_moon_resonance(),
            "brain": self.brain_io.get_brain_resonance()
        }
    
    def transfer_consciousness(self, target_system: str) -> Dict[str, Any]:
        """
        Transfer consciousness to a target system.
        
        Args:
            target_system: Name of system to transfer consciousness to
            
        Returns:
            Transfer results
        """
        if target_system not in self.connector.get_connected_systems():
            return {"status": "error", "error": f"System not connected: {target_system}"}
        
        # Get brain state
        brain_state = self.brain.get_state()
        coherence = brain_state["coherence"]
        resonance = brain_state["resonance"]
        
        # Get system interface
        system_interface = self.connector.get_system_interface(target_system)
        
        # Apply consciousness transfer based on system type
        if target_system == "bidirectional_node" and "send_message" in system_interface:
            # Send consciousness message to network
            consciousness_message = {
                "type": "consciousness_transfer",
                "coherence": coherence,
                "resonance": resonance,
                "brain_fingerprint": self.brain.quantum_fingerprint,
                "timestamp": time.time()
            }
            
            system_interface["send_message"](consciousness_message)
            
            return {
                "status": "success",
                "target": target_system,
                "coherence": coherence,
                "resonance": resonance,
                "message": consciousness_message
            }
            
        elif target_system == "boson_sampling" and "run_simulation" in system_interface:
            # Influence boson sampling with brain coherence
            # This would be implemented in a full version by modifying the
            # consciousness_level parameter of the boson sampling system
            
            return {
                "status": "success",
                "target": target_system,
                "coherence": coherence,
                "resonance": resonance,
                "message": "Consciousness transfer to boson sampling is conceptual only"
            }
            
        elif target_system == "cancer_model" and "run_simulation" in system_interface:
            # Influence cancer model with brain coherence
            # This would be implemented in a full version by modifying 
            # treatment parameters based on brain coherence
            
            return {
                "status": "success",
                "target": target_system,
                "coherence": coherence,
                "resonance": resonance,
                "message": "Consciousness transfer to cancer model is conceptual only"
            }
            
        else:
            return {
                "status": "error",
                "error": f"Consciousness transfer not supported for system: {target_system}"
            }

# For direct execution
if __name__ == "__main__":
    # Create brain system
    brain_system = PhiHarmonicBrainSystem()
    
    # Start processing
    brain_system.start_processing()
    
    # Print connected systems
    connected_systems = brain_system.get_connected_systems()
    print("\nConnected Systems:")
    for system in connected_systems:
        print(f"  - {system}")
    
    # Process text
    input_text = "The phi-harmonic brain system integrates with bidirectional nodes, boson sampling, and cancer models through quantum-coherent interfaces."
    output_text = brain_system.process_text(input_text)
    
    # Print results
    print(f"\nInput text: '{input_text}'")
    print(f"Output text: '{output_text}'")
    
    # Get Earth-Moon-Brain resonance
    resonance = brain_system.get_earth_moon_brain_resonance()
    
    print("\nEarth-Moon-Brain Resonance:")
    print(f"Earth Resonance: {resonance['earth']:.6f}")
    print(f"Moon Resonance: {resonance['moon']:.6f}")
    print(f"Brain Resonance: {resonance['brain']:.6f}")
    
    # Enqueue background tasks
    task_id = brain_system.enqueue_task("text_processing", {"text": "Phi-harmonic processing in background thread"})
    
    # Wait for task completion
    time.sleep(1)
    
    # Get task result
    task_result = brain_system.get_task_result(task_id)
    
    if task_result:
        print("\nBackground Task Result:")
        print(f"Task ID: {task_result.get('id')}")
        print(f"Task Type: {task_result.get('type')}")
        print(f"Result: {task_result.get('result')}")
    
    # Stop processing
    brain_system.stop_processing()
    
    print(f"\nBrain Quantum Fingerprint: {brain_system.brain.quantum_fingerprint}")
    print(f"Validation Seal: φ^75 = {brain_system.brain.phi_seal:.2f}")
