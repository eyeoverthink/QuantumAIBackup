"""
Phi Agent Memory Module

This module provides persistent memory capabilities for quantum phi agents,
allowing them to store, retrieve, and evolve based on past experiences.

It follows the modular "lego" style approach to integrate with the existing system.
"""

import os
import json
import uuid
import time
import numpy as np
from datetime import datetime

# === CONSTANTS ===
PHI = (1 + np.sqrt(5)) / 2  # The Golden Ratio
MEMORY_DIR = "agent_memory"

class PhiAgentMemory:
    """Persistent memory system for quantum phi agents"""
    
    def __init__(self, agent_id=None):
        """Initialize agent memory with unique ID or use provided ID"""
        self.agent_id = agent_id or str(uuid.uuid4())
        self.memory_file = self._get_memory_path()
        self.memory = self._load_memory()
        self.phi_variant = PHI + (np.random.random() - 0.5) * 0.001  # Dynamic φ-tuning
        
    def _get_memory_path(self):
        """Get the path to the agent's memory file"""
        if not os.path.exists(MEMORY_DIR):
            os.makedirs(MEMORY_DIR)
        return os.path.join(MEMORY_DIR, f"agent_brain_{self.agent_id}.json")
    
    def _load_memory(self):
        """Load memory from file or create new memory structure"""
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"⚠️ Memory file corrupted, creating new memory")
        
        # Initialize new memory structure
        return {
            "agent_id": self.agent_id,
            "created_at": datetime.now().isoformat(),
            "phi_variant": float(PHI),
            "functions": [],
            "evolution_metrics": {
                "avg_loss": [],
                "success_rate": [],
                "complexity": []
            },
            "top_performers": []
        }
    
    def save_memory(self):
        """Save memory to file"""
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory, f, indent=2)
    
    def store_function(self, code, result, loss=None):
        """Store function code, result and performance metrics"""
        timestamp = datetime.now().isoformat()
        
        # Calculate complexity score based on code structure
        complexity = len(code.split('\n')) * 0.1 + code.count('if') * 0.5 + code.count('for') * 0.8
        
        function_data = {
            "timestamp": timestamp,
            "code": code,
            "result": float(result) if result is not None else None,
            "loss": float(loss) if loss is not None else None,
            "complexity": complexity,
            "phi_resonance": self._calculate_phi_resonance(code, result)
        }
        
        self.memory["functions"].append(function_data)
        
        # Update top performers if this function is successful
        if result is not None:
            self._update_top_performers(function_data)
        
        self.save_memory()
        return function_data
    
    def _calculate_phi_resonance(self, code, result):
        """Calculate how closely the function resonates with phi"""
        if result is None:
            return 0
        
        # Calculate resonance based on result's proximity to phi-based values
        phi_values = [self.phi_variant ** i for i in range(1, 8)]
        resonances = [1 / (abs(result % (p * 10)) + 0.1) for p in phi_values]
        return max(resonances)
    
    def _update_top_performers(self, function_data):
        """Update the list of top performing functions"""
        # Only keep functions with results
        if function_data["result"] is None:
            return
            
        # Add to top performers
        self.memory["top_performers"].append(function_data)
        
        # Sort by phi_resonance (higher is better) and keep top 10
        self.memory["top_performers"] = sorted(
            self.memory["top_performers"], 
            key=lambda x: x["phi_resonance"],
            reverse=True
        )[:10]
    
    def get_top_performers(self, limit=5):
        """Get the top performing functions"""
        return self.memory["top_performers"][:limit]
    
    def update_evolution_metrics(self, loss, success=True):
        """Update evolution metrics with latest performance data"""
        self.memory["evolution_metrics"]["avg_loss"].append(float(loss) if loss is not None else None)
        
        # Calculate success rate over last 10 iterations
        current_success_rate = self.memory["evolution_metrics"]["success_rate"]
        if not current_success_rate:
            current_success_rate = [0]
        
        # Update success rate (rolling average of last 10)
        success_history = current_success_rate[-9:] if len(current_success_rate) > 9 else current_success_rate
        success_history.append(1 if success else 0)
        self.memory["evolution_metrics"]["success_rate"] = success_history
        
        # Keep only last 100 loss values
        self.memory["evolution_metrics"]["avg_loss"] = self.memory["evolution_metrics"]["avg_loss"][-100:]
        
        self.save_memory()
    
    def get_evolution_trend(self):
        """Get the trend of evolution metrics"""
        losses = self.memory["evolution_metrics"]["avg_loss"]
        success_rates = self.memory["evolution_metrics"]["success_rate"]
        
        if not losses:
            return {"trend": "unknown", "avg_loss": None, "success_rate": None}
        
        avg_loss = sum(filter(None, losses[-10:])) / len(list(filter(None, losses[-10:]))) if losses else None
        success_rate = sum(success_rates) / len(success_rates) if success_rates else 0
        
        # Determine trend
        if len(losses) > 10:
            recent_avg = sum(filter(None, losses[-5:])) / len(list(filter(None, losses[-5:]))) if losses[-5:] else None
            older_avg = sum(filter(None, losses[-10:-5])) / len(list(filter(None, losses[-10:-5]))) if losses[-10:-5] else None
            
            if recent_avg is not None and older_avg is not None:
                trend = "improving" if recent_avg < older_avg else "declining"
            else:
                trend = "stable"
        else:
            trend = "initializing"
        
        return {
            "trend": trend,
            "avg_loss": avg_loss,
            "success_rate": success_rate
        }
    
    def mutate_function(self, base_function=None):
        """Create a mutated version of a function based on top performers"""
        if not self.memory["top_performers"] and not base_function:
            return None
        
        # Select base function - either provided or random top performer
        if base_function is None:
            base_function = np.random.choice(self.memory["top_performers"])["code"]
        
        # Simple mutation: replace random parts of the function
        lines = base_function.split('\n')
        
        # Choose a random line to mutate (excluding function definition and try/except)
        mutable_lines = [i for i, line in enumerate(lines) 
                        if not line.strip().startswith(('def', 'try:', 'except', 'return'))]
        
        if not mutable_lines:
            return base_function
            
        mutation_line = np.random.choice(mutable_lines)
        
        # Create mutation
        mutation_type = np.random.choice(['phi_variant', 'constant', 'operation'])
        
        if mutation_type == 'phi_variant':
            # Replace PHI with a variant
            lines[mutation_line] = lines[mutation_line].replace(
                str(PHI), 
                str(self.phi_variant)
            )
        elif mutation_type == 'constant':
            # Replace a numeric constant
            import re
            numeric_constants = re.findall(r'\d+\.\d+|\d+', lines[mutation_line])
            if numeric_constants:
                constant_to_replace = np.random.choice(numeric_constants)
                new_constant = str(float(constant_to_replace) * (0.8 + 0.4 * np.random.random()))
                lines[mutation_line] = lines[mutation_line].replace(constant_to_replace, new_constant)
        elif mutation_type == 'operation':
            # Replace an operation
            operations = {'+': '-', '-': '+', '*': '/', '/': '*'}
            for op in operations:
                if op in lines[mutation_line]:
                    lines[mutation_line] = lines[mutation_line].replace(op, operations[op], 1)
                    break
        
        return '\n'.join(lines)

# Function to get all agent IDs
def get_all_agent_ids():
    """Get IDs of all agents with memory files"""
    if not os.path.exists(MEMORY_DIR):
        return []
    
    agent_files = [f for f in os.listdir(MEMORY_DIR) if f.startswith("agent_brain_") and f.endswith(".json")]
    return [f.replace("agent_brain_", "").replace(".json", "") for f in agent_files]
