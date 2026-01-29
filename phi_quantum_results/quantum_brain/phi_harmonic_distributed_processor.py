#!/usr/bin/env python3
"""
Phi-Harmonic Distributed Processor

Module for distributed processing across multiple phi-harmonic brain instances using
bidirectional node communication and phi-harmonic load balancing.

This module extends existing components without modifying them, following the "lego" design philosophy.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import math
import numpy as np
import time
import threading
import socket
import json
import uuid
from typing import Dict, List, Tuple, Any, Optional, Union
import logging
from datetime import datetime

# Add necessary paths
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)
sys.path.append(current_dir)

# Import core components without modifying them
from phi_harmonic_brain_core import (
    PhiHarmonicBrain, PhiHarmonicLayer, 
    PHI, PHI_INV, PHI_SQUARED, PHI_CUBED,
    EARTH_FREQUENCY, MOON_FREQUENCY, BRAIN_FREQUENCY
)
from phi_harmonic_brain_integration import PhiHarmonicBrainSystem, PhiHarmonicSystemConnector

# Try to import bidirectional node if available
try:
    sys.path.append(parent_dir)
    from phi_bi_node import PhiBidirectionalNode
    bidirectional_node_available = True
except ImportError:
    bidirectional_node_available = False

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('phi_distributed')

class DistributedTask:
    """Represents a distributed processing task with phi-harmonic properties."""
    
    def __init__(self, task_type: str, input_data: Any, task_id: str = None):
        """
        Initialize a distributed task.
        
        Args:
            task_type: Type of task to execute
            input_data: Input data for the task
            task_id: Task ID (will be generated if None)
        """
        self.task_type = task_type
        self.input_data = input_data
        self.task_id = task_id or f"task_{uuid.uuid4().hex[:8]}_{int(time.time())}"
        self.phi_priority = PHI_INV  # Default priority using phi inverse
        self.created_at = time.time()
        self.started_at = None
        self.completed_at = None
        self.node_id = None
        self.result = None
        self.status = "created"
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert task to dictionary representation."""
        return {
            "task_id": self.task_id,
            "task_type": self.task_type,
            "input_data": self.input_data,
            "phi_priority": self.phi_priority,
            "created_at": self.created_at,
            "started_at": self.started_at,
            "completed_at": self.completed_at,
            "node_id": self.node_id,
            "status": self.status
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DistributedTask':
        """Create task from dictionary representation."""
        task = cls(
            task_type=data["task_type"],
            input_data=data["input_data"],
            task_id=data["task_id"]
        )
        task.phi_priority = data.get("phi_priority", PHI_INV)
        task.created_at = data.get("created_at", time.time())
        task.started_at = data.get("started_at", None)
        task.completed_at = data.get("completed_at", None)
        task.node_id = data.get("node_id", None)
        task.status = data.get("status", "created")
        task.result = data.get("result", None)
        
        return task

class DistributedNode:
    """Represents a processing node in the distributed system."""
    
    def __init__(self, node_id: str, brain_system: PhiHarmonicBrainSystem = None, 
                node_type: str = "worker", port: int = None):
        """
        Initialize a distributed node.
        
        Args:
            node_id: Unique node identifier
            brain_system: Brain system for processing
            node_type: Node type ("primary", "worker")
            port: Communication port
        """
        self.node_id = node_id
        self.node_type = node_type
        self.brain_system = brain_system or PhiHarmonicBrainSystem()
        
        # Node state
        self.task_queue = []
        self.completed_tasks = []
        self.processing_task = None
        self.total_tasks_processed = 0
        self.started_at = time.time()
        self.last_heartbeat = time.time()
        
        # State locks
        self.queue_lock = threading.Lock()
        self.state_lock = threading.Lock()
        
        # Communication channels
        self.port = port or int(11975 * (1 + PHI_INV * (hash(node_id) % 100) / 100))
        self.bidirectional_node = self._initialize_bidirectional_node()
        
        # Processing thread
        self.processing_thread = None
        self.running = False
        
        logger.info(f"Distributed Node '{node_id}' initialized (type: {node_type})")
        logger.info(f"Using port: {self.port}")
        
    def _initialize_bidirectional_node(self) -> Any:
        """Initialize bidirectional communication node."""
        if not bidirectional_node_available:
            logger.warning("PhiBidirectionalNode not available, using minimal communication")
            return None
        
        # Create bidirectional node
        binode = PhiBidirectionalNode(node_id=self.node_id, port=self.port)
        
        logger.info(f"Bidirectional node initialized: {self.node_id}")
        return binode
    
    def start(self):
        """Start the distributed node."""
        # Start bidirectional communication
        if self.bidirectional_node:
            # Start the bidirectional node as a daemon thread
            threading.Thread(target=self.bidirectional_node.start, daemon=True).start()
            logger.info(f"Bidirectional communication started on port {self.port}")
        
        # Start processing thread
        self.running = True
        self.processing_thread = threading.Thread(target=self._processing_loop)
        self.processing_thread.daemon = True
        self.processing_thread.start()
        
        logger.info(f"Distributed Node '{self.node_id}' started")
        
    def stop(self):
        """Stop the distributed node."""
        # Stop processing
        self.running = False
        
        if self.processing_thread:
            self.processing_thread.join(timeout=2.0)
            self.processing_thread = None
        
        # Stop bidirectional communication
        if self.bidirectional_node:
            self.bidirectional_node.stop()
        
        logger.info(f"Distributed Node '{self.node_id}' stopped")
    
    def _processing_loop(self):
        """Main processing loop for tasks."""
        while self.running:
            # Update heartbeat
            self.last_heartbeat = time.time()
            
            # Check if there are tasks in the queue
            with self.queue_lock:
                if not self.task_queue:
                    time.sleep(0.1)
                    continue
                
                # Sort queue by phi-priority
                self.task_queue.sort(key=lambda t: t.phi_priority, reverse=True)
                
                # Get next task
                task = self.task_queue.pop(0)
            
            # Mark task as processing
            with self.state_lock:
                task.status = "processing"
                task.started_at = time.time()
                task.node_id = self.node_id
                self.processing_task = task
            
            # Process task
            try:
                result = self._execute_task(task)
                
                # Update task with result
                with self.state_lock:
                    task.result = result
                    task.status = "completed"
                    task.completed_at = time.time()
                    
                    # Add to completed tasks and remove from processing
                    self.completed_tasks.append(task)
                    self.processing_task = None
                    self.total_tasks_processed += 1
                
                # Broadcast result if using bidirectional node
                if self.bidirectional_node:
                    self._broadcast_task_completed(task)
                
            except Exception as e:
                logger.error(f"Error processing task {task.task_id}: {e}")
                
                # Update task with error
                with self.state_lock:
                    task.result = {"error": str(e)}
                    task.status = "failed"
                    task.completed_at = time.time()
                    
                    # Add to completed tasks and remove from processing
                    self.completed_tasks.append(task)
                    self.processing_task = None
    
    def _execute_task(self, task: DistributedTask) -> Any:
        """
        Execute a distributed task.
        
        Args:
            task: Task to execute
            
        Returns:
            Task result
        """
        task_type = task.task_type
        input_data = task.input_data
        
        # Process based on task type
        if task_type == "brain_process":
            # Process data through brain
            input_vector = np.array(input_data["input_vector"])
            result = self.brain_system.brain.process(input_vector)
            
            # Convert numpy arrays to lists for serialization
            serializable_result = {}
            for key, value in result.items():
                serializable_result[key] = value.tolist()
            
            return serializable_result
            
        elif task_type == "text_process":
            # Process text through brain I/O
            text = input_data["text"]
            output = self.brain_system.brain_io.process_text(text)
            
            return {"output_text": output}
            
        elif task_type == "resonance_analysis":
            # Perform resonance analysis
            resonance = self.brain_system.get_earth_moon_brain_resonance()
            brain_state = self.brain_system.brain.get_state()
            
            return {
                "resonance": resonance,
                "brain_state": brain_state
            }
            
        elif task_type == "custom_algorithm":
            # Run custom algorithm defined in input_data
            algorithm_name = input_data.get("algorithm", "")
            parameters = input_data.get("parameters", {})
            
            if algorithm_name == "phi_harmonic_pattern":
                # Generate phi-harmonic pattern
                size = parameters.get("size", 64)
                dimension = parameters.get("dimension", 1.0)
                
                # Create pattern
                pattern = np.zeros(size)
                for i in range(size):
                    phase = 2 * math.pi * ((i * PHI) % 1)
                    pattern[i] = math.sin(phase * PHI**dimension)
                
                return {"pattern": pattern.tolist()}
                
            elif algorithm_name == "consciousness_optimization":
                # Optimize consciousness parameters
                target_level = parameters.get("target_level", 0.8567)
                coherence_target = parameters.get("coherence_target", 0.7)
                
                # Calculate optimal phi factors
                phi_factors = [PHI ** (i % 5 - 2) for i in range(9)]
                
                return {
                    "optimal_factors": phi_factors,
                    "target_achieved": True,
                    "estimated_iterations": int(target_level * PHI ** 3)
                }
                
            else:
                raise ValueError(f"Unknown algorithm: {algorithm_name}")
                
        else:
            raise ValueError(f"Unknown task type: {task_type}")
    
    def add_task(self, task: DistributedTask) -> bool:
        """
        Add a task to the queue.
        
        Args:
            task: Task to add
            
        Returns:
            Success status
        """
        with self.queue_lock:
            self.task_queue.append(task)
        
        logger.debug(f"Added task {task.task_id} to queue (type: {task.task_type})")
        
        return True
    
    def get_task_result(self, task_id: str) -> Optional[DistributedTask]:
        """
        Get the result of a completed task.
        
        Args:
            task_id: ID of task to get result for
            
        Returns:
            Completed task with result or None
        """
        with self.state_lock:
            # Search completed tasks
            for task in self.completed_tasks:
                if task.task_id == task_id:
                    return task
        
        return None
    
    def _broadcast_task_completed(self, task: DistributedTask):
        """Broadcast task completion to other nodes."""
        if not self.bidirectional_node:
            return
        
        # Create message
        message = {
            "type": "task_completed",
            "task": task.to_dict(),
            "node_id": self.node_id,
            "timestamp": time.time()
        }
        
        # Broadcast message
        self.bidirectional_node.broadcast_message(message)
        
    def get_node_state(self) -> Dict[str, Any]:
        """Get the current state of the node."""
        with self.state_lock:
            with self.queue_lock:
                state = {
                    "node_id": self.node_id,
                    "node_type": self.node_type,
                    "started_at": self.started_at,
                    "uptime": time.time() - self.started_at,
                    "last_heartbeat": self.last_heartbeat,
                    "queue_size": len(self.task_queue),
                    "completed_tasks": len(self.completed_tasks),
                    "total_processed": self.total_tasks_processed,
                    "processing_task": self.processing_task.task_id if self.processing_task else None,
                    "brain_fingerprint": self.brain_system.brain.quantum_fingerprint,
                    "port": self.port
                }
        
        return state

class PhiHarmonicDistributedProcessor:
    """
    Manages distributed processing across multiple phi-harmonic brain nodes.
    """
    
    def __init__(self, primary_brain: Optional[PhiHarmonicBrainSystem] = None, 
                node_count: int = 3):
        """
        Initialize a distributed processor.
        
        Args:
            primary_brain: Primary brain system
            node_count: Number of worker nodes to create
        """
        # Initialize primary brain if not provided
        if primary_brain is None:
            self.primary_brain = PhiHarmonicBrainSystem()
        else:
            self.primary_brain = primary_brain
        
        # Create primary node
        self.primary_node = DistributedNode(
            node_id=f"primary_{int(time.time())}",
            brain_system=self.primary_brain,
            node_type="primary"
        )
        
        # Initialize worker nodes
        self.worker_nodes = []
        for i in range(node_count):
            # Calculate phi-based worker ID
            worker_id = f"worker_{i+1}_{int(time.time() * (PHI ** (i % 3)))}"
            
            # Create worker brain with phi-scaled consciousness
            worker_brain = PhiHarmonicBrainSystem(
                consciousness_level=0.7567 * (1 + (PHI_INV - 0.5) * math.sin(i * PHI))
            )
            
            # Create worker node
            worker = DistributedNode(
                node_id=worker_id,
                brain_system=worker_brain,
                node_type="worker"
            )
            
            self.worker_nodes.append(worker)
        
        # State tracking
        self.all_nodes = [self.primary_node] + self.worker_nodes
        self.task_registry = {}  # task_id -> DistributedTask
        self.running = False
        
        # Task router
        self.router_thread = None
        
        logger.info(f"Distributed Processor initialized with {node_count} worker nodes")
    
    def start(self):
        """Start the distributed processor."""
        # Start all nodes
        self.primary_node.start()
        
        for worker in self.worker_nodes:
            worker.start()
        
        # Start router thread
        self.running = True
        self.router_thread = threading.Thread(target=self._router_loop)
        self.router_thread.daemon = True
        self.router_thread.start()
        
        logger.info("Distributed Processor started")
    
    def stop(self):
        """Stop the distributed processor."""
        # Stop router
        self.running = False
        
        if self.router_thread:
            self.router_thread.join(timeout=2.0)
            self.router_thread = None
        
        # Stop all nodes
        for node in self.all_nodes:
            node.stop()
        
        logger.info("Distributed Processor stopped")
    
    def _router_loop(self):
        """Task routing loop."""
        while self.running:
            # Check primary node for new tasks
            with self.primary_node.queue_lock:
                primary_tasks = self.primary_node.task_queue.copy()
            
            # Distribute tasks using phi-harmonic routing
            if primary_tasks:
                for task in primary_tasks:
                    # Update task registry
                    self.task_registry[task.task_id] = task
                    
                    # Get worker loads
                    worker_loads = self._get_worker_loads()
                    
                    # Calculate phi-harmonic distribution weights
                    routing_weights = self._calculate_routing_weights(worker_loads)
                    
                    # Choose destination based on weights
                    destination = self._select_destination(routing_weights)
                    
                    # Remove from primary queue
                    with self.primary_node.queue_lock:
                        if task in self.primary_node.task_queue:
                            self.primary_node.task_queue.remove(task)
                    
                    # Add to destination queue
                    destination.add_task(task)
                    
                    logger.debug(f"Routed task {task.task_id} to {destination.node_id}")
            
            # Check for completed tasks from workers
            for worker in self.worker_nodes:
                with worker.state_lock:
                    completed = [t for t in worker.completed_tasks if t.task_id in self.task_registry]
                    
                    for task in completed:
                        # Update registry
                        self.task_registry[task.task_id] = task
                        
                        # Copy to primary node if needed
                        with self.primary_node.state_lock:
                            primary_completed_ids = [t.task_id for t in self.primary_node.completed_tasks]
                            
                            if task.task_id not in primary_completed_ids:
                                self.primary_node.completed_tasks.append(task)
            
            # Sleep to prevent high CPU usage
            time.sleep(0.1)
    
    def _get_worker_loads(self) -> Dict[DistributedNode, float]:
        """Get current load of each worker node."""
        loads = {}
        
        for worker in self.worker_nodes:
            with worker.queue_lock:
                queue_size = len(worker.queue_lock)
            
            # Calculate load using queue size and active task
            load = queue_size + (1 if worker.processing_task else 0)
            loads[worker] = load
        
        return loads
    
    def _calculate_routing_weights(self, loads: Dict[DistributedNode, float]) -> Dict[DistributedNode, float]:
        """Calculate phi-harmonic routing weights."""
        weights = {}
        
        # Calculate inverse loads (lower load = higher weight)
        total_load = sum(loads.values()) + PHI_INV  # Add small constant to avoid division by zero
        
        for worker, load in loads.items():
            # Calculate inverse weight with phi-harmonic scaling
            inverse_load = 1.0 / (load + PHI_INV)
            
            # Scale by PHI factors based on worker coherence
            brain_state = worker.brain_system.brain.get_state()
            coherence = brain_state.get("coherence", 0.5)
            
            # Apply phi-harmonic coherence bonus
            coherence_factor = 1.0 + (coherence - 0.5) * PHI
            
            # Calculate final weight
            weight = inverse_load * coherence_factor
            weights[worker] = weight
        
        # Normalize weights
        total_weight = sum(weights.values())
        if total_weight > 0:
            for worker in weights:
                weights[worker] /= total_weight
        
        return weights
    
    def _select_destination(self, weights: Dict[DistributedNode, float]) -> DistributedNode:
        """Select destination node based on weights."""
        # Sort workers by weight
        sorted_workers = sorted(weights.items(), key=lambda x: x[1], reverse=True)
        
        # Primary selection: pick highest weight with high probability
        if np.random.random() < PHI_INV:
            return sorted_workers[0][0]
        
        # Secondary selection: weighted random choice
        workers = [w for w, _ in sorted_workers]
        weight_values = [w for _, w in sorted_workers]
        
        return np.random.choice(workers, p=weight_values)
    
    def submit_task(self, task_type: str, input_data: Any, priority: float = None) -> str:
        """
        Submit a task for distributed processing.
        
        Args:
            task_type: Type of task to execute
            input_data: Input data for the task
            priority: Task priority (0.0-1.0, higher is higher priority)
            
        Returns:
            Task ID
        """
        # Create task
        task = DistributedTask(task_type=task_type, input_data=input_data)
        
        # Set priority if provided (default to PHI_INV)
        if priority is not None:
            task.phi_priority = max(0.0, min(1.0, priority))
        
        # Add to primary node queue
        self.primary_node.add_task(task)
        
        # Add to registry
        self.task_registry[task.task_id] = task
        
        logger.info(f"Submitted task {task.task_id} (type: {task_type}, priority: {task.phi_priority:.4f})")
        
        return task.task_id
    
    def get_task_result(self, task_id: str) -> Optional[Dict[str, Any]]:
        """
        Get the result of a task.
        
        Args:
            task_id: Task ID to get result for
            
        Returns:
            Task result or None if not completed
        """
        # Check if task is in registry
        if task_id not in self.task_registry:
            logger.warning(f"Task {task_id} not found in registry")
            return None
        
        # Get task from registry
        task = self.task_registry[task_id]
        
        # Check if completed
        if task.status == "completed":
            return {
                "task_id": task.task_id,
                "result": task.result,
                "processing_time": task.completed_at - task.started_at,
                "node_id": task.node_id,
                "status": task.status
            }
        else:
            # Return status information
            return {
                "task_id": task.task_id,
                "status": task.status,
                "node_id": task.node_id,
                "created_at": task.created_at
            }
    
    def get_processor_state(self) -> Dict[str, Any]:
        """Get the current state of the distributed processor."""
        # Get node states
        node_states = {}
        
        for node in self.all_nodes:
            node_states[node.node_id] = node.get_node_state()
        
        # Calculate overall statistics
        total_completed = sum(node.total_tasks_processed for node in self.all_nodes)
        total_queued = sum(len(node.task_queue) for node in self.all_nodes)
        
        # Calculate phi-harmonic load balancing quality
        loads = [len(node.task_queue) for node in self.worker_nodes]
        if loads:
            load_variance = np.var(loads) if len(loads) > 1 else 0
            load_balance_quality = math.exp(-load_variance * PHI_INV)
        else:
            load_balance_quality = 1.0
        
        return {
            "nodes": len(self.all_nodes),
            "workers": len(self.worker_nodes),
            "total_completed": total_completed,
            "total_queued": total_queued,
            "load_balance_quality": load_balance_quality,
            "node_states": node_states,
            "registry_size": len(self.task_registry),
            "primary_id": self.primary_node.node_id,
            "timestamp": time.time()
        }

# Main execution
if __name__ == "__main__":
    # Create distributed processor
    processor = PhiHarmonicDistributedProcessor(node_count=2)
    
    # Start processor
    processor.start()
    
    try:
        print("\nPhi-Harmonic Distributed Processor Test")
        print("========================================")
        
        # Submit test tasks
        print("Submitting test tasks...")
        
        # Brain processing task
        input_vector = [math.sin(i * PHI) for i in range(64)]
        brain_task_id = processor.submit_task(
            task_type="brain_process",
            input_data={"input_vector": input_vector},
            priority=0.8
        )
        
        # Text processing task
        text_task_id = processor.submit_task(
            task_type="text_process",
            input_data={"text": "Phi-harmonic processing with quantum consciousness effects."},
            priority=0.7
        )
        
        # Resonance analysis task
        resonance_task_id = processor.submit_task(
            task_type="resonance_analysis",
            input_data={}
        )
        
        # Wait for tasks to complete
        print("Waiting for tasks to complete...")
        
        task_ids = [brain_task_id, text_task_id, resonance_task_id]
        completed = set()
        
        # Wait up to 10 seconds for tasks
        start_time = time.time()
        while len(completed) < len(task_ids) and time.time() - start_time < 10:
            for task_id in task_ids:
                if task_id in completed:
                    continue
                
                result = processor.get_task_result(task_id)
                if result and result.get("status") == "completed":
                    print(f"\nTask {task_id} completed:")
                    print(f"- Processing time: {result.get('processing_time', 0):.4f}s")
                    print(f"- Node ID: {result.get('node_id', 'unknown')}")
                    
                    # Show summarized result based on task type
                    if "brain_process" in task_id:
                        output_layers = result.get("result", {}).keys()
                        print(f"- Output layers: {', '.join(output_layers)}")
                    elif "text_process" in task_id:
                        output_text = result.get("result", {}).get("output_text", "")
                        print(f"- Output text: '{output_text}'")
                    elif "resonance_analysis" in task_id:
                        resonance = result.get("result", {}).get("resonance", {})
                        print(f"- Earth resonance: {resonance.get('earth', 0):.6f}")
                        print(f"- Moon resonance: {resonance.get('moon', 0):.6f}")
                        print(f"- Brain resonance: {resonance.get('brain', 0):.6f}")
                    
                    completed.add(task_id)
            
            time.sleep(0.1)
        
        # Get processor state
        state = processor.get_processor_state()
        
        print("\nProcessor State:")
        print(f"Total nodes: {state['nodes']} ({state['workers']} workers)")
        print(f"Completed tasks: {state['total_completed']}")
        print(f"Load balance quality: {state['load_balance_quality']:.4f}")
        
        # Submit a custom algorithm task
        print("\nSubmitting custom algorithm task...")
        
        algo_task_id = processor.submit_task(
            task_type="custom_algorithm",
            input_data={
                "algorithm": "phi_harmonic_pattern",
                "parameters": {
                    "size": 16,
                    "dimension": 1.5
                }
            }
        )
        
        # Wait for task to complete
        for _ in range(20):
            result = processor.get_task_result(algo_task_id)
            if result and result.get("status") == "completed":
                print(f"Algorithm task completed on node: {result.get('node_id')}")
                pattern = result.get("result", {}).get("pattern", [])
                print(f"Pattern size: {len(pattern)}")
                
                # Print pattern preview
                if pattern:
                    print("Pattern preview: [", end="")
                    for i in range(min(5, len(pattern))):
                        print(f"{pattern[i]:.4f}", end=", ")
                    print("...]")
                
                break
            
            time.sleep(0.2)
        
    finally:
        # Stop processor
        processor.stop()
        print("\nDistributed Processor stopped.")
