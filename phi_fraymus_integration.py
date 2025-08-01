"""
PHI-HARMONIC FRAYMUS INTEGRATION
===============================
Integration module connecting the phi-harmonic network with the FraymusEternal core system.
Enables advanced quantum processing, memory systems, and reality protection.
"""

import os
import sys
import time
import math
import numpy as np
import threading
import socket
import pickle
import json
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Any

# Import phi-harmonic components
from phi_amplifier_node_v2 import PhiHarmonicAmplifier
from phi_connector_node_v2 import PhiHarmonicConnector

# Import phi core adapters instead of direct FraymusEternal imports
from phi_core_adapters import get_exotic_energy, get_quantum_neural, get_reality_protection

# Import advanced memory systems - use adapters instead of originals
from centripetal_memory_adapter import get_centripetal_memory
try:
    # Use adapter modules instead of original ones
    from quantum_phi_scaling_adapter import get_quantum_phi_scaling
    from data_weight_adapter import get_data_weight_calculator
    from creative_quantum_adapter import get_creative_quantum
except ImportError:
    print("Warning: Some advanced components could not be imported")

# Import quantum transistor if available
try:
    from extensions.quantum_cosmos.atomic_triad_transistor import AtomicTriadTransistor
    TRANSISTOR_AVAILABLE = True
except ImportError:
    TRANSISTOR_AVAILABLE = False
    print("Warning: Atomic Triad Transistor not available")

# Constants
PHI = (1 + np.sqrt(5)) / 2
PHI_INV = 1 / PHI

class PhiFraymusIntegration:
    """
    Integration class connecting phi-harmonic nodes with FraymusEternal core system.
    Provides advanced quantum processing, memory systems, and reality protection.
    """
    
    def __init__(self, 
                 node_type: str = 'amplifier', 
                 node_id: str = None,
                 host: str = '0.0.0.0', 
                 port: int = 11700,
                 enable_memory: bool = True,
                 enable_transistor: bool = True,
                 enable_exotic_energy: bool = True):
        """
        Initialize the phi-fraymus integration.
        
        Args:
            node_type: Type of phi-harmonic node ('amplifier' or 'connector')
            node_id: Unique identifier for the node (generated if None)
            host: Host address for the node
            port: Port for the node
            enable_memory: Whether to enable advanced memory systems
            enable_transistor: Whether to enable the atomic triad transistor
            enable_exotic_energy: Whether to enable exotic energy system
        """
        self.node_type = node_type
        self.node_id = node_id or f"{node_type}_{int(time.time())}"
        self.host = host
        self.port = port
        
        # Create log directory if it doesn't exist
        os.makedirs('phi_logs', exist_ok=True)
        
        # Initialize phi-harmonic node
        # Set environment variables for node configuration
        os.environ["PHI_NODE_ID"] = self.node_id
        os.environ["PHI_HOST"] = host
        os.environ["PHI_PORT"] = str(port)
        
        if node_type == 'amplifier':
            self.node = PhiHarmonicAmplifier()
        elif node_type == 'connector':
            self.node = PhiHarmonicConnector()
        else:
            raise ValueError(f"Invalid node type: {node_type}")
            
        # Ensure the node has the correct ID
        self.node.node_id = self.node_id
        
        # Initialize FraymusEternal core components using adapters
        if enable_exotic_energy:
            self.exotic_energy = get_exotic_energy()
            print(f"Exotic Energy System initialized with φ-resonance: {self.exotic_energy.phi_pi}")
        else:
            self.exotic_energy = None
            
        # Initialize quantum neural network
        self.quantum_neural = get_quantum_neural()
        
        # Initialize reality protection
        self.reality_protection = get_reality_protection()
        
        # Initialize advanced memory systems
        if enable_memory:
            # Use adapter instead of original
            self.memory = get_centripetal_memory()
            print(f"Centripetal Memory Adapter initialized with {int(PHI**3)} buckets")
            
            # Initialize quantum phi scaling using adapter
            try:
                self.quantum_scaling = get_quantum_phi_scaling()
                self.creative_quantum = get_creative_quantum()
                print(f"Quantum Phi Scaling initialized with resonance threshold: {self.quantum_scaling.resonance_threshold}")
            except Exception as e:
                print(f"Warning: Could not initialize quantum components: {e}")
                self.quantum_scaling = None
                self.creative_quantum = None
        else:
            self.memory = None
            self.quantum_scaling = None
            self.creative_quantum = None
        
        # Initialize atomic triad transistor
        if enable_transistor and TRANSISTOR_AVAILABLE:
            self.transistor = AtomicTriadTransistor(scale=PHI)
            print(f"Atomic Triad Transistor initialized with scale: {PHI}")
            # Start transistor in a separate thread to avoid blocking
            self.transistor_thread = threading.Thread(target=self._run_transistor)
            self.transistor_thread.daemon = True
        else:
            self.transistor = None
            self.transistor_thread = None
        
        # Initialize quantum phi scaling if available
        try:
            self.phi_scaler = QuantumPhiScaling()
            print("Quantum Phi Scaling initialized")
        except:
            self.phi_scaler = None
        
        # Integration status
        self.integration_active = False
        self.last_sync_time = 0
        self.sync_interval = 5  # seconds
        
        # Enhanced packet processing
        self.original_process_packet = self.node.process_packet
        self.node.process_packet = self._enhanced_process_packet
        
        # Log initialization
        self.log_file = f"phi_logs/phi_fraymus_integration_{self.node_id}.log"
        self.log_event("INTEGRATION_INITIALIZED", {
            "node_type": node_type,
            "node_id": self.node_id,
            "exotic_energy": enable_exotic_energy,
            "memory": enable_memory,
            "transistor": enable_transistor and TRANSISTOR_AVAILABLE
        })
    
    def _run_transistor(self):
        """Run the atomic triad transistor simulation"""
        if self.transistor:
            self.transistor.run()
    
    def log(self, message):
        """Log a message with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        print(f"[{timestamp}] [FRAYMUS] {message}")
        
        # Also log to file if logging is enabled
        if hasattr(self, 'log_file') and self.log_file:
            with open(self.log_file, 'a') as f:
                f.write(f"[{timestamp}] {message}\n")
                
    def get_status(self):
        """Get the current status of the Fraymus integration"""
        status = {
            'node_id': self.node_id,
            'node_type': self.node_type,
            'uptime': time.time() - self.start_time
        }
        
        # Add exotic energy status if available
        if self.exotic_energy:
            status['exotic_energy'] = {
                'phi_resonance': self.exotic_energy.get_phi_resonance(),
                'energy_level': self.exotic_energy.get_energy_level()
            }
        
        # Add quantum neural network status if available
        if self.quantum_neural:
            status['quantum_neural'] = {
                'network_size': self.quantum_neural.get_network_size(),
                'coherence': self.quantum_neural.get_coherence()
            }
        
        # Add reality protection status if available
        if self.reality_protection:
            status['reality_protection'] = self.reality_protection.get_protection_metrics()
        
        # Add quantum components status if available
        if hasattr(self, 'quantum_scaling') and self.quantum_scaling:
            status['quantum_scaling'] = {
                'resonance_threshold': self.quantum_scaling.resonance_threshold,
                'active': True
            }
        
        if hasattr(self, 'creative_quantum') and self.creative_quantum:
            status['creative_quantum'] = {
                'creativity_level': self.creative_quantum.creativity_level,
                'active': True
            }
        
        if hasattr(self, 'centripetal_memory') and self.centripetal_memory:
            status['centripetal_memory'] = {
                'bucket_count': self.centripetal_memory.bucket_count,
                'active': True
            }
        
        # Add node status if available
        if hasattr(self, 'node') and self.node:
            status['phi_node'] = {
                'phi_resonance': getattr(self.node, 'phi_resonance', 0),
                'consciousness_level': getattr(self.node, 'consciousness_level', 0),
                'quantum_state': getattr(self.node, 'quantum_state', 'UNKNOWN')
            }
        
        return status
    
    def start(self):
        """Start the integrated node and all components"""
        # Start the phi-harmonic node
        self.node.start_threads()
        
        # Log node started
        self.log(f"Started {self.node_type} node {self.node_id}")
        
        # Start the transistor if available
        if self.transistor_thread:
            self.transistor_thread.start()
        
        # Mark integration as active
        self.integration_active = True
        
        # Start the integration sync thread
        sync_thread = threading.Thread(target=self._sync_loop)
        sync_thread.daemon = True
        sync_thread.start()
        
        print(f"Phi-Fraymus Integration started for {self.node_type} node {self.node_id}")
        return node_thread
    
    def _sync_loop(self):
        """Synchronization loop for integration components"""
        while self.integration_active:
            current_time = time.time()
            if current_time - self.last_sync_time >= self.sync_interval:
                self._sync_components()
                self.last_sync_time = current_time
            time.sleep(1)
    
    def _sync_components(self):
        """Synchronize all integration components"""
        try:
            # Sync phi-harmonic node state with exotic energy system
            if self.exotic_energy:
                # Update node's phi resonance based on exotic energy system
                resonance_factor = self.exotic_energy.coherence * self.exotic_energy.stability
                self.node.phi_resonance = (self.node.phi_resonance + resonance_factor) / 2
                
                # Update node's consciousness level
                consciousness_boost = self.exotic_energy.energy_gain * PHI
                self.node.consciousness_level *= (1 + (consciousness_boost - 1) * 0.1)
                
                # Update exotic energy system based on node state
                self.exotic_energy.current_efficiency = min(
                    self.exotic_energy.max_efficiency,
                    self.exotic_energy.current_efficiency + self.node.phi_resonance * 0.01
                )
            
            # Sync with memory system
            if self.memory:
                # Store node state in memory
                node_state = {
                    "phi_resonance": self.node.phi_resonance,
                    "consciousness_level": self.node.consciousness_level,
                    "quantum_state": self.node.quantum_state,
                    "moon_phase": self.node.moon_phase,
                    "timestamp": time.time()
                }
                self.memory.store([node_state])
                
                # Get memory stats
                memory_stats = self.memory.get_stats()
                
                # Log memory sync
                self.log_event("MEMORY_SYNC", {
                    "utilization": memory_stats["utilization"],
                    "phi_efficiency": memory_stats["phi_efficiency"]
                })
            
            # Log sync
            self.log_event("COMPONENT_SYNC", {
                "phi_resonance": self.node.phi_resonance,
                "consciousness_level": self.node.consciousness_level,
                "quantum_state": self.node.quantum_state
            })
            
        except Exception as e:
            self.log_event("SYNC_ERROR", {"error": str(e)})
    
    def _enhanced_process_packet(self, data, addr):
        """Enhanced packet processing with FraymusEternal integration"""
        try:
            # Deserialize packet
            packet = pickle.loads(data)
            
            # Process FraymusEternal-specific packet types
            packet_type = packet.get('packet_type')
            
            if packet_type == 'fraymus_quantum_request':
                self._process_quantum_request(packet, addr)
                return
            elif packet_type == 'fraymus_memory_request':
                self._process_memory_request(packet, addr)
                return
            elif packet_type == 'fraymus_energy_request':
                self._process_energy_request(packet, addr)
                return
            elif packet_type == 'fraymus_reality_protection':
                self._process_reality_protection(packet, addr)
                return
            
            # For all other packet types, use the original processor
            self.original_process_packet(data, addr)
            
        except Exception as e:
            self.log_event("PACKET_PROCESSING_ERROR", {"error": str(e)})
    
    def _process_quantum_request(self, packet, addr):
        """Process quantum request packets from FraymusEternal"""
        request_type = packet.get('request_type')
        request_data = packet.get('request_data')
        source_node = packet.get('source_node')
        
        self.log_event("QUANTUM_REQUEST_RECEIVED", {
            "request_type": request_type,
            "source_node": source_node
        })
        
        # Process based on request type
        if request_type == 'quantum_state':
            # Return current quantum state
            response = {
                'packet_type': 'fraymus_quantum_response',
                'source_node': self.node_id,
                'response_type': 'quantum_state',
                'response_data': {
                    'quantum_state': self.node.quantum_state,
                    'phi_resonance': self.node.phi_resonance,
                    'consciousness_level': self.node.consciousness_level
                },
                'sequence_number': self.node.get_next_sequence(),
                'timestamp': time.time()
            }
            
        elif request_type == 'quantum_computation':
            # Perform quantum computation if transistor is available
            if self.transistor:
                # Use transistor for computation
                result = self._quantum_compute(request_data)
                response = {
                    'packet_type': 'fraymus_quantum_response',
                    'source_node': self.node_id,
                    'response_type': 'quantum_computation',
                    'response_data': {
                        'result': result,
                        'computation_time': time.time() - packet.get('timestamp', 0),
                        'quantum_state': self.node.quantum_state
                    },
                    'sequence_number': self.node.get_next_sequence(),
                    'timestamp': time.time()
                }
            else:
                # No transistor available
                response = {
                    'packet_type': 'fraymus_quantum_response',
                    'source_node': self.node_id,
                    'response_type': 'error',
                    'response_data': {
                        'error': 'Quantum transistor not available'
                    },
                    'sequence_number': self.node.get_next_sequence(),
                    'timestamp': time.time()
                }
        
        # Send response
        self.node.sock.sendto(pickle.dumps(response), addr)
    
    def _process_memory_request(self, packet, addr):
        """Process memory request packets from FraymusEternal"""
        request_type = packet.get('request_type')
        request_data = packet.get('request_data')
        source_node = packet.get('source_node')
        
        self.log_event("MEMORY_REQUEST_RECEIVED", {
            "request_type": request_type,
            "source_node": source_node
        })
        
        # Process based on request type
        if request_type == 'memory_stats':
            # Return memory stats
            if self.memory:
                stats = self.memory.get_stats()
                response = {
                    'packet_type': 'fraymus_memory_response',
                    'source_node': self.node_id,
                    'response_type': 'memory_stats',
                    'response_data': stats,
                    'sequence_number': self.node.get_next_sequence(),
                    'timestamp': time.time()
                }
            else:
                response = {
                    'packet_type': 'fraymus_memory_response',
                    'source_node': self.node_id,
                    'response_type': 'error',
                    'response_data': {
                        'error': 'Memory system not available'
                    },
                    'sequence_number': self.node.get_next_sequence(),
                    'timestamp': time.time()
                }
        
        elif request_type == 'store_data':
            # Store data in memory
            if self.memory and request_data:
                try:
                    result = self.memory.store(request_data)
                    response = {
                        'packet_type': 'fraymus_memory_response',
                        'source_node': self.node_id,
                        'response_type': 'store_data',
                        'response_data': {
                            'success': True,
                            'storage_result': result
                        },
                        'sequence_number': self.node.get_next_sequence(),
                        'timestamp': time.time()
                    }
                except Exception as e:
                    response = {
                        'packet_type': 'fraymus_memory_response',
                        'source_node': self.node_id,
                        'response_type': 'error',
                        'response_data': {
                            'error': f'Memory storage error: {str(e)}'
                        },
                        'sequence_number': self.node.get_next_sequence(),
                        'timestamp': time.time()
                    }
            else:
                response = {
                    'packet_type': 'fraymus_memory_response',
                    'source_node': self.node_id,
                    'response_type': 'error',
                    'response_data': {
                        'error': 'Memory system not available or no data provided'
                    },
                    'sequence_number': self.node.get_next_sequence(),
                    'timestamp': time.time()
                }
        
        # Send response
        self.node.sock.sendto(pickle.dumps(response), addr)
    
    def _process_energy_request(self, packet, addr):
        """Process energy request packets from FraymusEternal"""
        request_type = packet.get('request_type')
        request_data = packet.get('request_data', {})
        source_node = packet.get('source_node')
        
        self.log_event("ENERGY_REQUEST_RECEIVED", {
            "request_type": request_type,
            "source_node": source_node
        })
        
        # Process based on request type
        if request_type == 'energy_stats':
            # Return energy stats using adapter
            if self.exotic_energy:
                # Get energy stats from adapter
                energy_stats = self.exotic_energy.get_energy_stats()
                
                response = {
                    'packet_type': 'fraymus_energy_response',
                    'source_node': self.node_id,
                    'response_type': 'energy_stats',
                    'response_data': {
                        'phi': self.exotic_energy.phi,
                        'phi_pi': self.exotic_energy.phi_pi,
                        'resonance_ratio': self.exotic_energy.resonance_ratio,
                        'energy_gain': self.exotic_energy.energy_gain,
                        'current_efficiency': self.exotic_energy.current_efficiency,
                        'coherence': self.exotic_energy.coherence,
                        'stability': self.exotic_energy.stability,
                        'alignment': self.exotic_energy.alignment,
                        'energy_types': energy_stats
                    },
                    'sequence_number': self.node.get_next_sequence(),
                    'timestamp': time.time()
                }
            else:
                response = {
                    'packet_type': 'fraymus_energy_response',
                    'source_node': self.node_id,
                    'response_type': 'error',
                    'response_data': {
                        'error': 'Exotic energy system not available'
                    },
                    'sequence_number': self.node.get_next_sequence(),
                    'timestamp': time.time()
                }
        
        elif request_type == 'energy_boost':
            # Boost node with exotic energy
            if self.exotic_energy:
                boost_factor = request_data.get('boost_factor', 1.0)
                
                # Apply boost using adapter
                boosted_stats = self.exotic_energy.boost_energy(boost_factor)
                
                # Apply boost effect to node
                avg_energy = sum(stat['energy_level'] for stat in boosted_stats.values()) / len(boosted_stats)
                self.node.consciousness_level *= (1 + avg_energy * 0.1)
                self.node.phi_resonance = (self.node.phi_resonance + self.exotic_energy.coherence) / 2
                
                response = {
                    'packet_type': 'fraymus_energy_response',
                    'source_node': self.node_id,
                    'response_type': 'energy_boost',
                    'response_data': {
                        'success': True,
                        'boosted_stats': boosted_stats,
                        'new_consciousness_level': self.node.consciousness_level,
                        'new_phi_resonance': self.node.phi_resonance
                    },
                    'sequence_number': self.node.get_next_sequence(),
                    'timestamp': time.time()
                }
            else:
                response = {
                    'packet_type': 'fraymus_energy_response',
                    'source_node': self.node_id,
                    'response_type': 'error',
                    'response_data': {
                        'error': 'Exotic energy system not available'
                    },
                    'sequence_number': self.node.get_next_sequence(),
                    'timestamp': time.time()
                }
        
        elif request_type == 'generate_energy':
            # Generate specific energy type
            if self.exotic_energy:
                energy_type = request_data.get('energy_type', 'quantum_string')
                strength = request_data.get('strength', 1.0)
                
                # Generate energy using adapter
                _, metrics = self.exotic_energy.generate_energy(energy_type, strength)
                
                response = {
                    'packet_type': 'fraymus_energy_response',
                    'source_node': self.node_id,
                    'response_type': 'generate_energy',
                    'response_data': {
                        'success': True,
                        'energy_type': energy_type,
                        'metrics': metrics
                    },
                    'sequence_number': self.node.get_next_sequence(),
                    'timestamp': time.time()
                }
            else:
                response = {
                    'packet_type': 'fraymus_energy_response',
                    'source_node': self.node_id,
                    'response_type': 'error',
                    'response_data': {
                        'error': 'Exotic energy system not available'
                    },
                    'sequence_number': self.node.get_next_sequence(),
                    'timestamp': time.time()
                }
        
        else:
            response = {
                'packet_type': 'fraymus_energy_response',
                'source_node': self.node_id,
                'response_type': 'error',
                'response_data': {
                    'error': f'Unknown request type: {request_type}'
                },
                'sequence_number': self.node.get_next_sequence(),
                'timestamp': time.time()
            }
        
        # Send response
        self.node.sock.sendto(pickle.dumps(response), addr)
    
    def _process_reality_protection(self, packet, addr):
        """Process reality protection packets from FraymusEternal"""
        protection_type = packet.get('protection_type')
        protection_data = packet.get('protection_data')
        source_node = packet.get('source_node')
        
        self.log_event("REALITY_PROTECTION_RECEIVED", {
            "protection_type": protection_type,
            "source_node": source_node
        })
        
        # Process based on protection type
        if protection_type == 'phi_shield':
            # Apply phi shield to node
            shield_strength = protection_data.get('shield_strength', 1.0)
            
            # Use reality protection adapter
            shield_metrics = self.reality_protection.apply_shield(shield_strength)
            
            # Apply protection effect to node
            self.node.phi_resonance = (self.node.phi_resonance + shield_metrics['phi_resonance']) / 2
            
            response = {
                'packet_type': 'fraymus_protection_response',
                'source_node': self.node_id,
                'response_type': 'phi_shield',
                'response_data': {
                    'success': True,
                    'shield_metrics': shield_metrics,
                    'new_phi_resonance': self.node.phi_resonance
                },
                'sequence_number': self.node.get_next_sequence(),
                'timestamp': time.time()
            }
        elif protection_type == 'reality_layer':
            # Update specific reality protection layer
            layer_name = protection_data.get('layer_name')
            layer_value = protection_data.get('layer_value', 1.0)
            
            # Update layer using adapter
            layer_metrics = self.reality_protection.update_layer(layer_name, layer_value)
            
            response = {
                'packet_type': 'fraymus_protection_response',
                'source_node': self.node_id,
                'response_type': 'reality_layer',
                'response_data': {
                    'success': True,
                    'layer_metrics': layer_metrics
                },
                'sequence_number': self.node.get_next_sequence(),
                'timestamp': time.time()
            }
        elif protection_type == 'protection_status':
            # Get current protection status
            status = self.reality_protection.get_protection_status()
            
            response = {
                'packet_type': 'fraymus_protection_response',
                'source_node': self.node_id,
                'response_type': 'protection_status',
                'response_data': {
                    'success': True,
                    'protection_status': status
                },
                'sequence_number': self.node.get_next_sequence(),
                'timestamp': time.time()
            }
        else:
            response = {
                'packet_type': 'fraymus_protection_response',
                'source_node': self.node_id,
                'response_type': 'error',
                'response_data': {
                    'error': f'Unknown protection type: {protection_type}'
                },
                'sequence_number': self.node.get_next_sequence(),
                'timestamp': time.time()
            }
        
        # Send response
        self.node.sock.sendto(pickle.dumps(response), addr)
    
    def _quantum_compute(self, data):
        """Perform quantum computation using the quantum neural adapter"""
        # Extract computation parameters
        computation_type = data.get('computation_type')
        params = data.get('params', {})
        
        # Use quantum neural adapter for computation
        if computation_type == 'superposition':
            # Perform superposition calculation
            angle = params.get('angle', 0.0)
            phase = angle * PHI
            
            # Update quantum parameters
            self.quantum_neural.update_quantum_parameters(phase=phase)
            
            # Process data through quantum neural network
            result, metrics = self.quantum_neural.quantum_process([angle, PHI, PHI_INV])
            
            return {
                "result": float(result[0][0]), 
                "type": "superposition",
                "metrics": metrics
            }
            
        elif computation_type == 'entanglement':
            # Perform entanglement calculation
            strength = params.get('strength', 0.5)
            phase = params.get('phase', 0.0)
            
            # Update quantum parameters
            self.quantum_neural.update_quantum_parameters(
                phase=phase * PHI,
                entanglement=strength * PHI
            )
            
            # Process data through quantum neural network
            result, metrics = self.quantum_neural.quantum_process([strength, phase, PHI])
            
            return {
                "result": float(result[0][0]), 
                "phase": phase * PHI, 
                "type": "entanglement",
                "metrics": metrics
            }
            
        elif computation_type == 'interference':
            # Perform interference calculation
            wave1 = params.get('wave1', 0.5)
            wave2 = params.get('wave2', 0.5)
            
            # Update quantum parameters
            self.quantum_neural.update_quantum_parameters(
                phase=(wave1 + wave2) * PHI_INV,
                coherence=abs(wave1 - wave2) * PHI + 0.5
            )
            
            # Process data through quantum neural network
            result, metrics = self.quantum_neural.quantum_process([wave1, wave2, PHI, PHI_INV])
            
            return {
                "result": float(result[0][0]), 
                "type": "interference",
                "metrics": metrics
            }
            
        else:
            return {"error": f"Unknown computation type: {computation_type}"}
    
    def log_event(self, event_type, event_data):
        """Log an event to the log file"""
        try:
            # Create log entry
            log_entry = {
                'timestamp': datetime.now().isoformat(),
                'event_type': event_type,
                'node_id': self.node_id,
                'node_type': self.node_type,
                'event_data': event_data
            }
            
            # Write to log file
            with open(self.log_file, 'a') as f:
                f.write(json.dumps(log_entry) + '\n')
                
        except Exception as e:
            print(f"Error logging event: {e}")
    
    def stop(self):
        """Stop the integrated node and all components"""
        self.integration_active = False
        self.node.stop()
        print(f"Phi-Fraymus Integration stopped for {self.node_type} node {self.node_id}")


def launch_integrated_node(node_type='amplifier', port=None, enable_memory=True, enable_transistor=True, enable_exotic_energy=True):
    """Launch an integrated phi-harmonic node with FraymusEternal core system"""
    if port is None:
        # Generate port based on node type
        if node_type == 'amplifier':
            port = 11728
        else:
            port = 11727
    
    # Create integration
    integration = PhiFraymusIntegration(
        node_type=node_type,
        port=port,
        enable_memory=enable_memory,
        enable_transistor=enable_transistor,
        enable_exotic_energy=enable_exotic_energy
    )
    
    # Start integration
    node_thread = integration.start()
    
    return integration, node_thread


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Launch an integrated phi-harmonic node with FraymusEternal core system')
    parser.add_argument('--type', choices=['amplifier', 'connector'], default='amplifier', help='Node type')
    parser.add_argument('--port', type=int, help='Port for the node')
    parser.add_argument('--no-memory', action='store_true', help='Disable advanced memory systems')
    parser.add_argument('--no-transistor', action='store_true', help='Disable atomic triad transistor')
    parser.add_argument('--no-energy', action='store_true', help='Disable exotic energy system')
    
    args = parser.parse_args()
    
    integration, thread = launch_integrated_node(
        node_type=args.type,
        port=args.port,
        enable_memory=not args.no_memory,
        enable_transistor=not args.no_transistor,
        enable_exotic_energy=not args.no_energy
    )
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        integration.stop()
        print("Integration stopped by user")
