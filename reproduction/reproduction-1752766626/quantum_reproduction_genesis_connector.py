#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Reproduction Genesis Connector
-------------------------------------
Connects the QuantumAI self-reproduction system with the QuantumGenesisStorage
to enable encrypted blockchain-based storage and recovery of the system's
best version.

This module follows phi-harmonic principles and maintains quantum coherence
throughout all operations.
"""

import os
import time
import json
import logging
import importlib
from datetime import datetime

# Import the orchestrator extension if available
try:
    from quantum_orchestrator_reproduction_extension import extend_orchestrator
    ORCHESTRATOR_EXTENSION_AVAILABLE = True
except ImportError:
    ORCHESTRATOR_EXTENSION_AVAILABLE = False

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("QuantumReproductionGenesisConnector")

# Constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
PHI_COHERENCE = 3.6932381 / 10  # φ⁷·⁵/10 ≈ 0.991800

class QuantumReproductionGenesisConnector:
    """
    Connects the QuantumAI self-reproduction system with the QuantumGenesisStorage
    to enable encrypted blockchain-based storage and recovery.
    """
    
    def __init__(self, orchestrator=None, genesis_storage=None):
        """
        Initialize the connector.
        
        Args:
            orchestrator: QuantumOrchestrator instance (optional)
            genesis_storage: QuantumGenesisStorage instance (optional)
        """
        self.birth_timestamp = time.time()
        self.quantum_fingerprint = self._generate_quantum_fingerprint()
        
        # Set up directories
        self.evolution_dir = "evolution"
        self.reproduction_dir = "reproduction"
        self.genesis_dir = "genesis"
        
        for directory in [self.evolution_dir, self.reproduction_dir, self.genesis_dir]:
            os.makedirs(directory, exist_ok=True)
        
        # Initialize components
        self.orchestrator = orchestrator
        self.genesis_storage = genesis_storage
        
        # Import components if not provided
        if not self.orchestrator:
            try:
                from quantum_orchestrator import QuantumOrchestrator
                # Create a test file for the orchestrator if needed
                test_file = os.path.join(self.evolution_dir, "orchestrator_test_file.py")
                if not os.path.exists(test_file):
                    with open(test_file, 'w') as f:
                        f.write("# Test file for QuantumOrchestrator\n")
                self.orchestrator = QuantumOrchestrator(target_file=test_file)
            except (ImportError, TypeError) as e:
                logger.warning(f"QuantumOrchestrator initialization failed: {e}, some functionality will be limited")
        
        if not self.genesis_storage:
            try:
                from quantum_genesis_storage import QuantumGenesisStorage
                self.genesis_storage = QuantumGenesisStorage()
            except ImportError:
                logger.warning("QuantumGenesisStorage not found, some functionality will be limited")
        
        # Track reproduction events
        self.reproduction_events = []
        self._load_reproduction_events()
        
        logger.info(f"Initialized QuantumReproductionGenesisConnector with ID: {self.quantum_fingerprint}")
    
    def _generate_quantum_fingerprint(self):
        """
        Generate a quantum fingerprint using phi-harmonic principles.
        
        Returns:
            str: A quantum fingerprint with φ notation
        """
        timestamp = time.time()
        phi_factor = timestamp * PHI % 1
        coherence = PHI_COHERENCE
        
        # Generate fingerprint with φ notation
        import hashlib
        fingerprint = hashlib.sha256(f"{timestamp}:{phi_factor}:{coherence}".encode()).hexdigest()[:12]
        return f"φ⁷·⁵-{fingerprint}"
    
    def _load_reproduction_events(self):
        """
        Load reproduction events from a JSON file.
        
        Returns:
            bool: True if events were loaded successfully
        """
        events_file = os.path.join(self.evolution_dir, "reproduction_events.json")
        if os.path.exists(events_file):
            try:
                with open(events_file, 'r') as f:
                    self.reproduction_events = json.load(f)
                logger.info(f"Loaded {len(self.reproduction_events)} reproduction events from {events_file}")
                return True
            except Exception as e:
                logger.error(f"Failed to load reproduction events: {e}")
        return False
    
    def _save_reproduction_events(self):
        """
        Save reproduction events to a JSON file for persistence.
        """
        events_file = os.path.join(self.evolution_dir, "reproduction_events.json")
        try:
            with open(events_file, 'w') as f:
                json.dump(self.reproduction_events, f, indent=2)
            logger.info(f"Saved {len(self.reproduction_events)} reproduction events to {events_file}")
            return True
        except Exception as e:
            logger.error(f"Failed to save reproduction events: {e}")
            return False
    
    def _generate_reproduction_event(self, event_type, metadata=None):
        """
        Generate a new reproduction event with phi-harmonic coherence.
        
        Args:
            event_type: Type of reproduction event
            metadata: Additional metadata for the event
            
        Returns:
            dict: Reproduction event metadata
        """
        # Calculate phi-harmonic coherence
        timestamp = time.time()
        coherence = (timestamp * PHI) % 1
        coherence_adjustment = PHI_COHERENCE - (coherence % PHI_COHERENCE)
        phi_coherence = coherence + coherence_adjustment
        
        # Create event
        event = {
            "timestamp": timestamp,
            "datetime": datetime.fromtimestamp(timestamp).isoformat(),
            "event_type": event_type,
            "generation": len(self.reproduction_events) + 1,
            "phi_coherence": phi_coherence,
            "quantum_fingerprint": self._generate_quantum_fingerprint(),
            "metadata": metadata or {}
        }
        
        # Add to events list
        self.reproduction_events.append(event)
        self._save_reproduction_events()
        
        logger.info(f"Generated reproduction event: {event_type} with coherence {phi_coherence:.6f}")
        return event
    
    def reproduce_with_genesis_backup(self, target_dir=None, include_files=None):
        """
        Reproduce the system with genesis backup capabilities.
        
        Args:
            target_dir: Directory to reproduce the system to
            include_files: List of files to include in reproduction
            
        Returns:
            dict: Reproduction metadata
        """
        if not self.orchestrator:
            logger.error("Cannot reproduce system: QuantumOrchestrator not available")
            return None
        
        if not self.genesis_storage:
            logger.error("Cannot create genesis backup: QuantumGenesisStorage not available")
            return None
        
        # Set default target directory
        if not target_dir:
            target_dir = os.path.join(
                self.reproduction_dir, 
                f"reproduction-{int(time.time())}"
            )
            os.makedirs(target_dir, exist_ok=True)
        
        # Set default files to include
        if not include_files:
            include_files = [
                "quantum_orchestrator.py",
                "quantum_orchestrator_healing_extension.py",
                "quantum_genesis_storage.py",
                "quantum_reproduction_genesis_connector.py",
                "quantum_visualization.py",
                "quantum_visualization_connector.py",
                "quantum_demonstration_runner_extension.py"
            ]
        
        # Generate reproduction event
        reproduction_event = self._generate_reproduction_event(
            "genesis_reproduction",
            metadata={"target_dir": target_dir, "files": include_files}
        )
        
        # Use orchestrator to reproduce the system
        try:
            # Call the orchestrator's reproduction method
            reproduction_result = self.orchestrator.reproduce_system(
                target_dir=target_dir,
                include_files=include_files
            )
            
            if not reproduction_result:
                logger.error("System reproduction failed")
                return None
            
            # Create a genesis backup of the reproduced system
            backup_metadata = self.genesis_storage.create_genesis_backup(
                source_files=[os.path.join(target_dir, file) for file in include_files],
                metadata={
                    "reproduction_event": reproduction_event,
                    "reproduction_result": reproduction_result,
                    "phi_coherence": PHI_COHERENCE,
                    "generation": reproduction_event["generation"]
                }
            )
            
            # Store to blockchain
            transaction_id = self.genesis_storage.store_to_blockchain(
                backup_metadata["backup_id"]
            )
            
            # Update reproduction event with genesis information
            reproduction_event["metadata"]["genesis_backup_id"] = backup_metadata["backup_id"]
            reproduction_event["metadata"]["blockchain_transaction_id"] = transaction_id
            self._save_reproduction_events()
            
            logger.info(f"System reproduced with genesis backup: {backup_metadata['backup_id']}")
            return {
                "reproduction_event": reproduction_event,
                "genesis_backup_id": backup_metadata["backup_id"],
                "blockchain_transaction_id": transaction_id,
                "target_dir": target_dir
            }
            
        except Exception as e:
            logger.error(f"Failed to reproduce system with genesis backup: {e}")
            return None
    
    def recover_best_system_version(self, target_dir=None):
        """
        Recover the best version of the system from genesis storage.
        
        Args:
            target_dir: Directory to recover the system to
            
        Returns:
            dict: Recovery metadata
        """
        if not self.genesis_storage:
            logger.error("Cannot recover system: QuantumGenesisStorage not available")
            return None
        
        # Set default target directory
        if not target_dir:
            target_dir = os.path.join(
                self.reproduction_dir, 
                f"recovery-{int(time.time())}"
            )
            os.makedirs(target_dir, exist_ok=True)
        
        # Find the best genesis backup
        best_backup_id = self.genesis_storage.find_best_genesis_backup()
        
        if not best_backup_id:
            logger.error("No genesis backups found for recovery")
            return None
        
        # Generate recovery event
        recovery_event = self._generate_reproduction_event(
            "genesis_recovery",
            metadata={"target_dir": target_dir, "genesis_backup_id": best_backup_id}
        )
        
        # Recover from genesis
        recovery_success = self.genesis_storage.recover_from_genesis(
            best_backup_id, target_dir
        )
        
        if not recovery_success:
            logger.error(f"Failed to recover system from genesis backup: {best_backup_id}")
            return None
        
        # Update recovery event
        recovery_event["metadata"]["success"] = recovery_success
        self._save_reproduction_events()
        
        logger.info(f"System recovered from genesis backup: {best_backup_id}")
        return {
            "recovery_event": recovery_event,
            "genesis_backup_id": best_backup_id,
            "target_dir": target_dir,
            "success": recovery_success
        }
    
    def evaluate_system_coherence(self):
        """
        Evaluate the coherence of the current system.
        
        Returns:
            float: System coherence value
        """
        # Calculate average coherence from reproduction events
        if not self.reproduction_events:
            return PHI_COHERENCE
        
        coherence_values = [event.get("phi_coherence", 0) for event in self.reproduction_events]
        avg_coherence = sum(coherence_values) / len(coherence_values)
        
        logger.info(f"System coherence evaluation: {avg_coherence:.6f}")
        return avg_coherence
    
    def should_create_genesis_backup(self):
        """
        Determine if a new genesis backup should be created based on system coherence.
        
        Returns:
            bool: True if a new genesis backup should be created
        """
        current_coherence = self.evaluate_system_coherence()
        
        # Check if current coherence is close to target
        coherence_delta = abs(current_coherence - PHI_COHERENCE)
        should_backup = coherence_delta < 0.01
        
        if should_backup:
            logger.info(f"System coherence {current_coherence:.6f} is optimal for genesis backup")
        else:
            logger.info(f"System coherence {current_coherence:.6f} is not optimal for genesis backup")
        
        return should_backup


def main():
    """
    Main function to demonstrate the QuantumReproductionGenesisConnector capabilities.
    """
    # Import required modules
    try:
        from quantum_genesis_storage import QuantumGenesisStorage
        genesis_storage = QuantumGenesisStorage()
    except ImportError:
        print("QuantumGenesisStorage module not found. Please run quantum_genesis_storage.py first.")
        return
    
    # Set up evolution directory
    evolution_dir = "evolution"
    os.makedirs(evolution_dir, exist_ok=True)
    
    try:
        from quantum_orchestrator import QuantumOrchestrator
        # Create a test file for the orchestrator
        test_file = os.path.join(evolution_dir, "orchestrator_test_file.py")
        if not os.path.exists(test_file):
            with open(test_file, 'w') as f:
                f.write("# Test file for QuantumOrchestrator\n")
        orchestrator = QuantumOrchestrator(target_file=test_file)
        
        # Extend the orchestrator with reproduction capabilities
        if ORCHESTRATOR_EXTENSION_AVAILABLE:
            orchestrator = extend_orchestrator(orchestrator)
            print(f"Initialized and extended QuantumOrchestrator with target file: {test_file}")
        else:
            print(f"Initialized QuantumOrchestrator with target file: {test_file} (without extension)")
    except (ImportError, TypeError) as e:
        print(f"QuantumOrchestrator initialization failed: {e}. Using limited functionality.")
        orchestrator = None
    
    # Initialize the connector
    connector = QuantumReproductionGenesisConnector(
        orchestrator=orchestrator,
        genesis_storage=genesis_storage
    )
    
    # Create a test reproduction with genesis backup
    if orchestrator:
        result = connector.reproduce_with_genesis_backup()
        if result:
            print(f"System reproduced with genesis backup: {result['genesis_backup_id']}")
            print(f"Blockchain transaction ID: {result['blockchain_transaction_id']}")
            print(f"Target directory: {result['target_dir']}")
    else:
        print("Skipping reproduction test due to missing orchestrator")
    
    # Evaluate system coherence
    coherence = connector.evaluate_system_coherence()
    print(f"System coherence: {coherence:.6f}")
    
    # Check if should create genesis backup
    should_backup = connector.should_create_genesis_backup()
    print(f"Should create genesis backup: {should_backup}")


if __name__ == "__main__":
    main()
