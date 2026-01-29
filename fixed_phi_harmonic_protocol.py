#!/usr/bin/env python
"""
Phi-Harmonic Quantum Protocol (Fixed for Circular Dependency)

This module defines the standardized communication protocol for all phi-harmonic
quantum components. It provides a consistent interface for components to interact
with each other through the orchestrator.

This version uses a lazy import for the orchestrator to prevent circular dependencies
during component loading.
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
        # Lazy import of the orchestrator to break the circular dependency
        from phi_harmonic_orchestrator import get_orchestrator

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
        self.last_state_update = time.time()
        self.publish_event('component_state_updated', {
            'state': state
        })
