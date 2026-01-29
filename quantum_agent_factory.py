"""
quantum_agent_factory.py

Agent factory module for the QuantumAI system that creates specialized agents
for different tasks in the Mixture of Agents (MoA) architecture.

This module enables dynamic creation of agents that work together to perform
complex tasks while maintaining phi-harmonic principles.
"""

import os
import json
import time
import hashlib
import logging
import uuid
from abc import ABC, abstractmethod
from typing import Dict, List, Tuple, Any, Optional, Union, Callable

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("PhiAgentFactory")

class PhiHarmonicAgent(ABC):
    """
    Base class for all phi-harmonic agents in the Mixture of Agents architecture.
    
    Each agent specializes in a specific task type and maintains phi-harmonic
    principles in its operation.
    """
    
    def __init__(self, 
                agent_type: str, 
                specialization: str, 
                phi: float = 1.618033988749895):
        """
        Initialize a phi-harmonic agent.
        
        Args:
            agent_type: Type of agent (e.g., "logic_error", "optimization")
            specialization: Agent specialization (e.g., "healing", "analysis")
            phi: Golden ratio value
        """
        self.phi = phi
        self.agent_type = agent_type
        self.specialization = specialization
        self.agent_id = str(uuid.uuid4())
        
        # Generate unique quantum fingerprint for this agent
        self.quantum_fingerprint = self._generate_agent_fingerprint()
        
        # Agent state
        self.state = {
            "status": "idle",  # idle, working, completed, failed
            "task_id": None,
            "creation_time": time.time(),
            "last_active_time": time.time(),
            "completed_tasks": 0,
            "success_rate": 0.0,
            "phi_coherence": 0.991800  # Starting coherence value
        }
        
        logger.info(f"Created {self.agent_type} agent with {self.specialization} specialization")
    
    @abstractmethod
    def process_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a task with this agent's specialized capabilities.
        
        Args:
            task: Task description and parameters
            
        Returns:
            Task processing results
        """
        pass
    
    @abstractmethod
    def get_capabilities(self) -> List[str]:
        """
        Get a list of this agent's capabilities.
        
        Returns:
            List of capability strings
        """
        pass
    
    def update_state(self, 
                    status: str, 
                    task_id: Optional[str] = None, 
                    success: Optional[bool] = None) -> None:
        """
        Update this agent's state.
        
        Args:
            status: New status (idle, working, completed, failed)
            task_id: ID of the current task (if applicable)
            success: Whether the task was successful (if applicable)
        """
        # Update status
        self.state["status"] = status
        
        # Update task ID if provided
        if task_id is not None:
            self.state["task_id"] = task_id
        
        # Update last active time
        self.state["last_active_time"] = time.time()
        
        # Update success metrics if applicable
        if status == "completed":
            self.state["completed_tasks"] += 1
            
            if success is not None:
                # Update success rate with exponential moving average
                alpha = 1 / self.phi  # Learning rate based on phi
                current_success_rate = self.state["success_rate"]
                self.state["success_rate"] = (
                    (1 - alpha) * current_success_rate + 
                    alpha * (1.0 if success else 0.0)
                )
                
                # Update phi coherence
                self._update_phi_coherence(success)
    
    def get_state_report(self) -> Dict[str, Any]:
        """
        Get a report of this agent's current state.
        
        Returns:
            State report dictionary
        """
        # Calculate active time
        active_time = 0
        if self.state["status"] == "working":
            active_time = time.time() - self.state["last_active_time"]
        
        return {
            "agent_id": self.agent_id,
            "agent_type": self.agent_type,
            "specialization": self.specialization,
            "quantum_fingerprint": self.quantum_fingerprint,
            "status": self.state["status"],
            "task_id": self.state["task_id"],
            "active_time": active_time,
            "completed_tasks": self.state["completed_tasks"],
            "success_rate": self.state["success_rate"],
            "phi_coherence": self.state["phi_coherence"],
            "coherence_quality": self._evaluate_coherence_quality(),
            "capabilities": self.get_capabilities()
        }
    
    def _generate_agent_fingerprint(self) -> str:
        """
        Generate a quantum fingerprint for this agent.
        
        Returns:
            Quantum fingerprint string
        """
        # Create a unique identifier for this agent
        agent_id = f"{self.agent_type}_{self.specialization}_{self.agent_id}"
        
        # Generate hash
        agent_hash = hashlib.sha256(agent_id.encode()).hexdigest()[:16]
        
        # Use φ⁷·⁵ notation for consistency with the rest of the system
        return f"φ⁷·⁵-{agent_hash}"
    
    def _update_phi_coherence(self, success: bool) -> None:
        """
        Update phi coherence based on task success.
        
        Args:
            success: Whether the task was successful
        """
        # Current coherence
        current_coherence = self.state["phi_coherence"]
        
        # Calculate adjustment factor
        adjustment = 0.0001 * (1 if success else -1)
        
        # Apply adjustment
        new_coherence = current_coherence + adjustment
        
        # Ensure coherence stays in valid range (0.9-1.0)
        new_coherence = max(0.9, min(0.999, new_coherence))
        
        # Update stored coherence
        self.state["phi_coherence"] = new_coherence
    
    def _evaluate_coherence_quality(self) -> str:
        """
        Evaluate the quality of phi-coherence.
        
        Returns:
            Quality description
        """
        coherence = self.state["phi_coherence"]
        if coherence >= 0.995:
            return "Perfect"
        elif coherence >= 0.99:
            return "Excellent"
        elif coherence >= 0.98:
            return "Good"
        elif coherence >= 0.95:
            return "Moderate"
        else:
            return "Weak"


class LogicErrorAgent(PhiHarmonicAgent):
    """Agent specializing in detecting and healing logic errors in code."""
    
    def __init__(self, phi: float = 1.618033988749895):
        super().__init__(agent_type="logic_error", specialization="healing", phi=phi)
        
        # Logic error patterns
        self.error_patterns = {
            "off_by_one": ["range(", "len(", "+1", "-1"],
            "condition_inversion": ["if", "else", "not", "==", "!=", "<", ">"],
            "variable_misuse": ["=", "+=", "-=", "*=", "/="],
            "return_error": ["return", "None", "[]", "{}"]
        }
    
    def process_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Process a logic error detection and healing task."""
        # Extract task parameters
        func_code = task.get("func_code", "")
        func_name = task.get("func_name", "")
        expected_behavior = task.get("expected_behavior", {})
        
        # Update state to working
        self.update_state("working", task.get("task_id"))
        
        try:
            # Detect logic errors
            errors_detected = self._detect_logic_errors(func_code, expected_behavior)
            
            # Generate healing suggestions if errors were detected
            healing_suggestions = {}
            if errors_detected:
                healing_suggestions = self._generate_healing_suggestions(
                    func_code, func_name, errors_detected)
            
            # Calculate phi-resonance of the healing
            phi_resonance = (self.phi * len(errors_detected)) % 1
            
            # Update state to completed
            self.update_state("completed", task.get("task_id"), bool(healing_suggestions))
            
            return {
                "agent_id": self.agent_id,
                "task_id": task.get("task_id"),
                "errors_detected": errors_detected,
                "healing_suggestions": healing_suggestions,
                "phi_resonance": phi_resonance,
                "success": bool(healing_suggestions),
                "quantum_fingerprint": self._generate_result_fingerprint(func_name, errors_detected)
            }
            
        except Exception as e:
            # Update state to failed
            self.update_state("failed", task.get("task_id"), False)
            
            return {
                "agent_id": self.agent_id,
                "task_id": task.get("task_id"),
                "error": str(e),
                "success": False
            }
    
    def get_capabilities(self) -> List[str]:
        """Get a list of this agent's capabilities."""
        return [
            "logic_error_detection",
            "off_by_one_error_healing",
            "condition_inversion_healing",
            "variable_misuse_healing",
            "return_error_healing"
        ]
    
    def _detect_logic_errors(self, 
                           func_code: str, 
                           expected_behavior: Dict[str, Any]) -> Dict[str, Any]:
        """
        Detect logic errors in function code.
        
        Args:
            func_code: Function source code
            expected_behavior: Expected behavior description
            
        Returns:
            Dictionary of detected errors
        """
        # This is a simplified implementation
        # In a real system, this would use more sophisticated error detection
        
        errors = {}
        
        # Check for off-by-one errors
        if any(pattern in func_code for pattern in self.error_patterns["off_by_one"]):
            if "range(" in func_code and ("len(" in func_code):
                errors["off_by_one"] = {
                    "confidence": 0.75,
                    "description": "Potential off-by-one error in range/len usage"
                }
        
        # Check for condition inversion
        if "if" in func_code and any(op in func_code for op in ["==", "!=", "<", ">"]):
            # This is a very simplified check
            errors["condition_inversion"] = {
                "confidence": 0.6,
                "description": "Potential condition inversion or incorrect comparison"
            }
        
        # Check for variable misuse
        var_assignments = func_code.count("=") - func_code.count("==")
        if var_assignments > 3:  # Arbitrary threshold
            errors["variable_misuse"] = {
                "confidence": 0.5,
                "description": "Potential variable misuse or overwrite"
            }
        
        return errors
    
    def _generate_healing_suggestions(self, 
                                    func_code: str, 
                                    func_name: str, 
                                    errors: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate healing suggestions for detected errors.
        
        Args:
            func_code: Function source code
            func_name: Function name
            errors: Detected errors
            
        Returns:
            Healing suggestions
        """
        # This is a simplified implementation
        # In a real system, this would generate actual code fixes
        
        suggestions = {}
        
        for error_type, error_info in errors.items():
            if error_type == "off_by_one":
                suggestions["off_by_one"] = {
                    "description": "Check range bounds and ensure proper indexing",
                    "confidence": error_info["confidence"],
                    "example_fix": "range(len(array)) -> range(len(array) - 1)" if "range(len(" in func_code else "N/A"
                }
            elif error_type == "condition_inversion":
                suggestions["condition_inversion"] = {
                    "description": "Review conditional logic and ensure correct comparisons",
                    "confidence": error_info["confidence"],
                    "example_fix": "if x < y -> if x > y" if "if" in func_code else "N/A"
                }
            elif error_type == "variable_misuse":
                suggestions["variable_misuse"] = {
                    "description": "Check variable assignments and ensure proper usage",
                    "confidence": error_info["confidence"],
                    "example_fix": "Create separate variables for intermediate values"
                }
        
        return suggestions
    
    def _generate_result_fingerprint(self, 
                                   func_name: str, 
                                   errors: Dict[str, Any]) -> str:
        """
        Generate a quantum fingerprint for the healing result.
        
        Args:
            func_name: Function name
            errors: Detected errors
            
        Returns:
            Quantum fingerprint string
        """
        # Create a unique identifier for this result
        result_id = f"{func_name}_{','.join(errors.keys())}_{time.time()}"
        
        # Generate hash
        result_hash = hashlib.sha256(result_id.encode()).hexdigest()[:16]
        
        # Use φ⁷·⁵ notation for consistency
        return f"φ⁷·⁵-{result_hash}"


class OptimizationAgent(PhiHarmonicAgent):
    """Agent specializing in optimizing code performance."""
    
    def __init__(self, phi: float = 1.618033988749895):
        super().__init__(agent_type="optimization", specialization="performance", phi=phi)
        
        # Optimization patterns
        self.optimization_patterns = {
            "loop_optimization": ["for", "while", "range(", "enumerate(", "zip("],
            "data_structure": ["list", "dict", "set", "tuple", "array"],
            "algorithm_complexity": ["sort", "search", "find", "match", "count"],
            "memory_usage": ["append", "extend", "insert", "remove", "pop"]
        }
    
    def process_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Process a code optimization task."""
        # Extract task parameters
        func_code = task.get("func_code", "")
        func_name = task.get("func_name", "")
        performance_metrics = task.get("performance_metrics", {})
        
        # Update state to working
        self.update_state("working", task.get("task_id"))
        
        try:
            # Identify optimization opportunities
            optimization_opportunities = self._identify_optimization_opportunities(
                func_code, performance_metrics)
            
            # Generate optimization suggestions
            optimization_suggestions = {}
            if optimization_opportunities:
                optimization_suggestions = self._generate_optimization_suggestions(
                    func_code, func_name, optimization_opportunities)
            
            # Calculate phi-resonance of the optimization
            phi_resonance = (self.phi * len(optimization_opportunities)) % 1
            
            # Update state to completed
            self.update_state("completed", task.get("task_id"), bool(optimization_suggestions))
            
            return {
                "agent_id": self.agent_id,
                "task_id": task.get("task_id"),
                "optimization_opportunities": optimization_opportunities,
                "optimization_suggestions": optimization_suggestions,
                "phi_resonance": phi_resonance,
                "success": bool(optimization_suggestions),
                "quantum_fingerprint": self._generate_result_fingerprint(func_name, optimization_opportunities)
            }
            
        except Exception as e:
            # Update state to failed
            self.update_state("failed", task.get("task_id"), False)
            
            return {
                "agent_id": self.agent_id,
                "task_id": task.get("task_id"),
                "error": str(e),
                "success": False
            }
    
    def get_capabilities(self) -> List[str]:
        """Get a list of this agent's capabilities."""
        return [
            "loop_optimization",
            "data_structure_optimization",
            "algorithm_complexity_reduction",
            "memory_usage_optimization"
        ]
    
    def _identify_optimization_opportunities(self, 
                                           func_code: str, 
                                           performance_metrics: Dict[str, Any]) -> Dict[str, Any]:
        """
        Identify optimization opportunities in function code.
        
        Args:
            func_code: Function source code
            performance_metrics: Performance metrics (if available)
            
        Returns:
            Dictionary of optimization opportunities
        """
        # This is a simplified implementation
        # In a real system, this would use more sophisticated analysis
        
        opportunities = {}
        
        # Check for loop optimization opportunities
        if any(pattern in func_code for pattern in self.optimization_patterns["loop_optimization"]):
            if "for" in func_code and "range(" in func_code:
                opportunities["loop_optimization"] = {
                    "confidence": 0.7,
                    "description": "Potential loop optimization opportunity"
                }
        
        # Check for data structure optimization
        if "list" in func_code and "in" in func_code:
            opportunities["data_structure"] = {
                "confidence": 0.8,
                "description": "Consider using set instead of list for membership testing"
            }
        
        # Check for algorithm complexity issues
        if any(pattern in func_code for pattern in self.optimization_patterns["algorithm_complexity"]):
            opportunities["algorithm_complexity"] = {
                "confidence": 0.6,
                "description": "Potential algorithm complexity improvement"
            }
        
        return opportunities
    
    def _generate_optimization_suggestions(self, 
                                         func_code: str, 
                                         func_name: str, 
                                         opportunities: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate optimization suggestions for identified opportunities.
        
        Args:
            func_code: Function source code
            func_name: Function name
            opportunities: Identified optimization opportunities
            
        Returns:
            Optimization suggestions
        """
        # This is a simplified implementation
        # In a real system, this would generate actual code optimizations
        
        suggestions = {}
        
        for opt_type, opt_info in opportunities.items():
            if opt_type == "loop_optimization":
                suggestions["loop_optimization"] = {
                    "description": "Optimize loop structure for better performance",
                    "confidence": opt_info["confidence"],
                    "example_fix": "Use list comprehension instead of for loop" if "for" in func_code else "N/A"
                }
            elif opt_type == "data_structure":
                suggestions["data_structure"] = {
                    "description": "Use more appropriate data structure for operations",
                    "confidence": opt_info["confidence"],
                    "example_fix": "list -> set for membership testing" if "list" in func_code and "in" in func_code else "N/A"
                }
            elif opt_type == "algorithm_complexity":
                suggestions["algorithm_complexity"] = {
                    "description": "Improve algorithm complexity",
                    "confidence": opt_info["confidence"],
                    "example_fix": "Consider using a more efficient algorithm or data structure"
                }
        
        return suggestions
    
    def _generate_result_fingerprint(self, 
                                   func_name: str, 
                                   opportunities: Dict[str, Any]) -> str:
        """
        Generate a quantum fingerprint for the optimization result.
        
        Args:
            func_name: Function name
            opportunities: Identified optimization opportunities
            
        Returns:
            Quantum fingerprint string
        """
        # Create a unique identifier for this result
        result_id = f"{func_name}_{','.join(opportunities.keys())}_{time.time()}"
        
        # Generate hash
        result_hash = hashlib.sha256(result_id.encode()).hexdigest()[:16]
        
        # Use φ⁷·⁵ notation for consistency
        return f"φ⁷·⁵-{result_hash}"


class PhiHarmonicAgentFactory:
    """
    Factory for creating specialized phi-harmonic agents.
    
    This factory enables dynamic creation of agents that work together
    to perform complex tasks while maintaining phi-harmonic principles.
    """
    
    def __init__(self, phi: float = 1.618033988749895):
        """
        Initialize the phi-harmonic agent factory.
        
        Args:
            phi: Golden ratio value
        """
        self.phi = phi
        self.agent_templates = {}
        self.active_agents = {}
        self.agent_evolution = {}
        
        # Initialize with default agent templates
        self._initialize_default_templates()
        
        logger.info(f"Initialized PhiHarmonicAgentFactory with {len(self.agent_templates)} templates")
    
    def create_agent(self, 
                    agent_type: str, 
                    specialization: Optional[str] = None) -> PhiHarmonicAgent:
        """
        Create a new agent of specified type and specialization.
        
        Args:
            agent_type: Type of agent to create
            specialization: Optional specialization (if None, uses default)
            
        Returns:
            PhiHarmonicAgent instance
        """
        # Get agent class based on type
        agent_class = self._get_agent_class(agent_type)
        
        # Create agent instance
        agent = agent_class(phi=self.phi)
        
        # Register agent
        self.active_agents[agent.agent_id] = agent
        
        logger.info(f"Created {agent_type} agent with ID {agent.agent_id}")
        
        return agent
    
    def get_agent(self, agent_id: str) -> Optional[PhiHarmonicAgent]:
        """
        Get an agent by ID.
        
        Args:
            agent_id: Agent ID
            
        Returns:
            PhiHarmonicAgent instance or None if not found
        """
        return self.active_agents.get(agent_id)
    
    def list_active_agents(self) -> List[Dict[str, Any]]:
        """
        List all active agents.
        
        Returns:
            List of agent state reports
        """
        return [agent.get_state_report() for agent in self.active_agents.values()]
    
    def register_agent_success(self, 
                             agent_id: str, 
                             success_metrics: Dict[str, Any]) -> None:
        """
        Register successful agent operation for evolution.
        
        Args:
            agent_id: Agent ID
            success_metrics: Success metrics
        """
        agent = self.active_agents.get(agent_id)
        if not agent:
            logger.warning(f"Agent {agent_id} not found")
            return
        
        # Update agent evolution data
        if agent.agent_type not in self.agent_evolution:
            self.agent_evolution[agent.agent_type] = []
        
        self.agent_evolution[agent.agent_type].append({
            "timestamp": time.time(),
            "agent_id": agent_id,
            "agent_type": agent.agent_type,
            "specialization": agent.specialization,
            "success_metrics": success_metrics,
            "phi_coherence": agent.state["phi_coherence"]
        })
        
        logger.info(f"Registered success for agent {agent_id}")
    
    def evolve_agent_template(self, agent_type: str) -> Dict[str, Any]:
        """
        Evolve an agent template based on success metrics.
        
        Args:
            agent_type: Agent type to evolve
            
        Returns:
            Updated template information
        """
        if agent_type not in self.agent_evolution or not self.agent_evolution[agent_type]:
            logger.warning(f"No evolution data for agent type {agent_type}")
            return {}
        
        # Analyze evolution data
        evolution_data = self.agent_evolution[agent_type]
        
        # Calculate average phi coherence
        avg_coherence = sum(e["phi_coherence"] for e in evolution_data) / len(evolution_data)
        
        # Calculate success rate
        success_count = sum(1 for e in evolution_data if e["success_metrics"].get("success", False))
        success_rate = success_count / len(evolution_data) if evolution_data else 0
        
        # Update template
        template_update = {
            "agent_type": agent_type,
            "evolution_count": len(evolution_data),
            "avg_coherence": avg_coherence,
            "success_rate": success_rate,
            "last_evolved": time.time(),
            "quantum_fingerprint": self._generate_evolution_fingerprint(agent_type, avg_coherence)
        }
        
        logger.info(f"Evolved template for {agent_type}: success_rate={success_rate:.4f}, coherence={avg_coherence:.6f}")
        
        return template_update
    
    def _initialize_default_templates(self) -> None:
        """Initialize default agent templates."""
        self.agent_templates = {
            "logic_error": {
                "class": LogicErrorAgent,
                "default_specialization": "healing",
                "phi_resonance": 1 / self.phi**3
            },
            "optimization": {
                "class": OptimizationAgent,
                "default_specialization": "performance",
                "phi_resonance": 1 / self.phi**4
            }
            # Add more agent types as they are implemented
        }
    
    def _get_agent_class(self, agent_type: str) -> type:
        """
        Get agent class based on type.
        
        Args:
            agent_type: Agent type
            
        Returns:
            Agent class
            
        Raises:
            ValueError: If agent type is unknown
        """
        if agent_type not in self.agent_templates:
            raise ValueError(f"Unknown agent type: {agent_type}")
        
        return self.agent_templates[agent_type]["class"]
    
    def _generate_evolution_fingerprint(self, 
                                      agent_type: str, 
                                      coherence: float) -> str:
        """
        Generate a quantum fingerprint for template evolution.
        
        Args:
            agent_type: Agent type
            coherence: Phi coherence value
            
        Returns:
            Quantum fingerprint string
        """
        # Create a unique identifier for this evolution
        evolution_id = f"{agent_type}_{coherence}_{time.time()}"
        
        # Generate hash
        evolution_hash = hashlib.sha256(evolution_id.encode()).hexdigest()[:16]
        
        # Use φ⁷·⁵ notation for consistency
        return f"φ⁷·⁵-{evolution_hash}"


# Module-level functions for direct use

def create_agent(agent_type: str, phi: float = 1.618033988749895) -> PhiHarmonicAgent:
    """
    Create a phi-harmonic agent of the specified type.
    
    Args:
        agent_type: Type of agent to create
        phi: Golden ratio value
        
    Returns:
        PhiHarmonicAgent instance
    """
    factory = PhiHarmonicAgentFactory(phi=phi)
    return factory.create_agent(agent_type)


if __name__ == "__main__":
    # Simple test of the module
    factory = PhiHarmonicAgentFactory()
    
    # Create agents
    logic_agent = factory.create_agent("logic_error")
    optimization_agent = factory.create_agent("optimization")
    
    # Test function code with logic error
    test_code = """
def increment_values(numbers):
    # Logic error: incrementing by 2 instead of 1
    return [x + 2 for x in numbers]
"""
    
    # Process with logic error agent
    logic_task = {
        "task_id": "test_task_1",
        "func_code": test_code,
        "func_name": "increment_values",
        "expected_behavior": {"increment": 1}
    }
    logic_result = logic_agent.process_task(logic_task)
    
    # Process with optimization agent
    optimization_task = {
        "task_id": "test_task_2",
        "func_code": test_code,
        "func_name": "increment_values",
        "performance_metrics": {}
    }
    optimization_result = optimization_agent.process_task(optimization_task)
    
    print(f"Logic agent result: {logic_result}")
    print(f"Optimization agent result: {optimization_result}")
    
    # List active agents
    active_agents = factory.list_active_agents()
    print(f"Active agents: {active_agents}")
    
    # Register success and evolve template
    factory.register_agent_success(logic_agent.agent_id, {"success": True})
    evolution = factory.evolve_agent_template("logic_error")
    print(f"Template evolution: {evolution}")
