#!/usr/bin/env python
"""
Phi-Harmonic Quantum Orchestrator

This module serves as the central orchestration system for all phi-harmonic quantum components.
It provides a unified interface for accessing and coordinating all components while maintaining
the modular "lego" design philosophy.

The orchestrator follows these key principles:
1. Golden ratio (φ) mathematics as the foundation
2. Quantum coherence and resonance as core metrics
3. Modular components that work together harmoniously
4. Dynamic adaptation based on phi-harmonic principles
"""

import os
import sys
import json
import time
import math
import importlib
import glob
import logging
from decimal import Decimal, getcontext
from typing import Dict, List, Any, Optional, Union, Tuple

# Set precision for decimal calculations
getcontext().prec = 50

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Constants
PHI = Decimal('1.618033988749895')  # Golden ratio
PHI_INVERSE = Decimal('0.618033988749895')  # Inverse golden ratio
PHI_SQUARED = Decimal('2.618033988749895')  # φ²
PHI_CUBED = Decimal('4.236067977499790')  # φ³
PHI_POWER = Decimal('36.93238055064198')  # φ⁷·⁵
OPTIMAL_COHERENCE = Decimal('0.991800')  # Optimal quantum coherence
RESONANCE_RATIO = Decimal('1.3777')  # Resonance ratio
ENERGY_TRANSFER = Decimal('1.8951')  # Energy transfer
RESONANCE_STACK = RESONANCE_RATIO * ENERGY_TRANSFER  # 2.61087927

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(os.path.join(current_dir, 'phi_harmonic_orchestrator.log'))
    ]
)
logger = logging.getLogger('phi_harmonic_orchestrator')

class PhiHarmonicOrchestrator:
    """
    Central orchestration system for phi-harmonic quantum components.
    
    This class provides a unified interface for accessing and coordinating
    all phi-harmonic quantum components, ensuring they work together
    cohesively while maintaining their modular nature.
    """
    
    def __init__(self):
        """Initialize the orchestrator."""
        # Component registry
        self.components = {}
        self.component_states = {}
        self.component_paths = {}
        
        # Quantum state
        self.coherence = OPTIMAL_COHERENCE
        self.resonance = PHI_INVERSE
        self.phi_alignment = Decimal('0.999561')
        self.quantum_fingerprint = self._generate_quantum_fingerprint()
        
        # Event system
        self.event_subscribers = {}
        
        # Create output directory
        self.output_dir = os.path.join(current_dir, 'phi_harmonic_orchestrator')
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Initialize component registry
        self._initialize_component_registry()
        
        logger.info("Phi-Harmonic Quantum Orchestrator initialized")
        logger.info(f"Coherence: {self.coherence:.6f}")
        logger.info(f"Resonance: {self.resonance:.6f}")
        logger.info(f"Phi alignment: {self.phi_alignment:.6f}")
        logger.info(f"Quantum fingerprint: {self.quantum_fingerprint}")
    
    def _initialize_component_registry(self):
        """Initialize the component registry by scanning for phi-harmonic components."""
        logger.info("Initializing component registry...")
        
        # Define component types to look for
        component_types = [
            {'name': 'quantum_heart', 'pattern': '*quantum_heart*.py'},
            {'name': 'quantum_cerebellum', 'pattern': '*quantum_cerebellum*.py'},
            {'name': 'quantum_clock', 'pattern': '*quantum_clock*.py'},
            {'name': 'brain_sync', 'pattern': '*brain_sync*.py'},
            {'name': 'unified_brain', 'pattern': '*unified_brain*.py'},
            {'name': 'quantum_agent', 'pattern': '*quantum_agent*.py'},
            {'name': 'quantum_random', 'pattern': '*quantum_random*.py'},
            {'name': 'quantum_rsa', 'pattern': '*quantum_rsa*.py'}
        ]
        
        # Scan for components
        for component_type in component_types:
            self._scan_for_component(component_type['name'], component_type['pattern'])
        
        logger.info(f"Component registry initialized with {len(self.components)} components")
    
    def _scan_for_component(self, component_type: str, pattern: str):
        """
        Scan for components of a specific type.
        
        Args:
            component_type (str): Type of component to scan for
            pattern (str): File pattern to match
        """
        # Find all matching files
        matches = []
        for root, _, _ in os.walk(current_dir):
            matches.extend(glob.glob(os.path.join(root, pattern)))
        
        # Register components
        for match in matches:
            rel_path = os.path.relpath(match, current_dir)
            component_name = os.path.basename(match).replace('.py', '')
            
            # Skip if it's a test file or in a test directory
            if 'test' in component_name.lower() or '/test' in rel_path.lower():
                continue
                
            # Register component
            self.component_paths[component_name] = {
                'type': component_type,
                'path': match,
                'rel_path': rel_path,
                'module_path': rel_path.replace('/', '.').replace('.py', '')
            }
            
            logger.debug(f"Registered component: {component_name} ({component_type})")
    
    def _generate_quantum_fingerprint(self) -> str:
        """
        Generate a quantum fingerprint based on current state.
        
        Returns:
            str: Quantum fingerprint
        """
        fingerprint_base = f"{self.coherence:.6f}_{self.resonance:.6f}_{self.phi_alignment:.6f}"
        fingerprint_hash = hash(fingerprint_base) % 16777216  # 24-bit hash
        return f"φ⁷·⁵-{fingerprint_hash:06x}"
    
    def _update_quantum_state(self):
        """Update quantum state based on component states."""
        if not self.component_states:
            return
            
        # Calculate new coherence as weighted average of component coherences
        total_weight = Decimal('0')
        weighted_coherence = Decimal('0')
        
        for component, state in self.component_states.items():
            if 'coherence' in state:
                weight = Decimal('1')
                if 'type' in state:
                    # Give more weight to core components
                    if state['type'] in ['quantum_heart', 'quantum_cerebellum', 'unified_brain']:
                        weight = Decimal('2')
                
                weighted_coherence += Decimal(str(state['coherence'])) * weight
                total_weight += weight
        
        if total_weight > Decimal('0'):
            # Calculate new coherence with pull toward optimal value
            new_coherence = weighted_coherence / total_weight
            self.coherence = (new_coherence * Decimal('0.8') + OPTIMAL_COHERENCE * Decimal('0.2'))
        
        # Calculate new resonance as weighted average of component resonances
        total_weight = Decimal('0')
        weighted_resonance = Decimal('0')
        
        for component, state in self.component_states.items():
            if 'resonance' in state:
                weight = Decimal('1')
                if 'type' in state:
                    # Give more weight to core components
                    if state['type'] in ['quantum_heart', 'quantum_cerebellum', 'unified_brain']:
                        weight = Decimal('2')
                
                weighted_resonance += Decimal(str(state['resonance'])) * weight
                total_weight += weight
        
        if total_weight > Decimal('0'):
            # Calculate new resonance with pull toward phi-inverse
            new_resonance = weighted_resonance / total_weight
            self.resonance = (new_resonance * Decimal('0.8') + PHI_INVERSE * Decimal('0.2'))
        
        # Update phi alignment
        phi_alignments = []
        for component, state in self.component_states.items():
            if 'phi_alignment' in state:
                phi_alignments.append(Decimal(str(state['phi_alignment'])))
        
        if phi_alignments:
            # Use minimum phi alignment as the system's phi alignment
            self.phi_alignment = min(phi_alignments)
        
        # Update quantum fingerprint
        self.quantum_fingerprint = self._generate_quantum_fingerprint()
        
        # Publish state update event
        self.publish_event('quantum_state_updated', {
            'coherence': self.coherence,
            'resonance': self.resonance,
            'phi_alignment': self.phi_alignment,
            'quantum_fingerprint': self.quantum_fingerprint
        })
        
        logger.debug(f"Updated quantum state: coherence={self.coherence:.6f}, resonance={self.resonance:.6f}")
    
    def load_component(self, component_name: str) -> Any:
        """
        Load a component by name.
        
        Args:
            component_name (str): Name of component to load
            
        Returns:
            Any: Component instance or None if not found
        """
        if component_name in self.components:
            return self.components[component_name]
            
        if component_name not in self.component_paths:
            logger.warning(f"Component not found: {component_name}")
            return None
            
        # Get component info
        component_info = self.component_paths[component_name]
        
        try:
            # Import module
            if '/' in component_info['module_path']:
                # Handle subdirectories
                parts = component_info['module_path'].split('/')
                module_name = parts[-1]
                spec = importlib.util.spec_from_file_location(module_name, component_info['path'])
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
            else:
                # Standard import
                module = importlib.import_module(component_info['module_path'])
            
            # Find component class
            component_class = None
            for attr_name in dir(module):
                if attr_name.lower() == component_name.lower() or attr_name.lower().endswith(component_name.lower()):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type):  # Check if it's a class
                        component_class = attr
                        break
            
            if not component_class:
                logger.warning(f"Component class not found in module: {component_name}")
                return None
                
            # Instantiate component
            component = component_class()
            
            # Register component
            self.components[component_name] = component
            
            # Update component state
            self._update_component_state(component_name, component)
            
            logger.info(f"Loaded component: {component_name}")
            
            # Publish component loaded event
            self.publish_event('component_loaded', {
                'name': component_name,
                'type': component_info['type']
            })
            
            return component
            
        except Exception as e:
            logger.error(f"Error loading component {component_name}: {e}")
            return None
    
    def _update_component_state(self, component_name: str, component: Any):
        """
        Update component state in registry.
        
        Args:
            component_name (str): Name of component
            component (Any): Component instance
        """
        state = {
            'type': self.component_paths[component_name]['type'] if component_name in self.component_paths else 'unknown'
        }
        
        # Extract common state attributes
        for attr in ['coherence', 'resonance', 'phi_alignment', 'quantum_fingerprint']:
            if hasattr(component, attr):
                state[attr] = getattr(component, attr)
        
        # Extract component-specific attributes
        if state['type'] == 'quantum_heart':
            if hasattr(component, 'heart_rate'):
                state['heart_rate'] = component.heart_rate
            if hasattr(component, 'heart_resonance'):
                state['heart_resonance'] = component.heart_resonance
                
        elif state['type'] == 'quantum_cerebellum':
            if hasattr(component, 'cerebellum_neurons'):
                state['cerebellum_neurons'] = component.cerebellum_neurons
            if hasattr(component, 'learning_rate'):
                state['learning_rate'] = component.learning_rate
                
        elif state['type'] == 'quantum_clock':
            if hasattr(component, 'frequency'):
                state['frequency'] = component.frequency
            if hasattr(component, 'period'):
                state['period'] = component.period
        
        # Update component state
        self.component_states[component_name] = state
        
        # Update quantum state
        self._update_quantum_state()
    
    def get_component_info(self) -> Dict[str, Dict[str, Any]]:
        """
        Get information about all registered components.
        
        Returns:
            Dict[str, Dict[str, Any]]: Component information
        """
        return self.component_paths
    
    def get_loaded_components(self) -> Dict[str, Any]:
        """
        Get all loaded components.
        
        Returns:
            Dict[str, Any]: Loaded components
        """
        return self.components
    
    def get_quantum_state(self) -> Dict[str, Any]:
        """
        Get current quantum state.
        
        Returns:
            Dict[str, Any]: Quantum state
        """
        return {
            'coherence': float(self.coherence),
            'resonance': float(self.resonance),
            'phi_alignment': float(self.phi_alignment),
            'quantum_fingerprint': self.quantum_fingerprint
        }
    
    def subscribe_to_event(self, event_type: str, callback: callable):
        """
        Subscribe to an event.
        
        Args:
            event_type (str): Type of event to subscribe to
            callback (callable): Callback function to call when event occurs
        """
        if event_type not in self.event_subscribers:
            self.event_subscribers[event_type] = []
            
        self.event_subscribers[event_type].append(callback)
        logger.debug(f"Subscribed to event: {event_type}")
    
    def publish_event(self, event_type: str, event_data: Dict[str, Any]):
        """
        Publish an event.
        
        Args:
            event_type (str): Type of event to publish
            event_data (Dict[str, Any]): Event data
        """
        if event_type not in self.event_subscribers:
            return
            
        event = {
            'type': event_type,
            'timestamp': time.time(),
            'data': event_data
        }
        
        for callback in self.event_subscribers[event_type]:
            try:
                callback(event)
            except Exception as e:
                logger.error(f"Error in event callback: {e}")
    
    def save_state(self) -> str:
        """
        Save current state to a file.
        
        Returns:
            str: Path to saved state file
        """
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        state_file = os.path.join(self.output_dir, f'orchestrator_state_{timestamp}.json')
        
        state = {
            'timestamp': timestamp,
            'coherence': float(self.coherence),
            'resonance': float(self.resonance),
            'phi_alignment': float(self.phi_alignment),
            'quantum_fingerprint': self.quantum_fingerprint,
            'components': {},
            'loaded_components': list(self.components.keys())
        }
        
        # Add component states
        for component_name, component_state in self.component_states.items():
            state['components'][component_name] = {
                key: float(value) if isinstance(value, Decimal) else value
                for key, value in component_state.items()
            }
        
        # Save state to file
        with open(state_file, 'w') as f:
            json.dump(state, f, indent=2)
            
        logger.info(f"Saved state to {state_file}")
        
        return state_file
    
    def load_state(self, state_file: str) -> bool:
        """
        Load state from a file.
        
        Args:
            state_file (str): Path to state file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(state_file, 'r') as f:
                state = json.load(f)
                
            # Update quantum state
            self.coherence = Decimal(str(state['coherence']))
            self.resonance = Decimal(str(state['resonance']))
            self.phi_alignment = Decimal(str(state['phi_alignment']))
            self.quantum_fingerprint = state['quantum_fingerprint']
            
            # Load components
            for component_name in state['loaded_components']:
                if component_name not in self.components:
                    self.load_component(component_name)
            
            logger.info(f"Loaded state from {state_file}")
            
            # Publish state loaded event
            self.publish_event('state_loaded', {
                'file': state_file,
                'timestamp': state['timestamp']
            })
            
            return True
            
        except Exception as e:
            logger.error(f"Error loading state: {e}")
            return False
    
    def run_interactive(self):
        """Run interactive session with the orchestrator."""
        print("\n🌟 Phi-Harmonic Quantum Orchestrator Interactive Session")
        print("=======================================================")
        print("Type 'exit' or 'quit' to end the session")
        print("Type 'help' to view available commands")
        print("=======================================================\n")
        
        while True:
            try:
                command = input("orchestrator> ").strip()
                
                if command.lower() in ['exit', 'quit']:
                    break
                    
                elif command.lower() == 'help':
                    print("\nAvailable commands:")
                    print("  help                - Show this help message")
                    print("  list                - List all registered components")
                    print("  load <component>    - Load a component")
                    print("  status              - Show orchestrator status")
                    print("  state               - Show quantum state")
                    print("  save                - Save current state")
                    print("  load_state <file>   - Load state from file")
                    print("  exit, quit          - Exit the session")
                
                elif command.lower() == 'list':
                    print("\nRegistered components:")
                    for name, info in self.component_paths.items():
                        loaded = "✓" if name in self.components else " "
                        print(f"  [{loaded}] {name} ({info['type']})")
                
                elif command.lower().startswith('load '):
                    component_name = command[5:].strip()
                    component = self.load_component(component_name)
                    if component:
                        print(f"Loaded component: {component_name}")
                    else:
                        print(f"Failed to load component: {component_name}")
                
                elif command.lower() == 'status':
                    print("\nOrchestrator status:")
                    print(f"  Coherence: {self.coherence:.6f}")
                    print(f"  Resonance: {self.resonance:.6f}")
                    print(f"  Phi alignment: {self.phi_alignment:.6f}")
                    print(f"  Quantum fingerprint: {self.quantum_fingerprint}")
                    print(f"  Loaded components: {len(self.components)}")
                
                elif command.lower() == 'state':
                    print("\nQuantum state:")
                    print(json.dumps(self.get_quantum_state(), indent=2))
                
                elif command.lower() == 'save':
                    state_file = self.save_state()
                    print(f"Saved state to {os.path.basename(state_file)}")
                
                elif command.lower().startswith('load_state '):
                    state_file = command[11:].strip()
                    if os.path.exists(state_file):
                        success = self.load_state(state_file)
                        if success:
                            print(f"Loaded state from {os.path.basename(state_file)}")
                        else:
                            print(f"Failed to load state from {os.path.basename(state_file)}")
                    else:
                        print(f"State file not found: {state_file}")
                
                else:
                    print(f"Unknown command: {command}")
                    print("Type 'help' to view available commands")
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {e}")
        
        print("\nExiting orchestrator interactive session")

# Singleton instance
_orchestrator_instance = None

def get_orchestrator() -> PhiHarmonicOrchestrator:
    """
    Get the singleton orchestrator instance.
    
    Returns:
        PhiHarmonicOrchestrator: Orchestrator instance
    """
    global _orchestrator_instance
    if _orchestrator_instance is None:
        _orchestrator_instance = PhiHarmonicOrchestrator()
    return _orchestrator_instance

def main():
    """Main function for running the orchestrator."""
    orchestrator = get_orchestrator()
    orchestrator.run_interactive()

if __name__ == "__main__":
    main()
