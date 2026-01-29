#!/usr/bin/env python3
"""
Quantum Phi-Harmonic Meta-Refactorer

This module extends the Quantum Phi-Harmonic Meta-Learner with
actual code refactoring capabilities, allowing it to transform code structure
based on phi-harmonic principles rather than just suggesting improvements.
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
            
        # Use regex to find function definitions
        func_pattern = r"def\s+(\w+)\s*\([^)]*\)\s*:([^\n]*\n)((?:\s+[^\n]*\n)+)"
        functions = re.finditer(func_pattern, self.source_code)
        refactored_code = self.source_code
        refactorings_made = []
        
        for match in functions:
            func_name = match.group(1)
            func_sig = match.group(0).split(':', 1)[0] + ':'
            func_body = match.group(3)
            # Calculate function complexity (simplified)
            complexity = (func_body.count('if ') + 
                         func_body.count('for ') + 
                         func_body.count('while ') + 
                         func_body.count('try:') + 1)
            # If function is too complex, split it
            if complexity > PHI * 2:  # More than ~3.2 branches
                # Identify logical blocks to split
                lines = func_body.split('\n')
                indent_level = len(lines[0]) - len(lines[0].lstrip())
                # Find blocks of code that can be extracted
                blocks = []
                current_block = []
                block_indent = None
                for line in lines:
                    if not line.strip():
                        continue
                    line_indent = len(line) - len(line.lstrip())
                    # Check for block start (if/for/while at function level)
                    if line_indent == indent_level and any(keyword in line.lstrip() for keyword in ['if ', 'for ', 'while ', 'try:']):
                        if current_block:
                            blocks.append(current_block)
                            current_block = []
                        block_indent = line_indent
                    current_block.append(line)
                if current_block:
                    blocks.append(current_block)
                
                # Create helper functions for each block
                helper_functions = []
                helper_calls = []
                for i, block in enumerate(blocks):
                    helper_name = f"{func_name}_helper_{i+1}"
                    helper_indent = ' ' * indent_level
                    helper_def = f"def {helper_name}(self):\n"
                    helper_body = '\n'.join(block)
                    helper_functions.append(helper_def + helper_body)
                    helper_calls.append(f"{helper_indent}self.{helper_name}()")
                
                # Replace original function with helper calls
                new_body = '\n'.join(helper_calls)
                new_func = f"{func_sig}\n{new_body}"
                
                # Add helper functions after the class
                class_end_pattern = r"(class\s+\w+[^\n]*:[\s\S]*?)(?=\n\S|$)"
                class_match = re.search(class_end_pattern, refactored_code)
                if class_match:
                    class_content = class_match.group(1)
                    helpers_text = '\n\n' + '\n\n'.join(helper_functions)
                    refactored_code = refactored_code.replace(class_content, class_content + helpers_text)
                
                # Replace original function with helper calls
                refactored_code = refactored_code.replace(match.group(0), new_func)
                refactorings_made.append(f"Split complex function '{func_name}' into {len(blocks)} helper functions")
        
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
        func_pattern = r"def\s+(\w+)\s*\(([^)]*)\)\s*:([^\n]*\n)((?:\s+[^\n]*\n)+)"
        functions = re.finditer(func_pattern, code_to_refactor)
        refactored_code = code_to_refactor
        refactorings_made = []
        
        for match in functions:
            func_name = match.group(1)
            func_params = match.group(2)
            func_body = match.group(4)
            
            # Skip functions that already have validation
            if 'if ' in func_body and any(param.strip() in func_body for param in func_params.split(',') if param.strip()):
                continue
            
            # Add validation for parameters
            params = [p.strip().split(':')[0].split('=')[0].strip() for p in func_params.split(',') if p.strip()]
            if not params or 'self' == params[0] and len(params) == 1:
                continue  # Skip methods with no params besides self
            
            # Create validation code
            indent_level = len(func_body.split('\n')[0]) - len(func_body.split('\n')[0].lstrip())
            indent = ' ' * indent_level
            validation_lines = []
            for param in params:
                if param == 'self':
                    continue
                validation_lines.append(f"{indent}if {param} is None:\n{indent}    raise ValueError(f\"{param} cannot be None\")")
            
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
    
    def group_functions_into_class(self) -> bool:
        """Group standalone functions into a class to improve phi-harmonic balance.
        Returns:
            True if refactoring was successful, False otherwise
        """
        if not self.source_code:
            return False
        
        # Use the refactored code if available, otherwise use source code
        code_to_refactor = self.refactored_code if self.refactored_code else self.source_code
        
        # Use regex to find standalone function definitions (not inside a class)
        class_pattern = r"class\s+\w+[^\n]*:[\s\S]*?(?=\n\S|$)"
        classes = list(re.finditer(class_pattern, code_to_refactor))
        
        # Find all function definitions
        func_pattern = r"def\s+(\w+)\s*\([^)]*\)\s*:[^\n]*\n(?:\s+[^\n]*\n)+"
        all_funcs = list(re.finditer(func_pattern, code_to_refactor))
        
        # Identify standalone functions (not in classes)
        standalone_funcs = []
        for func in all_funcs:
            is_standalone = True
            for cls in classes:
                if cls.start() < func.start() < cls.end():
                    is_standalone = False
                    break
            if is_standalone:
                standalone_funcs.append(func)
        
        if not standalone_funcs:
            return False
        
        # Create a new class to hold the standalone functions
        class_name = f"PhiHarmonic{self.module_name.title()}Functions"
        class_def = f"\n\nclass {class_name}:\n    """Phi-harmonically grouped functions from {self.module_name}."""\n\n"
        
        # Indent the functions and add them to the class
        indented_funcs = []
        for func in standalone_funcs:
            func_text = func.group(0)
            # Indent the function (add 4 spaces to each line)
            indented_func = '\n'.join(['    ' + line for line in func_text.split('\n')])
            indented_funcs.append(indented_func)
        
        # Create the class with the functions
        class_content = class_def + '\n'.join(indented_funcs)
        
        # Remove the standalone functions from the code
        refactored_code = code_to_refactor
        for func in reversed(standalone_funcs):  # Process in reverse to maintain correct indices
            refactored_code = refactored_code[:func.start()] + refactored_code[func.end():]
        
        # Add the new class to the end of the file
        refactored_code += class_content
        
        self.refactored_code = refactored_code
        if self.debug:
            print(f"\n✨ Grouped {len(standalone_funcs)} standalone functions into class '{class_name}'")
        return True
    
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
        
        if self.group_functions_into_class():
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
