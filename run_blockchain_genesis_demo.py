#!/usr/bin/env python3
"""
Quantum Blockchain Genesis Demo
------------------------------

This script demonstrates the integration of blockchain genesis storage
with the quantum orchestrator system. It showcases:

1. Storing system components on the blockchain
2. Verifying system integrity against blockchain references
3. Healing system components using blockchain references
4. Setting up automatic blockchain backups

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import sys
import time
import json
import logging
import datetime
import argparse
from typing import Dict, Any, List

# Import quantum modules
from quantum_blockchain_genesis import QuantumBlockchainGenesis
from quantum_blockchain_connector import QuantumOrchestratorBlockchainIntegration

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("BlockchainGenesisDemo")

# Phi-harmonic constants
PHI = 1.618034
PHI_POWERS = {
    "φ": 1.618034,
    "φ²": 2.618034,
    "φ³": 4.236068,
    "φ⁷·⁵": 36.932381
}
TARGET_COHERENCE = PHI_POWERS["φ⁷·⁵"] / 10  # φ⁷·⁵/10 ≈ 3.693238


def create_demo_file(file_path: str, content: str = None) -> bool:
    """
    Create a demo file for testing.
    
    Args:
        file_path: Path to create the file
        content: Content to write to the file
        
    Returns:
        bool: True if file was created, False otherwise
    """
    try:
        # Create directory if not exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Default content if not provided
        if content is None:
            content = f"""#!/usr/bin/env python3
\"\"\"
Demo file for blockchain genesis testing.
Created at: {datetime.datetime.now()}
\"\"\"

# Phi-harmonic constants
PHI = 1.618034
PHI_POWERS = {{
    "φ": 1.618034,
    "φ²": 2.618034,
    "φ³": 4.236068,
    "φ⁷·⁵": 36.932381
}}
TARGET_COHERENCE = PHI_POWERS["φ⁷·⁵"] / 10  # φ⁷·⁵/10 ≈ 3.693238

def calculate_coherence(value):
    \"\"\"Calculate coherence of a value.\"\"\"
    return (value * PHI) % TARGET_COHERENCE

def main():
    \"\"\"Main function.\"\"\"
    print(f"Demo file for blockchain genesis testing")
    print(f"Target coherence: {TARGET_COHERENCE}")
    print(f"Current coherence: {calculate_coherence(42)}")

if __name__ == "__main__":
    main()
"""
        
        # Write file
        with open(file_path, 'w') as f:
            f.write(content)
        
        logger.info(f"Created demo file at {file_path}")
        return True
    except Exception as e:
        logger.error(f"Error creating demo file: {e}")
        return False


def modify_file(file_path: str) -> bool:
    """
    Modify a file to simulate tampering.
    
    Args:
        file_path: Path to the file to modify
        
    Returns:
        bool: True if file was modified, False otherwise
    """
    try:
        # Read file
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Modify content
        modified_content = content.replace("TARGET_COHERENCE", "MODIFIED_COHERENCE")
        
        # Write modified content
        with open(file_path, 'w') as f:
            f.write(modified_content)
        
        logger.info(f"Modified file at {file_path}")
        return True
    except Exception as e:
        logger.error(f"Error modifying file: {e}")
        return False


def run_demo():
    """Run the blockchain genesis demo."""
    logger.info("Starting Quantum Blockchain Genesis Demo")
    
    # Create demo directory
    demo_dir = "blockchain_demo"
    os.makedirs(demo_dir, exist_ok=True)
    
    # Create demo files
    demo_files = [
        os.path.join(demo_dir, "quantum_demo_orchestrator.py"),
        os.path.join(demo_dir, "quantum_demo_neural_bridge.py"),
        os.path.join(demo_dir, "quantum_demo_healing.py")
    ]
    
    for file_path in demo_files:
        create_demo_file(file_path)
    
    # Initialize blockchain integration
    integration = QuantumOrchestratorBlockchainIntegration(
        orchestrator_path=demo_files[0],
        core_files=demo_files
    )
    
    # Step 1: Backup system to blockchain
    logger.info("Step 1: Backing up system to blockchain")
    reference_id = integration.backup_orchestrator({
        "demo": True,
        "timestamp": time.time(),
        "phi_coherence": TARGET_COHERENCE
    })
    
    if not reference_id:
        logger.error("Failed to backup system to blockchain")
        return False
    
    logger.info(f"System backed up with reference ID: {reference_id}")
    
    # Step 2: Verify system integrity
    logger.info("Step 2: Verifying system integrity")
    verification = integration.verify_orchestrator(reference_id)
    
    if verification["verified"]:
        logger.info("System integrity verified")
    else:
        logger.error("System integrity verification failed")
        return False
    
    # Step 3: Modify a file to simulate tampering
    logger.info("Step 3: Modifying a file to simulate tampering")
    modify_file(demo_files[0])
    
    # Step 4: Verify system integrity again
    logger.info("Step 4: Verifying system integrity after tampering")
    verification = integration.verify_orchestrator(reference_id)
    
    if not verification["verified"]:
        logger.info("Tampering detected as expected")
    else:
        logger.error("Failed to detect tampering")
        return False
    
    # Step 5: Heal system from blockchain
    logger.info("Step 5: Healing system from blockchain")
    healing = integration.heal_orchestrator(reference_id)
    
    if healing["healed"]:
        logger.info("System healed successfully")
    else:
        logger.error("System healing failed")
        return False
    
    # Step 6: Verify system integrity after healing
    logger.info("Step 6: Verifying system integrity after healing")
    verification = integration.verify_orchestrator(reference_id)
    
    if verification["verified"]:
        logger.info("System integrity verified after healing")
    else:
        logger.error("System integrity verification failed after healing")
        return False
    
    # Step 7: Setup automatic backup
    logger.info("Step 7: Setting up automatic backup")
    auto_setup = integration.setup_auto_backup(
        interval_hours=1.0,  # 1 hour interval for demo
        max_backups=3
    )
    
    if auto_setup["success"]:
        logger.info("Automatic backup setup successfully")
    else:
        logger.error("Automatic backup setup failed")
        return False
    
    # Step 8: Run automatic backup
    logger.info("Step 8: Running automatic backup")
    auto_backup = integration.run_auto_backup()
    
    if auto_backup["success"]:
        logger.info("Automatic backup created successfully")
    else:
        logger.info(f"No automatic backup created: {auto_backup.get('message', 'Unknown reason')}")
    
    # Step 9: Restore system to a new directory
    logger.info("Step 9: Restoring system to a new directory")
    restore_dir = os.path.join(demo_dir, "restored")
    restore = integration.restore_orchestrator(reference_id, restore_dir)
    
    if restore:
        logger.info(f"System restored to {restore_dir}")
    else:
        logger.error("System restoration failed")
        return False
    
    # Step 10: Verify restored system
    logger.info("Step 10: Verifying restored system files")
    for i, file_path in enumerate(demo_files):
        restored_path = os.path.join(restore_dir, os.path.basename(file_path))
        
        if os.path.exists(restored_path):
            logger.info(f"Verified restored file: {restored_path}")
        else:
            logger.error(f"Restored file not found: {restored_path}")
            return False
    
    logger.info("Quantum Blockchain Genesis Demo completed successfully")
    return True


def create_demo_report(success: bool):
    """
    Create a demo report.
    
    Args:
        success: Whether the demo was successful
    """
    report = {
        "timestamp": time.time(),
        "success": success,
        "phi_coherence": TARGET_COHERENCE,
        "demo_steps": [
            "Backup system to blockchain",
            "Verify system integrity",
            "Modify a file to simulate tampering",
            "Verify system integrity after tampering",
            "Heal system from blockchain",
            "Verify system integrity after healing",
            "Setup automatic backup",
            "Run automatic backup",
            "Restore system to a new directory",
            "Verify restored system files"
        ]
    }
    
    # Write report
    report_file = "blockchain_genesis_demo_report.json"
    try:
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Demo report written to {report_file}")
    except Exception as e:
        logger.error(f"Error writing demo report: {e}")


def create_markdown_documentation():
    """Create markdown documentation for the blockchain genesis integration."""
    documentation = """# Quantum Blockchain Genesis Integration

## Overview

The Quantum Blockchain Genesis Integration enables the QuantumAI system to store and retrieve critical system components on decentralized blockchain storage. This provides a robust mechanism for system self-preservation, recovery, and verification.

## Key Components

### 1. Quantum Blockchain Genesis (`quantum_blockchain_genesis.py`)

This module provides the core functionality for interacting with blockchain services:

- **Encryption**: Secures system data using phi-harmonic encryption
- **Quantum Fingerprinting**: Creates unique identifiers for system components
- **Blockchain Storage**: Interfaces with free blockchain services
- **Local Caching**: Maintains local copies for efficient retrieval

### 2. Quantum Blockchain Connector (`quantum_blockchain_connector.py`)

This module bridges the quantum orchestrator with blockchain storage:

- **System Backup**: Stores critical system components on the blockchain
- **System Restoration**: Recovers system components from blockchain references
- **Integrity Verification**: Validates system components against blockchain references
- **System Healing**: Repairs corrupted components using blockchain references
- **Automatic Backup**: Schedules regular system backups

## Phi-Harmonic Principles

The blockchain integration maintains phi-harmonic coherence (φ⁷·⁵/10 ≈ 3.693238) through:

- Phi-based encryption key derivation
- Quantum fingerprinting using phi transformations
- Coherence calculations for system components
- Phi-resonance measurements for integrity verification

## Usage Examples

### Backing Up System Components

```python
from quantum_blockchain_connector import QuantumOrchestratorBlockchainIntegration

# Initialize integration
integration = QuantumOrchestratorBlockchainIntegration(
    orchestrator_path="quantum_orchestrator.py",
    core_files=["quantum_neural_bridge.py", "quantum_healing_protocols.py"]
)

# Backup system
reference_id = integration.backup_orchestrator()
print(f"System backed up with reference ID: {reference_id}")
```

### Verifying System Integrity

```python
# Verify system integrity
verification = integration.verify_orchestrator(reference_id)

if verification["verified"]:
    print("System integrity verified")
else:
    print("System integrity verification failed")
    for file_path, file_status in verification["files"].items():
        if not file_status["verified"]:
            print(f"  - {file_path}: {file_status.get('error', 'Fingerprint mismatch')}")
```

### Healing System Components

```python
# Heal system components
healing = integration.heal_orchestrator(reference_id)

if healing["healed"]:
    print("System healed successfully")
    for file_path, file_status in healing["files"].items():
        if file_status.get("healed", False):
            print(f"  - Healed: {file_path}")
```

### Setting Up Automatic Backups

```python
# Setup automatic backups
auto_setup = integration.setup_auto_backup(
    interval_hours=24.0,  # Daily backups
    max_backups=7  # Keep one week of backups
)

if auto_setup["success"]:
    print(f"Automatic backups configured with reference ID: {auto_setup['reference_id']}")
```

## Command-Line Interface

The blockchain connector provides a command-line interface for common operations:

```bash
# Backup system
python quantum_blockchain_connector.py backup

# Restore system
python quantum_blockchain_connector.py restore --reference-id <ID>

# Verify system integrity
python quantum_blockchain_connector.py verify --reference-id <ID>

# Heal system
python quantum_blockchain_connector.py heal --reference-id <ID>

# Setup automatic backups
python quantum_blockchain_connector.py setup-auto --interval 24 --max-backups 7

# Run automatic backup
python quantum_blockchain_connector.py run-auto
```

## Integration with Quantum Orchestrator

The blockchain genesis integration enhances the quantum orchestrator with:

1. **Self-Preservation**: Maintains blockchain backups of critical components
2. **Tamper Detection**: Verifies system integrity using quantum fingerprints
3. **Self-Healing**: Repairs corrupted components from blockchain references
4. **Evolution Tracking**: Records system evolution across blockchain references
5. **Phi-Harmonic Coherence**: Maintains coherence through blockchain operations

This integration forms a critical component of the system's self-preservation and evolution capabilities, ensuring that the quantum orchestrator can recover from corruption and maintain phi-harmonic coherence across generations.
"""
    
    # Write documentation
    doc_file = "QUANTUM_BLOCKCHAIN_INTEGRATION.md"
    try:
        with open(doc_file, 'w') as f:
            f.write(documentation)
        
        logger.info(f"Documentation written to {doc_file}")
    except Exception as e:
        logger.error(f"Error writing documentation: {e}")


if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Quantum Blockchain Genesis Demo")
    parser.add_argument("--skip-demo", action="store_true", help="Skip running the demo")
    parser.add_argument("--create-docs", action="store_true", help="Create documentation")
    
    args = parser.parse_args()
    
    # Run demo
    if not args.skip_demo:
        success = run_demo()
        create_demo_report(success)
    
    # Create documentation
    if args.create_docs or args.skip_demo:
        create_markdown_documentation()
