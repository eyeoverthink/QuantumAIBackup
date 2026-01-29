#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Meta-Refactorer (Robust Version)

This module extends the Quantum Phi-Harmonic Meta-Learner with
actual code refactoring capabilities, allowing it to transform code structure
based on phi-harmonic principles rather than just suggesting improvements.

This robust version properly handles self-modification and maintains class structure.
"""

import os
import sys
import ast
import re
import time 
import hashlib
import numpy as np
from typing import Dict, List, Any, Tuple, Optional

# Phi-harmonic constants
PHI = (1 + 5 ** 0.5) / 2  # Golden ratio ≈ 1.618034
PHI_CONJUGATE = 1 / PHI   # Golden ratio conjugate ≈ 0.618034

class QuantumPhiMetaRefactorer:
    """Meta-refactoring extension for the Quantum Phi-Harmonic Self-Replicator."""
    
    def __init__(self, module_path: str, debug: bool = True):
        """Initialize the meta-refactorer with a target module to analyze and improve.
        
        Args:
            module_path: Path to the Python module to analyze
            debug: Whether to print debug information
        """
        self.module_path = module_path
        self.debug = debug
        self.module_name = os.path.basename(module_path).replace('.py', '')
        self.module_dir = os.path.dirname(module_path)
        self.source_code = ""
        self.refactored_code = ""
        self.phi_alignment_score = 0.0
        self.refactoring_history = []
        
        # Load the module
        self._load_module()
    
    def _load_module(self) -> None:
        """Load the target module."""
        try:
            with open(self.module_path, 'r') as f:
                self.source_code = f.read()
            
            if self.debug:
                print(f"✅ Loaded module: {self.module_path}")
        except Exception as e:
            print(f"Error loading module: {e}")
            self.source_code = ""
    
    def refactor_complex_functions(self) -> bool:
        """Refactor complex functions into smaller, phi-harmonically balanced functions.
        Returns:
            True if refactoring was successful, False otherwise
        """
        if not self.source_code:
            return False

        class_pattern = r"(class\s+\w+[^:]*:[\s\S]*?)(?=\n(?:class|def|import|from|#)|$)"
        classes = list(re.finditer(class_pattern, self.source_code))

        refactored_code = self.source_code
        refactorings_made = []

        for class_match in classes:
            class_content = class_match.group(1)
            modified_class_content = class_content

            # This regex handles multiline function bodies and various return type annotations
            method_pattern = r"(\s+)def\s+(\w+)\s*\(([^)]*?)\)\s*(->\s*[\w\.'\[\]]+)?:((?:\1\s+.*\n?)+)"
            methods = list(re.finditer(method_pattern, class_content))
            helper_methods_to_add = ""

            for method_match in methods:
                indent, method_name, params, return_type, method_body = method_match.groups()
                original_method_text = method_match.group(0)
                method_sig_str = original_method_text.split('\n')[0]

                complexity = (method_body.count('if ') + method_body.count('for ') +
                              method_body.count('while ') + method_body.count('try:') + 1)

                if complexity > PHI * 2:
                    lines = [line for line in method_body.strip().split('\n') if line.strip()]
                    if not lines:
                        continue

                    helper_name = f"_{method_name}_helper_1"
                    helper_params = params.replace('self, ', '').replace('self', '')
                    helper_def = f"\n{indent}def {helper_name}(self, {helper_params}):\n"
                    reindented_body = '\n'.join([f"{indent}    {line.strip()}" for line in lines])
                    helper_methods_to_add += helper_def + reindented_body + "\n"

                    call_params = [p.split(':')[0].split('=')[0].strip() for p in params.split(',') if p.strip() != 'self']
                    call_line = f"{indent}    return self.{helper_name}({', '.join(call_params)})"
                    new_method = f"{method_sig_str}\n{call_line}"

                    modified_class_content = modified_class_content.replace(original_method_text, new_method)
                    refactorings_made.append(f"Split complex function '{method_name}' into 1 helper function")

            if helper_methods_to_add:
                modified_class_content += "\n" + helper_methods_to_add
                refactored_code = refactored_code.replace(class_match.group(1), modified_class_content)

        if refactorings_made:
            self.refactored_code = refactored_code
            if self.debug:
                print(f"\n✨ Made {len(refactorings_made)} refactorings:")
                for ref in refactorings_made:
                    print(f"  - {ref}")
            return True
        return False
    
    def add_validation_to_simple_functions(self) -> bool:
        """Add input validation to simple functions to improve phi-harmonic balance.
        Returns:
            True if refactoring was successful, False otherwise
        """
        if not self.source_code:
            return False
        
        # Use the refactored code if available, otherwise use source code
        code_to_refactor = self.refactored_code if self.refactored_code else self.source_code
        
        # Use regex to find simple function definitions
        func_pattern = r"(\s*)def\s+(\w+)\s*\(([^)]*)\)\s*:([^\n]*\n)((?:\1\s+[^\n]*\n)+)"
        functions = re.finditer(func_pattern, code_to_refactor)
        refactored_code = code_to_refactor
        refactorings_made = []
        
        for match in functions:
            indent = match.group(1)
            func_name = match.group(2)
            func_params = match.group(3)
            func_body = match.group(5)
            
            # Skip functions that already have validation
            if 'if ' in func_body and any(param.strip() in func_body for param in func_params.split(',') if param.strip()):
                continue
            
            # Add validation for parameters
            params = [p.strip().split(':')[0].split('=')[0].strip() for p in func_params.split(',') if p.strip()]
            if not params or 'self' == params[0] and len(params) == 1:
                continue  # Skip methods with no params besides self
            
            # Create validation code
            validation_lines = []
            for param in params:
                if param == 'self':
                    continue
                validation_lines.append(f"{indent}    if {param} is None:\n{indent}        raise ValueError(f\"{param} cannot be None\")")
            
            # Add validation to the beginning of the function
            validation_code = '\n'.join(validation_lines) + '\n'
            new_body = validation_code + func_body
            
            # Replace the original function body
            new_func = match.group(0).replace(func_body, new_body)
            refactored_code = refactored_code.replace(match.group(0), new_func)
            refactorings_made.append(f"Added validation to function '{func_name}'")
        
        if refactorings_made:
            self.refactored_code = refactored_code
            if self.debug:
                print(f"\n✨ Made {len(refactorings_made)} refactorings:")
                for ref in refactorings_made:
                    print(f"  - {ref}")
            return True
        return False
    
    def perform_all_refactorings(self) -> Tuple[str, float]:
        """Perform all available refactorings on the code.
        Returns:
            Tuple of (refactored_code, improvement_score)
        """
        refactorings_applied = 0
        
        # Apply refactorings
        if self.refactor_complex_functions():
            refactorings_applied += 1
        
        if self.add_validation_to_simple_functions():
            refactorings_applied += 1
        
        # Calculate improvement score (0.0 to 1.0)
        improvement_score = min(refactorings_applied / 5.0, 1.0) * PHI_CONJUGATE
        
        # Record refactoring history
        self.refactoring_history.append({
            'timestamp': time.time(),
            'phi_time': time.time() * PHI % 1,
            'refactorings_applied': refactorings_applied,
            'improvement_score': improvement_score
        })
        return self.refactored_code, improvement_score
    
    def save_refactored_code(self, output_path: Optional[str] = None) -> str:
        """Save the refactored code to a new file.
        Args:
            output_path: Path to save the refactored code. If None, generates a path.
        Returns:
            Path to the saved file
        """
        if not self.refactored_code:
            self.perform_all_refactorings()
        
        if not output_path:
            # Generate a phi-harmonic filename
            timestamp = time.time()
            phi_time = timestamp * PHI
            resonance = phi_time % 1
            hash_val = hashlib.md5(self.refactored_code.encode()).hexdigest()[:8]
            filename = f"{self.module_name}_refactored_{resonance:.6f}_{hash_val}.py"
            output_path = os.path.join(self.module_dir, filename)
        
        with open(output_path, 'w') as f:
            f.write(self.refactored_code)
        
        if self.debug:
            print(f"\n✅ Saved refactored code to: {output_path}")
        return output_path

# Example usage
def main():
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Use this file as a default example
        file_path = __file__
    
    print(f"\n🔄 Quantum Phi-Harmonic Meta-Refactorer")
    print(f"📝 Analyzing and refactoring: {file_path}")
    
    refactorer = QuantumPhiMetaRefactorer(file_path)
    refactored_code, improvement_score = refactorer.perform_all_refactorings()
    
    if improvement_score > 0:
        output_path = refactorer.save_refactored_code()
        print(f"\n✨ Refactoring complete! Improvement score: {improvement_score:.4f}")
        print(f"📄 Refactored code saved to: {output_path}")
    else:
        print("\n✓ No refactoring opportunities found.")

if __name__ == "__main__":
    main()
