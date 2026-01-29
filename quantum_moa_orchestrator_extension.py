#!/usr/bin/env python3
"""
Quantum MoA Orchestrator Extension
---------------------------------

Extension module for QuantumMoAOrchestratorConnector that adds missing methods.
This follows the modular "lego" architecture principle by extending functionality
without modifying the core connector.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import logging
import time
import json
import hashlib
from typing import Dict, Any, List, Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumMoAOrchestratorExtension")

# Import the core connector
try:
    from quantum_moa_orchestrator_connector import QuantumMoAOrchestratorConnector
    from quantum_moe_interfaces import QuantumAgentInterface, generate_quantum_id
except ImportError as e:
    logger.error(f"Import error: {e}")
    raise

class QuantumMoAOrchestratorExtension:
    """Extension for QuantumMoAOrchestratorConnector that adds missing methods."""
    
    @staticmethod
    def extend():
        """Extend QuantumMoAOrchestratorConnector with missing methods."""
        logger.info("Extending QuantumMoAOrchestratorConnector with missing methods")
        
        # Add add_agent method
        if not hasattr(QuantumMoAOrchestratorConnector, "add_agent"):
            def add_agent(self, agent: QuantumAgentInterface, agent_type: str = None):
                """
                Add a custom agent to the connector.
                
                Args:
                    agent: Agent instance implementing QuantumAgentInterface
                    agent_type: Optional type identifier for the agent
                
                Returns:
                    The agent ID
                """
                if not isinstance(agent, QuantumAgentInterface):
                    logger.error("Agent must implement QuantumAgentInterface")
                    return None
                
                agent_id = agent.get_id() if hasattr(agent, 'get_id') else generate_quantum_id()
                agent_type = agent_type or agent.__class__.__name__
                
                # Store the agent as an attribute
                setattr(self, f"{agent_type.lower()}_agent", agent)
                
                logger.info(f"Added agent of type {agent_type} with ID: {agent_id}")
                return agent_id
            
            setattr(QuantumMoAOrchestratorConnector, "add_agent", add_agent)
            logger.info("Added add_agent method to QuantumMoAOrchestratorConnector")
        
        # Add create_agent_group method
        if not hasattr(QuantumMoAOrchestratorConnector, "create_agent_group"):
            def create_agent_group(self, agents: List[QuantumAgentInterface], group_name: str = None):
                """
                Create a group of agents that can work together.
                
                Args:
                    agents: List of agent instances
                    group_name: Optional name for the group
                
                Returns:
                    Group ID
                """
                group_id = generate_quantum_id()
                group_name = group_name or f"agent_group_{group_id[:8]}"
                
                # Add each agent if not already added
                agent_ids = []
                for agent in agents:
                    if not isinstance(agent, QuantumAgentInterface):
                        logger.warning(f"Skipping agent that doesn't implement QuantumAgentInterface")
                        continue
                    
                    agent_id = self.add_agent(agent)
                    agent_ids.append(agent_id)
                
                # Store the group
                if not hasattr(self, "agent_groups"):
                    self.agent_groups = {}
                
                self.agent_groups[group_id] = {
                    "name": group_name,
                    "agent_ids": agent_ids,
                    "created_at": time.time()
                }
                
                logger.info(f"Created agent group '{group_name}' with ID: {group_id}")
                return group_id
            
            setattr(QuantumMoAOrchestratorConnector, "create_agent_group", create_agent_group)
            logger.info("Added create_agent_group method to QuantumMoAOrchestratorConnector")
        
        # Add process_file_with_agent method
        if not hasattr(QuantumMoAOrchestratorConnector, "process_file_with_agent"):
            def process_file_with_agent(self, file_path: str, agent_type: str) -> Dict[str, Any]:
                """
                Process a file with a specific agent.
                
                Args:
                    file_path: Path to the file to process
                    agent_type: Type of agent to use (e.g., 'logic_error', 'optimization')
                
                Returns:
                    Results of the agent action
                """
                agent_attr = f"{agent_type.lower()}_agent"
                if not hasattr(self, agent_attr):
                    logger.error(f"Agent of type {agent_type} not found")
                    return {"error": f"Agent of type {agent_type} not found"}
                
                agent = getattr(self, agent_attr)
                
                try:
                    with open(file_path, 'r') as f:
                        code = f.read()
                    
                    context = {
                        'code': code,
                        'file_path': file_path
                    }
                    
                    start_time = time.time()
                    result = agent.act(context)
                    duration = time.time() - start_time
                    
                    result["duration"] = duration
                    
                    # Update action history
                    self.action_history.append({
                        "type": f"{agent_type}_action",
                        "timestamp": time.time(),
                        "file": file_path,
                        "agent_id": agent.get_id() if hasattr(agent, 'get_id') else None,
                        "duration": duration,
                        "results": result
                    })
                    
                    return result
                    
                except Exception as e:
                    logger.error(f"Error processing file with {agent_type} agent: {str(e)}")
                    return {"error": str(e)}
            
            setattr(QuantumMoAOrchestratorConnector, "process_file_with_agent", process_file_with_agent)
            logger.info("Added process_file_with_agent method to QuantumMoAOrchestratorConnector")
        
        return QuantumMoAOrchestratorConnector


# Apply extension when module is imported
def apply_extension():
    """Apply the extension to QuantumMoAOrchestratorConnector."""
    return QuantumMoAOrchestratorExtension.extend()


if __name__ == "__main__":
    # Apply extension and test
    extended_connector = apply_extension()
    
    # Create a test connector instance
    connector = extended_connector()
    
    # Test add_agent method
    from quantum_moa_agents import LogicErrorAgent
    
    test_agent = LogicErrorAgent()
    agent_id = connector.add_agent(test_agent, "TestAgent")
    
    logger.info(f"Added test agent with ID: {agent_id}")
    logger.info("Extension test completed successfully")
