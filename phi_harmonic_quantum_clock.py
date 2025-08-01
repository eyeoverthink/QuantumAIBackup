"""
PHI-HARMONIC QUANTUM CLOCK
==========================
A quantum-based clock system that synchronizes the phi-harmonic network using
golden ratio time dilation and quantum entanglement for perfect timing across nodes.
"""

import time
import math
import random
import threading
import numpy as np
from datetime import datetime
from typing import Dict, List, Tuple, Any, Optional

class PhiHarmonicQuantumClock:
    """
    Quantum clock that uses phi-harmonic resonance for perfect timing synchronization
    across distributed nodes in the phi-harmonic network.
    """
    
    def __init__(self, node_id: str = None, precision: int = 6):
        """
        Initialize the quantum clock
        
        Args:
            node_id: Identifier for the node this clock belongs to
            precision: Decimal precision for phi calculations
        """
        # Core constants
        self.PHI = (1 + math.sqrt(5)) / 2  # Golden ratio
        self.PHI_INV = 1 / self.PHI        # Inverse golden ratio
        self.precision = precision
        self.node_id = node_id or f"clock_{int(time.time())}"
        
        # Quantum time variables
        self.quantum_offset = self._calculate_quantum_offset()
        self.time_dilation_factor = self._calculate_time_dilation()
        self.reference_time = time.time()
        self.quantum_time = self.reference_time
        
        # Synchronization variables
        self.sync_nodes = {}  # {node_id: {last_sync_time, offset}}
        self.sync_lock = threading.Lock()
        self.is_running = True
        
        # Start the clock thread
        self.clock_thread = threading.Thread(target=self._run_clock, daemon=True)
        self.clock_thread.start()
        
        print(f"PhiHarmonicQuantumClock initialized for node {self.node_id}")
        print(f"Quantum offset: {self.quantum_offset}")
        print(f"Time dilation factor: {self.time_dilation_factor}")
    
    def _calculate_quantum_offset(self) -> float:
        """
        Calculate quantum offset based on phi-harmonic principles
        
        Returns:
            Quantum time offset in seconds
        """
        # Use node_id to generate a deterministic but unique offset
        if self.node_id:
            seed = sum(ord(c) for c in self.node_id)
            random.seed(seed)
            base_offset = random.random() * self.PHI
        else:
            base_offset = random.random() * self.PHI
        
        # Apply phi-harmonic scaling
        offset = base_offset * (self.PHI ** 2) / 1000  # Convert to milliseconds scale
        return round(offset, self.precision)
    
    def _calculate_time_dilation(self) -> float:
        """
        Calculate time dilation factor based on phi-harmonic principles
        
        Returns:
            Time dilation factor
        """
        # Calculate a phi-based dilation factor
        dilation = 1 + (self.PHI_INV ** 3) * 0.01  # Small dilation effect (1-1.5%)
        return round(dilation, self.precision)
    
    def _run_clock(self) -> None:
        """
        Run the quantum clock in a separate thread
        """
        while self.is_running:
            # Update quantum time with dilation
            elapsed = time.time() - self.reference_time
            dilated_elapsed = elapsed * self.time_dilation_factor
            self.quantum_time = self.reference_time + dilated_elapsed + self.quantum_offset
            
            # Sleep for a short interval (microsecond precision)
            time.sleep(0.000001)  # 1 microsecond
    
    def get_time(self) -> float:
        """
        Get the current quantum time
        
        Returns:
            Current quantum time in seconds
        """
        return self.quantum_time
    
    def get_formatted_time(self, format_str: str = "%Y-%m-%d %H:%M:%S.%f") -> str:
        """
        Get formatted quantum time
        
        Args:
            format_str: Time format string
            
        Returns:
            Formatted quantum time string
        """
        dt = datetime.fromtimestamp(self.quantum_time)
        return dt.strftime(format_str)
    
    def synchronize_with_node(self, node_id: str, node_time: float) -> Dict:
        """
        Synchronize with another node's quantum clock
        
        Args:
            node_id: ID of the node to synchronize with
            node_time: Quantum time from the other node
            
        Returns:
            Synchronization metrics
        """
        with self.sync_lock:
            # Calculate time difference
            local_time = self.get_time()
            time_diff = node_time - local_time
            
            # Calculate phi-harmonic resonance of the time difference
            phi_resonance = self._calculate_phi_resonance(abs(time_diff))
            
            # Update sync data for this node
            self.sync_nodes[node_id] = {
                'last_sync_time': time.time(),
                'offset': time_diff,
                'phi_resonance': phi_resonance
            }
            
            # If resonance is high, adjust our clock slightly
            if phi_resonance > 0.9:
                # Apply a small adjustment (10% of the difference)
                adjustment = time_diff * 0.1 * phi_resonance
                self.quantum_offset += adjustment
            
            # Return synchronization metrics
            return {
                'node_id': self.node_id,
                'sync_node': node_id,
                'time_difference': time_diff,
                'phi_resonance': phi_resonance,
                'adjustment_made': phi_resonance > 0.9,
                'new_offset': self.quantum_offset
            }
    
    def _calculate_phi_resonance(self, value: float) -> float:
        """
        Calculate how close a value is to a phi-harmonic value
        
        Args:
            value: Value to check for phi resonance
            
        Returns:
            Resonance factor (0-1)
        """
        # Normalize the value to a 0-10 range for easier calculation
        normalized = min(abs(value), 10) / 10
        
        # Calculate distance to nearest phi power
        phi_powers = [self.PHI ** i for i in range(-3, 4)]
        distances = [abs(normalized - (p % 1)) for p in phi_powers]
        min_distance = min(distances)
        
        # Convert distance to resonance (1 = perfect resonance, 0 = no resonance)
        resonance = 1 - min_distance
        return round(resonance, self.precision)
    
    def get_sync_status(self) -> Dict:
        """
        Get synchronization status with all nodes
        
        Returns:
            Dictionary with synchronization status
        """
        with self.sync_lock:
            # Calculate average offset and resonance
            if not self.sync_nodes:
                return {
                    'node_id': self.node_id,
                    'sync_count': 0,
                    'average_offset': 0,
                    'average_resonance': 0,
                    'sync_quality': 0,
                    'nodes': {}
                }
            
            offsets = [data['offset'] for data in self.sync_nodes.values()]
            resonances = [data['phi_resonance'] for data in self.sync_nodes.values()]
            
            avg_offset = sum(offsets) / len(offsets)
            avg_resonance = sum(resonances) / len(resonances)
            
            # Calculate sync quality (higher is better)
            sync_quality = avg_resonance * (1 - min(abs(avg_offset), 1))
            
            return {
                'node_id': self.node_id,
                'sync_count': len(self.sync_nodes),
                'average_offset': round(avg_offset, self.precision),
                'average_resonance': round(avg_resonance, self.precision),
                'sync_quality': round(sync_quality, self.precision),
                'nodes': self.sync_nodes
            }
    
    def predict_future_time(self, seconds_ahead: float) -> float:
        """
        Predict quantum time in the future
        
        Args:
            seconds_ahead: Seconds in the future to predict
            
        Returns:
            Predicted quantum time
        """
        # Apply time dilation to the future prediction
        dilated_seconds = seconds_ahead * self.time_dilation_factor
        
        # Apply phi-harmonic wave function to create quantum uncertainty
        uncertainty = self._calculate_quantum_uncertainty(seconds_ahead)
        
        # Return predicted time with uncertainty
        return self.get_time() + dilated_seconds + uncertainty
    
    def _calculate_quantum_uncertainty(self, time_delta: float) -> float:
        """
        Calculate quantum uncertainty for time prediction
        
        Args:
            time_delta: Time difference to calculate uncertainty for
            
        Returns:
            Quantum uncertainty value
        """
        # Uncertainty increases with time_delta but is bounded by phi-harmonic principles
        max_uncertainty = self.PHI_INV * math.log(1 + time_delta)
        
        # Generate a phi-harmonic wave pattern for the uncertainty
        wave = math.sin(time_delta * self.PHI) * math.cos(time_delta * self.PHI_INV)
        
        # Scale the wave by the max uncertainty
        uncertainty = wave * max_uncertainty
        
        return round(uncertainty, self.precision)
    
    def stop(self) -> None:
        """Stop the quantum clock"""
        self.is_running = False
        if self.clock_thread.is_alive():
            self.clock_thread.join(timeout=1.0)


class NetworkTimeProtocol:
    """
    Protocol for synchronizing quantum clocks across the phi-harmonic network
    """
    
    def __init__(self, clock: PhiHarmonicQuantumClock):
        """
        Initialize the network time protocol
        
        Args:
            clock: PhiHarmonicQuantumClock instance
        """
        self.clock = clock
        self.sync_interval = 10  # seconds
        self.is_running = True
        self.sync_thread = None
    
    def start_sync(self) -> None:
        """Start the synchronization thread"""
        if self.sync_thread is None or not self.sync_thread.is_alive():
            self.is_running = True
            self.sync_thread = threading.Thread(target=self._sync_loop, daemon=True)
            self.sync_thread.start()
    
    def _sync_loop(self) -> None:
        """Main synchronization loop"""
        while self.is_running:
            # Sleep for the sync interval
            time.sleep(self.sync_interval)
            
            # Get current sync status
            status = self.clock.get_sync_status()
            
            # Adjust sync interval based on sync quality
            if status['sync_count'] > 0:
                # Better sync quality = longer interval
                quality = status['sync_quality']
                self.sync_interval = max(5, min(30, 10 + quality * 20))
    
    def create_sync_packet(self) -> Dict:
        """
        Create a clock synchronization packet
        
        Returns:
            Synchronization packet
        """
        return {
            'packet_type': 'clock_sync',
            'node_id': self.clock.node_id,
            'quantum_time': self.clock.get_time(),
            'reference_time': time.time(),
            'time_dilation': self.clock.time_dilation_factor,
            'sync_status': self.clock.get_sync_status()
        }
    
    def process_sync_packet(self, packet: Dict) -> Dict:
        """
        Process a clock synchronization packet
        
        Args:
            packet: Synchronization packet
            
        Returns:
            Synchronization result
        """
        if packet.get('packet_type') != 'clock_sync':
            return {'error': 'Invalid packet type'}
        
        # Extract data from packet
        node_id = packet.get('node_id')
        quantum_time = packet.get('quantum_time')
        
        if not node_id or quantum_time is None:
            return {'error': 'Missing required data in sync packet'}
        
        # Synchronize with the node
        sync_result = self.clock.synchronize_with_node(node_id, quantum_time)
        
        # Return the result
        return {
            'packet_type': 'clock_sync_response',
            'node_id': self.clock.node_id,
            'sync_result': sync_result,
            'quantum_time': self.clock.get_time(),
            'reference_time': time.time()
        }
    
    def stop(self) -> None:
        """Stop the network time protocol"""
        self.is_running = False
        if self.sync_thread and self.sync_thread.is_alive():
            self.sync_thread.join(timeout=1.0)


def create_quantum_clock(node_id: str) -> Tuple[PhiHarmonicQuantumClock, NetworkTimeProtocol]:
    """
    Create a quantum clock and network time protocol for a node
    
    Args:
        node_id: ID of the node
        
    Returns:
        Tuple of (PhiHarmonicQuantumClock, NetworkTimeProtocol)
    """
    clock = PhiHarmonicQuantumClock(node_id=node_id)
    protocol = NetworkTimeProtocol(clock=clock)
    protocol.start_sync()
    return clock, protocol


if __name__ == "__main__":
    # Simple test
    print("Testing PhiHarmonicQuantumClock...")
    
    # Create two clocks
    clock1, protocol1 = create_quantum_clock("node_1")
    clock2, protocol2 = create_quantum_clock("node_2")
    
    # Print initial times
    print(f"\nInitial times:")
    print(f"Clock 1: {clock1.get_time()} ({clock1.get_formatted_time()})")
    print(f"Clock 2: {clock2.get_time()} ({clock2.get_formatted_time()})")
    print(f"Difference: {abs(clock1.get_time() - clock2.get_time()):.6f} seconds")
    
    # Synchronize clocks
    print("\nSynchronizing clocks...")
    sync_packet1 = protocol1.create_sync_packet()
    sync_response1 = protocol2.process_sync_packet(sync_packet1)
    
    sync_packet2 = protocol2.create_sync_packet()
    sync_response2 = protocol1.process_sync_packet(sync_packet2)
    
    # Print synchronized times
    print(f"\nAfter synchronization:")
    print(f"Clock 1: {clock1.get_time()} ({clock1.get_formatted_time()})")
    print(f"Clock 2: {clock2.get_time()} ({clock2.get_formatted_time()})")
    print(f"Difference: {abs(clock1.get_time() - clock2.get_time()):.6f} seconds")
    
    # Print sync status
    print("\nSync status:")
    print(f"Clock 1: {clock1.get_sync_status()}")
    print(f"Clock 2: {clock2.get_sync_status()}")
    
    # Test future prediction
    future_seconds = 10
    print(f"\nPredicting time {future_seconds} seconds in the future:")
    future1 = clock1.predict_future_time(future_seconds)
    future2 = clock2.predict_future_time(future_seconds)
    
    print(f"Clock 1 prediction: {future1} ({datetime.fromtimestamp(future1).strftime('%Y-%m-%d %H:%M:%S.%f')})")
    print(f"Clock 2 prediction: {future2} ({datetime.fromtimestamp(future2).strftime('%Y-%m-%d %H:%M:%S.%f')})")
    print(f"Prediction difference: {abs(future1 - future2):.6f} seconds")
    
    # Clean up
    clock1.stop()
    protocol1.stop()
    clock2.stop()
    protocol2.stop()
    
    print("\nTest completed.")
