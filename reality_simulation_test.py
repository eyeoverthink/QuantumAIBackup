"""
Reality Simulation Test - Phi-Harmonic Evidence Detector
Tests whether fundamental physical constants show evidence of phi-harmonic encoding
that would suggest a computational nature to reality
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Constants
PHI = (1 + np.sqrt(5)) / 2  # Golden ratio
PHI_INV = 1 / PHI  # Golden ratio inverse

# Physical constants (values from NIST)
PHYSICAL_CONSTANTS = {
    'c': 299792458,  # Speed of light in vacuum (m/s)
    'G': 6.67430e-11,  # Gravitational constant (m^3 kg^-1 s^-2)
    'h': 6.62607015e-34,  # Planck constant (J Hz^-1)
    'e': 1.602176634e-19,  # Elementary charge (C)
    'me': 9.1093837015e-31,  # Electron mass (kg)
    'mp': 1.67262192369e-27,  # Proton mass (kg)
    'alpha': 7.2973525693e-3,  # Fine-structure constant
    'mu0': 1.25663706212e-6,  # Magnetic constant (N A^-2)
    'epsilon0': 8.8541878128e-12,  # Electric constant (F m^-1)
    'k': 1.380649e-23,  # Boltzmann constant (J K^-1)
    'Na': 6.02214076e23,  # Avogadro constant (mol^-1)
    'R': 8.314462618,  # Gas constant (J mol^-1 K^-1)
    'sigma': 5.670374419e-8,  # Stefan-Boltzmann constant (W m^-2 K^-4)
    'Ry': 10973731.568160,  # Rydberg constant (m^-1)
}

class RealitySimulationTest:
    """Tests whether reality shows evidence of being a simulation with phi-harmonic encoding"""
    
    def __init__(self):
        self.phi_relationships = []
        self.digital_patterns = []
        self.simulation_evidence = []
    
    def _check_phi_relationships(self):
        """Check for phi-harmonic relationships between physical constants"""
        constants = list(PHYSICAL_CONSTANTS.items())
        relationships = []
        
        for i in range(len(constants)):
            for j in range(i+1, len(constants)):
                name1, value1 = constants[i]
                name2, value2 = constants[j]
                
                # Calculate ratio
                ratio = abs(value1 / value2)
                log_ratio = np.log10(ratio)
                
                # Check for phi-related patterns
                phi_patterns = [
                    (PHI, "φ"),
                    (PHI_INV, "1/φ"),
                    (PHI**2, "φ²"),
                    (PHI_INV**2, "1/φ²"),
                    (PHI**3, "φ³"),
                    (PHI_INV**3, "1/φ³"),
                    (PHI**5, "φ⁵"),
                    (PHI**8, "φ⁸"),
                    (np.pi*PHI, "πφ"),
                    (np.e*PHI, "eφ")
                ]
                
                for pattern_value, pattern_name in phi_patterns:
                    # Check if ratio is close to a phi pattern
                    if abs(ratio - pattern_value) / pattern_value < 0.01:
                        relationships.append({
                            'constant1': name1,
                            'constant2': name2,
                            'value1': value1,
                            'value2': value2,
                            'ratio': ratio,
                            'pattern': pattern_name,
                            'pattern_value': pattern_value,
                            'accuracy': 100 * (1 - abs(ratio - pattern_value) / pattern_value)
                        })
                    
                    # Also check if the log ratio is close to a phi pattern
                    # This would indicate a power relationship
                    if abs(log_ratio - pattern_value) / pattern_value < 0.05:
                        relationships.append({
                            'constant1': name1,
                            'constant2': name2,
                            'value1': value1,
                            'value2': value2,
                            'log_ratio': log_ratio,
                            'pattern': f"log10(ratio) ≈ {pattern_name}",
                            'pattern_value': pattern_value,
                            'accuracy': 100 * (1 - abs(log_ratio - pattern_value) / pattern_value)
                        })
        
        self.phi_relationships = relationships
        return relationships
    
    def _check_digital_encoding(self):
        """Check for digital encoding patterns in physical constants"""
        digital_patterns = []
        
        for name, value in PHYSICAL_CONSTANTS.items():
            # Convert to string and look for patterns
            value_str = str(value)
            
            # Check for repeating digits
            for i in range(len(value_str) - 3):
                if value_str[i] == value_str[i+2] and value_str[i+1] == value_str[i+3]:
                    digital_patterns.append({
                        'constant': name,
                        'value': value,
                        'pattern_type': 'repeating_digits',
                        'pattern': value_str[i:i+4],
                        'position': i
                    })
            
            # Check for phi in digits
            phi_str = str(PHI).replace('.', '')
            for i in range(len(value_str) - 4):
                if value_str[i:i+5] in phi_str:
                    digital_patterns.append({
                        'constant': name,
                        'value': value,
                        'pattern_type': 'phi_digits',
                        'pattern': value_str[i:i+5],
                        'position': i
                    })
            
            # Check for binary-like patterns (alternating digits)
            for i in range(len(value_str) - 5):
                if (value_str[i] == value_str[i+2] == value_str[i+4] and 
                    value_str[i+1] == value_str[i+3] == value_str[i+5] and
                    value_str[i] != value_str[i+1]):
                    digital_patterns.append({
                        'constant': name,
                        'value': value,
                        'pattern_type': 'binary_pattern',
                        'pattern': value_str[i:i+6],
                        'position': i
                    })
        
        self.digital_patterns = digital_patterns
        return digital_patterns
    
    def _check_simulation_evidence(self):
        """Check for specific evidence that would suggest a simulated reality"""
        evidence = []
        
        # Check 1: Are there more phi-harmonic relationships than would be expected by chance?
        expected_by_chance = len(PHYSICAL_CONSTANTS) * (len(PHYSICAL_CONSTANTS) - 1) / 2 * 0.01
        actual_relationships = len(self.phi_relationships)
        
        if actual_relationships > expected_by_chance:
            evidence.append({
                'type': 'statistical',
                'description': 'More phi-harmonic relationships than expected by chance',
                'expected': expected_by_chance,
                'actual': actual_relationships,
                'significance': actual_relationships / expected_by_chance
            })
        
        # Check 2: Do the most fundamental constants show phi-harmonic relationships?
        fundamental_constants = ['c', 'h', 'G', 'alpha']
        fundamental_relationships = [r for r in self.phi_relationships 
                                    if r['constant1'] in fundamental_constants 
                                    and r['constant2'] in fundamental_constants]
        
        if fundamental_relationships:
            evidence.append({
                'type': 'fundamental',
                'description': 'Phi-harmonic relationships between fundamental constants',
                'relationships': fundamental_relationships,
                'count': len(fundamental_relationships)
            })
        
        # Check 3: Is there a pattern to the digital encodings?
        if len(self.digital_patterns) > len(PHYSICAL_CONSTANTS) * 0.1:
            evidence.append({
                'type': 'digital',
                'description': 'Unusual number of digital patterns in physical constants',
                'count': len(self.digital_patterns),
                'expected': len(PHYSICAL_CONSTANTS) * 0.1
            })
        
        # Check 4: Fine-structure constant (alpha) is particularly important
        # It's dimensionless and determines the strength of electromagnetic interactions
        alpha_value = PHYSICAL_CONSTANTS['alpha']
        alpha_phi_ratio = alpha_value / (PHI_INV**3)
        
        if abs(alpha_phi_ratio - 1) < 0.1:
            evidence.append({
                'type': 'alpha_phi',
                'description': 'Fine-structure constant shows relationship to phi',
                'alpha': alpha_value,
                'phi_relationship': f"α ≈ 1/φ³",
                'accuracy': 100 * (1 - abs(alpha_phi_ratio - 1))
            })
        
        self.simulation_evidence = evidence
        return evidence
    
    def run_tests(self):
        """Run all tests for simulation evidence"""
        print("Running Reality Simulation Tests...")
        
        # Check for phi-harmonic relationships
        phi_relationships = self._check_phi_relationships()
        print(f"Found {len(phi_relationships)} phi-harmonic relationships between physical constants")
        
        # Check for digital encoding
        digital_patterns = self._check_digital_encoding()
        print(f"Found {len(digital_patterns)} digital encoding patterns in physical constants")
        
        # Check for simulation evidence
        simulation_evidence = self._check_simulation_evidence()
        print(f"Found {len(simulation_evidence)} pieces of evidence suggesting a simulated reality")
        
        return {
            'phi_relationships': phi_relationships,
            'digital_patterns': digital_patterns,
            'simulation_evidence': simulation_evidence
        }
    
    def visualize_results(self, save_path='reality_simulation_test.png'):
        """Visualize the test results"""
        plt.figure(figsize=(15, 10))
        
        # Plot phi-harmonic relationships
        plt.subplot(2, 2, 1)
        if self.phi_relationships:
            # Group by pattern type
            patterns = {}
            for rel in self.phi_relationships:
                pattern = rel['pattern']
                if pattern not in patterns:
                    patterns[pattern] = 0
                patterns[pattern] += 1
            
            # Plot
            plt.bar(patterns.keys(), patterns.values())
            plt.title(f'Phi-Harmonic Relationships ({len(self.phi_relationships)} total)')
            plt.xticks(rotation=45, ha='right')
            plt.ylabel('Count')
        else:
            plt.text(0.5, 0.5, 'No phi-harmonic relationships found', 
                    ha='center', va='center', fontsize=12)
            plt.axis('off')
        
        # Plot digital patterns
        plt.subplot(2, 2, 2)
        if self.digital_patterns:
            # Group by pattern type
            pattern_types = {}
            for pattern in self.digital_patterns:
                ptype = pattern['pattern_type']
                if ptype not in pattern_types:
                    pattern_types[ptype] = 0
                pattern_types[ptype] += 1
            
            # Plot
            plt.bar(pattern_types.keys(), pattern_types.values())
            plt.title(f'Digital Encoding Patterns ({len(self.digital_patterns)} total)')
            plt.xticks(rotation=45, ha='right')
            plt.ylabel('Count')
        else:
            plt.text(0.5, 0.5, 'No digital encoding patterns found', 
                    ha='center', va='center', fontsize=12)
            plt.axis('off')
        
        # Plot simulation evidence
        plt.subplot(2, 2, 3)
        if self.simulation_evidence:
            # Group by evidence type
            evidence_types = {}
            for evidence in self.simulation_evidence:
                etype = evidence['type']
                if etype not in evidence_types:
                    evidence_types[etype] = 0
                evidence_types[etype] += 1
            
            # Plot
            plt.bar(evidence_types.keys(), evidence_types.values(), color='red')
            plt.title(f'Simulation Evidence ({len(self.simulation_evidence)} pieces)')
            plt.xticks(rotation=45, ha='right')
            plt.ylabel('Count')
        else:
            plt.text(0.5, 0.5, 'No simulation evidence found', 
                    ha='center', va='center', fontsize=12)
            plt.axis('off')
        
        # Plot simulation probability
        plt.subplot(2, 2, 4)
        
        # Calculate simulation probability based on evidence
        if self.simulation_evidence:
            # Weight different types of evidence
            weights = {
                'statistical': 0.3,
                'fundamental': 0.4,
                'digital': 0.2,
                'alpha_phi': 0.5
            }
            
            # Calculate weighted probability
            probability = 0
            for evidence in self.simulation_evidence:
                etype = evidence['type']
                if etype in weights:
                    probability += weights[etype]
            
            # Cap at 100%
            probability = min(probability, 1.0)
            
            # Plot gauge chart
            theta = np.linspace(0, 180, 100) * np.pi / 180
            r = 1
            
            # Convert to cartesian
            x = r * np.cos(theta)
            y = r * np.sin(theta)
            
            # Plot gauge background
            plt.plot(x, y, 'k-')
            
            # Plot probability indicator
            prob_theta = probability * 180 * np.pi / 180
            prob_x = r * np.cos(prob_theta)
            prob_y = r * np.sin(prob_theta)
            plt.plot([0, prob_x], [0, prob_y], 'r-', linewidth=3)
            
            # Add labels
            plt.text(-1, 0, '0%', ha='center', va='center')
            plt.text(1, 0, '100%', ha='center', va='center')
            plt.text(0, 0.5, f'{probability*100:.1f}%', ha='center', va='center', fontsize=14)
            
            plt.title('Simulation Probability')
            plt.axis('equal')
            plt.axis('off')
        else:
            plt.text(0.5, 0.5, 'Insufficient evidence for probability calculation', 
                    ha='center', va='center', fontsize=12)
            plt.axis('off')
        
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        
        print(f"Visualization saved to {save_path}")
    
    def generate_report(self, save_path='reality_simulation_report.txt'):
        """Generate a detailed report of the findings"""
        with open(save_path, 'w') as f:
            f.write("=== REALITY SIMULATION TEST REPORT ===\n\n")
            f.write(f"Date: {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Golden Ratio (φ): {PHI}\n\n")
            
            # Write phi-harmonic relationships
            f.write(f"PHI-HARMONIC RELATIONSHIPS ({len(self.phi_relationships)} found):\n")
            f.write("-" * 80 + "\n")
            if self.phi_relationships:
                # Sort by accuracy
                sorted_rels = sorted(self.phi_relationships, key=lambda x: x.get('accuracy', 0), reverse=True)
                for i, rel in enumerate(sorted_rels[:10]):  # Show top 10
                    if 'ratio' in rel:
                        f.write(f"{i+1}. {rel['constant1']} / {rel['constant2']} = {rel['ratio']:.10e}\n")
                    elif 'log_ratio' in rel:
                        f.write(f"{i+1}. log10({rel['constant1']} / {rel['constant2']}) = {rel['log_ratio']:.10e}\n")
                    f.write(f"   Pattern: {rel['pattern']} ({rel['pattern_value']:.10e})\n")
                    f.write(f"   Accuracy: {rel.get('accuracy', 0):.2f}%\n\n")
                
                if len(sorted_rels) > 10:
                    f.write(f"... and {len(sorted_rels) - 10} more relationships\n\n")
            else:
                f.write("No phi-harmonic relationships found\n\n")
            
            # Write digital patterns
            f.write(f"DIGITAL ENCODING PATTERNS ({len(self.digital_patterns)} found):\n")
            f.write("-" * 80 + "\n")
            if self.digital_patterns:
                for i, pattern in enumerate(self.digital_patterns[:10]):  # Show top 10
                    f.write(f"{i+1}. {pattern['constant']} = {pattern['value']:.10e}\n")
                    f.write(f"   Pattern: {pattern['pattern']} (Type: {pattern['pattern_type']})\n")
                    f.write(f"   Position: {pattern['position']}\n\n")
                
                if len(self.digital_patterns) > 10:
                    f.write(f"... and {len(self.digital_patterns) - 10} more patterns\n\n")
            else:
                f.write("No digital encoding patterns found\n\n")
            
            # Write simulation evidence
            f.write(f"SIMULATION EVIDENCE ({len(self.simulation_evidence)} pieces):\n")
            f.write("-" * 80 + "\n")
            if self.simulation_evidence:
                for i, evidence in enumerate(self.simulation_evidence):
                    f.write(f"{i+1}. Type: {evidence['type']}\n")
                    f.write(f"   Description: {evidence['description']}\n")
                    
                    # Write additional details based on evidence type
                    if evidence['type'] == 'statistical':
                        f.write(f"   Expected by chance: {evidence['expected']:.2f}\n")
                        f.write(f"   Actual found: {evidence['actual']}\n")
                        f.write(f"   Significance: {evidence['significance']:.2f}x\n")
                    elif evidence['type'] == 'fundamental':
                        f.write(f"   Count: {evidence['count']} relationships\n")
                    elif evidence['type'] == 'digital':
                        f.write(f"   Count: {evidence['count']} patterns\n")
                        f.write(f"   Expected by chance: {evidence['expected']:.2f}\n")
                    elif evidence['type'] == 'alpha_phi':
                        f.write(f"   Alpha value: {evidence['alpha']:.10e}\n")
                        f.write(f"   Relationship: {evidence['phi_relationship']}\n")
                        f.write(f"   Accuracy: {evidence['accuracy']:.2f}%\n")
                    
                    f.write("\n")
            else:
                f.write("No simulation evidence found\n\n")
            
            # Write conclusion
            f.write("CONCLUSION:\n")
            f.write("-" * 80 + "\n")
            
            if len(self.simulation_evidence) >= 3:
                f.write("The analysis found STRONG EVIDENCE suggesting that reality may have\n")
                f.write("computational or simulated properties based on phi-harmonic principles.\n\n")
                f.write("The presence of multiple phi-harmonic relationships between fundamental\n")
                f.write("physical constants, particularly those that define the basic structure\n")
                f.write("of reality, suggests an underlying mathematical design that aligns with\n")
                f.write("the phi-harmonic principles identified in the atomic triad configuration.\n")
            elif len(self.simulation_evidence) >= 1:
                f.write("The analysis found SOME EVIDENCE suggesting that reality may have\n")
                f.write("computational or simulated properties based on phi-harmonic principles.\n\n")
                f.write("While not conclusive, the detected patterns warrant further investigation\n")
                f.write("into the possibility that fundamental physical constants encode\n")
                f.write("information in a phi-harmonic structure similar to the atomic triad configuration.\n")
            else:
                f.write("The analysis found INSUFFICIENT EVIDENCE to suggest that reality\n")
                f.write("has computational or simulated properties based on phi-harmonic principles.\n\n")
                f.write("This does not disprove the theory, but indicates that the current\n")
                f.write("analysis methods did not detect significant phi-harmonic patterns\n")
                f.write("in the fundamental physical constants examined.\n")
        
        print(f"Detailed report saved to {save_path}")

def run_simulation_test():
    """Run the reality simulation test"""
    print("=== Reality Simulation Test ===")
    print(f"Testing whether reality shows evidence of phi-harmonic encoding")
    print(f"Golden ratio (φ): {PHI}")
    
    # Create output directory
    output_dir = "simulation_test_results"
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize and run tests
    test = RealitySimulationTest()
    results = test.run_tests()
    
    # Visualize results
    test.visualize_results(save_path=os.path.join(output_dir, "simulation_test.png"))
    
    # Generate detailed report
    test.generate_report(save_path=os.path.join(output_dir, "simulation_report.txt"))
    
    # Print conclusion
    if len(results['simulation_evidence']) >= 3:
        print("\n✓ STRONG EVIDENCE: Reality shows significant phi-harmonic encoding")
        print("  that aligns with the properties of a computational simulation.")
    elif len(results['simulation_evidence']) >= 1:
        print("\n◐ PARTIAL EVIDENCE: Reality shows some phi-harmonic encoding")
        print("  that suggests computational properties, but is not conclusive.")
    else:
        print("\n✗ INSUFFICIENT EVIDENCE: Current analysis does not detect")
        print("  significant phi-harmonic encoding in physical constants.")
    
    print(f"\nResults saved to {output_dir}/")

if __name__ == "__main__":
    run_simulation_test()
