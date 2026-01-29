#!/usr/bin/env python3
"""
Quantum MoA Connector Adapter
----------------------------

This module provides an adapter for the QuantumMoAOrchestratorConnector to ensure
proper initialization with agents. It follows the 'lego' modular philosophy by
extending functionality without modifying core files.
"""

import os
import sys
import logging
import importlib
from typing import List, Dict, Any, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumMoAConnectorAdapter")

class QuantumMoAConnectorAdapter:
    """
    Adapter for the QuantumMoAOrchestratorConnector to ensure proper initialization with agents.
    """
    
    def __init__(self, agents=None, orchestrator=None):
        """
        Initialize the adapter with agents and optionally an orchestrator.
        
        Args:
            agents (list): List of agent instances
            orchestrator: Optional orchestrator instance
        """
        self.agents = agents or []
        self.orchestrator = orchestrator
        self.connector = None
        logger.info(f"Initialized QuantumMoAConnectorAdapter with {len(self.agents)} agents")
    
    def initialize_connector(self):
        """
        Initialize the connector with the agents.
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            # Try to import the connector
            from quantum_moa_orchestrator_connector import QuantumMoAOrchestratorConnector
            
            # Create connector instance based on its signature
            # Try different initialization approaches
            try:
                # Try with agents as a parameter
                self.connector = QuantumMoAOrchestratorConnector(agents=self.agents)
            except TypeError:
                try:
                    # Try with no parameters
                    self.connector = QuantumMoAOrchestratorConnector()
                    # Attach agents after initialization
                    if hasattr(self.connector, 'set_agents'):
                        self.connector.set_agents(self.agents)
                    else:
                        # Dynamically add agents attribute
                        setattr(self.connector, 'agents', self.agents)
                except Exception as e2:
                    logger.error(f"Failed to initialize connector without parameters: {e2}")
                    return False
            
            # Attach orchestrator if provided
            if self.orchestrator:
                if hasattr(self.connector, 'attach_orchestrator'):
                    self.connector.attach_orchestrator(self.orchestrator)
                else:
                    # Dynamically add orchestrator attribute
                    setattr(self.connector, 'orchestrator', self.orchestrator)
            
            # Add process_file method if it doesn't exist
            if not hasattr(self.connector, 'process_file') or not callable(getattr(self.connector, 'process_file')):
                self._add_process_file_method()
            
            logger.info("Successfully initialized QuantumMoAOrchestratorConnector")
            return True
        except ImportError as e:
            logger.error(f"Failed to import QuantumMoAOrchestratorConnector: {e}")
            return False
        except Exception as e:
            logger.error(f"Failed to initialize connector: {e}")
            return False
    
    def _add_process_file_method(self):
        """Add process_file method to the connector if it doesn't exist."""
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
        logger.info("Added process_file method to connector")
    
    def process_file(self, file_path):
        """
        Process a file using the connector.
        
        Args:
            file_path (str): Path to the file to process
            
        Returns:
            dict: Processing result
        """
        if not self.connector:
            if not self.initialize_connector():
                return {"success": False, "error": "Failed to initialize connector"}
        
        return self.connector.process_file(file_path)

def create_connector_with_agents(agents, orchestrator=None):
    """
    Create a connector with the given agents.
    
    Args:
        agents (list): List of agent instances
        orchestrator: Optional orchestrator instance
        
    Returns:
        tuple: (success, connector)
    """
    adapter = QuantumMoAConnectorAdapter(agents, orchestrator)
    success = adapter.initialize_connector()
    return success, adapter if success else None
