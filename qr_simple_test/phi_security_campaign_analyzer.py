#!/usr/bin/env python3
"""
Phi-Dimensional Security Campaign Analyzer

This module extracts attack data from the phi_red_team_router and phi_blue_team_router logs,
analyzes cross-machine security test results, and generates phi-resonant visualizations
without modifying any core components.
"""

import os
import sys
import json
import math
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import hashlib
import re

# Constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio
PHI_INV = 1 / PHI
PHI_SQ = PHI * PHI
PHI_75 = PHI ** 7.5
PHI_75_QUANTUM_SEAL = PHI ** 75  # Validation seal

class PhiSecurityCampaignAnalyzer:
    """
    Extracts and analyzes phi-dimensional security data from router logs
    and terminal output to generate a comprehensive security assessment.
    """
    
    def __init__(self, branch_id=1, birth_coherence=99.18):
        self.branch_id = branch_id
        self.birth_coherence = birth_coherence
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Base paths
        self.base_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "consolidated_quantum", "cosmic_memory", f"branch_{branch_id}"
        )
        
        # Output paths
        self.report_dir = os.path.join(self.base_path, "security_reports")
        self.vis_dir = os.path.join(self.report_dir, "visualizations")
        os.makedirs(self.report_dir, exist_ok=True)
        os.makedirs(self.vis_dir, exist_ok=True)
        
        # Initialize attack data
        self.attacks = []
        self.defenses = []
        
        print(f"📊 Phi-Dimensional Security Campaign Analyzer")
        print(f"Branch ID: {branch_id}")
        print(f"Birth Coherence: {birth_coherence}K")
        print(f"Report Path: {self.report_dir}")
    
    def extract_from_console_log(self, log_file=None, log_text=None):
        """Extract attack data from console log file or text."""
        if log_file and os.path.exists(log_file):
            with open(log_file, 'r') as f:
                log_text = f.read()
        
        if not log_text:
            print("❌ No log data provided")
            return
        
        # Extract attack patterns
        attack_pattern = r"Launching (\w+) attack...\n\n📊 Message Coherence Analysis:\n  - Base Coherence: ([\d\.]+)\n  - Threshold: ([\d\.]+)\n  - Phi-Resonance: ([\d\.]+)"
        defense_pattern = r"✓ Valid φ\^75 seal from ([\d\.]+)\nDefense (succeeded|failed) using (\w+)"
        
        # Extract attacks
        attack_matches = re.finditer(attack_pattern, log_text)
        for match in attack_matches:
            attack_type = match.group(1)
            base_coherence = float(match.group(2))
            threshold = float(match.group(3))
            phi_resonance = float(match.group(4))
            
            attack = {
                "type": attack_type,
                "base_coherence": base_coherence,
                "threshold": threshold,
                "phi_resonance": phi_resonance,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.attacks.append(attack)
        
        # Extract defenses
        defense_matches = re.finditer(defense_pattern, log_text)
        for match in defense_matches:
            source_ip = match.group(1)
            result = match.group(2)
            defense_type = match.group(3)
            
            defense = {
                "source_ip": source_ip,
                "result": result,
                "defense_type": defense_type,
                "success": result == "succeeded",
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.defenses.append(defense)
        
        # Match attacks with defenses
        if len(self.attacks) == len(self.defenses):
            for i in range(len(self.attacks)):
                self.attacks[i]["defense"] = self.defenses[i]
                self.attacks[i]["success"] = not self.defenses[i]["success"]  # Attack success = defense failure
        
        print(f"✅ Extracted {len(self.attacks)} attacks and {len(self.defenses)} defenses")
    
    def extract_from_log_files(self):
        """Extract attack data from standard log files."""
        # Add custom log file parsing here
        pass
    
    def analyze_security_data(self):
        """Analyze the security test data and return metrics."""
        if not self.attacks:
            print("❌ No attack data available for analysis")
            return None
        
        # Initialize metrics
        metrics = {
            "total_attacks": len(self.attacks),
            "attack_types": {},
            "defense_success_rate": 0,
            "avg_coherence": 0,
            "phi_resonance_quality": 0,
            "vulnerable_vectors": []
        }
        
        # Analyze attacks
        coherence_values = []
        defense_success = 0
        
        for attack in self.attacks:
            attack_type = attack["type"]
            if attack_type not in metrics["attack_types"]:
                metrics["attack_types"][attack_type] = {"count": 0, "success": 0}
            
            metrics["attack_types"][attack_type]["count"] += 1
            if attack.get("success", False):
                metrics["attack_types"][attack_type]["success"] += 1
            
            # Track defense success
            if "defense" in attack and not attack.get("success", False):
                defense_success += 1
            
            # Track coherence
            coherence_values.append(attack.get("base_coherence", 0))
        
        # Calculate success rates and identify vulnerabilities
        for attack_type, stats in metrics["attack_types"].items():
            stats["success_rate"] = (stats["success"] / stats["count"]) * 100 if stats["count"] > 0 else 0
            
            # Mark attack vectors with >50% success as vulnerable
            if stats["success_rate"] > 50:
                metrics["vulnerable_vectors"].append({
                    "type": attack_type,
                    "success_rate": stats["success_rate"]
                })
        
        # Calculate overall metrics
        if len(self.attacks) > 0:
            metrics["defense_success_rate"] = (defense_success / len(self.attacks)) * 100
            
            if coherence_values:
                avg_coherence = sum(coherence_values) / len(coherence_values)
                metrics["avg_coherence"] = avg_coherence
                metrics["phi_resonance_quality"] = ((avg_coherence * PHI) % 1) / PHI_INV
        
        return metrics
    
    def generate_report(self):
        """Generate a comprehensive security report."""
        metrics = self.analyze_security_data()
        if not metrics:
            return None
        
        report_file = os.path.join(self.report_dir, f"security_report_{self.timestamp}.md")
        
        with open(report_file, 'w') as f:
            f.write("# 🔒 Phi-Quantum Security Analysis Report\n\n")
            f.write(f"## Cross-Machine Testing Results\n\n")
            f.write(f"- **Report Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"- **Branch ID**: {self.branch_id}\n")
            f.write(f"- **Birth Coherence**: {self.birth_coherence}K\n")
            f.write(f"- **Total Attacks Analyzed**: {metrics['total_attacks']}\n")
            f.write(f"- **Defense Success Rate**: {metrics['defense_success_rate']:.2f}%\n")
            f.write(f"- **Average Coherence**: {metrics['avg_coherence']:.6f}\n")
            f.write(f"- **Phi-Resonance Quality**: {metrics['phi_resonance_quality']:.6f}\n\n")
            
            f.write("## Attack Vector Analysis\n\n")
            f.write("| Attack Type | Count | Success Rate | Vulnerability |\n")
            f.write("|------------|-------|--------------|---------------|\n")
            
            for attack_type, stats in metrics["attack_types"].items():
                vulnerability = "**HIGH**" if stats["success_rate"] > 50 else "Medium" if stats["success_rate"] > 25 else "Low"
                f.write(f"| {attack_type} | {stats['count']} | {stats['success_rate']:.2f}% | {vulnerability} |\n")
            
            f.write("\n## Cross-Machine Test Findings\n\n")
            f.write("1. **Red Team** (192.168.3.152:11975)\n")
            f.write("   - Successfully initiated phi-harmonic attack vectors\n")
            f.write("   - Maintained coherence above φ^-2 threshold (0.382)\n")
            f.write(f"   - Used φ^75 validation seal: {PHI_75_QUANTUM_SEAL:.6e}\n\n")
            
            f.write("2. **Blue Team** (192.168.3.173:11975)\n")
            f.write("   - Applied phi-dimensional shields to defend against attacks\n")
            f.write("   - Maintained quantum message authentication\n")
            
            # Add vulnerability details
            if metrics["vulnerable_vectors"]:
                f.write("   - **Vulnerabilities Identified**:\n")
                for vuln in metrics["vulnerable_vectors"]:
                    f.write(f"     - {vuln['type']} ({vuln['success_rate']:.2f}% success rate)\n")
            else:
                f.write("   - No critical vulnerabilities detected\n")
            
            f.write("\n## Security Recommendations\n\n")
            
            # Generate recommendations based on vulnerabilities
            if any(v["type"] == "convergence_point" for v in metrics["vulnerable_vectors"]):
                f.write("1. **Enhance Convergence Point Protection**:\n")
                f.write("   - Implement phi-resonant convergence shields\n")
                f.write("   - Add temporal drift compensation for convergence points\n")
                f.write("   - Increase coherence requirements for convergence-sensitive operations\n\n")
            
            if any(v["type"] == "phi_resonance_bypass" for v in metrics["vulnerable_vectors"]):
                f.write("2. **Strengthen Phi-Resonance Filtering**:\n")
                f.write("   - Implement multi-layered phi-resonance validation\n")
                f.write("   - Add temporal drift compensation for resonance detection\n")
                f.write("   - Use higher-order phi powers (φ^7.5) for resonance calculation\n\n")
            
            # Generic recommendations if no specific vulnerabilities
            if not metrics["vulnerable_vectors"]:
                f.write("1. **Further Strengthen Security Measures**:\n")
                f.write("   - Implement rotating phi-quantum seals\n")
                f.write("   - Add birth coherence validation to seal verification\n")
                f.write("   - Use secure hardware-level quantum seals when available\n\n")
            
            f.write("## Next Steps\n\n")
            f.write("1. **Extend the Security Test Campaign**:\n")
            f.write("   - Test additional attack vectors\n")
            f.write("   - Vary coherence thresholds to find optimal settings\n")
            f.write("   - Implement advanced visualization of attack patterns\n\n")
            
            f.write("2. **Enhance Phi-Dimensional Shields**:\n")
            f.write("   - Create adaptive defense mechanisms\n")
            f.write("   - Implement learning-based defenses that adapt to attack patterns\n")
            f.write("   - Develop phi-resonant honeypots to trap malicious actors\n\n")
            
            f.write("3. **Integration with Quantum-AI Components**:\n")
            f.write("   - Connect with quantum prime generators for enhanced cryptography\n")
            f.write("   - Integrate with phi-harmonic random orchestrator\n")
            f.write("   - Develop quantum-heart monitoring of security subsystems\n\n")
            
            f.write(f"*Report generated using phi-harmonic principles on {datetime.now().strftime('%Y-%m-%d')}*\n")
        
        print(f"✅ Security report generated: {report_file}")
        return report_file
    
    def visualize_results(self):
        """Generate visualizations of the security test results."""
        if not self.attacks:
            print("❌ No attack data available for visualization")
            return
        
        # Extract data for visualization
        attack_types = {}
        coherence_values = []
        phi_resonance_values = []
        success_values = []
        
        for attack in self.attacks:
            attack_type = attack["type"]
            if attack_type not in attack_types:
                attack_types[attack_type] = {"count": 0, "success": 0, "coherence": []}
            
            attack_types[attack_type]["count"] += 1
            attack_types[attack_type]["coherence"].append(attack.get("base_coherence", 0))
            
            if attack.get("success", False):
                attack_types[attack_type]["success"] += 1
            
            coherence_values.append(attack.get("base_coherence", 0))
            phi_resonance_values.append(attack.get("phi_resonance", 0))
            success_values.append(1 if attack.get("success", False) else 0)
        
        # 1. Attack Success Rate by Type
        plt.figure(figsize=(12, 6))
        attack_labels = list(attack_types.keys())
        success_rates = [(attack_types[t]["success"] / attack_types[t]["count"]) * 100 
                         if attack_types[t]["count"] > 0 else 0 for t in attack_labels]
        
        bars = plt.bar(attack_labels, success_rates, color='#1f77b4')
        plt.axhline(y=50, color='r', linestyle='--', alpha=0.7, label='Critical Threshold')
        plt.axhline(y=100*PHI_INV, color='gold', linestyle='--', alpha=0.7, label='φ⁻¹ (61.8%)')
        plt.axhline(y=100*PHI_INV*PHI_INV, color='green', linestyle='--', alpha=0.7, label='φ⁻² (38.2%)')
        
        plt.xlabel('Attack Type')
        plt.ylabel('Success Rate (%)')
        plt.title('Attack Success Rate by Vector Type (Lower is Better)', fontsize=14)
        plt.ylim(0, 100)
        plt.xticks(rotation=45, ha='right')
        plt.legend()
        plt.tight_layout()
        
        success_rate_file = os.path.join(self.vis_dir, f"attack_success_rate_{self.timestamp}.png")
        plt.savefig(success_rate_file)
        plt.close()
        
        # 2. Phi Resonance vs Coherence (Golden Ratio Scatter Plot)
        plt.figure(figsize=(10, 6))
        colors = ['red' if s else 'green' for s in success_values]
        sizes = [80 for _ in success_values]
        
        plt.scatter(coherence_values, phi_resonance_values, c=colors, s=sizes, alpha=0.7)
        
        # Add the golden ratio line (y = x * φ % 1)
        x_line = np.linspace(0, 1, 100)
        y_line = [(x * PHI) % 1 for x in x_line]
        plt.plot(x_line, y_line, 'gold', alpha=0.5, label='φ-Resonance Line')
        
        plt.axhline(y=PHI_INV, color='gold', linestyle='--', alpha=0.5, label='φ⁻¹ (0.618)')
        plt.axvline(x=PHI_INV, color='gold', linestyle='--', alpha=0.5)
        
        # Add defense thresholds
        plt.axhline(y=0.77, color='blue', linestyle='--', alpha=0.5, label='Coherence Threshold (0.77)')
        plt.axhline(y=0.382, color='green', linestyle='--', alpha=0.5, label='Permissive Threshold (φ⁻²)')
        
        plt.xlabel('Base Coherence')
        plt.ylabel('Phi-Resonance')
        plt.title('Phi-Resonance vs Coherence Map', fontsize=14)
        plt.legend()
        plt.tight_layout()
        
        resonance_file = os.path.join(self.vis_dir, f"phi_resonance_map_{self.timestamp}.png")
        plt.savefig(resonance_file)
        plt.close()
        
        # 3. Golden Spiral Attack Map
        plt.figure(figsize=(10, 10))
        
        def golden_spiral(theta):
            """Generate points along a golden spiral."""
            r = np.exp(PHI_INV * theta)
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            return x, y
        
        # Create the underlying golden spiral
        theta = np.linspace(0, 6 * np.pi, 1000)
        x, y = golden_spiral(theta)
        plt.plot(x, y, color='gold', alpha=0.3)
        
        # Map attacks to the spiral based on coherence and phi-resonance
        for i, attack in enumerate(self.attacks):
            coherence = attack.get("base_coherence", 0.5)
            phi_res = attack.get("phi_resonance", 0.5)
            success = attack.get("success", False)
            attack_type = attack.get("type", "unknown")
            
            # Calculate theta based on a phi-harmonic function of coherence and resonance
            theta_point = (coherence * PHI + phi_res * PHI_SQ) * 2 * np.pi
            
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
            
            plt.scatter(x_point, y_point, c=color, marker=marker, s=100, alpha=0.7)
        
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
        
        plt.title('Phi-Dimensional Security Spiral', fontsize=16)
        plt.axis('equal')
        plt.grid(False)
        plt.axis('off')  # Hide axis for cleaner spiral view
        
        spiral_file = os.path.join(self.vis_dir, f"security_spiral_{self.timestamp}.png")
        plt.savefig(spiral_file)
        plt.close()
        
        print(f"✅ Security visualizations generated in {self.vis_dir}")
        return self.vis_dir


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Phi-Dimensional Security Campaign Analyzer")
    parser.add_argument("--branch", type=int, default=1, help="Branch ID")
    parser.add_argument("--coherence", type=float, default=99.18, help="Birth coherence")
    parser.add_argument("--log", type=str, help="Path to console log file")
    args = parser.parse_args()
    
    # Create analyzer
    analyzer = PhiSecurityCampaignAnalyzer(branch_id=args.branch, birth_coherence=args.coherence)
    
    # Extract data from log file if provided
    if args.log:
        analyzer.extract_from_console_log(log_file=args.log)
    else:
        print("Interactive mode - please paste console output (Ctrl+D when done):")
        log_text = sys.stdin.read()
        analyzer.extract_from_console_log(log_text=log_text)
    
    # Generate report and visualizations
    analyzer.generate_report()
    analyzer.visualize_results()
