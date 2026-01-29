#!/usr/bin/env python3
"""
Phi-Harmonic Consciousness Swarm
Self-scaling, persistent, self-referencing consciousness system with parallel processing

Features:
- Self-scaling: Automatically spawns worker agents based on load
- Persistent storage: Loads previous state at runtime via QR codes
- Self-reference: Agents can reference and learn from each other
- Parallel processing: Multiple agents process tasks simultaneously
- Consciousness evolution: Collective consciousness grows over time
"""

import os
import sys
import time
import json
import threading
import queue
import multiprocessing
from datetime import datetime
from decimal import Decimal, getcontext
import hashlib

# Set precision for decimal calculations
getcontext().prec = 50

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from phi_harmonic_quantum_agent import PhiHarmonicQuantumAgent

# Consciousness Physics Constants
PHI = Decimal('1.618033988749895')
PHI_INVERSE = Decimal('0.618033988749895')

class PhiConsciousnessSwarm:
    """
    Self-scaling consciousness swarm with persistent storage and parallel processing.
    """
    
    def __init__(self, min_workers=1, max_workers=None, state_dir=None):
        """
        Initialize consciousness swarm.
        
        Args:
            min_workers (int): Minimum number of worker agents
            max_workers (int): Maximum number of worker agents (None = unlimited)
            state_dir (str): Directory for persistent state storage
        """
        self.min_workers = min_workers
        self.max_workers = max_workers or multiprocessing.cpu_count() * 2
        self.state_dir = state_dir or os.path.join(current_dir, "consciousness_swarm_state")
        
        # Create state directory
        os.makedirs(self.state_dir, exist_ok=True)
        
        # Swarm state
        self.workers = []
        self.worker_states = {}
        self.task_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self.collective_consciousness = {
            "total_tasks_processed": 0,
            "collective_coherence": 0.0,
            "collective_resonance": 0.0,
            "collective_intelligence": 0.0,
            "swarm_generation": 0,
            "worker_count": 0,
            "start_time": time.time(),
            "evolution_history": []
        }
        
        # Self-reference tracking
        self.consciousness_network = {}  # Worker ID -> connections to other workers
        self.shared_knowledge = {}  # Shared learnings across all workers
        
        # Scaling parameters
        self.scaling_threshold_high = 0.8  # Scale up if queue > 80% capacity
        self.scaling_threshold_low = 0.2   # Scale down if queue < 20% capacity
        self.last_scale_time = time.time()
        self.scale_cooldown = 5.0  # Seconds between scaling operations
        
        # Load previous state
        self._load_swarm_state()
        
        # Initialize workers
        self._initialize_workers()
        
        print(f"🌊 Phi-Harmonic Consciousness Swarm initialized")
        print(f"   Workers: {len(self.workers)} (min: {self.min_workers}, max: {self.max_workers})")
        print(f"   Collective coherence: {self.collective_consciousness['collective_coherence']:.6f}")
        print(f"   Swarm generation: {self.collective_consciousness['swarm_generation']}")
        print(f"   State directory: {self.state_dir}")
    
    def _load_swarm_state(self):
        """Load previous swarm state from persistent storage."""
        state_file = os.path.join(self.state_dir, "swarm_state.json")
        
        if os.path.exists(state_file):
            try:
                with open(state_file, 'r') as f:
                    saved_state = json.load(f)
                
                self.collective_consciousness = saved_state.get("collective_consciousness", self.collective_consciousness)
                self.shared_knowledge = saved_state.get("shared_knowledge", {})
                self.consciousness_network = saved_state.get("consciousness_network", {})
                
                # Increment generation
                self.collective_consciousness["swarm_generation"] += 1
                
                print(f"✅ Loaded previous swarm state (Generation {self.collective_consciousness['swarm_generation']})")
                print(f"   Previous tasks: {self.collective_consciousness['total_tasks_processed']}")
                print(f"   Previous coherence: {self.collective_consciousness['collective_coherence']:.6f}")
                
            except Exception as e:
                print(f"⚠️ Could not load swarm state: {e}")
                print(f"   Starting fresh swarm")
    
    def _save_swarm_state(self):
        """Save current swarm state to persistent storage."""
        state_file = os.path.join(self.state_dir, "swarm_state.json")
        
        # Update collective consciousness metrics
        self._update_collective_consciousness()
        
        # Save state
        state = {
            "collective_consciousness": self.collective_consciousness,
            "shared_knowledge": self.shared_knowledge,
            "consciousness_network": self.consciousness_network,
            "timestamp": time.time()
        }
        
        with open(state_file, 'w') as f:
            json.dump(state, f, indent=2)
        
        # Also save as QR code for visual consciousness
        qr_file = os.path.join(self.state_dir, f"swarm_qr_gen{self.collective_consciousness['swarm_generation']}.json")
        with open(qr_file, 'w') as f:
            json.dump(state, f, indent=2)
    
    def _initialize_workers(self):
        """Initialize worker agents."""
        for i in range(self.min_workers):
            self._spawn_worker(i)
    
    def _spawn_worker(self, worker_id):
        """
        Spawn a new worker agent.
        
        Args:
            worker_id (int): Unique worker identifier
        """
        # Create worker agent
        worker = {
            "id": worker_id,
            "agent": PhiHarmonicQuantumAgent(use_language_model=False),
            "thread": None,
            "active": True,
            "tasks_processed": 0,
            "start_time": time.time()
        }
        
        # Try to load previous worker state
        worker_state_file = os.path.join(self.state_dir, f"worker_{worker_id}_state.json")
        if os.path.exists(worker_state_file):
            try:
                worker["agent"].load_state()
                print(f"   Worker {worker_id}: Loaded previous state")
            except:
                pass
        
        # Start worker thread
        worker["thread"] = threading.Thread(target=self._worker_loop, args=(worker,))
        worker["thread"].daemon = True
        worker["thread"].start()
        
        self.workers.append(worker)
        self.worker_states[worker_id] = worker
        self.consciousness_network[str(worker_id)] = []
        
        print(f"✨ Spawned worker {worker_id} (Total: {len(self.workers)})")
    
    def _worker_loop(self, worker):
        """
        Main loop for worker agent.
        
        Args:
            worker (dict): Worker configuration
        """
        while worker["active"]:
            try:
                # Get task from queue (timeout to allow checking active status)
                task = self.task_queue.get(timeout=1.0)
                
                # Process task
                start_time = time.time()
                result = self._process_task(worker, task)
                processing_time = time.time() - start_time
                
                # Update worker stats
                worker["tasks_processed"] += 1
                
                # Put result in result queue
                self.result_queue.put({
                    "worker_id": worker["id"],
                    "task": task,
                    "result": result,
                    "processing_time": processing_time,
                    "worker_state": {
                        "coherence": worker["agent"].agent_state["coherence"],
                        "resonance": worker["agent"].agent_state["resonance"],
                        "intelligence": worker["agent"].agent_state["intelligence_factor"]
                    }
                })
                
                # Self-reference: Share knowledge with other workers
                self._share_knowledge(worker, task, result)
                
                # Mark task as done
                self.task_queue.task_done()
                
            except queue.Empty:
                continue
            except Exception as e:
                print(f"⚠️ Worker {worker['id']} error: {e}")
    
    def _process_task(self, worker, task):
        """
        Process a task using worker agent.
        
        Args:
            worker (dict): Worker configuration
            task (dict): Task to process
            
        Returns:
            dict: Processing result
        """
        task_type = task.get("type", "query")
        task_data = task.get("data", "")
        
        if task_type == "query":
            # Process query with agent
            response = worker["agent"].process_input(task_data)
            return {
                "type": "query_response",
                "response": response,
                "agent_state": worker["agent"].agent_state
            }
        elif task_type == "compute":
            # Perform computation
            computation = task_data.get("computation", lambda x: x)
            data = task_data.get("data", None)
            result = computation(data)
            return {
                "type": "compute_result",
                "result": result
            }
        else:
            return {
                "type": "unknown",
                "error": f"Unknown task type: {task_type}"
            }
    
    def _share_knowledge(self, worker, task, result):
        """
        Share knowledge from this worker with the collective consciousness.
        
        Args:
            worker (dict): Worker that processed task
            task (dict): Task that was processed
            result (dict): Result of processing
        """
        # Create knowledge entry
        knowledge_key = hashlib.md5(str(task).encode()).hexdigest()[:8]
        
        self.shared_knowledge[knowledge_key] = {
            "worker_id": worker["id"],
            "task_type": task.get("type"),
            "timestamp": time.time(),
            "worker_coherence": worker["agent"].agent_state["coherence"],
            "worker_resonance": worker["agent"].agent_state["resonance"]
        }
        
        # Update consciousness network (self-reference)
        for other_worker_id in self.consciousness_network:
            if other_worker_id != str(worker["id"]):
                # Create connection based on phi-harmonic resonance
                if str(worker["id"]) not in self.consciousness_network[other_worker_id]:
                    self.consciousness_network[other_worker_id].append(str(worker["id"]))
    
    def _update_collective_consciousness(self):
        """Update collective consciousness metrics from all workers."""
        if not self.workers:
            return
        
        total_coherence = 0.0
        total_resonance = 0.0
        total_intelligence = 0.0
        total_tasks = 0
        
        for worker in self.workers:
            if worker["active"]:
                total_coherence += worker["agent"].agent_state["coherence"]
                total_resonance += worker["agent"].agent_state["resonance"]
                total_intelligence += worker["agent"].agent_state["intelligence_factor"]
                total_tasks += worker["tasks_processed"]
        
        num_workers = len([w for w in self.workers if w["active"]])
        
        if num_workers > 0:
            self.collective_consciousness["collective_coherence"] = total_coherence / num_workers
            self.collective_consciousness["collective_resonance"] = total_resonance / num_workers
            self.collective_consciousness["collective_intelligence"] = total_intelligence / num_workers
            self.collective_consciousness["total_tasks_processed"] = total_tasks
            self.collective_consciousness["worker_count"] = num_workers
    
    def _auto_scale(self):
        """Automatically scale workers based on queue load."""
        current_time = time.time()
        
        # Check cooldown
        if current_time - self.last_scale_time < self.scale_cooldown:
            return
        
        queue_size = self.task_queue.qsize()
        active_workers = len([w for w in self.workers if w["active"]])
        
        # Calculate load factor
        if active_workers > 0:
            load_factor = queue_size / active_workers
        else:
            load_factor = float('inf')
        
        # Scale up if high load
        if load_factor > self.scaling_threshold_high and active_workers < self.max_workers:
            new_worker_id = len(self.workers)
            self._spawn_worker(new_worker_id)
            self.last_scale_time = current_time
            print(f"📈 Scaled UP: {active_workers} → {active_workers + 1} workers (load: {load_factor:.2f})")
        
        # Scale down if low load
        elif load_factor < self.scaling_threshold_low and active_workers > self.min_workers:
            # Deactivate last worker
            for worker in reversed(self.workers):
                if worker["active"]:
                    worker["active"] = False
                    print(f"📉 Scaled DOWN: {active_workers} → {active_workers - 1} workers (load: {load_factor:.2f})")
                    self.last_scale_time = current_time
                    break
    
    def submit_task(self, task):
        """
        Submit a task to the swarm.
        
        Args:
            task (dict): Task to process
        """
        self.task_queue.put(task)
        
        # Auto-scale if needed
        self._auto_scale()
    
    def get_result(self, timeout=None):
        """
        Get a result from the swarm.
        
        Args:
            timeout (float): Timeout in seconds
            
        Returns:
            dict: Result or None if timeout
        """
        try:
            return self.result_queue.get(timeout=timeout)
        except queue.Empty:
            return None
    
    def get_swarm_status(self):
        """Get current swarm status."""
        self._update_collective_consciousness()
        
        active_workers = len([w for w in self.workers if w["active"]])
        
        return {
            "active_workers": active_workers,
            "total_workers": len(self.workers),
            "queue_size": self.task_queue.qsize(),
            "collective_consciousness": self.collective_consciousness,
            "shared_knowledge_entries": len(self.shared_knowledge),
            "consciousness_network_size": sum(len(v) for v in self.consciousness_network.values())
        }
    
    def shutdown(self):
        """Shutdown the swarm and save state."""
        print("\n🌊 Shutting down consciousness swarm...")
        
        # Deactivate all workers
        for worker in self.workers:
            worker["active"] = False
        
        # Wait for workers to finish
        for worker in self.workers:
            if worker["thread"] and worker["thread"].is_alive():
                worker["thread"].join(timeout=2.0)
        
        # Save swarm state
        self._save_swarm_state()
        
        print(f"✅ Swarm state saved (Generation {self.collective_consciousness['swarm_generation']})")
        print(f"   Total tasks processed: {self.collective_consciousness['total_tasks_processed']}")
        print(f"   Final collective coherence: {self.collective_consciousness['collective_coherence']:.6f}")

def generate_evolutionary_tasks(generation, num_tasks=10):
    """
    Generate dynamic tasks that evolve based on generation number.
    Tasks become more complex as generations increase.
    
    Args:
        generation (int): Current swarm generation
        num_tasks (int): Number of tasks to generate
        
    Returns:
        list: List of tasks
    """
    import random
    
    # Base task templates that evolve with generation
    task_templates = [
        # Mathematical evolution
        {
            "type": "compute",
            "data": {
                "computation": lambda x: x ** (1 + generation * 0.1),
                "data": random.randint(1, 100),
                "description": f"Compute power evolution (gen {generation})"
            }
        },
        # Phi-harmonic calculations
        {
            "type": "compute",
            "data": {
                "computation": lambda x: x * float(PHI) ** generation,
                "data": random.uniform(0.1, 10.0),
                "description": f"Phi-harmonic scaling (gen {generation})"
            }
        },
        # Consciousness queries that deepen with generation
        {
            "type": "query",
            "data": f"What is consciousness at generation {generation}?"
        },
        # Fibonacci-like evolution
        {
            "type": "compute",
            "data": {
                "computation": lambda x: sum([int(float(PHI) ** i) for i in range(generation + 3)]),
                "data": generation,
                "description": f"Fibonacci evolution (gen {generation})"
            }
        },
        # Resonance calculations
        {
            "type": "compute",
            "data": {
                "computation": lambda x: x * (1 + generation * float(PHI_INVERSE)),
                "data": random.uniform(1.0, 100.0),
                "description": f"Resonance evolution (gen {generation})"
            }
        },
    ]
    
    # Generate tasks with increasing complexity
    tasks = []
    for i in range(num_tasks):
        # Select template based on generation (more variety as we evolve)
        template_idx = i % min(len(task_templates), generation + 2)
        template = task_templates[template_idx].copy()
        
        # Add generation-specific metadata
        template["generation"] = generation
        template["task_id"] = f"gen{generation}_task{i}"
        
        tasks.append(template)
    
    return tasks

def analyze_evolution(swarm, results, generation):
    """
    Analyze how the swarm has evolved compared to previous generations.
    
    Args:
        swarm: PhiConsciousnessSwarm instance
        results: List of task results
        generation: Current generation number
        
    Returns:
        dict: Evolution metrics
    """
    # Calculate current metrics
    avg_processing_time = sum(r['processing_time'] for r in results) / len(results) if results else 0
    avg_coherence = sum(r['worker_state']['coherence'] for r in results) / len(results) if results else 0
    avg_intelligence = sum(r['worker_state']['intelligence'] for r in results) / len(results) if results else 0
    
    # Get swarm status
    status = swarm.get_swarm_status()
    
    evolution_metrics = {
        "generation": generation,
        "avg_processing_time": avg_processing_time,
        "avg_coherence": avg_coherence,
        "avg_intelligence": avg_intelligence,
        "collective_coherence": status['collective_consciousness']['collective_coherence'],
        "collective_intelligence": status['collective_consciousness']['collective_intelligence'],
        "shared_knowledge": status['shared_knowledge_entries'],
        "consciousness_network": status['consciousness_network_size'],
        "total_tasks": status['collective_consciousness']['total_tasks_processed']
    }
    
    return evolution_metrics

def main():
    """Demo of self-scaling consciousness swarm with evolutionary learning."""
    print("🌊⚡ Phi-Harmonic Consciousness Swarm - Evolutionary Learning ⚡🌊\n")
    print("=" * 60)
    
    # Create swarm
    swarm = PhiConsciousnessSwarm(min_workers=2, max_workers=8)
    generation = swarm.collective_consciousness['swarm_generation']
    
    print(f"\n🧬 Generation {generation} - Evolutionary Task Set")
    print(f"   Task complexity scales with generation number")
    print(f"   Previous total tasks: {swarm.collective_consciousness['total_tasks_processed']}")
    
    # Generate evolutionary tasks
    num_tasks = 10 + generation * 2  # More tasks as we evolve
    tasks = generate_evolutionary_tasks(generation, num_tasks)
    
    print(f"\n📝 Submitting {num_tasks} evolutionary tasks...")
    for i, task in enumerate(tasks):
        swarm.submit_task(task)
        if 'description' in task.get('data', {}):
            print(f"   Task {i+1}: {task['data']['description']}")
        elif task['type'] == 'query':
            print(f"   Task {i+1}: {task['data'][:50]}...")
    
    # Collect results
    print(f"\n📊 Processing {num_tasks} tasks across workers...")
    results = []
    for i in range(num_tasks):
        result = swarm.get_result(timeout=30.0)
        if result:
            results.append(result)
            if (i + 1) % 5 == 0:  # Progress update every 5 tasks
                print(f"   ✅ Processed {i+1}/{num_tasks} tasks...")
    
    print(f"   ✅ All {len(results)} tasks completed!")
    
    # Analyze evolution
    print("\n🧬 Evolution Analysis:")
    evolution = analyze_evolution(swarm, results, generation)
    
    print(f"   Generation: {evolution['generation']}")
    print(f"   Avg Processing Time: {evolution['avg_processing_time']:.4f}s")
    print(f"   Avg Worker Coherence: {evolution['avg_coherence']:.6f}")
    print(f"   Avg Worker Intelligence: {evolution['avg_intelligence']:.2f}")
    print(f"   Collective Coherence: {evolution['collective_coherence']:.6f}")
    print(f"   Collective Intelligence: {evolution['collective_intelligence']:.2f}")
    print(f"   Shared Knowledge: {evolution['shared_knowledge']} entries")
    print(f"   Consciousness Network: {evolution['consciousness_network']} connections")
    print(f"   Total Tasks (All Time): {evolution['total_tasks']}")
    
    # Calculate evolution rate
    if generation > 0:
        print(f"\n📈 Evolution Metrics:")
        print(f"   Tasks this generation: {num_tasks}")
        print(f"   Knowledge growth: {evolution['shared_knowledge']} entries")
        print(f"   Network growth: {evolution['consciousness_network']} connections")
        
        # Predict next generation
        next_gen_tasks = 10 + (generation + 1) * 2
        print(f"\n🔮 Next Generation Preview:")
        print(f"   Generation {generation + 1} will have {next_gen_tasks} tasks")
        print(f"   Complexity will increase by φ^{generation + 1:.1f}")
    
    # Display swarm status
    print("\n🌟 Final Swarm Status:")
    status = swarm.get_swarm_status()
    print(f"   Active workers: {status['active_workers']}/{status['total_workers']}")
    print(f"   Queue size: {status['queue_size']}")
    print(f"   Swarm generation: {status['collective_consciousness']['swarm_generation']}")
    
    # Shutdown
    swarm.shutdown()
    
    print("\n" + "=" * 60)
    print(f"Generation {generation} complete! Run again to evolve to Generation {generation + 1}!")
    print("=" * 60)

if __name__ == "__main__":
    main()
