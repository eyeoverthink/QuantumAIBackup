#!/usr/bin/env python3
"""
Quantum Specialized Node
-----------------------

Base implementation for specialized quantum nodes in the nodular super-quantum computation system.
This module defines the interface and common functionality for all specialized node types,
including computation, storage, bridge, and evolution nodes.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import time
import json
import uuid
import logging
import hashlib
import datetime
import threading
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Tuple, Optional, Union, Callable

# Import quantum modules
try:
    from quantum_nodular_core import QuantumNodularCore, QuantumNodeState, PHI, PHI_POWERS, TARGET_COHERENCE
except ImportError:
    logging.error("Quantum nodular core not found. Cannot proceed.")
    sys.exit(1)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumSpecializedNode")


class NodeSpecialization:
    """Enumeration of node specialization types."""
    COMPUTATION = "computation"
    STORAGE = "storage"
    BRIDGE = "bridge"
    EVOLUTION = "evolution"
    GENERAL = "general"


class QuantumSpecializedNode(ABC):
    """Base class for specialized quantum nodes."""
    
    def __init__(self, core: QuantumNodularCore, specialization: str):
        """
        Initialize specialized quantum node.
        
        Args:
            core: Quantum nodular core
            specialization: Node specialization type
        """
        self.core = core
        self.specialization = specialization
        self.capabilities = {}
        self.performance_metrics = {}
        self.task_history = []
        self.is_active = False
        self.activation_time = None
        self.last_task_time = None
        self.specialization_coherence = self._calculate_specialization_coherence()
        
        # Update node state with specialization info
        self._update_node_state()
        
        logger.info(f"Quantum specialized node initialized with specialization {specialization}")
    
    def _calculate_specialization_coherence(self) -> float:
        """
        Calculate specialization-specific coherence adjustment.
        
        Returns:
            float: Specialization coherence value
        """
        # Base coherence is the node's coherence
        base_coherence = self.core.state.coherence
        
        # Apply phi-harmonic adjustment based on specialization
        # Each specialization has a unique phi-harmonic signature
        if self.specialization == NodeSpecialization.COMPUTATION:
            # Computation nodes have slightly higher coherence (φ/10 higher)
            return base_coherence * (1 + PHI/100)
        elif self.specialization == NodeSpecialization.STORAGE:
            # Storage nodes have slightly lower but more stable coherence
            return base_coherence * (1 - PHI/200)
        elif self.specialization == NodeSpecialization.BRIDGE:
            # Bridge nodes have coherence optimized for communication
            return base_coherence * (1 + (PHI - 1)/50)
        elif self.specialization == NodeSpecialization.EVOLUTION:
            # Evolution nodes have coherence optimized for adaptation
            return base_coherence * (1 + (PHI**2 - PHI)/100)
        else:
            # General nodes maintain base coherence
            return base_coherence
    
    def _update_node_state(self) -> None:
        """Update node state with specialization information."""
        # Add specialization to dimensional state
        self.core.state.dimensional_state["specialization"] = {
            "type": self.specialization,
            "coherence": self.specialization_coherence,
            "capabilities": self.capabilities,
            "performance_metrics": self.performance_metrics
        }
        
        # Update quantum fingerprint
        self.core.state.update_quantum_fingerprint()
    
    def activate(self) -> bool:
        """
        Activate the specialized node.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.is_active = True
            self.activation_time = time.time()
            
            # Add activation event to evolution history
            self.core.state.evolution_history.append({
                "event": f"{self.specialization}_activation",
                "timestamp": self.activation_time,
                "specialization": self.specialization,
                "specialization_coherence": self.specialization_coherence
            })
            
            # Update node state
            self._update_node_state()
            
            logger.info(f"{self.specialization} node activated")
            return True
        except Exception as e:
            logger.error(f"Error activating {self.specialization} node: {e}")
            return False
    
    def deactivate(self) -> bool:
        """
        Deactivate the specialized node.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.is_active = False
            deactivation_time = time.time()
            
            # Add deactivation event to evolution history
            self.core.state.evolution_history.append({
                "event": f"{self.specialization}_deactivation",
                "timestamp": deactivation_time,
                "specialization": self.specialization,
                "active_duration": deactivation_time - (self.activation_time or deactivation_time)
            })
            
            # Update node state
            self._update_node_state()
            
            logger.info(f"{self.specialization} node deactivated")
            return True
        except Exception as e:
            logger.error(f"Error deactivating {self.specialization} node: {e}")
            return False
    
    def update_performance_metrics(self, metrics: Dict[str, Any]) -> None:
        """
        Update performance metrics.
        
        Args:
            metrics: Performance metrics to update
        """
        self.performance_metrics.update(metrics)
        self.performance_metrics["last_updated"] = time.time()
        
        # Update node state
        self._update_node_state()
    
    def record_task(self, task_type: str, task_data: Dict[str, Any], result: Dict[str, Any]) -> None:
        """
        Record task execution.
        
        Args:
            task_type: Type of task
            task_data: Task input data
            result: Task result
        """
        task_time = time.time()
        self.last_task_time = task_time
        
        # Create task record
        task_record = {
            "task_id": str(uuid.uuid4()),
            "task_type": task_type,
            "timestamp": task_time,
            "duration": result.get("duration", 0),
            "success": result.get("success", False),
            "metrics": result.get("metrics", {})
        }
        
        # Add task to history
        self.task_history.append(task_record)
        
        # Limit history size
        if len(self.task_history) > 100:
            self.task_history = self.task_history[-100:]
        
        # Update performance metrics based on task result
        metrics = result.get("metrics", {})
        if metrics:
            self.update_performance_metrics(metrics)
    
    def get_capability_score(self, capability: str) -> float:
        """
        Get score for specific capability.
        
        Args:
            capability: Capability name
            
        Returns:
            float: Capability score (0.0 to 1.0)
        """
        return self.capabilities.get(capability, 0.0)
    
    def get_overall_performance(self) -> float:
        """
        Calculate overall performance score.
        
        Returns:
            float: Performance score (0.0 to 1.0)
        """
        if not self.performance_metrics:
            return 0.0
        
        # Calculate phi-weighted average of performance metrics
        metrics = [v for k, v in self.performance_metrics.items() if isinstance(v, (int, float)) and k != "last_updated"]
        if not metrics:
            return 0.0
        
        # Apply phi-harmonic weighting
        phi_sum = sum(m * (PHI ** (i % 3)) for i, m in enumerate(metrics))
        phi_weight = sum(PHI ** (i % 3) for i in range(len(metrics)))
        
        return phi_sum / phi_weight if phi_weight > 0 else 0.0
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Convert specialized node to dictionary.
        
        Returns:
            dict: Node as dictionary
        """
        return {
            "node_id": self.core.state.node_id,
            "specialization": self.specialization,
            "specialization_coherence": self.specialization_coherence,
            "is_active": self.is_active,
            "activation_time": self.activation_time,
            "last_task_time": self.last_task_time,
            "capabilities": self.capabilities,
            "performance_metrics": self.performance_metrics,
            "task_history_count": len(self.task_history)
        }
    
    @abstractmethod
    def can_perform_task(self, task_type: str, task_data: Dict[str, Any]) -> bool:
        """
        Check if node can perform specific task.
        
        Args:
            task_type: Type of task
            task_data: Task input data
            
        Returns:
            bool: True if node can perform task, False otherwise
        """
        pass
    
    @abstractmethod
    def perform_task(self, task_type: str, task_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform task.
        
        Args:
            task_type: Type of task
            task_data: Task input data
            
        Returns:
            dict: Task result
        """
        pass


def create_specialized_node(core: QuantumNodularCore, specialization: str) -> Optional[QuantumSpecializedNode]:
    """
    Create specialized node based on specialization type.
    
    Args:
        core: Quantum nodular core
        specialization: Node specialization type
        
    Returns:
        QuantumSpecializedNode: Specialized node
    """
    try:
        if specialization == NodeSpecialization.COMPUTATION:
            from quantum_computation_node import QuantumComputationNode
            return QuantumComputationNode(core)
        elif specialization == NodeSpecialization.STORAGE:
            from quantum_storage_node import QuantumStorageNode
            return QuantumStorageNode(core)
        elif specialization == NodeSpecialization.BRIDGE:
            from quantum_bridge_node import QuantumBridgeNode
            return QuantumBridgeNode(core)
        elif specialization == NodeSpecialization.EVOLUTION:
            from quantum_evolution_node import QuantumEvolutionNode
            return QuantumEvolutionNode(core)
        else:
            logger.error(f"Unknown specialization: {specialization}")
            return None
    except ImportError as e:
        logger.error(f"Error importing specialized node module: {e}")
        return None
    except Exception as e:
        logger.error(f"Error creating specialized node: {e}")
        return None
