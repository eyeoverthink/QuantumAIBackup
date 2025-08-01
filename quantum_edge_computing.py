#!/usr/bin/env python3
"""
QUANTUM EDGE COMPUTING
Distributed quantum-inspired computation at the edge using φ-harmonic principles
"""

import os
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import hashlib
import threading
import queue
from datetime import datetime
from collections import defaultdict

# Import existing quantum components
try:
    from quantum_collision_evolution import QuantumCollisionEvolution
    from quantum_molecular_visualizer import QuantumMolecularVisualizer
    from quantum_complex_visualizer import QuantumComplexVisualizer
    from quantum_hybrid_memory import QuantumHybridMemory
    from quantum_ferris_memory import QuantumFerrisMemory
    from centripetal_memory import CentripetalMemory
except ImportError:
    print("Warning: Some quantum components could not be imported")
    
    # Define fallback implementations if imports fail
    class QuantumFerrisMemory:
        """Fallback implementation of QuantumFerrisMemory"""
        def __init__(self, num_buckets=8):
            self.num_buckets = num_buckets
            self.buckets = [{} for _ in range(num_buckets)]
            self.usage = [0 for _ in range(num_buckets)]
            self.phi_factor = (1 + np.sqrt(5)) / 2
        
        def store(self, key, value):
            bucket_index = hash(key) % self.num_buckets
            self.buckets[bucket_index][key] = value
            self.usage[bucket_index] += 1
            return True
        
        def retrieve(self, key):
            bucket_index = hash(key) % self.num_buckets
            return self.buckets[bucket_index].get(key)
        
        def get_stats(self):
            total_items = sum(len(bucket) for bucket in self.buckets)
            return {
                'total_capacity': self.num_buckets * 100,  # Arbitrary capacity
                'total_used': total_items,
                'utilization': total_items / (self.num_buckets * 100) if self.num_buckets > 0 else 0,
                'phi_efficiency': 0.8,  # Default value
                'ferris_usage': sum(self.usage) / len(self.usage) if self.usage else 0
            }
    
    class CentripetalMemory:
        """Fallback implementation of CentripetalMemory"""
        def __init__(self, num_buckets=8):
            self.num_buckets = num_buckets
            self.buckets = [{} for _ in range(num_buckets)]
            self.access_counts = [{} for _ in range(num_buckets)]
            self.phi_factor = (1 + np.sqrt(5)) / 2
        
        def store(self, key, value):
            bucket_index = hash(key) % self.num_buckets
            self.buckets[bucket_index][key] = value
            if key not in self.access_counts[bucket_index]:
                self.access_counts[bucket_index][key] = 0
            return True
        
        def retrieve(self, key):
            bucket_index = hash(key) % self.num_buckets
            if key in self.buckets[bucket_index]:
                self.access_counts[bucket_index][key] += 1
                return self.buckets[bucket_index][key]
            return None
        
        def get_stats(self):
            total_items = sum(len(bucket) for bucket in self.buckets)
            return {
                'total_capacity': self.num_buckets * 100,  # Arbitrary capacity
                'total_used': total_items,
                'utilization': total_items / (self.num_buckets * 100) if self.num_buckets > 0 else 0,
                'phi_efficiency': 0.85,  # Default value
                'centripetal_usage': sum(sum(counts.values()) for counts in self.access_counts) / self.num_buckets if self.num_buckets > 0 else 0
            }
    
    class QuantumHybridMemory:
        """Fallback implementation of QuantumHybridMemory"""
        def __init__(self, ferris_buckets=8, centripetal_buckets=8):
            self.ferris_memory = QuantumFerrisMemory(ferris_buckets)
            self.centripetal_memory = CentripetalMemory(centripetal_buckets)
            self.phi_factor = (1 + np.sqrt(5)) / 2
            self.ferris_buckets = ferris_buckets
            self.centripetal_buckets = centripetal_buckets
        
        def store(self, key, value):
            # Store in both memory systems for redundancy
            ferris_success = self.ferris_memory.store(key, value)
            centripetal_success = self.centripetal_memory.store(key, value)
            return ferris_success and centripetal_success
        
        def retrieve(self, key):
            # Try centripetal first (most frequently accessed)
            result = self.centripetal_memory.retrieve(key)
            if result is None:
                # Fall back to ferris memory
                result = self.ferris_memory.retrieve(key)
            return result
        
        def get_stats(self):
            ferris_stats = self.ferris_memory.get_stats()
            centripetal_stats = self.centripetal_memory.get_stats()
            
            total_capacity = ferris_stats['total_capacity'] + centripetal_stats['total_capacity']
            total_used = ferris_stats['total_used'] + centripetal_stats['total_used']
            
            return {
                'total_capacity': total_capacity,
                'total_used': total_used,
                'utilization': total_used / total_capacity if total_capacity > 0 else 0,
                'ferris_ratio': self.ferris_buckets / (self.ferris_buckets + self.centripetal_buckets),
                'centripetal_ratio': self.centripetal_buckets / (self.ferris_buckets + self.centripetal_buckets),
                'phi_efficiency': (ferris_stats['phi_efficiency'] + centripetal_stats['phi_efficiency']) / 2,
                'avg_compression_ratio': 1.2,  # Default value
                'ferris_usage': ferris_stats.get('ferris_usage', 0),
                'centripetal_usage': centripetal_stats.get('centripetal_usage', 0)
            }
            
        def optimize(self):
            # Placeholder for optimization logic
            pass

# Define φ (phi) constant
PHI = (1 + np.sqrt(5)) / 2

class QuantumEdgeNode:
    """
    A quantum-inspired edge computing node that processes data using φ-harmonic principles
    with integrated hybrid memory system for optimal data storage and retrieval
    """
    
    def __init__(self, node_id=None, phi_resonance=None, memory_buckets=8):
        """Initialize a quantum edge node with unique ID, φ-resonance, and hybrid memory system"""
        # Generate node ID if not provided
        if node_id is None:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            random_suffix = ''.join(random.choices('0123456789ABCDEF', k=6))
            node_id = f"QEN_{timestamp}_{random_suffix}"
        self.node_id = node_id
        
        # Assign φ-resonance if not provided
        if phi_resonance is None:
            # Generate a φ-resonant value (biased toward resonant values)
            r = random.random()
            if r < 0.4:  # 40% chance of highly resonant
                phi_resonance = random.uniform(0, 0.2)
            elif r < 0.7:  # 30% chance of moderately resonant
                phi_resonance = random.uniform(0.2, 0.4)
            else:  # 30% chance of other values
                phi_resonance = random.random()
        self.phi_resonance = phi_resonance
        
        # Node properties
        self.processing_capacity = 1.0 + self.phi_resonance * PHI
        self.energy_efficiency = 1.0 - (self.phi_resonance * 0.5)
        self.reliability = 0.85 + (1.0 - self.phi_resonance) * 0.15
        
        # Initialize hybrid memory system
        # Scale memory buckets based on phi resonance
        ferris_buckets = int(memory_buckets * (1 + self.phi_resonance))
        centripetal_buckets = int(memory_buckets * (1 + (1 - self.phi_resonance)))
        
        try:
            self.memory = QuantumHybridMemory(
                ferris_buckets=ferris_buckets,
                centripetal_buckets=centripetal_buckets
            )
            self.memory_available = True
            print(f"Hybrid memory system initialized with {ferris_buckets} ferris buckets and {centripetal_buckets} centripetal buckets")
        except Exception as e:
            print(f"Warning: Could not initialize hybrid memory: {e}")
            self.memory_available = False
        
        # Processing state
        self.task_queue = queue.Queue()
        self.results = {}
        self.is_processing = False
        self.connected_nodes = []
        self.memory_cache = {}  # Local cache for frequent data access
        
        # Create output directory
        self.output_dir = 'quantum_edge_results'
        os.makedirs(self.output_dir, exist_ok=True)
        
        print(f"Quantum Edge Node {self.node_id} initialized with φ-resonance: {self.phi_resonance:.6f}")
        print(f"Processing capacity: {self.processing_capacity:.2f}")
        print(f"Energy efficiency: {self.energy_efficiency:.2f}")
        print(f"Reliability: {self.reliability:.2f}")
    
    def get_node_status(self):
        """Get the current status of the node"""
        status = {
            'node_id': self.node_id,
            'phi_resonance': self.phi_resonance,
            'processing_capacity': self.processing_capacity,
            'energy_efficiency': self.energy_efficiency,
            'reliability': self.reliability,
            'is_processing': self.is_processing,
            'queue_size': self.task_queue.qsize(),
            'results_count': len(self.results),
            'connected_nodes': len(self.connected_nodes),
            'memory_available': self.memory_available
        }
        
        # Add memory stats if available
        if self.memory_available:
            try:
                memory_stats = self.memory.get_stats()
                status['memory'] = {
                    'total_capacity': memory_stats.get('total_capacity', 0),
                    'total_used': memory_stats.get('total_used', 0),
                    'utilization': memory_stats.get('utilization', 0),
                    'ferris_ratio': memory_stats.get('ferris_ratio', 0),
                    'centripetal_ratio': memory_stats.get('centripetal_ratio', 0),
                    'phi_efficiency': memory_stats.get('phi_efficiency', 0),
                    'avg_compression_ratio': memory_stats.get('avg_compression_ratio', 1.0)
                }
            except Exception as e:
                status['memory'] = {'error': str(e)}
                
        return status
    
    def connect_to_node(self, other_node):
        """Connect to another quantum edge node"""
        if other_node not in self.connected_nodes:
            # Calculate connection strength based on φ-resonance compatibility
            compatibility = 1.0 - abs(self.phi_resonance - other_node.phi_resonance)
            
            # Only connect if compatibility is good enough
            if compatibility > 0.7:
                self.connected_nodes.append(other_node)
                print(f"Node {self.node_id} connected to {other_node.node_id} with compatibility {compatibility:.2f}")
                return True
            else:
                print(f"Connection failed: incompatible φ-resonance ({compatibility:.2f} < 0.7)")
                return False
        return False
    
    def submit_task(self, task_type, task_data, priority=1.0):
        """Submit a task to the quantum edge node"""
        task = {
            'id': f"TASK_{datetime.now().strftime('%Y%m%d%H%M%S')}_{random.randint(1000, 9999)}",
            'type': task_type,
            'data': task_data,
            'priority': priority,
            'submitted_at': datetime.now(),
            'status': 'queued'
        }
        
        # Add task to queue with priority
        self.task_queue.put((priority, task))
        print(f"Task {task['id']} ({task_type}) submitted to node {self.node_id}")
        
        # Start processing if not already running
        if not self.is_processing:
            self._start_processing()
        
        return task['id']
    
    def _start_processing(self):
        """Start processing tasks in the queue"""
        self.is_processing = True
        processing_thread = threading.Thread(target=self._process_tasks)
        processing_thread.daemon = True
        processing_thread.start()
    
    def _process_tasks(self):
        """Process tasks in the queue"""
        while not self.task_queue.empty():
            # Get next task with highest priority
            _, task = self.task_queue.get()
            
            print(f"Processing task {task['id']} ({task['type']})...")
            task['status'] = 'processing'
            
            try:
                # Check memory cache for similar tasks first
                cache_hit = False
                if self.memory_available:
                    cache_key = self._generate_task_cache_key(task['type'], task)
                    cached_result = self.retrieve_from_memory(cache_key)
                    if cached_result and cached_result.get('success', False):
                        result = cached_result.get('data', {}).get('result', None)
                        if result:
                            print(f"Memory cache hit for task {task['id']}")
                            cache_hit = True
                            # Apply small processing time for cache hit
                            processing_time = random.uniform(0.1, 0.3) / self.processing_capacity
                            time.sleep(processing_time)
                
                # Process task if not in cache
                if not cache_hit:
                    # Process task based on type
                    if task['type'] == 'collision':
                        result = self._process_collision_task(task['data'])
                    elif task['type'] == 'visualization':
                        result = self._process_visualization_task(task['data'])
                    elif task['type'] == 'factorization':
                        result = self._process_factorization_task(task['data'])
                    elif task['type'] == 'distributed':
                        result = self._process_distributed_task(task['data'])
                    elif task['type'] == 'memory':
                        result = self._process_memory_task(task['data'])
                    else:
                        result = {'error': f"Unknown task type: {task['type']}"}
                    
                    # Simulate processing time based on node capacity
                    processing_time = random.uniform(0.5, 2.0) / self.processing_capacity
                    time.sleep(processing_time)
                    
                    # Apply reliability factor
                    if random.random() > self.reliability:
                        # Simulate occasional failure
                        result = {'error': 'Processing failed due to quantum decoherence'}
                        task['status'] = 'failed'
                    else:
                        task['status'] = 'completed'
                        
                        # Cache the result for future use
                        if self.memory_available:
                            self.store_in_memory(cache_key, {'result': result})
                else:
                    task['status'] = 'completed'
                    task['cache_hit'] = True
                
                # Store result
                task['completed_at'] = datetime.now()
                task['processing_time'] = processing_time if 'processing_time' not in locals() else processing_time
                task['result'] = result
                self.results[task['id']] = task
                
                # Save result to file
                self._save_task_result(task, result)
                
                print(f"Task {task['id']} completed in {task['processing_time']:.2f}s")
                
            except Exception as e:
                # Handle errors
                task['status'] = 'error'
                task['error'] = str(e)
                print(f"Error processing task {task['id']}: {e}")
            
            # Mark task as done in queue
            self.task_queue.task_done()
        
        # Reset processing flag when queue is empty
        self.is_processing = False
        
        # Optimize memory if available
        if self.memory_available:
            try:
                self.memory.optimize()
            except Exception as e:
                print(f"Warning: Memory optimization failed: {e}")
    
    def _process_collision_task(self, data):
        """Process a quantum collision task"""
        try:
            # Extract elements and energy factor
            elements = data.get('elements', [])
            energy_factor = data.get('energy_factor', 1.0)
            
            # Apply φ-resonance to energy factor
            phi_adjusted_energy = energy_factor * (1.0 + self.phi_resonance * 0.5)
            
            # Create collision evolution instance
            collision = QuantumCollisionEvolution()
            
            # Simulate collision
            result = collision.simulate_collision(elements, phi_adjusted_energy)
            
            return {
                'collision_result': result,
                'phi_adjusted_energy': phi_adjusted_energy,
                'node_resonance_factor': self.phi_resonance
            }
        except Exception as e:
            return {'error': f"Collision processing error: {str(e)}"}
    
    def _process_factorization_task(self, data):
        """Process a quantum factorization task"""
        try:
            # Extract number to factorize
            number = data.get('number', 0)
            
            # Simple factorization for demonstration
            factors = []
            i = 2
            while i * i <= number:
                if number % i:
                    i += 1
                else:
                    number //= i
                    factors.append(i)
            if number > 1:
                factors.append(number)
            
            return {
                'original_number': data.get('number', 0),
                'factors': factors,
                'phi_resonance_factor': self.phi_resonance,
                'processing_efficiency': self.energy_efficiency
            }
        except Exception as e:
            return {'error': f"Factorization processing error: {str(e)}"}
            
    def _process_distributed_task(self, data):
        """Process a distributed task by coordinating with other nodes"""
        try:
            # Extract subtasks and combination method
            subtasks = data.get('subtasks', [])
            combination_method = data.get('combination_method', 'resonant')
            
            if not subtasks:
                return {'error': "No subtasks provided for distributed processing"}
            
            # Process each subtask
            results = []
            for subtask in subtasks:
                task_type = subtask.get('type')
                task_data = subtask.get('data')
                
                # Process based on task type
                if task_type == 'collision':
                    result = self._process_collision_task(task_data)
                elif task_type == 'visualization':
                    result = self._process_visualization_task(task_data)
                elif task_type == 'factorization':
                    result = self._process_factorization_task(task_data)
                elif task_type == 'memory':
                    result = self._process_memory_task(task_data)
                else:
                    result = {'error': f"Unknown subtask type: {task_type}"}
                
                # Add to results
                results.append({
                    'task_type': task_type,
                    'result': result
                })
                
            # Combine results based on method
            if combination_method == 'resonant':
                # Apply φ-resonance to combine results
                combined = {
                    'method': 'φ-resonant combination',
                    'phi_factor': self.phi_resonance,
                    'subtask_results': results,
                    'combined_efficiency': self.energy_efficiency,
                    'combined_reliability': self.reliability
                }
            else:
                # Simple combination
                combined = {
                    'method': 'simple combination',
                    'subtask_results': results
                }
            
            return combined
        except Exception as e:
            return {'error': f"Distributed task processing error: {str(e)}"}
    
    def _process_visualization_task(self, data):
        """Process a quantum visualization task"""
        try:
            # Process visualization data
            result = {
                'status': 'success',
                'visualization_type': data.get('type', 'default'),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            return result
        except Exception as e:
            return {'error': f"Visualization processing error: {str(e)}"}
            
    def _process_memory_task(self, data):
        """Process a quantum memory task"""
        try:
            # Extract operation and key
            operation = data.get('operation', '')
            key = data.get('key', '')
            value = data.get('value', None)
            
            if not key:
                return {'error': "No key provided for memory operation"}
            
            result = {}
            
            if operation == 'store':
                if value is None:
                    return {'error': "No value provided for store operation"}
                
                # Store in memory
                if not hasattr(self, 'memory') or self.memory is None:
                    return {'error': "Memory system not available"}
                    
                success = self.memory.store(key, value)
                result = {
                    'operation': 'store',
                    'key': key,
                    'success': success
                }
                
            elif operation == 'retrieve':
                # Retrieve from memory
                value = self.retrieve_from_memory(key)
                result = {
                    'operation': 'retrieve',
                    'key': key,
                    'value': value,
                    'found': value is not None
                }
                
            elif operation == 'stats':
                # Get memory stats
                if not hasattr(self, 'memory') or self.memory is None:
                    return {'error': "Memory system not available"}
                    
                stats = self.memory.get_stats()
                result = {
                    'operation': 'stats',
                    'stats': stats
                }
                
            else:
                result = {'error': f"Unknown memory operation: {operation}"}
            
            return result
        except Exception as e:
            return {'error': f"Memory processing error: {str(e)}"}
            
    def retrieve_from_memory(self, key):
        """Retrieve a value from the node's memory
        
        Args:
            key: The key to retrieve
            
        Returns:
            The value if found, None otherwise
        """
        try:
            if hasattr(self, 'memory') and self.memory is not None:
                return self.memory.retrieve(key)
            else:
                print(f"Warning: Node {self.node_id} has no memory initialized")
                return None
        except Exception as e:
            print(f"Error retrieving from memory: {str(e)}")
            return None
            
    def store_in_memory(self, key, value):
        """Store a value in the node's memory
        
        Args:
            key: The key to store
            value: The value to store
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if hasattr(self, 'memory') and self.memory is not None:
                return self.memory.store(key, value)
            else:
                print(f"Warning: Node {self.node_id} has no memory initialized")
                return False
        except Exception as e:
            print(f"Error storing in memory: {str(e)}")
            return False
            
    def _save_task_result(self, task, result):
        """Save task result to file and memory
        
        Args:
            task: The task dictionary
            result: The result to save
        """
        try:
            # Save to results dictionary
            task_id = task.get('id', 'unknown')
            self.results[task_id] = result
            
            # Save to file if output directory exists
            if hasattr(self, 'output_dir') and self.output_dir:
                import os
                os.makedirs(self.output_dir, exist_ok=True)
                
                # Create filename with timestamp
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                filename = f"{self.output_dir}/task_{task_id}_{timestamp}.json"
                
                # Prepare data for saving
                save_data = {
                    'task': task,
                    'result': result,
                    'node_id': self.node_id,
                    'phi_resonance': self.phi_resonance,
                    'timestamp': timestamp
                }
                
                # Helper function to convert datetime objects
                def convert_datetime(obj):
                    if isinstance(obj, dict):
                        return {k: convert_datetime(v) for k, v in obj.items()}
                    elif isinstance(obj, list):
                        return [convert_datetime(item) for item in obj]
                    elif isinstance(obj, datetime):
                        return obj.isoformat()
                    else:
                        return obj
                
                # Convert all datetime objects
                save_data = convert_datetime(save_data)
                
                # Save to file
                with open(filename, 'w') as f:
                    json.dump(save_data, f, indent=2)
                    
                print(f"Task result saved to {filename}")
                
        except Exception as e:
            print(f"Warning: Could not save task result: {str(e)}")
            
    def _generate_task_cache_key(self, task_type, task_data):
        """Generate a cache key for a task based on its type and data"""
        # Create a string representation of the task data
        if isinstance(task_data, dict):
            # Create a serializable copy of the task data
            task_data_copy = {}
            for key, value in task_data.items():
                # Handle datetime objects
                if isinstance(value, datetime):
                    task_data_copy[key] = value.isoformat()
                elif key == 'submitted_at' or key == 'completed_at':
                    # Skip datetime fields that might be in the task
                    continue
                else:
                    task_data_copy[key] = value
            
            try:
                data_str = json.dumps(task_data_copy, sort_keys=True)
            except TypeError:
                # If there are still non-serializable objects, use a simpler approach
                # Create a hash of the task type and ID if available
                if 'id' in task_data:
                    data_str = f"{task_type}:{task_data.get('id', '')}"
                else:
                    # Last resort: use string representation
                    data_str = str(hash(str(task_data)))
        else:
            data_str = str(task_data)
            
        # Combine task type and data hash
        combined = f"{task_type}:{data_str}"
        
        # Generate a hash
        hash_obj = hashlib.md5(combined.encode())
        cache_key = hash_obj.hexdigest()
        
        # Add φ-resonance factor to make the key quantum-inspired
        phi_factor = int(self.phi_resonance * 1000) % 100
        cache_key = f"{cache_key}_{phi_factor:02d}"
        
        return cache_key


class QuantumEdgeNetwork:
    """
    A network of quantum edge nodes that collaborate on distributed tasks
    with global hybrid memory management
    """
    
    def __init__(self, num_nodes=3, memory_buckets=12):
        """Initialize a quantum edge network with specified number of nodes"""
        self.nodes = []
        self.node_id = f"QEN_NETWORK_{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Create nodes with varied φ-resonance
        for i in range(num_nodes):
            # Create a mix of resonant and non-resonant nodes
            if i < num_nodes // 3:
                # Highly resonant nodes (φ-resonance < 0.2)
                phi_resonance = random.uniform(0.01, 0.2)
            elif i < 2 * (num_nodes // 3):
                # Moderately resonant nodes (φ-resonance 0.2-0.5)
                phi_resonance = random.uniform(0.2, 0.5)
            else:
                # Other nodes (full range)
                phi_resonance = random.random()
            
            # Create node with memory system
            node = QuantumEdgeNode(phi_resonance=phi_resonance, memory_buckets=memory_buckets)
            self.nodes.append(node)
        
        # Connect nodes based on φ-resonance compatibility
        self._connect_nodes()
        
        # Initialize global memory system
        try:
            self.global_memory = QuantumHybridMemory(
                ferris_buckets=memory_buckets * 2,  # Double the buckets for network-level memory
                centripetal_buckets=memory_buckets * 2
            )
            self.memory_available = True
            print(f"Global hybrid memory system initialized with {memory_buckets * 2} buckets of each type")
        except Exception as e:
            print(f"Warning: Could not initialize global hybrid memory: {e}")
            self.memory_available = False
        
        # Memory cache for network-level data
        self.memory_cache = {}
        
        # Initialize global memory metrics
        self.global_memory_stats = {
            'total_capacity': 0,
            'total_used': 0,
            'avg_compression': 0.0,
            'phi_efficiency': 0.0,
            'node_memory_stats': {}
        }
        
        print(f"Quantum Edge Network initialized with {len(self.nodes)} nodes")
        
        # Update global memory stats
        self._update_global_memory_stats()
    
    def _update_global_memory_stats(self):
        """Update global memory statistics from all nodes"""
        if not self.memory_available:
            return
            
        # Reset stats
        self.global_memory_stats = {
            'total_capacity': 0,
            'total_used': 0,
            'avg_compression': 0.0,
            'phi_efficiency': 0.0,
            'node_memory_stats': {}
        }
        
        # Collect stats from global memory
        global_stats = self.global_memory.get_stats()
        self.global_memory_stats['total_capacity'] += global_stats['total_capacity']
        self.global_memory_stats['total_used'] += global_stats['total_used']
        
        # Collect stats from each node
        compression_values = []
        phi_efficiency_values = []
        
        for node in self.nodes:
            if node.memory_available:
                node_stats = node.memory.get_stats()
                node_id = node.node_id
                
                # Store node stats
                self.global_memory_stats['node_memory_stats'][node_id] = node_stats
                
                # Update totals
                self.global_memory_stats['total_capacity'] += node_stats['total_capacity']
                self.global_memory_stats['total_used'] += node_stats['total_used']
                
                # Collect values for averaging
                if 'avg_compression_ratio' in node_stats:
                    compression_values.append(node_stats['avg_compression_ratio'])
                if 'phi_efficiency' in node_stats:
                    phi_efficiency_values.append(node_stats['phi_efficiency'])
        
        # Calculate averages
        if compression_values:
            self.global_memory_stats['avg_compression'] = sum(compression_values) / len(compression_values)
        if phi_efficiency_values:
            self.global_memory_stats['phi_efficiency'] = sum(phi_efficiency_values) / len(phi_efficiency_values)
    
    def _connect_nodes(self):
        """Connect nodes based on φ-resonance compatibility"""
        connections = 0
        
        # Try to connect each pair of nodes
        for i, node1 in enumerate(self.nodes):
            for j, node2 in enumerate(self.nodes):
                if i != j:  # Don't connect to self
                    if node1.connect_to_node(node2):
                        connections += 1
        
        print(f"Created {connections} connections in the quantum edge network")
    
    def submit_distributed_task(self, task_type, subtasks, combination_method='resonant'):
        """Submit a distributed task to the network"""
        if not self.nodes:
            print("Error: No nodes in the network")
            return None
        
        # Find most suitable node based on task type and φ-resonance
        if task_type == 'collision':
            # For collisions, prefer nodes with lower φ-resonance
            suitable_nodes = sorted(self.nodes, key=lambda n: n.phi_resonance)
        elif task_type == 'visualization':
            # For visualizations, prefer nodes with mid-range φ-resonance
            suitable_nodes = sorted(self.nodes, key=lambda n: abs(n.phi_resonance - 0.5))
        elif task_type == 'factorization':
            # For factorization, prefer nodes with higher φ-resonance
            suitable_nodes = sorted(self.nodes, key=lambda n: -n.phi_resonance)
        else:
            # Default sorting by processing capacity
            suitable_nodes = sorted(self.nodes, key=lambda n: -n.processing_capacity)
        
        # Select coordinator node (first in suitable nodes)
        coordinator = suitable_nodes[0]
        
        # Create distributed task
        task_data = {
            'subtasks': subtasks,
            'combination_method': combination_method
        }
        
        # Submit to coordinator
        task_id = coordinator.submit_task('distributed', task_data, priority=2.0)
        
        print(f"Distributed task {task_id} submitted to coordinator node {coordinator.node_id}")
        return task_id, coordinator


def main():
    """Main function to demonstrate quantum edge computing"""
    print("Initializing Quantum Edge Computing Network...")
    
    # Create a network with exponential scaling capabilities
    network = QuantumEdgeNetwork(num_nodes=5)
    
    # Create some example tasks
    collision_task = {
        'type': 'collision',
        'data': {
            'elements': ['H', 'O', 'C'],
            'energy_factor': 1.618
        },
        'priority': 1.5
    }
    
    visualization_task = {
        'type': 'visualization',
        'data': {
            'elements': ['Au', 'H', 'O'],
            'type': 'complex'
        },
        'priority': 1.0
    }
    
    factorization_task = {
        'type': 'factorization',
        'data': {
            'number': 1234567
        },
        'priority': 2.0
    }
    
    # Create a distributed task with these subtasks
    subtasks = [collision_task, visualization_task, factorization_task]
    
    # Submit the distributed task
    task_id, coordinator = network.submit_distributed_task(
        'distributed', 
        subtasks, 
        combination_method='resonant'
    )
    
    # Wait for task to complete
    print("Waiting for distributed task to complete...")
    while task_id not in coordinator.results:
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\nTask completed!")
    
    # Get and display results
    result = coordinator.results[task_id]
    
    # Check if result has status or if it's an error
    if 'error' in result:
        print(f"Task status: error")
        print(f"Error: {result['error']}")
    else:
        print(f"Task status: {result.get('status', 'completed')}")
    
    print(f"Processing time: {result.get('processing_time', 0):.2f}s")
    
    # Save detailed results to file
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    results_file = f"quantum_edge_results_{timestamp}.json"
    
    with open(results_file, 'w') as f:
        # Create a serializable copy
        result_copy = result.copy()
        
        # Helper function to convert datetime objects
        def convert_datetime(obj):
            if isinstance(obj, dict):
                return {k: convert_datetime(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_datetime(item) for item in obj]
            elif isinstance(obj, datetime):
                return obj.isoformat()
            else:
                return obj
        
        # Convert all datetime objects in the result
        result_copy = convert_datetime(result_copy)
        
        json.dump(result_copy, f, indent=2)
    
    print(f"Detailed results saved to {results_file}")
    print("Quantum Edge Computing demonstration completed!")


if __name__ == "__main__":
    main()
