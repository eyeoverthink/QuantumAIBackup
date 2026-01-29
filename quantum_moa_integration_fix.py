#!/usr/bin/env python3
"""
Quantum MoA Integration Fix
--------------------------

This module provides a comprehensive fix for the Mixture of Agents (MoA) integration
with the quantum orchestrator. It ensures proper agent initialization and counting.

This follows the 'lego' modular philosophy by extending functionality without
modifying core files.
"""

import os
import sys
import logging
import importlib
import inspect
from typing import Dict, List, Tuple, Optional, Any, Callable

# Import our connector adapter
try:
    from quantum_moa_connector_adapter import create_connector_with_agents
except ImportError:
    pass  # Will handle this in the code

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumMoAIntegrationFix")

class QuantumMoAIntegrationFix:
    """
    Fix for the Mixture of Agents (MoA) integration with the quantum orchestrator.
    """
    
    def __init__(self):
        """Initialize the MoA integration fix."""
        self.agents = []
        self.agent_modules = {}
        self.connector = None
        logger.info("Initialized QuantumMoAIntegrationFix")
    
    def load_agent_modules(self):
        """
        Load all agent modules dynamically.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Try to import the agent modules
            from quantum_moa_agents import LogicErrorAgent, OptimizationAgent, CoherenceAgent, EvolutionAgent
            from quantum_moa_visitors import LogicErrorVisitor, OptimizationVisitor
            
            self.agent_modules = {
                'LogicErrorAgent': LogicErrorAgent,
                'OptimizationAgent': OptimizationAgent,
                'CoherenceAgent': CoherenceAgent,
                'EvolutionAgent': EvolutionAgent,
                'LogicErrorVisitor': LogicErrorVisitor,
                'OptimizationVisitor': OptimizationVisitor
            }
            
            logger.info(f"Successfully loaded {len(self.agent_modules)} agent modules")
            return True
        except ImportError as e:
            logger.error(f"Failed to import agent modules: {e}")
            
            # Try to find the modules in the current directory
            try:
                sys.path.append(os.getcwd())
                
                # Try to import again
                from quantum_moa_agents import LogicErrorAgent, OptimizationAgent, CoherenceAgent, EvolutionAgent
                from quantum_moa_visitors import LogicErrorVisitor, OptimizationVisitor
                
                self.agent_modules = {
                    'LogicErrorAgent': LogicErrorAgent,
                    'OptimizationAgent': OptimizationAgent,
                    'CoherenceAgent': CoherenceAgent,
                    'EvolutionAgent': EvolutionAgent,
                    'LogicErrorVisitor': LogicErrorVisitor,
                    'OptimizationVisitor': OptimizationVisitor
                }
                
                logger.info(f"Successfully loaded {len(self.agent_modules)} agent modules after path adjustment")
                return True
            except ImportError as e2:
                logger.error(f"Failed to import agent modules after path adjustment: {e2}")
                return False
    
    def load_connector(self):
        """
        Load the MoA orchestrator connector.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Try to import the connector
            from quantum_moa_orchestrator_connector import QuantumMoAOrchestratorConnector
            
            self.connector_class = QuantumMoAOrchestratorConnector
            logger.info("Successfully loaded QuantumMoAOrchestratorConnector")
            return True
        except ImportError as e:
            logger.error(f"Failed to import QuantumMoAOrchestratorConnector: {e}")
            
            # Try to find the module in the current directory
            try:
                sys.path.append(os.getcwd())
                
                # Try to import again
                from quantum_moa_orchestrator_connector import QuantumMoAOrchestratorConnector
                
                self.connector_class = QuantumMoAOrchestratorConnector
                logger.info("Successfully loaded QuantumMoAOrchestratorConnector after path adjustment")
                return True
            except ImportError as e2:
                logger.error(f"Failed to import QuantumMoAOrchestratorConnector after path adjustment: {e2}")
                return False
    
    def create_agents(self):
        """
        Create all agent instances.
        
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.agent_modules:
            logger.error("No agent modules loaded")
            return False
        
        try:
            # Create agent instances
            self.agents = [
                self.agent_modules['LogicErrorAgent'](),
                self.agent_modules['OptimizationAgent'](),
                self.agent_modules['CoherenceAgent'](),
                self.agent_modules['EvolutionAgent']()
            ]
            
            logger.info(f"Successfully created {len(self.agents)} agent instances")
            return True
        except Exception as e:
            logger.error(f"Failed to create agent instances: {e}")
            return False
    
    def create_connector(self, orchestrator=None):
        """
        Create the MoA orchestrator connector.
        
        Args:
            orchestrator: Optional orchestrator instance
            
        Returns:
            bool: True if successful, False otherwise
        """
        # Try using our connector adapter first
        try:
            success, adapter = create_connector_with_agents(self.agents, orchestrator)
            if success:
                self.connector = adapter
                logger.info("Successfully created connector instance using adapter")
                return True
        except (NameError, ImportError):
            # Fall back to original method if adapter is not available
            pass
        
        # Original method as fallback
        if not self.connector_class:
            if not self.load_connector():
                return False
        
        try:
            # Create connector instance
            self.connector = self.connector_class()
            
            # Attach orchestrator if provided
            if orchestrator and hasattr(self.connector, 'attach_orchestrator'):
                self.connector.attach_orchestrator(orchestrator)
            
            logger.info("Successfully created connector instance")
            return True
        except Exception as e:
            logger.error(f"Failed to create connector instance: {e}")
            return False
    
    def patch_connector_process_file(self):
        """
        Patch the connector's process_file method if it doesn't exist.
        
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.connector:
            logger.error("No connector instance to patch")
            return False
        
        # Check if process_file method exists
        if hasattr(self.connector, 'process_file') and callable(getattr(self.connector, 'process_file')):
            logger.info("Connector already has process_file method")
            return True
        
        try:
            # Define process_file method
            def process_file(self, file_path):
                """
                Process a file using the MoA agents.
                
                Args:
                    file_path (str): Path to the file to process
                    
                Returns:
                    dict: Processing result
                """
                logger.info(f"Processing file: {file_path}")
                
                # Check if file exists
                if not os.path.exists(file_path):
                    logger.error(f"File not found: {file_path}")
                    return {"success": False, "error": f"File not found: {file_path}"}
                
                # Read the file content
                try:
                    with open(file_path, 'r') as f:
                        content = f.read()
                except Exception as e:
                    logger.error(f"Error reading file {file_path}: {e}")
                    return {"success": False, "error": str(e)}
                
                # Process the file with each agent
                results = []
                for agent in self.agents:
                    try:
                        result = agent.process(content, file_path)
                        results.append({"agent": agent.__class__.__name__, "result": result})
                    except Exception as e:
                        logger.error(f"Error processing file with {agent.__class__.__name__}: {e}")
                        results.append({"agent": agent.__class__.__name__, "error": str(e)})
                
                # If orchestrator is attached, enhance evolution
                if hasattr(self, 'orchestrator') and self.orchestrator:
                    try:
                        # Try to call enhance_evolution
                        if hasattr(self, 'enhance_evolution') and callable(getattr(self, 'enhance_evolution')):
                            self.enhance_evolution(file_path)
                        # Fall back to evolve_code if enhance_evolution doesn't exist
                        elif hasattr(self, 'evolve_code') and callable(getattr(self, 'evolve_code')):
                            self.evolve_code(file_path)
                    except Exception as e:
                        logger.error(f"Error enhancing evolution: {e}")
                
                return {"success": True, "results": results, "file": file_path}
            
            # Attach the method to the connector
            import types
            self.connector.process_file = types.MethodType(process_file, self.connector)
            
            logger.info("Successfully patched connector with process_file method")
            return True
        except Exception as e:
            logger.error(f"Failed to patch connector: {e}")
            return False
    
    def initialize(self, orchestrator=None):
        """
        Initialize the MoA integration.
        
        Args:
            orchestrator: Optional orchestrator instance
            
        Returns:
            tuple: (success, connector, agents)
        """
        # Load agent modules
        if not self.load_agent_modules():
            return False, None, []
        
        # Load connector
        if not self.load_connector():
            return False, None, []
        
        # Create agents
        if not self.create_agents():
            return False, None, []
        
        # Create connector
        if not self.create_connector(orchestrator):
            return False, None, []
        
        # Patch connector
        if not self.patch_connector_process_file():
            return False, None, []
        
        logger.info("MoA integration successfully initialized")
        return True, self.connector, self.agents

def initialize_moa_integration(orchestrator=None):
    """
    Initialize the MoA integration.
    
    Args:
        orchestrator: Optional orchestrator instance
        
    Returns:
        tuple: (success, connector, agents)
    """
    fix = QuantumMoAIntegrationFix()
    return fix.initialize(orchestrator)

# Example usage
if __name__ == "__main__":
    success, connector, agents = initialize_moa_integration()
    if success:
        print(f"MoA integration successfully initialized with {len(agents)} agents")
    else:
        print("Failed to initialize MoA integration")
