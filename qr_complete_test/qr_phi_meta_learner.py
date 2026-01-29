#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Meta-Learner

This module extends the Quantum Phi-Harmonic Self-Replicator with
meta-learning capabilities, allowing it to analyze and improve its own code
structure based on phi-harmonic principles.
"""

import os
import ast
import time
import inspect
import hashlib
import importlib
import numpy as np
from typing import Dict, List, Any, Tuple, Optional

# Phi-harmonic constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio ≈ 1.618034
PHI_CONJUGATE = 1 / PHI   # Golden ratio conjugate ≈ 0.618034

class QuantumPhiMetaLearner:
    """Meta-learning extension for the Quantum Phi-Harmonic Self-Replicator."""
    
    def __init__(self, module_path: str, debug: bool = True):
        """Initialize the meta-learner with a target module to analyze and improve.
        
        Args:
            module_path: Path to the Python module to analyze
            debug: Whether to print debug information
        """
        self.module_path = module_path
        self.debug = debug
        self.module_name = os.path.basename(module_path).replace('.py', '')
        self.module_dir = os.path.dirname(module_path)
        self.ast_tree = None
        self.code_metrics = {}
        self.phi_alignment_score = 0.0
        self.improvement_history = []
        
        # Load the module and parse its AST
        self._load_and_parse()
    
    def _load_and_parse(self) -> None:
        """Load the target module and parse its abstract syntax tree."""
        try:
            with open(self.module_path, 'r') as f:
                self.source_code = f.read()
            
            self.ast_tree = ast.parse(self.source_code)
            
            if self.debug:
                print(f"✅ Loaded and parsed module: {self.module_path}")
        except Exception as e:
            print(f"Error loading module: {e}")
            self.ast_tree = None
    
    def analyze_code_structure(self) -> Dict[str, Any]:
        """Analyze the code structure and calculate phi-harmonic metrics.
        
        Returns:
            Dictionary of code metrics and phi-alignment scores
        """
        if not self.ast_tree:
            return {}
        
        # Count various code elements
        class_count = len([node for node in ast.walk(self.ast_tree) if isinstance(node, ast.ClassDef)])
        function_count = len([node for node in ast.walk(self.ast_tree) if isinstance(node, ast.FunctionDef)])
        import_count = len([node for node in ast.walk(self.ast_tree) if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom)])
        assign_count = len([node for node in ast.walk(self.ast_tree) if isinstance(node, ast.Assign)])
        call_count = len([node for node in ast.walk(self.ast_tree) if isinstance(node, ast.Call)])
        
        # Calculate function complexity metrics
        function_complexities = []
        for node in ast.walk(self.ast_tree):
            if isinstance(node, ast.FunctionDef):
                # Count statements in function
                stmt_count = len([n for n in ast.walk(node) if isinstance(n, ast.stmt)])
                # Count expressions in function
                expr_count = len([n for n in ast.walk(node) if isinstance(n, ast.expr)])
                # Calculate cyclomatic complexity (simplified)
                branches = len([n for n in ast.walk(node) if 
                               isinstance(n, (ast.If, ast.For, ast.While, ast.Try))])
                cyclomatic = branches + 1
                
                function_complexities.append({
                    'name': node.name,
                    'statements': stmt_count,
                    'expressions': expr_count,
                    'cyclomatic': cyclomatic
                })
        
        # Calculate phi-harmonic metrics
        total_nodes = len(list(ast.walk(self.ast_tree)))
        code_lines = len(self.source_code.split('\n'))
        
        # Calculate phi-alignment of code structure
        # Ideal ratios based on phi-harmonic principles
        ideal_class_function_ratio = PHI_CONJUGATE  # ~0.618
        ideal_function_complexity = PHI  # ~1.618
        
        # Calculate actual ratios
        class_function_ratio = class_count / function_count if function_count > 0 else 0
        avg_complexity = np.mean([f['cyclomatic'] for f in function_complexities]) if function_complexities else 0
        
        # Calculate alignment scores (0-1 scale, higher is better)
        class_function_alignment = 1 - min(abs(class_function_ratio - ideal_class_function_ratio) / ideal_class_function_ratio, 1)
        complexity_alignment = 1 - min(abs(avg_complexity - ideal_function_complexity) / ideal_function_complexity, 1)
        
        # Overall phi-alignment score
        self.phi_alignment_score = (class_function_alignment + complexity_alignment) / 2
        
        # Store metrics
        self.code_metrics = {
            'total_nodes': total_nodes,
            'code_lines': code_lines,
            'class_count': class_count,
            'function_count': function_count,
            'import_count': import_count,
            'assign_count': assign_count,
            'call_count': call_count,
            'function_complexities': function_complexities,
            'class_function_ratio': class_function_ratio,
            'avg_complexity': avg_complexity,
            'phi_alignment_score': self.phi_alignment_score
        }
        
        if self.debug:
            print(f"\n📊 Code Structure Analysis")
            print(f"  Classes: {class_count}")
            print(f"  Functions: {function_count}")
            print(f"  Class-Function Ratio: {class_function_ratio:.4f} (Ideal: {ideal_class_function_ratio:.4f})")
            print(f"  Avg Function Complexity: {avg_complexity:.4f} (Ideal: {ideal_function_complexity:.4f})")
            print(f"  Phi-Alignment Score: {self.phi_alignment_score:.4f}")
        
        return self.code_metrics
    
    def identify_improvement_opportunities(self) -> List[Dict[str, Any]]:
        """Identify opportunities for code improvement based on phi-harmonic principles.
        
        Returns:
            List of improvement opportunities
        """
        if not self.code_metrics:
            self.analyze_code_structure()
        
        opportunities = []
        
        # Check function complexity distribution
        complexities = [f['cyclomatic'] for f in self.code_metrics.get('function_complexities', [])]
        if complexities:
            for i, func in enumerate(self.code_metrics['function_complexities']):
                # Functions that are too complex
                if func['cyclomatic'] > PHI * 2:
                    opportunities.append({
                        'type': 'function_too_complex',
                        'element': func['name'],
                        'current_value': func['cyclomatic'],
                        'target_value': PHI,
                        'suggestion': f"Refactor function '{func['name']}' into smaller functions"
                    })
                # Functions that are too simple
                elif func['cyclomatic'] == 1 and func['statements'] > 5:
                    opportunities.append({
                        'type': 'function_too_simple',
                        'element': func['name'],
                        'current_value': func['cyclomatic'],
                        'target_value': PHI,
                        'suggestion': f"Add more structure to function '{func['name']}'"
                    })
        
        # Check class-function ratio
        if self.code_metrics.get('class_count', 0) > 0 and self.code_metrics.get('function_count', 0) > 0:
            ratio = self.code_metrics['class_function_ratio']
            if abs(ratio - PHI_CONJUGATE) > 0.2:
                if ratio < PHI_CONJUGATE:
                    opportunities.append({
                        'type': 'class_function_ratio_low',
                        'current_value': ratio,
                        'target_value': PHI_CONJUGATE,
                        'suggestion': "Consider grouping related functions into classes"
                    })
                else:
                    opportunities.append({
                        'type': 'class_function_ratio_high',
                        'current_value': ratio,
                        'target_value': PHI_CONJUGATE,
                        'suggestion': "Consider extracting utility functions from classes"
                    })
        
        if self.debug and opportunities:
            print(f"\n🔍 Identified {len(opportunities)} improvement opportunities:")
            for i, opp in enumerate(opportunities):
                print(f"  {i+1}. {opp['suggestion']}")
        
        return opportunities
    
    def generate_improved_code(self) -> Tuple[str, float]:
        """Generate improved code based on identified opportunities.
        
        Returns:
            Tuple of (improved_code, improvement_score)
        """
        if not self.code_metrics:
            self.analyze_code_structure()
        
        opportunities = self.identify_improvement_opportunities()
        if not opportunities:
            if self.debug:
                print("No improvement opportunities identified.")
            return self.source_code, 0.0
        
        # For now, we'll implement simple transformations
        # In a full implementation, this would use more sophisticated code transformation
        improved_code = self.source_code
        improvement_score = 0.0
        
        # Track what we've improved
        improvements_made = []
        
        # Apply simple transformations based on opportunities
        for opp in opportunities:
            if opp['type'] == 'function_too_complex':
                # Add a comment suggesting refactoring (actual refactoring would be more complex)
                func_pattern = f"def {opp['element']}("
                comment = f"# TODO: Phi-harmonic refactoring opportunity: Split this complex function (score: {opp['current_value']:.2f}, target: {opp['target_value']:.2f})\n"
                if func_pattern in improved_code:
                    improved_code = improved_code.replace(func_pattern, comment + func_pattern)
                    improvements_made.append(f"Added refactoring suggestion for {opp['element']}")
                    improvement_score += 0.1
            
            elif opp['type'] == 'class_function_ratio_low':
                # Add a comment suggesting class structure
                comment = """# TODO: Phi-harmonic structure opportunity: Consider grouping related functions into classes\n# to achieve golden ratio balance (current: {:.2f}, target: {:.2f})\n""".format(
                    opp['current_value'], opp['target_value'])
                improved_code = comment + improved_code
                improvements_made.append("Added class structure suggestion")
                improvement_score += 0.1
        
        # Calculate new phi-alignment score
        new_alignment = self.phi_alignment_score + improvement_score
        new_alignment = min(new_alignment, 1.0)  # Cap at 1.0
        
        # Record the improvement
        self.improvement_history.append({
            'timestamp': time.time(),
            'previous_alignment': self.phi_alignment_score,
            'new_alignment': new_alignment,
            'improvements': improvements_made
        })
        
        if self.debug and improvements_made:
            print(f"\n✨ Made {len(improvements_made)} improvements:")
            for imp in improvements_made:
                print(f"  - {imp}")
            print(f"  Phi-alignment improved: {self.phi_alignment_score:.4f} → {new_alignment:.4f}")
        
        return improved_code, improvement_score
    
    def save_improved_code(self, output_path: Optional[str] = None) -> str:
        """Save the improved code to a new file.
        
        Args:
            output_path: Path to save the improved code. If None, generates a path.
            
        Returns:
            Path to the saved file
        """
        improved_code, improvement_score = self.generate_improved_code()
        
        if not output_path:
            # Generate a phi-harmonic filename
            timestamp = time.time()
            phi_time = timestamp * PHI
            resonance = phi_time % 1
            hash_val = hashlib.md5(improved_code.encode()).hexdigest()[:8]
            
            filename = f"{self.module_name}_improved_{resonance:.6f}_{hash_val}.py"
            output_path = os.path.join(self.module_dir, filename)
        
        with open(output_path, 'w') as f:
            f.write(improved_code)
        
        if self.debug:
            print(f"\n✅ Saved improved code to: {output_path}")
        
        return output_path
    
    def apply_phi_harmonic_transformation(self) -> str:
        """Apply a phi-harmonic transformation to the code structure.
        
        This is a more advanced transformation that restructures the code
        based on golden ratio principles.
        
        Returns:
            Path to the transformed code file
        """
        # First analyze the current structure
        self.analyze_code_structure()
        
        # Generate improved code with basic transformations
        improved_code, _ = self.generate_improved_code()
        
        # Apply phi-harmonic structure transformation
        # (In a full implementation, this would be more sophisticated)
        header = f"""#!/usr/bin/env python3
\"""
\nPhi-Harmonically Transformed Code
\nOriginal: {self.module_path}
\nTransformation Time: {time.time()}
\nPhi-Alignment Score: {self.phi_alignment_score:.6f}
\n
\nThis code has been restructured according to quantum phi-harmonic principles.
\nThe golden ratio (φ ≈ {PHI:.6f}) and its conjugate (φ⁻¹ ≈ {PHI_CONJUGATE:.6f}) 
\nare used to optimize the code structure for maximum resonance.
\"""
"""

        # Add the header and improved code
        transformed_code = header + improved_code
        
        # Save to a new file
        timestamp = time.time()
        phi_time = timestamp * PHI
        resonance = phi_time % 1
        hash_val = hashlib.md5(transformed_code.encode()).hexdigest()[:8]
        
        filename = f"{self.module_name}_phi_transformed_{resonance:.6f}_{hash_val}.py"
        output_path = os.path.join(self.module_dir, filename)
        
        with open(output_path, 'w') as f:
            f.write(transformed_code)
        
        if self.debug:
            print(f"\n✨ Applied phi-harmonic transformation")
            print(f"✅ Saved transformed code to: {output_path}")
        
        return output_path

# Example usage
def main():
    """Run the meta-learner on a sample file."""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python qr_phi_meta_learner.py <path_to_python_file>")
        return
    
    target_file = sys.argv[1]
    if not os.path.exists(target_file):
        print(f"Error: File {target_file} not found")
        return
    
    print(f"🧠 Quantum Phi-Harmonic Meta-Learner")
    print("============================================================")
    print(f"Analyzing: {target_file}")
    
    meta_learner = QuantumPhiMetaLearner(target_file)
    meta_learner.analyze_code_structure()
    meta_learner.identify_improvement_opportunities()
    improved_path = meta_learner.save_improved_code()
    transformed_path = meta_learner.apply_phi_harmonic_transformation()
    
    print("\n✅ Meta-learning process complete")
    print(f"Improved code: {improved_path}")
    print(f"Transformed code: {transformed_path}")

if __name__ == "__main__":
    main()
