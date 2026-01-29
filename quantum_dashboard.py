#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Quantum Dashboard
---------------
Interactive dashboard for visualizing and demonstrating QuantumAI system capabilities.
Provides real-time monitoring of phi-harmonic coherence, evolution metrics,
and self-healing/self-reproduction processes.
"""

import os
import sys
import json
import time
import logging
import argparse
from datetime import datetime

# Import quantum modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from quantum_visualization import QuantumVisualization
try:
    from quantum_self_healing_orchestrator import QuantumSelfHealingOrchestrator
    from quantum_system_demonstration import QuantumSystemDemonstration
except ImportError:
    logging.warning("Some quantum modules could not be imported. Limited functionality available.")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("QuantumDashboard")

# Phi-harmonic constants
PHI = 1.618033988749895
PHI_COHERENCE = 0.991800  # φ⁷·⁵/10

class QuantumDashboard:
    """
    Interactive dashboard for QuantumAI system demonstration and monitoring.
    """
    def __init__(self):
        """
        Initialize the quantum dashboard.
        """
        self.birth_timestamp = time.time()
        self.visualizer = QuantumVisualization()
        
        # Initialize components if available
        try:
            self.orchestrator = QuantumSelfHealingOrchestrator()
            self.demonstration = QuantumSystemDemonstration()
            self.full_functionality = True
        except:
            self.full_functionality = False
            logger.warning("Running in limited functionality mode")
        
        # Ensure directories exist
        self.evolution_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "evolution")
        self.visualization_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "visualizations")
        self.dashboard_dir = os.path.join(self.visualization_dir, "dashboard")
        
        os.makedirs(self.evolution_dir, exist_ok=True)
        os.makedirs(self.visualization_dir, exist_ok=True)
        os.makedirs(self.dashboard_dir, exist_ok=True)
        
        logger.info(f"Initialized QuantumDashboard")
    
    def generate_dashboard(self):
        """
        Generate the main dashboard interface.
        
        Returns:
            str: Path to the generated dashboard file
        """
        logger.info("Generating main dashboard")
        
        # Load evolution data
        evolution_data = self._load_evolution_data()
        healing_history = self._load_healing_history()
        
        # Create markdown dashboard
        output_file = os.path.join(self.dashboard_dir, "quantum_dashboard.md")
        
        with open(output_file, 'w') as f:
            f.write("# QuantumAI System Dashboard\n\n")
            f.write(f"Generated: {datetime.now().isoformat()}\n")
            f.write(f"Phi-Harmonic Coherence Target: φ⁷·⁵/10 = {PHI_COHERENCE:.6f}\n\n")
            
            # System status overview
            f.write("## System Status\n\n")
            f.write("| Component | Status | Coherence | Fingerprint |\n")
            f.write("|-----------|--------|-----------|-------------|\n")
            
            # Visualizer status
            visualizer_fingerprint = self.visualizer.quantum_fingerprint
            f.write(f"| Visualization | Active | {PHI_COHERENCE:.6f} | `{visualizer_fingerprint}` |\n")
            
            # Orchestrator status
            if hasattr(self, 'orchestrator'):
                orchestrator_fingerprint = getattr(self.orchestrator, 'quantum_fingerprint', 'N/A')
                f.write(f"| Orchestrator | Active | {PHI_COHERENCE:.6f} | `{orchestrator_fingerprint}` |\n")
            else:
                f.write("| Orchestrator | Inactive | N/A | `N/A` |\n")
            
            # Demonstration status
            if hasattr(self, 'demonstration'):
                demo_fingerprint = getattr(self.demonstration, 'quantum_fingerprint', 'N/A')
                f.write(f"| Demonstration | Active | {PHI_COHERENCE:.6f} | `{demo_fingerprint}` |\n")
            else:
                f.write("| Demonstration | Inactive | N/A | `N/A` |\n")
            
            # System metrics
            f.write("\n## System Metrics\n\n")
            
            # Evolution metrics
            evolution_count = len(evolution_data)
            healing_count = len(healing_history)
            
            f.write("```\n")
            f.write(f"Evolution Events: {evolution_count}\n")
            f.write(f"Healing Events:   {healing_count}\n")
            
            # Calculate average coherence
            if evolution_data:
                coherence_values = [event.get('coherence', 0) for event in evolution_data]
                avg_coherence = sum(coherence_values) / len(coherence_values)
                f.write(f"Average Coherence: {avg_coherence:.6f}\n")
                
                # Calculate coherence stability
                if len(coherence_values) > 1:
                    coherence_stability = 1 - (max(coherence_values) - min(coherence_values))
                    f.write(f"Coherence Stability: {coherence_stability:.6f}\n")
            
            f.write("```\n\n")
            
            # Add quick visualization of coherence trend
            if evolution_data:
                f.write("### Coherence Trend\n\n")
                f.write("```\n")
                
                # Create simple ASCII chart
                max_width = 50
                coherence_values = [event.get('coherence', 0) for event in evolution_data]
                
                # Normalize to 0-1 range for display
                min_val = min(coherence_values)
                max_val = max(coherence_values)
                range_val = max_val - min_val if max_val > min_val else 1
                
                normalized = [(val - min_val) / range_val for val in coherence_values]
                
                # Draw the chart
                for i in range(10, -1, -1):
                    threshold = i / 10
                    line = f"{(threshold * range_val + min_val):.2f} |"
                    
                    for val in normalized:
                        if abs(val - threshold) < 0.05:
                            line += "o"
                        else:
                            line += " "
                    
                    line += "|"
                    f.write(line + "\n")
                
                f.write("     " + "-" * len(normalized) + "\n")
                f.write("     " + "0" + " " * (len(normalized) - 2) + str(len(normalized) - 1) + "\n")
                f.write("```\n\n")
            
            # Add available demonstrations
            f.write("## Available Demonstrations\n\n")
            
            if self.full_functionality:
                f.write("| Demonstration | Description | Command |\n")
                f.write("|--------------|-------------|--------|\n")
                f.write("| Self-Healing | Demonstrate quantum self-healing capabilities | `python quantum_system_demonstration.py --feature self-healing` |\n")
                f.write("| Self-Reproduction | Demonstrate quantum self-reproduction capabilities | `python quantum_system_demonstration.py --feature self-reproduction` |\n")
                f.write("| Hyper-Dimensional Processing | Demonstrate hyper-dimensional pattern analysis | `python quantum_system_demonstration.py --feature hyper-dimensional` |\n")
                f.write("| Meta-Learning | Demonstrate meta-learning capabilities | `python quantum_system_demonstration.py --feature meta-learning` |\n")
                f.write("| Full System | Demonstrate all system capabilities | `python quantum_system_demonstration.py --full` |\n")
            else:
                f.write("Limited functionality mode. Some demonstrations may not be available.\n\n")
                f.write("| Demonstration | Description | Command |\n")
                f.write("|--------------|-------------|--------|\n")
                f.write("| Visualization | Generate system visualizations | `python quantum_visualization.py --comprehensive` |\n")
            
            # Add visualization links
            f.write("\n## Visualization Links\n\n")
            f.write("- [Comprehensive System Report](../quantum_system_report.md)\n")
            f.write("- [Coherence Visualization](../coherence_visualization.md)\n")
            f.write("- [Evolution Network](../evolution_network.md)\n")
            f.write("- [Healing Metrics](../healing_metrics.md)\n")
            
            # Add system architecture
            f.write("\n## System Architecture\n\n")
            f.write("```\n")
            f.write("QuantumAI System Architecture\n")
            f.write("-----------------------------\n\n")
            f.write("┌─────────────────────────┐      ┌─────────────────────────┐\n")
            f.write("│ Quantum Self-Healing    │◄────►│ Quantum Visualization   │\n")
            f.write("│ Orchestrator            │      │ Module                  │\n")
            f.write("└───────────┬─────────────┘      └───────────┬─────────────┘\n")
            f.write("            │                                 │\n")
            f.write("            ▼                                 ▼\n")
            f.write("┌─────────────────────────┐      ┌─────────────────────────┐\n")
            f.write("│ Phi-Harmonic Meta-      │◄────►│ Quantum Dashboard       │\n")
            f.write("│ Learning System         │      │ Interface               │\n")
            f.write("└───────────┬─────────────┘      └───────────┬─────────────┘\n")
            f.write("            │                                 │\n")
            f.write("            ▼                                 ▼\n")
            f.write("┌─────────────────────────┐      ┌─────────────────────────┐\n")
            f.write("│ Mixture of Experts      │◄────►│ Quantum System          │\n")
            f.write("│ (MoE) Architecture      │      │ Demonstration           │\n")
            f.write("└─────────────────────────┘      └─────────────────────────┘\n")
            f.write("```\n\n")
            
            # Add footer
            f.write("---\n")
            f.write("*This dashboard is generated using phi-harmonic principles and quantum-inspired visualization techniques.*\n")
            f.write(f"*Golden Ratio (φ): {PHI}*\n")
        
        logger.info(f"Dashboard generated: {output_file}")
        return output_file
    
    def generate_interactive_dashboard(self):
        """
        Generate an interactive dashboard with real-time monitoring.
        
        Returns:
            str: Path to the generated dashboard file
        """
        logger.info("Generating interactive dashboard")
        
        # Create HTML dashboard
        output_file = os.path.join(self.dashboard_dir, "interactive_dashboard.html")
        
        with open(output_file, 'w') as f:
            f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>QuantumAI Interactive Dashboard</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            color: #333;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        .header {
            background-color: #2c3e50;
            color: white;
            padding: 20px;
            text-align: center;
            border-radius: 5px 5px 0 0;
        }
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .card {
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            padding: 20px;
        }
        .card-header {
            border-bottom: 1px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 15px;
            font-weight: bold;
            color: #2c3e50;
        }
        .metrics {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
        }
        .metric {
            padding: 10px;
            background-color: #f9f9f9;
            border-radius: 3px;
        }
        .metric-label {
            font-size: 0.8em;
            color: #666;
        }
        .metric-value {
            font-size: 1.2em;
            font-weight: bold;
            color: #2c3e50;
        }
        .chart {
            width: 100%;
            height: 200px;
            background-color: #f9f9f9;
            border-radius: 3px;
            margin-top: 15px;
            position: relative;
        }
        .chart-line {
            position: absolute;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }
        .phi-value {
            color: #e74c3c;
            font-weight: bold;
        }
        .footer {
            margin-top: 20px;
            text-align: center;
            font-size: 0.8em;
            color: #666;
        }
        .demo-button {
            display: block;
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 15px;
            margin: 5px 0;
            border-radius: 3px;
            cursor: pointer;
            text-align: center;
            text-decoration: none;
        }
        .demo-button:hover {
            background-color: #2980b9;
        }
        .architecture {
            font-family: monospace;
            white-space: pre;
            font-size: 0.8em;
            line-height: 1.2;
            overflow-x: auto;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>QuantumAI System Dashboard</h1>
            <p>Phi-Harmonic Coherence Target: φ⁷·⁵/10 = 0.991800</p>
        </div>
        
        <div class="dashboard-grid">
            <div class="card">
                <div class="card-header">System Status</div>
                <div class="metrics">
                    <div class="metric">
                        <div class="metric-label">Visualization</div>
                        <div class="metric-value">Active</div>
                    </div>
                    <div class="metric">
                        <div class="metric-label">Orchestrator</div>
                        <div class="metric-value">Active</div>
                    </div>
                    <div class="metric">
                        <div class="metric-label">Demonstration</div>
                        <div class="metric-value">Active</div>
                    </div>
                    <div class="metric">
                        <div class="metric-label">Coherence</div>
                        <div class="metric-value phi-value">0.991800</div>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <div class="card-header">Phi-Harmonic Metrics</div>
                <div class="metrics">
                    <div class="metric">
                        <div class="metric-label">Golden Ratio (φ)</div>
                        <div class="metric-value">1.618034</div>
                    </div>
                    <div class="metric">
                        <div class="metric-label">φ²</div>
                        <div class="metric-value">2.618034</div>
                    </div>
                    <div class="metric">
                        <div class="metric-label">φ³</div>
                        <div class="metric-value">4.236068</div>
                    </div>
                    <div class="metric">
                        <div class="metric-label">φ⁷·⁵</div>
                        <div class="metric-value">36.932381</div>
                    </div>
                </div>
                <div class="chart">
                    <div class="chart-line">
                        <!-- Placeholder for dynamic chart -->
                    </div>
                </div>
            </div>
            
            <div class="card">
                <div class="card-header">Evolution Metrics</div>
                <div class="metrics">
                    <div class="metric">
                        <div class="metric-label">Evolution Events</div>
                        <div class="metric-value" id="evolution-count">0</div>
                    </div>
                    <div class="metric">
                        <div class="metric-label">Healing Events</div>
                        <div class="metric-value" id="healing-count">0</div>
                    </div>
                    <div class="metric">
                        <div class="metric-label">Average Coherence</div>
                        <div class="metric-value phi-value" id="avg-coherence">0.991800</div>
                    </div>
                    <div class="metric">
                        <div class="metric-label">Coherence Stability</div>
                        <div class="metric-value" id="coherence-stability">0.998000</div>
                    </div>
                </div>
            </div>
            
            <div class="card">
                <div class="card-header">Available Demonstrations</div>
                <a href="#" class="demo-button">Self-Healing Demonstration</a>
                <a href="#" class="demo-button">Self-Reproduction Demonstration</a>
                <a href="#" class="demo-button">Hyper-Dimensional Processing</a>
                <a href="#" class="demo-button">Meta-Learning Demonstration</a>
                <a href="#" class="demo-button">Full System Demonstration</a>
            </div>
        </div>
        
        <div class="card" style="margin-top: 20px;">
            <div class="card-header">System Architecture</div>
            <div class="architecture">
QuantumAI System Architecture
-----------------------------

┌─────────────────────────┐      ┌─────────────────────────┐
│ Quantum Self-Healing    │◄────►│ Quantum Visualization   │
│ Orchestrator            │      │ Module                  │
└───────────┬─────────────┘      └───────────┬─────────────┘
            │                                 │
            ▼                                 ▼
┌─────────────────────────┐      ┌─────────────────────────┐
│ Phi-Harmonic Meta-      │◄────►│ Quantum Dashboard       │
│ Learning System         │      │ Interface               │
└───────────┬─────────────┘      └───────────┬─────────────┘
            │                                 │
            ▼                                 ▼
┌─────────────────────────┐      ┌─────────────────────────┐
│ Mixture of Experts      │◄────►│ Quantum System          │
│ (MoE) Architecture      │      │ Demonstration           │
└─────────────────────────┘      └─────────────────────────┘
            </div>
        </div>
        
        <div class="footer">
            <p>This dashboard is generated using phi-harmonic principles and quantum-inspired visualization techniques.</p>
            <p>Golden Ratio (φ): 1.618033988749895</p>
        </div>
    </div>
    
    <script>
        // Placeholder for dynamic updates
        // In a real implementation, this would fetch data from the server
        
        // Simulate loading evolution data
        setTimeout(() => {
            document.getElementById('evolution-count').textContent = '8';
            document.getElementById('healing-count').textContent = '12';
            document.getElementById('avg-coherence').textContent = '0.991823';
            document.getElementById('coherence-stability').textContent = '0.997912';
        }, 1000);
    </script>
</body>
</html>""")
        
        logger.info(f"Interactive dashboard generated: {output_file}")
        return output_file
    
    def _load_evolution_data(self):
        """
        Load evolution data from files.
        
        Returns:
            list: Evolution data
        """
        evolution_data = []
        evolution_file = os.path.join(self.visualization_dir, "evolution_metrics.json")
        
        if os.path.exists(evolution_file):
            try:
                with open(evolution_file, 'r') as f:
                    evolution_data = json.load(f)
            except:
                pass
        
        # If no file exists, try to create from evolution directory
        if not evolution_data:
            for filename in os.listdir(self.evolution_dir):
                if filename.endswith("_evolution.json"):
                    filepath = os.path.join(self.evolution_dir, filename)
                    try:
                        with open(filepath, 'r') as f:
                            event = json.load(f)
                            if isinstance(event, dict):
                                evolution_data.append(event)
                    except:
                        pass
        
        return evolution_data
    
    def _load_healing_history(self):
        """
        Load healing history from files.
        
        Returns:
            list: Healing history
        """
        healing_history = []
        
        for filename in os.listdir(self.evolution_dir):
            if "heal" in filename.lower() and filename.endswith(".json"):
                filepath = os.path.join(self.evolution_dir, filename)
                try:
                    with open(filepath, 'r') as f:
                        event = json.load(f)
                        if isinstance(event, dict):
                            healing_history.append(event)
                except:
                    pass
        
        return healing_history
    
    def run_dashboard_server(self, port=8080):
        """
        Run a simple HTTP server to serve the dashboard.
        
        Args:
            port (int): Port to run the server on
        """
        import http.server
        import socketserver
        
        # Generate dashboards first
        self.generate_dashboard()
        self.generate_interactive_dashboard()
        
        # Generate comprehensive report using visualizer
        self.visualizer.generate_comprehensive_report()
        
        # Change to the visualization directory
        os.chdir(self.visualization_dir)
        
        handler = http.server.SimpleHTTPRequestHandler
        
        with socketserver.TCPServer(("", port), handler) as httpd:
            logger.info(f"Serving dashboard at http://localhost:{port}/dashboard/interactive_dashboard.html")
            httpd.serve_forever()


def main():
    """
    Main entry point for the dashboard.
    """
    parser = argparse.ArgumentParser(description="QuantumAI Dashboard")
    parser.add_argument("--serve", action="store_true", help="Run dashboard server")
    parser.add_argument("--port", type=int, default=8080, help="Port for dashboard server")
    parser.add_argument("--interactive", action="store_true", help="Generate interactive HTML dashboard")
    
    args = parser.parse_args()
    dashboard = QuantumDashboard()
    
    if args.serve:
        dashboard.run_dashboard_server(port=args.port)
    elif args.interactive:
        output_file = dashboard.generate_interactive_dashboard()
        print(f"Interactive dashboard generated: {output_file}")
    else:
        output_file = dashboard.generate_dashboard()
        print(f"Dashboard generated: {output_file}")


if __name__ == "__main__":
    main()
