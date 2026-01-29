#!/usr/bin/env python
"""
Phi-Harmonic Quantum Protocol

This module defines the standardized communication protocol for all phi-harmonic
quantum components. It provides a consistent interface for components to interact
with each other through the orchestrator.

The protocol follows these key principles:
1. Golden ratio (φ) mathematics as the foundation
2. Quantum coherence and resonance as core metrics
3. Standardized message format for all communications
4. Event-driven architecture for real-time updates
"""

import os
import sys
import json
import time
import uuid
from decimal import Decimal, getcontext
from typing import Dict, List, Any, Optional, Union, Tuple, Callable

# Set precision for decimal calculations
getcontext().prec = 50

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import orchestrator
from phi_harmonic_orchestrator import get_orchestrator

# Constants
PHI = Decimal('1.618033988749895')  # Golden ratio
PHI_INVERSE = Decimal('0.618033988749895')  # Inverse golden ratio
PHI_SQUARED = Decimal('2.618033988749895')  # φ²
PHI_CUBED = Decimal('4.236067977499790')  # φ³
PHI_POWER = Decimal('36.93238055064198')  # φ⁷·⁵

class PhiHarmonicProtocol:
    """
    Standardized communication protocol for phi-harmonic quantum components.
    
    This class provides a consistent interface for components to interact
    with each other through the orchestrator, using a standardized message
    format and event-driven architecture.
    """
    
    def __init__(self, component_name: str, component_type: str):
        """
        Initialize the protocol.
        
        Args:
            component_name (str): Name of the component
            component_type (str): Type of the component
        """
        self.component_name = component_name
        self.component_type = component_type
        self.component_id = str(uuid.uuid4())
        self.orchestrator = get_orchestrator()
        self.event_handlers = {}
        self.message_queue = []
        self.last_state_update = 0
        
        # Register with orchestrator
        self._register_with_orchestrator()
    
    def _register_with_orchestrator(self):
        """Register with the orchestrator."""
        # Subscribe to events
        self.orchestrator.subscribe_to_event('quantum_state_updated', self._handle_quantum_state_update)
        self.orchestrator.subscribe_to_event('component_loaded', self._handle_component_loaded)
        self.orchestrator.subscribe_to_event('state_loaded', self._handle_state_loaded)
        
        # Publish registration event
        self.publish_event('component_registered', {
            'name': self.component_name,
            'type': self.component_type,
            'id': self.component_id
        })
    
    def _handle_quantum_state_update(self, event: Dict[str, Any]):
        """
        Handle quantum state update event.
        
        Args:
            event (Dict[str, Any]): Event data
        """
        if 'quantum_state_updated' in self.event_handlers:
            self.event_handlers['quantum_state_updated'](event['data'])
    
    def _handle_component_loaded(self, event: Dict[str, Any]):
        """
        Handle component loaded event.
        
        Args:
            event (Dict[str, Any]): Event data
        """
        if 'component_loaded' in self.event_handlers:
            self.event_handlers['component_loaded'](event['data'])
    
    def _handle_state_loaded(self, event: Dict[str, Any]):
        """
        Handle state loaded event.
        
        Args:
            event (Dict[str, Any]): Event data
        """
        if 'state_loaded' in self.event_handlers:
            self.event_handlers['state_loaded'](event['data'])
    
    def register_event_handler(self, event_type: str, handler: Callable):
        """
        Register an event handler.
        
        Args:
            event_type (str): Type of event to handle
            handler (Callable): Handler function
        """
        self.event_handlers[event_type] = handler
    
    def publish_event(self, event_type: str, event_data: Dict[str, Any]):
        """
        Publish an event.
        
        Args:
            event_type (str): Type of event to publish
            event_data (Dict[str, Any]): Event data
        """
        # Add component info to event data
        event_data['component'] = {
            'name': self.component_name,
            'type': self.component_type,
            'id': self.component_id
        }
        
        # Publish event through orchestrator
        self.orchestrator.publish_event(event_type, event_data)
    
    def send_message(self, target_component: str, message_type: str, message_data: Dict[str, Any]) -> str:
        """
        Send a message to another component.
        
        Args:
            target_component (str): Name of target component
            message_type (str): Type of message
            message_data (Dict[str, Any]): Message data
            
        Returns:
            str: Message ID
        """
        message_id = str(uuid.uuid4())
        
        message = {
            'id': message_id,
            'timestamp': time.time(),
            'sender': {
                'name': self.component_name,
                'type': self.component_type,
                'id': self.component_id
            },
            'target': target_component,
            'type': message_type,
            'data': message_data
        }
        
        # Add to message queue
        self.message_queue.append(message)
        
        # Publish message event
        self.publish_event('message_sent', {
            'message_id': message_id,
            'target': target_component,
            'type': message_type
        })
        
        return message_id
    
    def receive_message(self, message: Dict[str, Any]) -> bool:
        """
        Receive a message from another component.
        
        Args:
            message (Dict[str, Any]): Message data
            
        Returns:
            bool: True if message was handled, False otherwise
        """
        if 'message_received' in self.event_handlers:
            self.event_handlers['message_received'](message)
            return True
        return False
    
    def update_state(self, state: Dict[str, Any]):
        """
        Update component state.
        
        Args:
            state (Dict[str, Any]): Component state
        """
        # Add component info to state
        state['component'] = {
            'name': self.component_name,
            'type': self.component_type,
            'id': self.component_id
        }
        
        # Add timestamp
        state['timestamp'] = time.time()
        
        # Publish state update event
        self.publish_event('component_state_updated', state)
        
        # Update last state update timestamp
        self.last_state_update = state['timestamp']
    
    def get_quantum_state(self) -> Dict[str, Any]:
        """
        Get current quantum state from orchestrator.
        
        Returns:
            Dict[str, Any]: Quantum state
        """
        return self.orchestrator.get_quantum_state()
    
    def get_component(self, component_name: str) -> Any:
        """
        Get a component by name.
        
        Args:
            component_name (str): Name of component
            
        Returns:
            Any: Component instance or None if not found
        """
        return self.orchestrator.load_component(component_name)
    
    def get_component_info(self) -> Dict[str, Dict[str, Any]]:
        """
        Get information about all registered components.
        
        Returns:
            Dict[str, Dict[str, Any]]: Component information
        """
        return self.orchestrator.get_component_info()
    
    def save_state(self) -> str:
        """
        Save current state to a file.
        
        Returns:
            str: Path to saved state file
        """
        return self.orchestrator.save_state()
    
    def load_state(self, state_file: str) -> bool:
        """
        Load state from a file.
        
        Args:
            state_file (str): Path to state file
            
        Returns:
            bool: True if successful, False otherwise
        """
        return self.orchestrator.load_state(state_file)

# Decorator for phi-harmonic components
def phi_harmonic_component(component_type: str):
    """
    Decorator for phi-harmonic components.
    
    This decorator adds the phi-harmonic protocol to a component class,
    allowing it to communicate with other components through the orchestrator.
    
    Args:
        component_type (str): Type of component
        
    Returns:
        callable: Decorator function
    """
    def decorator(cls):
        original_init = cls.__init__
        
        def __init__(self, *args, **kwargs):
            # Call original __init__
            original_init(self, *args, **kwargs)
            
            # Add protocol
            self.protocol = PhiHarmonicProtocol(self.__class__.__name__, component_type)
            
            # Register event handlers
            if hasattr(self, 'handle_quantum_state_update'):
                self.protocol.register_event_handler('quantum_state_updated', self.handle_quantum_state_update)
            
            if hasattr(self, 'handle_component_loaded'):
                self.protocol.register_event_handler('component_loaded', self.handle_component_loaded)
            
            if hasattr(self, 'handle_state_loaded'):
                self.protocol.register_event_handler('state_loaded', self.handle_state_loaded)
            
            if hasattr(self, 'handle_message_received'):
                self.protocol.register_event_handler('message_received', self.handle_message_received)
            
            # Update initial state
            self._update_protocol_state()
        
        def _update_protocol_state(self):
            """Update protocol state with component state."""
            state = {}
            
            # Extract common state attributes
            for attr in ['coherence', 'resonance', 'phi_alignment', 'quantum_fingerprint']:
                if hasattr(self, attr):
                    state[attr] = getattr(self, attr)
            
            # Extract component-specific attributes
            if component_type == 'quantum_heart':
                if hasattr(self, 'heart_rate'):
                    state['heart_rate'] = self.heart_rate
                if hasattr(self, 'heart_resonance'):
                    state['heart_resonance'] = self.heart_resonance
                    
            elif component_type == 'quantum_cerebellum':
                if hasattr(self, 'cerebellum_neurons'):
                    state['cerebellum_neurons'] = self.cerebellum_neurons
                if hasattr(self, 'learning_rate'):
                    state['learning_rate'] = self.learning_rate
                    
            elif component_type == 'quantum_clock':
                if hasattr(self, 'frequency'):
                    state['frequency'] = self.frequency
                if hasattr(self, 'period'):
                    state['period'] = self.period
            
            # Update protocol state
            self.protocol.update_state(state)
        
        # Add method to class
        cls._update_protocol_state = _update_protocol_state
        
        # Replace __init__
        cls.__init__ = __init__
        
        return cls
    
    return decorator

# Example usage
if __name__ == "__main__":
    # Example component using the protocol
    @phi_harmonic_component('example')
    class ExampleComponent:
        def __init__(self):
            self.coherence = Decimal('0.991800')
            self.resonance = Decimal('0.618034')
            self.phi_alignment = Decimal('0.999561')
            print("Example component initialized")
        
        def handle_quantum_state_update(self, state):
            print(f"Quantum state updated: {state}")
        
        def handle_component_loaded(self, data):
            print(f"Component loaded: {data}")
        
        def handle_message_received(self, message):
            print(f"Message received: {message}")
    
    # Create example component
    example = ExampleComponent()
    
    # Get quantum state
    quantum_state = example.protocol.get_quantum_state()
    print(f"Quantum state: {quantum_state}")
    
    # Send a message
    message_id = example.protocol.send_message('orchestrator', 'example_message', {
        'hello': 'world'
    })
    print(f"Sent message with ID: {message_id}")
    
    # Update state
    example._update_protocol_state()
    print("Updated state")
