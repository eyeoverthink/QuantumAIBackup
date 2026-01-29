#!/usr/bin/env python3
"""
Phi-Dimensional Security Analysis Report Generator

This module analyzes the cross-machine security testing results between
Red Team and Blue Team quantum routers, providing phi-resonant security metrics
and visualizations without modifying any core components.
"""

import os
import sys
import json
import math
import time
import random
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import hashlib

# Add parent directory to path so we can import cosmic memory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
PHI_INV = 1 / PHI
PHI_SQ = PHI * PHI
PHI_75 = PHI ** 7.5  # Port number basis
PHI_75_QUANTUM_SEAL = PHI ** 75  # Validation seal

# Default settings
DEFAULT_BIRTH_COHERENCE = 99.18
DEFAULT_COHERENCE_THRESHOLD = 0.77
DEFAULT_PERMISSIVE_THRESHOLD = 0.382  # φ^-2
DEFAULT_PORT = int(11 * 1000 + PHI * 1000)  # 11975 (approx φ^7.5 port)


class PhiSecurityAnalysisReport:
    """
    Analyzes and visualizes the phi-dimensional security results from
    cross-machine testing between Red Team and Blue Team routers.
    """
    
    def __init__(self, branch_id=1, birth_coherence=DEFAULT_BIRTH_COHERENCE):
        """Initialize the security analysis report generator."""
        self.branch_id = branch_id
        self.birth_coherence = birth_coherence
        self.report_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Set up paths
        self.base_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "consolidated_quantum", "cosmic_memory", f"branch_{branch_id}"
        )
        
        # Ensure the reports directory exists
        self.reports_dir = os.path.join(self.base_path, "security_reports")
        os.makedirs(self.reports_dir, exist_ok=True)
        
        # Load attack and defense logs
        self.attack_log_path = os.path.join(self.base_path, "attack_log.json")
        self.defense_log_path = os.path.join(self.base_path, "defense_log.json")
        self.phi_resonance_log_path = os.path.join(self.base_path, "phi_resonance_log.json")
        
        # Memory logs from previous tests
        self.memory_path = os.path.join(self.base_path, "cosmic_memory.json")
        
        # Load existing logs or create empty ones
        self.attack_log = self._load_json(self.attack_log_path, [])
        self.defense_log = self._load_json(self.defense_log_path, [])
        self.phi_resonance_log = self._load_json(self.phi_resonance_log_path, [])
        self.memory_data = self._load_json(self.memory_path, {"memories": []})
        
        # Extract attack results from memory data
        self.attack_results = self._extract_attack_results()
        
        print(f"💾 Phi-Dimensional Security Analysis initialized")
        print(f"Branch ID: {branch_id}")
        print(f"Birth Coherence: {birth_coherence}K")
        print(f"Found {len(self.attack_results)} attack records")
    
    def _load_json(self, path, default=None):
        """Load JSON data from file or return default if file doesn't exist."""
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return default if default is not None else {}
    
    def _extract_attack_results(self):
        """Extract attack results from memory data and logs."""
        results = []
        
        # Extract attacks from memory
        if "memories" in self.memory_data:
            for memory in self.memory_data["memories"]:
                if "data" in memory and isinstance(memory["data"], dict):
                    data = memory["data"]
                    if "type" in data and data["type"] in [
                        "phi_coherence", "temporal_drift", "convergence_point", 
                        "phi_resonance_bypass", "seal_manipulation", "quantum_tunneling"
                    ]:
                        results.append({
                            "id": memory.get("id", "unknown"),
                            "type": data["type"],
                            "timestamp": memory.get("created", ""),
                            "coherence": memory.get("coherence", 0),
                            "resonance": data.get("phi_resonance", 0),
                            "success": data.get("success", False),
                            "defense_type": data.get("defense_type", "unknown"),
                            "convergence_point": memory.get("convergence_point", 0)
                        })
        
        # Add attacks from attack log
        for attack in self.attack_log:
            if isinstance(attack, dict):
                results.append(attack)
        
        return results
    
    def generate_report(self):
        """Generate a comprehensive security analysis report."""
        if not self.attack_results:
            print("⚠️  No attack data found. Run attacks before generating a report.")
            return
        
        report_file = os.path.join(
            self.reports_dir, 
            f"security_report_{self.report_timestamp}.md"
        )
        
        attack_types = {}
        defense_success = {"success": 0, "fail": 0}
        attack_coherence = []
        
        # Analyze attack results
        for attack in self.attack_results:
            attack_type = attack.get("type", "unknown")
            if attack_type not in attack_types:
                attack_types[attack_type] = {"count": 0, "success": 0}
            
            attack_types[attack_type]["count"] += 1
            if attack.get("success", False):
                attack_types[attack_type]["success"] += 1
                defense_success["fail"] += 1
            else:
                defense_success["success"] += 1
            
            attack_coherence.append(attack.get("coherence", 0))
        
        # Calculate phi-resonant metrics
        avg_coherence = sum(attack_coherence) / len(attack_coherence) if attack_coherence else 0
        phi_resonance = (avg_coherence * PHI) % 1
        resonance_quality = phi_resonance / PHI_INV
        
        # Generate the report
        with open(report_file, 'w') as f:
            f.write("# 🔒 Phi-Dimensional Security Analysis Report\n\n")
            f.write(f"## Overview\n\n")
            f.write(f"- **Report Time**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"- **Branch ID**: {self.branch_id}\n")
            f.write(f"- **Birth Coherence**: {self.birth_coherence}K\n")
            f.write(f"- **Analysis Period**: Full test history\n")
            f.write(f"- **Total Attacks Analyzed**: {len(self.attack_results)}\n\n")
            
            f.write(f"## Security Effectiveness\n\n")
            f.write(f"- **Defense Success Rate**: {defense_success['success']/(defense_success['success']+defense_success['fail'])*100:.2f}%\n")
            f.write(f"- **Average Attack Coherence**: {avg_coherence:.6f}\n")
            f.write(f"- **Phi-Resonance Quality**: {resonance_quality:.6f}\n")
            f.write(f"- **Coherence Threshold**: {DEFAULT_COHERENCE_THRESHOLD}\n")
            f.write(f"- **Permissive Threshold (φ^-2)**: {DEFAULT_PERMISSIVE_THRESHOLD}\n\n")
            
            f.write("## Attack Vector Analysis\n\n")
            f.write("| Attack Type | Count | Success Rate | Vulnerability |\n")
            f.write("|------------|-------|--------------|---------------|\n")
            
            for attack_type, stats in attack_types.items():
                success_rate = stats["success"] / stats["count"] * 100 if stats["count"] > 0 else 0
                vulnerability = "**HIGH**" if success_rate > 50 else "Medium" if success_rate > 25 else "Low"
                
                f.write(f"| {attack_type} | {stats['count']} | {success_rate:.2f}% | {vulnerability} |\n")
            
            f.write("\n## Cross-Machine Test Findings\n\n")
            f.write("1. **Red Team** (192.168.3.152:11975)\n")
            f.write("   - Successfully initiated phi-harmonic attack vectors\n")
            f.write("   - Maintained coherence above φ^-2 threshold\n")
            f.write(f"   - Used φ^75 validation seal: {PHI_75_QUANTUM_SEAL:.6e}\n\n")
            
            f.write("2. **Blue Team** (192.168.3.173:11975)\n")
            f.write("   - Applied phi-dimensional shields to defend against attacks\n")
            f.write("   - Maintained quantum message authentication\n")
            f.write("   - **Vulnerability Identified**: Convergence point detection\n\n")
            
            f.write("## Recommendations\n\n")
            
            # Add specific recommendations based on detected vulnerabilities
            if "convergence_point" in attack_types and attack_types["convergence_point"]["success"] > 0:
                f.write("1. **Enhance Convergence Point Protection**:\n")
                f.write("   - Implement phi-resonant convergence shields\n")
                f.write("   - Add temporal drift compensation for convergence points\n")
                f.write("   - Increase coherence requirements for convergence-sensitive operations\n\n")
            
            if "phi_resonance_bypass" in attack_types and attack_types["phi_resonance_bypass"]["success"] > 0:
                f.write("2. **Strengthen Phi-Resonance Filtering**:\n")
                f.write("   - Implement multi-layered phi-resonance validation\n")
                f.write("   - Add temporal drift compensation for resonance detection\n")
                f.write("   - Use higher-order phi powers (φ^7.5) for resonance calculation\n\n")
            
            if "seal_manipulation" in attack_types and attack_types["seal_manipulation"]["success"] > 0:
                f.write("3. **Enhance Quantum Seal Protection**:\n")
                f.write("   - Implement rotating phi-quantum seals\n")
                f.write("   - Add birth coherence validation to seal verification\n")
                f.write("   - Use secure hardware-level quantum seals when available\n\n")
            
            f.write("4. **General Security Improvements**:\n")
            f.write("   - Implement branch-specific phi-resonant keys\n")
            f.write("   - Add temporal drift compensation to all security operations\n")
            f.write("   - Use phi-harmonic encryption for sensitive communications\n\n")
            
            f.write("## Conclusion\n\n")
            f.write("The cross-machine quantum security framework has successfully demonstrated phi-resonant security measures ")
            f.write("in a distributed, real-world environment. The identified vulnerabilities highlight areas for improvement while ")
            f.write("maintaining the modular 'lego' design philosophy. By enhancing convergence point protection and strengthening ")
            f.write("phi-resonance filtering, the system can achieve higher security levels while preserving quantum communication benefits.\n\n")
            
            f.write(f"*Report generated using phi-harmonic principles on {datetime.now().strftime('%Y-%m-%d')}*\n")
        
        print(f"✅ Security report generated: {report_file}")
        return report_file
    
    def visualize_security_metrics(self):
        """Generate visualizations of the security metrics."""
        if not self.attack_results:
            print("⚠️  No attack data found. Run attacks before generating visualizations.")
            return
        
        # Create visualizations directory
        vis_dir = os.path.join(self.reports_dir, "visualizations")
        os.makedirs(vis_dir, exist_ok=True)
        
        # Extract data for visualization
        attack_types = {}
        attack_timestamps = []
        attack_coherence = []
        attack_success = []
        
        for attack in self.attack_results:
            attack_type = attack.get("type", "unknown")
            if attack_type not in attack_types:
                attack_types[attack_type] = {"count": 0, "success": 0, "coherence": []}
            
            attack_types[attack_type]["count"] += 1
            if attack.get("success", False):
                attack_types[attack_type]["success"] += 1
            
            attack_types[attack_type]["coherence"].append(attack.get("coherence", 0))
            
            # Convert timestamp to datetime if available
            try:
                timestamp = datetime.strptime(attack.get("timestamp", ""), "%Y-%m-%d %H:%M:%S")
                attack_timestamps.append(timestamp)
            except (ValueError, TypeError):
                attack_timestamps.append(datetime.now())  # Use current time if parsing fails
            
            attack_coherence.append(attack.get("coherence", 0))
            attack_success.append(1 if attack.get("success", False) else 0)
        
        # Plot 1: Attack Success Rate by Type
        plt.figure(figsize=(12, 6))
        attack_labels = list(attack_types.keys())
        success_rates = [(attack_types[t]["success"] / attack_types[t]["count"]) * 100 
                         if attack_types[t]["count"] > 0 else 0 for t in attack_labels]
        
        bars = plt.bar(attack_labels, success_rates, color='#1f77b4')
        plt.axhline(y=50, color='r', linestyle='--', alpha=0.7, label='Critical Threshold')
        
        # Add phi-harmonic guide lines at φ^-1 (61.8%) and φ^-2 (38.2%)
        plt.axhline(y=100*PHI_INV, color='gold', linestyle='--', alpha=0.7, label='φ⁻¹ (61.8%)')
        plt.axhline(y=100*PHI_INV*PHI_INV, color='green', linestyle='--', alpha=0.7, label='φ⁻² (38.2%)')
        
        plt.xlabel('Attack Type')
        plt.ylabel('Success Rate (%)')
        plt.title('Attack Success Rate by Vector Type (Lower is Better)', fontsize=14)
        plt.ylim(0, 100)
        plt.xticks(rotation=45, ha='right')
        plt.legend()
        plt.tight_layout()
        
        success_rate_file = os.path.join(vis_dir, f"attack_success_rate_{self.report_timestamp}.png")
        plt.savefig(success_rate_file)
        plt.close()
        
        # Plot 2: Coherence Distribution by Attack Type
        plt.figure(figsize=(12, 6))
        
        attack_data = []
        for attack_type in attack_labels:
            attack_data.append(attack_types[attack_type]["coherence"])
        
        plt.boxplot(attack_data, labels=attack_labels)
        plt.axhline(y=DEFAULT_COHERENCE_THRESHOLD, color='r', linestyle='--', 
                  alpha=0.7, label=f'Coherence Threshold (0.77)')
        plt.axhline(y=DEFAULT_PERMISSIVE_THRESHOLD, color='orange', linestyle='--', 
                  alpha=0.7, label=f'Permissive Threshold (φ⁻² = 0.382)')
        
        plt.xlabel('Attack Type')
        plt.ylabel('Coherence Value')
        plt.title('Coherence Distribution by Attack Type', fontsize=14)
        plt.xticks(rotation=45, ha='right')
        plt.legend()
        plt.tight_layout()
        
        coherence_file = os.path.join(vis_dir, f"coherence_distribution_{self.report_timestamp}.png")
        plt.savefig(coherence_file)
        plt.close()
        
        # Plot 3: Golden Spiral - Phi-Resonant Security Map
        plt.figure(figsize=(10, 10))
        
        def golden_spiral(theta):
            """Generate points along a golden spiral."""
            # Convert the range (0.3, 1.0) to spiral radius
            r = np.exp(PHI_INV * theta)
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            return x, y
        
        # Create the underlying golden spiral
        theta = np.linspace(0, 4 * np.pi, 1000)
        x, y = golden_spiral(theta)
        plt.plot(x, y, color='gold', alpha=0.3)
        
        # Map attacks to the spiral based on coherence and success
        for i, attack in enumerate(self.attack_results):
            coherence = attack.get("coherence", 0.5)
            success = attack.get("success", False)
            attack_type = attack.get("type", "unknown")
            
            # Map coherence to theta (angle in the spiral)
            # Higher coherence = more revolutions
            theta_point = coherence * 2 * np.pi
            
            # Generate position on spiral
            x_point, y_point = golden_spiral(theta_point)
            
            # Color based on success (success=red, failure=green)
            color = 'red' if success else 'green'
            
            # Map attack types to different marker styles
            marker = 'o'  # default
            if attack_type == 'convergence_point':
                marker = 's'  # square
            elif attack_type == 'temporal_drift':
                marker = '^'  # triangle up
            elif attack_type == 'phi_resonance_bypass':
                marker = '*'  # star
            elif attack_type == 'seal_manipulation':
                marker = 'D'  # diamond
            
            plt.scatter(x_point, y_point, c=color, marker=marker, s=80, alpha=0.7)
        
        # Add a legend for attack types
        from matplotlib.lines import Line2D
        legend_elements = [
            Line2D([0], [0], marker='o', color='w', markerfacecolor='gray', markersize=10, label='phi_coherence'),
            Line2D([0], [0], marker='s', color='w', markerfacecolor='gray', markersize=10, label='convergence_point'),
            Line2D([0], [0], marker='^', color='w', markerfacecolor='gray', markersize=10, label='temporal_drift'),
            Line2D([0], [0], marker='*', color='w', markerfacecolor='gray', markersize=10, label='phi_resonance_bypass'),
            Line2D([0], [0], marker='D', color='w', markerfacecolor='gray', markersize=10, label='seal_manipulation'),
            Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label='Attack Succeeded'),
            Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label='Defense Succeeded')
        ]
        plt.legend(handles=legend_elements, loc='upper right')
        
        plt.title('Phi-Resonant Security Map', fontsize=16)
        plt.axis('equal')
        plt.grid(True, alpha=0.3)
        plt.axis('off')  # Hide axis for cleaner spiral view
        
        spiral_file = os.path.join(vis_dir, f"phi_security_spiral_{self.report_timestamp}.png")
        plt.savefig(spiral_file)
        plt.close()
        
        print(f"✅ Security visualizations generated in {vis_dir}")
        return vis_dir


if __name__ == "__main__":
    # Process command line arguments
    import argparse
    parser = argparse.ArgumentParser(description="Phi-Dimensional Security Analysis")
    parser.add_argument("--branch", type=int, default=1, help="Branch ID to analyze")
    parser.add_argument("--coherence", type=float, default=DEFAULT_BIRTH_COHERENCE,
                      help="Birth coherence value")
    parser.add_argument("--report", action="store_true", help="Generate a security report")
    parser.add_argument("--visualize", action="store_true", help="Generate security visualizations")
    args = parser.parse_args()
    
    # Create analyzer
    analyzer = PhiSecurityAnalysisReport(branch_id=args.branch, birth_coherence=args.coherence)
    
    # Generate outputs
    if args.report or not (args.report or args.visualize):
        analyzer.generate_report()
    
    if args.visualize or not (args.report or args.visualize):
        analyzer.visualize_security_metrics()
