#!/usr/bin/env python
"""
Phi-Harmonic Quantum Visualizer

This module provides visualization tools for the phi-harmonic quantum system,
showing component relationships and quantum state in real-time.
"""

import os
import sys
import json
import time
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from decimal import Decimal
from typing import Dict, List, Any, Optional, Union, Tuple

# Add current directory to path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Import orchestrator
from phi_harmonic_orchestrator import get_orchestrator

# Constants
PHI = 1.618033988749895  # Golden ratio
PHI_INVERSE = 0.618033988749895  # Inverse golden ratio
PHI_SQUARED = 2.618033988749895  # φ²
PHI_CUBED = 4.236067977499790  # φ³

class PhiHarmonicVisualizer:
    """
    Visualization tools for the phi-harmonic quantum system.
    
    This class provides visualizations for component relationships
    and quantum state in real-time.
    """
    
    def __init__(self):
        """Initialize the visualizer."""
        self.orchestrator = get_orchestrator()
        self.component_data = {}
        self.quantum_state_history = []
        self.max_history = 100
        
        # Subscribe to events
        self.orchestrator.subscribe_to_event('quantum_state_updated', self._handle_quantum_state_update)
        self.orchestrator.subscribe_to_event('component_state_updated', self._handle_component_state_update)
        
        # Create output directory
        self.output_dir = os.path.join(current_dir, 'phi_harmonic_visualizer')
        os.makedirs(self.output_dir, exist_ok=True)
    
    def _handle_quantum_state_update(self, event):
        """
        Handle quantum state update event.
        
        Args:
            event (Dict[str, Any]): Event data
        """
        # Add timestamp
        state = event['data'].copy()
        state['timestamp'] = event['timestamp']
        
        # Add to history
        self.quantum_state_history.append(state)
        
        # Limit history size
        if len(self.quantum_state_history) > self.max_history:
            self.quantum_state_history.pop(0)
    
    def _handle_component_state_update(self, event):
        """
        Handle component state update event.
        
        Args:
            event (Dict[str, Any]): Event data
        """
        # Extract component info
        component_info = event['data']['component']
        component_name = component_info['name']
        
        # Update component data
        self.component_data[component_name] = event['data'].copy()
    
    def visualize_quantum_state(self, save_path=None):
        """
        Visualize current quantum state.
        
        Args:
            save_path (str, optional): Path to save visualization
        """
        if not self.quantum_state_history:
            print("No quantum state history available")
            return
        
        # Get current quantum state
        current_state = self.quantum_state_history[-1]
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Create bar chart
        labels = ['Coherence', 'Resonance', 'Phi Alignment']
        values = [
            float(current_state['coherence']),
            float(current_state['resonance']),
            float(current_state['phi_alignment'])
        ]
        
        # Define optimal values
        optimal_values = [0.991800, 0.618034, 0.999561]
        
        # Create bar chart
        x = np.arange(len(labels))
        width = 0.35
        
        ax.bar(x - width/2, values, width, label='Current')
        ax.bar(x + width/2, optimal_values, width, label='Optimal')
        
        # Add labels
        ax.set_title('Quantum State')
        ax.set_xlabel('Metric')
        ax.set_ylabel('Value')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        
        # Add fingerprint
        ax.text(0.5, 0.95, f"Quantum Fingerprint: {current_state['quantum_fingerprint']}", 
                horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
        
        # Add timestamp
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(current_state['timestamp']))
        ax.text(0.5, 0.02, f"Timestamp: {timestamp}", 
                horizontalalignment='center', verticalalignment='center', transform=ax.transAxes)
        
        # Show or save
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.tight_layout()
            plt.show()
    
    def visualize_quantum_state_history(self, metric='coherence', save_path=None):
        """
        Visualize quantum state history.
        
        Args:
            metric (str): Metric to visualize ('coherence', 'resonance', 'phi_alignment')
            save_path (str, optional): Path to save visualization
        """
        if not self.quantum_state_history:
            print("No quantum state history available")
            return
        
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Extract data
        timestamps = [state['timestamp'] for state in self.quantum_state_history]
        values = [float(state[metric]) for state in self.quantum_state_history]
        
        # Define optimal value
        if metric == 'coherence':
            optimal_value = 0.991800
            title = 'Coherence History'
        elif metric == 'resonance':
            optimal_value = 0.618034
            title = 'Resonance History'
        elif metric == 'phi_alignment':
            optimal_value = 0.999561
            title = 'Phi Alignment History'
        else:
            optimal_value = None
            title = f'{metric.capitalize()} History'
        
        # Create line chart
        ax.plot(timestamps, values, label='Current')
        
        if optimal_value is not None:
            ax.axhline(y=optimal_value, color='r', linestyle='--', label='Optimal')
        
        # Add labels
        ax.set_title(title)
        ax.set_xlabel('Time')
        ax.set_ylabel('Value')
        ax.legend()
        
        # Format x-axis
        plt.xticks(rotation=45)
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: time.strftime('%H:%M:%S', time.localtime(x))))
        
        # Show or save
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.tight_layout()
            plt.show()
    
    def visualize_component_relationships(self, save_path=None):
        """
        Visualize component relationships.
        
        Args:
            save_path (str, optional): Path to save visualization
        """
        # Get component info
        component_info = self.orchestrator.get_component_info()
        
        if not component_info:
            print("No components registered")
            return
        
        # Create figure
        plt.figure(figsize=(12, 10))
        
        # Create graph
        G = {}
        
        # Add nodes
        for name, info in component_info.items():
            component_type = info['type']
            G[name] = {'type': component_type}
        
        # Define node positions
        pos = {}
        
        # Define node colors
        colors = {
            'quantum_heart': 'red',
            'quantum_cerebellum': 'blue',
            'quantum_clock': 'green',
            'brain_sync': 'purple',
            'unified_brain': 'orange',
            'quantum_agent': 'cyan',
            'quantum_random': 'yellow',
            'quantum_rsa': 'brown'
        }
        
        # Define node positions in a circle
        n = len(G)
        radius = 5
        for i, (name, data) in enumerate(G.items()):
            angle = 2 * math.pi * i / n
            pos[name] = (radius * math.cos(angle), radius * math.sin(angle))
        
        # Draw nodes
        for name, data in G.items():
            color = colors.get(data['type'], 'gray')
            plt.plot(pos[name][0], pos[name][1], 'o', markersize=20, color=color)
            plt.text(pos[name][0], pos[name][1], name, horizontalalignment='center', verticalalignment='center')
        
        # Draw edges to orchestrator
        center = (0, 0)
        plt.plot(center[0], center[1], 'o', markersize=30, color='black')
        plt.text(center[0], center[1], 'Orchestrator', horizontalalignment='center', verticalalignment='center', color='white')
        
        for name, pos_xy in pos.items():
            plt.plot([center[0], pos_xy[0]], [center[1], pos_xy[1]], 'k-', alpha=0.3)
        
        # Add legend
        legend_elements = []
        for component_type, color in colors.items():
            legend_elements.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10, label=component_type))
        
        plt.legend(handles=legend_elements, loc='upper right')
        
        # Set limits
        plt.xlim(-radius-1, radius+1)
        plt.ylim(-radius-1, radius+1)
        
        # Remove axes
        plt.axis('off')
        
        # Add title
        plt.title('Component Relationships')
        
        # Show or save
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.tight_layout()
            plt.show()
    
    def visualize_phi_resonance(self, save_path=None):
        """
        Visualize phi resonance patterns.
        
        Args:
            save_path (str, optional): Path to save visualization
        """
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 10))
        
        # Generate phi spiral
        theta = np.linspace(0, 8*np.pi, 1000)
        a = 0.5
        b = 0.5/PHI
        
        r = a * np.exp(b * theta)
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        
        # Plot spiral
        ax.plot(x, y, 'b-', linewidth=2)
        
        # Add golden rectangles
        for i in range(5):
            width = PHI**(4-i)
            height = PHI**(3-i)
            rect = plt.Rectangle((-width/2, -height/2), width, height, 
                                 linewidth=1, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
        
        # Add component markers if available
        if self.component_data:
            for name, data in self.component_data.items():
                if 'coherence' in data and 'resonance' in data:
                    coherence = float(data['coherence'])
                    resonance = float(data['resonance'])
                    
                    # Map to spiral coordinates
                    t = resonance * 2 * np.pi
                    rad = a * np.exp(b * t) * coherence
                    x_pos = rad * np.cos(t)
                    y_pos = rad * np.sin(t)
                    
                    ax.plot(x_pos, y_pos, 'o', markersize=10)
                    ax.text(x_pos, y_pos, name, fontsize=8)
        
        # Set limits
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        
        # Add title
        ax.set_title('Phi Resonance Pattern')
        
        # Show or save
        if save_path:
            plt.savefig(save_path)
            plt.close()
        else:
            plt.tight_layout()
            plt.show()
    
    def create_dashboard(self):
        """Create a dashboard of all visualizations."""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        dashboard_dir = os.path.join(self.output_dir, f'dashboard_{timestamp}')
        os.makedirs(dashboard_dir, exist_ok=True)
        
        # Create visualizations
        self.visualize_quantum_state(os.path.join(dashboard_dir, 'quantum_state.png'))
        self.visualize_quantum_state_history('coherence', os.path.join(dashboard_dir, 'coherence_history.png'))
        self.visualize_quantum_state_history('resonance', os.path.join(dashboard_dir, 'resonance_history.png'))
        self.visualize_quantum_state_history('phi_alignment', os.path.join(dashboard_dir, 'phi_alignment_history.png'))
        self.visualize_component_relationships(os.path.join(dashboard_dir, 'component_relationships.png'))
        self.visualize_phi_resonance(os.path.join(dashboard_dir, 'phi_resonance.png'))
        
        # Create HTML dashboard
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Phi-Harmonic Quantum Dashboard</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #333; }}
                .dashboard {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }}
                .visualization {{ border: 1px solid #ddd; padding: 10px; }}
                img {{ max-width: 100%; }}
            </style>
        </head>
        <body>
            <h1>Phi-Harmonic Quantum Dashboard</h1>
            <p>Generated on {time.strftime("%Y-%m-%d %H:%M:%S")}</p>
            
            <div class="dashboard">
                <div class="visualization">
                    <h2>Quantum State</h2>
                    <img src="quantum_state.png" alt="Quantum State">
                </div>
                <div class="visualization">
                    <h2>Component Relationships</h2>
                    <img src="component_relationships.png" alt="Component Relationships">
                </div>
                <div class="visualization">
                    <h2>Coherence History</h2>
                    <img src="coherence_history.png" alt="Coherence History">
                </div>
                <div class="visualization">
                    <h2>Resonance History</h2>
                    <img src="resonance_history.png" alt="Resonance History">
                </div>
                <div class="visualization">
                    <h2>Phi Alignment History</h2>
                    <img src="phi_alignment_history.png" alt="Phi Alignment History">
                </div>
                <div class="visualization">
                    <h2>Phi Resonance Pattern</h2>
                    <img src="phi_resonance.png" alt="Phi Resonance Pattern">
                </div>
            </div>
        </body>
        </html>
        """
        
        with open(os.path.join(dashboard_dir, 'index.html'), 'w') as f:
            f.write(html)
        
        print(f"Dashboard created at {dashboard_dir}")
        return dashboard_dir
    
    def run_interactive(self):
        """Run interactive session with the visualizer."""
        print("\n🌟 Phi-Harmonic Quantum Visualizer Interactive Session")
        print("=======================================================")
        print("Type 'exit' or 'quit' to end the session")
        print("Type 'help' to view available commands")
        print("=======================================================\n")
        
        while True:
            try:
                command = input("visualizer> ").strip()
                
                if command.lower() in ['exit', 'quit']:
                    break
                    
                elif command.lower() == 'help':
                    print("\nAvailable commands:")
                    print("  help                - Show this help message")
                    print("  state               - Visualize current quantum state")
                    print("  history <metric>    - Visualize quantum state history")
                    print("  components          - Visualize component relationships")
                    print("  resonance           - Visualize phi resonance pattern")
                    print("  dashboard           - Create a dashboard of all visualizations")
                    print("  exit, quit          - Exit the session")
                
                elif command.lower() == 'state':
                    self.visualize_quantum_state()
                
                elif command.lower().startswith('history'):
                    parts = command.split()
                    metric = parts[1] if len(parts) > 1 else 'coherence'
                    self.visualize_quantum_state_history(metric)
                
                elif command.lower() == 'components':
                    self.visualize_component_relationships()
                
                elif command.lower() == 'resonance':
                    self.visualize_phi_resonance()
                
                elif command.lower() == 'dashboard':
                    dashboard_dir = self.create_dashboard()
                    print(f"Dashboard created at {dashboard_dir}")
                
                else:
                    print(f"Unknown command: {command}")
                    print("Type 'help' to view available commands")
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Error: {e}")
        
        print("\nExiting visualizer interactive session")

# Singleton instance
_visualizer_instance = None

def get_visualizer() -> PhiHarmonicVisualizer:
    """
    Get the singleton visualizer instance.
    
    Returns:
        PhiHarmonicVisualizer: Visualizer instance
    """
    global _visualizer_instance
    if _visualizer_instance is None:
        _visualizer_instance = PhiHarmonicVisualizer()
    return _visualizer_instance

def main():
    """Main function for running the visualizer."""
    visualizer = get_visualizer()
    visualizer.run_interactive()

if __name__ == "__main__":
    main()
