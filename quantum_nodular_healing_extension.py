"""
Quantum Nodular Healing Extension

This module provides a non-invasive extension to enable distributed healing
across the quantum nodular network, connecting healing protocols with
specialized nodes while maintaining phi-harmonic coherence.

Created: 2025-07-17
Coherence: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import json
import logging
import uuid
import ast
from typing import Dict, Any, List, Optional, Tuple, Union

# Import core quantum modules
from quantum_orchestrator_healing_extension import QuantumOrchestratorHealingExtension
from quantum_nodular_adapter import QuantumNodularAdapter
from quantum_specialized_node_adapter import (
    QuantumComputationNodeAdapter,
    QuantumStorageNodeAdapter,
    QuantumBridgeNodeAdapter,
    QuantumEvolutionNodeAdapter
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('QuantumNodularHealing')

class QuantumNodularHealingExtension:
    """
    Extension class to enable distributed healing across the quantum nodular network.
    
    This class follows the phi-harmonic principles and maintains the modular "lego"
    architecture without modifying core files.
    """
    
    def __init__(
        self, 
        nodular_adapter: QuantumNodularAdapter,
        orchestrator_healing_extension: Optional[QuantumOrchestratorHealingExtension] = None,
        phi_coherence: float = 3.6932381
    ) -> None:
        """
        Initialize the Quantum Nodular Healing Extension.
        
        Args:
            nodular_adapter: The Quantum Nodular Adapter instance
            orchestrator_healing_extension: Optional Quantum Orchestrator Healing Extension
            phi_coherence: Target phi-harmonic coherence (default: φ⁷·⁵/10 ≈ 3.6932381)
        """
        self.nodular_adapter = nodular_adapter
        self.phi_coherence = phi_coherence
        self.extension_id = str(uuid.uuid4())
        
        # Create orchestrator healing extension if not provided
        if orchestrator_healing_extension is None:
            from quantum_orchestrator_healing_extension import create_orchestrator_healing_extension
            self.orchestrator_healing = create_orchestrator_healing_extension()
        else:
            self.orchestrator_healing = orchestrator_healing_extension
        
        # Initialize healing history
        self.healing_history = []
        
        logger.info(f"Quantum Nodular Healing Extension initialized with ID: {self.extension_id}")
    
    def heal_file(self, file_path: str) -> Dict[str, Any]:
        """
        Heal a file using the distributed nodular network.
        
        This method coordinates healing across specialized nodes:
        1. Computation Node: Analyzes and identifies issues
        2. Bridge Node: Connects healing protocols
        3. Evolution Node: Applies evolutionary healing
        4. Storage Node: Stores healing history
        
        Args:
            file_path: Path to the file to heal
            
        Returns:
            Dict containing healing results
        """
        logger.info(f"Healing file with nodular network: {file_path}")
        
        # Step 1: Analyze file with computation node
        computation_adapter = self.nodular_adapter.get_node_adapter("QuantumComputationNode")
        if computation_adapter:
            analysis_result = computation_adapter.process_file(file_path)
            coherence_before = analysis_result.get("coherence", self.phi_coherence)
        else:
            analysis_result = {"success": False, "error": "Computation node not found"}
            coherence_before = self.phi_coherence
        
        # Step 2: Apply orchestrator healing
        orchestrator_healing_result = self.orchestrator_healing.heal_file(file_path)
        
        # Step 3: Bridge healing protocols
        bridge_adapter = self.nodular_adapter.get_node_adapter("QuantumBridgeNode")
        if bridge_adapter:
            bridge_result = bridge_adapter.bridge_file(file_path)
        else:
            bridge_result = {"success": False, "error": "Bridge node not found"}
        
        # Step 4: Apply evolutionary healing
        evolution_adapter = self.nodular_adapter.get_node_adapter("QuantumEvolutionNode")
        if evolution_adapter:
            evolution_result = evolution_adapter.evolve_file(file_path)
        else:
            evolution_result = {"success": False, "error": "Evolution node not found"}
        
        # Step 5: Analyze file after healing
        if computation_adapter:
            post_analysis_result = computation_adapter.process_file(file_path)
            coherence_after = post_analysis_result.get("coherence", self.phi_coherence)
        else:
            post_analysis_result = {"success": False, "error": "Computation node not found"}
            coherence_after = self.phi_coherence
        
        # Calculate coherence improvement
        coherence_improvement = coherence_after - coherence_before
        phi_resonance = coherence_after / self.phi_coherence
        
        # Create healing report
        healing_report = {
            "file_path": file_path,
            "timestamp": self._get_timestamp(),
            "healing_id": str(uuid.uuid4()),
            "coherence_before": coherence_before,
            "coherence_after": coherence_after,
            "coherence_improvement": coherence_improvement,
            "phi_resonance": phi_resonance,
            "orchestrator_healing": orchestrator_healing_result,
            "nodular_healing": {
                "computation": analysis_result,
                "bridge": bridge_result,
                "evolution": evolution_result,
                "post_analysis": post_analysis_result
            },
            "healing_complete": orchestrator_healing_result.get("success", False)
        }
        
        # Add to healing history
        self.healing_history.append(healing_report)
        
        # Store healing report
        self._store_healing_report(healing_report)
        
        logger.info(f"File healing complete with coherence improvement: {coherence_improvement:.6f}")
        return healing_report
    
    def _store_healing_report(self, healing_report: Dict[str, Any]) -> None:
        """
        Store the healing report using the storage node.
        
        Args:
            healing_report: The healing report to store
        """
        # Create healing report file
        file_name = os.path.basename(healing_report["file_path"])
        healing_report_path = f"quantum_healing/{file_name}.healing.json"
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(healing_report_path), exist_ok=True)
        
        # Write healing report
        with open(healing_report_path, "w") as f:
            json.dump(healing_report, f, indent=2)
        
        # Store with storage node
        storage_adapter = self.nodular_adapter.get_node_adapter("QuantumStorageNode")
        if storage_adapter:
            storage_adapter.store_file(healing_report_path)
            logger.info(f"Healing report stored: {healing_report_path}")
        else:
            logger.warning("Storage node not found, healing report not stored")
    
    def _get_timestamp(self) -> str:
        """
        Get current timestamp in ISO format.
        
        Returns:
            Timestamp string
        """
        from datetime import datetime
        return datetime.now().isoformat()
    
    def analyze_healing_history(self) -> Dict[str, Any]:
        """
        Analyze the healing history to identify patterns and improvements.
        
        Returns:
            Dict containing analysis results
        """
        if not self.healing_history:
            return {"success": False, "error": "No healing history available"}
        
        # Calculate average coherence improvement
        coherence_improvements = [
            report.get("coherence_improvement", 0)
            for report in self.healing_history
        ]
        avg_improvement = sum(coherence_improvements) / len(coherence_improvements)
        
        # Calculate phi-resonance
        phi_resonances = [
            report.get("phi_resonance", 1.0)
            for report in self.healing_history
        ]
        avg_resonance = sum(phi_resonances) / len(phi_resonances)
        
        # Count healing events by type
        healing_types = {}
        for report in self.healing_history:
            orchestrator_healing = report.get("orchestrator_healing", {})
            healing_type = orchestrator_healing.get("healing_type", "unknown")
            healing_types[healing_type] = healing_types.get(healing_type, 0) + 1
        
        return {
            "success": True,
            "healing_count": len(self.healing_history),
            "average_coherence_improvement": avg_improvement,
            "average_phi_resonance": avg_resonance,
            "healing_types": healing_types
        }


def create_nodular_healing_extension(
    nodular_adapter: Optional[QuantumNodularAdapter] = None,
    orchestrator_healing_extension: Optional[QuantumOrchestratorHealingExtension] = None
) -> QuantumNodularHealingExtension:
    """
    Factory function to create a Quantum Nodular Healing Extension.
    
    If nodular_adapter or orchestrator_healing_extension are not provided,
    new instances will be created.
    
    Args:
        nodular_adapter: Optional existing Quantum Nodular Adapter instance
        orchestrator_healing_extension: Optional existing Quantum Orchestrator Healing Extension
        
    Returns:
        QuantumNodularHealingExtension instance
    """
    # Create nodular adapter if not provided
    if nodular_adapter is None:
        from quantum_nodular_adapter import create_nodular_adapter
        nodular_adapter = create_nodular_adapter()
    
    # Create orchestrator healing extension if not provided
    if orchestrator_healing_extension is None:
        from quantum_orchestrator_healing_extension import create_orchestrator_healing_extension
        orchestrator_healing_extension = create_orchestrator_healing_extension()
    
    # Create and return extension
    return QuantumNodularHealingExtension(
        nodular_adapter=nodular_adapter,
        orchestrator_healing_extension=orchestrator_healing_extension
    )
