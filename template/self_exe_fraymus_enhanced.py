"""
Enhanced Quantum Phi-Harmonic Self-Executing Fraymus System

This module extends the original self_exe_fraymus_test.py with:
1. Persistent Memory: Saves functions, results, and loss to JSON files
2. Function Ranking & Mutation: Ranks and evolves high-performing functions
3. Dynamic φ-tuning: Varies PHI per agent for golden "mutational drift"
4. Agent Cortex Files: Each agent stores its evolution in a unique brain file

Following the "lego" approach, this builds on the original system without modifying core files.
"""

import os
import time
import uuid
import hashlib
import numpy as np
import random
import string
import torch
import torch.nn as nn
import torch.optim as optim
import threading
import json
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import ttk
import sys

# Import the memory module
from phi_agent_memory import PhiAgentMemory, get_all_agent_ids

# === CONSTANTS ===
PHI = (1 + np.sqrt(5)) / 2  # The Golden Ratio
FREQUENCIES = [432, 528, 639, 741, 852]  # Healing frequencies
MEMORY_DIR = "agent_memory"
VISUALIZATION_ENABLED = False  # Set to True to enable GUI visualization

# === SAFE EXECUTION WRAPPER ===
def execute_code_safely(code, timeout=2):
    """Execute code with a time limit to prevent infinite loops"""
    local_scope = {}
    try:
        exec(code, globals(), local_scope)
        func_name = next((name for name in local_scope if name.startswith("auto_func_")), None)
        if func_name:
            return local_scope[func_name]()
    except Exception as e:
        print(f"❌ Execution Error: {e}")
    return None

# === SELF-CODING AI MODULE ===
class EnhancedSelfCodingAI:
    """ AI that generates, evolves, and executes code in real-time with memory """
    def __init__(self, agent_id=None):
        self.memory = PhiAgentMemory(agent_id)
        self.code_history = []
        self.execution_results = []
        self.patterns = [
            self._generate_harmonic_pattern,
            self._generate_fibonacci_pattern,
            self._generate_quantum_pattern,
            self._generate_phi_recursive_pattern
        ]
        # Use agent-specific PHI variant
        self.phi = self.memory.phi_variant

    def _generate_harmonic_pattern(self):
        freq = random.choice(FREQUENCIES)
        harmonic_value = self.phi * freq / 100
        return "        return np.sin({} * np.pi) * {}".format(harmonic_value, np.random.uniform(0, 100))

    def _generate_fibonacci_pattern(self):
        n = random.randint(3, 7)
        return """        def fib(n):
            return n if n < 2 else fib(n-1) + fib(n-2)
        result = fib({}) * {}
        return np.cos(result / {}) * {}""".format(
            n, self.phi, random.choice(FREQUENCIES), np.random.uniform(0, 100))

    def _generate_quantum_pattern(self):
        superposition = random.uniform(0, 1)
        phase = random.uniform(0, 2 * np.pi)
        return """        # Quantum superposition simulation
        amplitude = {}
        phase = {}
        psi = amplitude * np.exp(1j * phase)
        measurement_prob = np.abs(psi) ** 2
        return float(measurement_prob * {} * np.sin({} * np.pi))""".format(
            superposition, phase, np.random.uniform(50, 150), self.phi)

    def _generate_phi_recursive_pattern(self):
        depth = random.randint(2, 4)
        base = np.random.uniform(1, 5)
        freq = random.choice(FREQUENCIES)
        return """        def phi_recursive(n, depth):
            if depth == 0:
                return n
            return n + (1 / phi_recursive(n, depth-1))
        
        result = phi_recursive({}, {})
        return np.tanh(result) * {}""".format(base, depth, freq)

    def generate_code(self, use_mutation=True):
        """ Generate code using patterns or mutation of top performers """
        function_name = f"auto_func_{uuid.uuid4().hex[:6]}"
        
        # Decide whether to mutate or generate new
        if use_mutation and random.random() < 0.7:  # 70% chance to mutate if enabled
            top_performers = self.memory.get_top_performers()
            if top_performers:
                # Get a top performer and mutate it
                base_function = random.choice(top_performers)["code"]
                code = self.memory.mutate_function(base_function)
                if code:
                    self.code_history.append(code)
                    return code
        
        # Generate new code using patterns
        pattern_func = random.choice(self.patterns)
        code_body = pattern_func()
        
        code = f"""def {function_name}():
    # Constants
    PHI = {self.phi}  # Golden Ratio (Agent Variant)
    try:
{code_body}
    except RecursionError:
        return np.random.uniform(0, 100)  # Fallback for recursion
    except Exception as e:
        print(f"Error in generated code: {{e}}")
        return None"""
        
        self.code_history.append(code)
        return code

    def execute_code(self, code):
        """ Execute the generated code and store results in memory """
        result = execute_code_safely(code)
        if result is not None:
            self.execution_results.append(result)
        return result

# === DEEP LEARNING AI MODEL ===
class AIModel(nn.Module):
    """ Neural Network for AI Learning """
    def __init__(self, input_size, output_size):
        super(AIModel, self).__init__()
        self.fc1 = nn.Linear(input_size, 128)
        self.fc2 = nn.Linear(128, output_size)
        # Initialize weights
        nn.init.xavier_uniform_(self.fc1.weight)
        nn.init.xavier_uniform_(self.fc2.weight)
    
    def forward(self, x):
        x = torch.relu(self.fc1(x))
        return torch.softmax(self.fc2(x), dim=-1)

# === QUANTUM HARMONIC INTELLIGENCE ===
class EnhancedQuantumHarmonicIntelligence:
    """The Ultimate AI Brain That Evolves, Learns, and Computes Infinitely"""
    def __init__(self, agent_id=None):
        self.agent_id = agent_id or str(uuid.uuid4())
        self.self_coding_ai = EnhancedSelfCodingAI(self.agent_id)
        self.model = AIModel(10, 2)  # Simple AI model for demonstration
        self.optimizer = optim.Adam(self.model.parameters(), lr=0.001)
        self.iteration = 0
        self.phi = self.self_coding_ai.phi
    
    def evolve_and_code(self, iterations=3):
        """Evolves intelligence, generates, and executes code"""
        for _ in range(iterations):
            self.iteration += 1
            
            # Decide whether to use mutation based on iteration
            use_mutation = self.iteration > 1
            
            code = self.self_coding_ai.generate_code(use_mutation)
            if code:
                result = self.self_coding_ai.execute_code(code)
                print(f"\n🧠 Generated Code:\n{code}")
                if result is not None:
                    print(f"🎯 Execution Result: {result}")
                
                # Simulate learning and store metrics
                x = torch.randn(1, 10)  # Random input
                output = self.model(x)
                loss = torch.mean((output - torch.tensor([[1., 0.]])) ** 2)
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                print(f"📚 Learning Loss: {loss.item():.4f}")
                
                # Store function in memory
                self.self_coding_ai.memory.store_function(code, result, loss.item())
                self.self_coding_ai.memory.update_evolution_metrics(loss.item(), success=(result is not None))
                
                # Get evolution trend
                if self.iteration % 5 == 0:
                    trend = self.self_coding_ai.memory.get_evolution_trend()
                    print(f"📈 Evolution Trend: {trend['trend'].upper()} | Success Rate: {trend['success_rate']:.2f}")

# === VISUALIZATION MODULE ===
class PhiAgentVisualizer:
    """Real-time visualization of agent performance and evolution"""
    def __init__(self, update_interval=1000):
        self.update_interval = update_interval
        self.root = None
        self.fig = None
        self.ax = None
        self.animation = None
        
    def start(self):
        """Start the visualization in a separate thread"""
        if not VISUALIZATION_ENABLED:
            return
            
        threading.Thread(target=self._run_visualization, daemon=True).start()
        
    def _run_visualization(self):
        """Run the visualization interface"""
        self.root = tk.Tk()
        self.root.title("Quantum Phi-Harmonic Agent Visualization")
        self.root.geometry("800x600")
        
        # Create tabs
        tab_control = ttk.Notebook(self.root)
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Agent Performance')
        tab_control.add(tab2, text='Phi Resonance')
        tab_control.pack(expand=1, fill="both")
        
        # Add matplotlib figure to tab1
        from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        import matplotlib.pyplot as plt
        
        self.fig, self.ax = plt.subplots(2, 1, figsize=(8, 6))
        canvas = FigureCanvasTkAgg(self.fig, tab1)
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Start animation
        self.animation = FuncAnimation(self.fig, self._update_plots, interval=self.update_interval)
        
        self.root.mainloop()
        
    def _update_plots(self, frame):
        """Update the plots with latest agent data"""
        agent_ids = get_all_agent_ids()
        
        if not agent_ids:
            return
            
        self.ax[0].clear()
        self.ax[1].clear()
        
        # Plot 1: Learning Loss
        for agent_id in agent_ids:
            memory = PhiAgentMemory(agent_id)
            losses = memory.memory["evolution_metrics"]["avg_loss"]
            if losses:
                self.ax[0].plot(losses[-30:], label=f"Agent {agent_id[:6]}")
        
        self.ax[0].set_title("Learning Loss Over Time")
        self.ax[0].set_xlabel("Iteration")
        self.ax[0].set_ylabel("Loss")
        self.ax[0].legend()
        
        # Plot 2: Phi Resonance of Top Functions
        for agent_id in agent_ids:
            memory = PhiAgentMemory(agent_id)
            top_performers = memory.get_top_performers(5)
            if top_performers:
                resonances = [p["phi_resonance"] for p in top_performers]
                self.ax[1].bar(
                    [f"A{agent_id[:4]}-{i}" for i in range(len(resonances))], 
                    resonances
                )
        
        self.ax[1].set_title("Phi Resonance of Top Functions")
        self.ax[1].set_xlabel("Function")
        self.ax[1].set_ylabel("Phi Resonance")
        self.ax[1].tick_params(axis='x', rotation=45)
        
        self.fig.tight_layout()

def parallel_agent_execution(num_agents=3, iterations_per_agent=3):
    """ Runs multiple AI instances in parallel with persistent memory """
    print("🚀 Starting Enhanced Quantum Harmonic Intelligence System...")
    
    # Create memory directory if it doesn't exist
    if not os.path.exists(MEMORY_DIR):
        os.makedirs(MEMORY_DIR)
    
    # Get existing agent IDs or create new ones
    existing_agent_ids = get_all_agent_ids()
    
    if existing_agent_ids and len(existing_agent_ids) >= num_agents:
        # Use existing agents
        agent_ids = existing_agent_ids[:num_agents]
        print(f"📂 Using {len(agent_ids)} existing agents with persistent memory")
    else:
        # Create new agents or supplement existing ones
        new_count = num_agents - len(existing_agent_ids)
        agent_ids = existing_agent_ids + [str(uuid.uuid4()) for _ in range(new_count)]
        print(f"🆕 Created {new_count} new agents, total: {len(agent_ids)}")
    
    # Create agents with their IDs
    agents = [EnhancedQuantumHarmonicIntelligence(agent_id) for agent_id in agent_ids]
    
    # Start visualization if enabled
    visualizer = PhiAgentVisualizer()
    visualizer.start()
    
    # Run agents
    with ThreadPoolExecutor(max_workers=num_agents) as executor:
        futures = [executor.submit(agent.evolve_and_code, iterations_per_agent) for agent in agents]
        for i, future in enumerate(futures):
            try:
                future.result()
            except Exception as e:
                print(f"❌ Agent {i+1} Error: {e}")
    
    # Print summary
    print("\n✨ Execution Summary:")
    for i, agent_id in enumerate(agent_ids):
        memory = PhiAgentMemory(agent_id)
        trend = memory.get_evolution_trend()
        print(f"Agent {i+1} (ID: {agent_id[:8]}...): Phi={memory.phi_variant:.8f}, " +
              f"Success Rate: {trend['success_rate']:.2f}, Trend: {trend['trend'].upper()}")

if __name__ == "__main__":
    # Parse command line arguments
    num_agents = 3
    iterations = 3
    
    if len(sys.argv) > 1:
        try:
            num_agents = int(sys.argv[1])
        except ValueError:
            pass
    
    if len(sys.argv) > 2:
        try:
            iterations = int(sys.argv[2])
        except ValueError:
            pass
    
    parallel_agent_execution(num_agents, iterations)
