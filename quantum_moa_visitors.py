#!/usr/bin/env python3
"""
Quantum MoA AST Visitors
-----------------------

This module implements specialized AST visitors for the Mixture of Agents (MoA)
architecture in the QuantumAI system. These visitors analyze Python code to detect
various issues and opportunities while maintaining phi-harmonic coherence.

The visitors follow the modular "lego" approach, allowing them to be combined
and extended while maintaining quantum principles and phi-harmonic resonance.
"""

import ast
import re
from typing import Dict, Any, List, Optional, Set, Union

class LogicErrorVisitor(ast.NodeVisitor):
    """
    AST visitor that detects potential logic errors in Python code.
    """
    
    def __init__(self):
        """Initialize the logic error visitor."""
        self.issues = []
        self.variables = set()
        self.defined_variables = set()
        self.used_variables = set()
        self.loops = []
        self.conditionals = []
    
    def visit_Name(self, node):
        """Visit a variable name."""
        if isinstance(node.ctx, ast.Store):
            self.defined_variables.add(node.id)
        elif isinstance(node.ctx, ast.Load):
            self.used_variables.add(node.id)
        self.generic_visit(node)
    
    def visit_For(self, node):
        """Visit a for loop."""
        self.loops.append(('for', node))
        self.generic_visit(node)
        
        # Check for empty loops
        if not node.body:
            self.issues.append({
                "type": "empty_loop",
                "description": "Empty for loop",
                "line": node.lineno,
                "confidence": 0.9
            })
        
        # Check for loop variable not used in body
        if isinstance(node.target, ast.Name):
            loop_var = node.target.id
            used_in_body = False
            
            for subnode in ast.walk(node):
                if isinstance(subnode, ast.Name) and subnode.id == loop_var and isinstance(subnode.ctx, ast.Load):
                    if hasattr(subnode, 'lineno') and subnode.lineno > node.lineno:
                        used_in_body = True
                        break
            
            if not used_in_body:
                self.issues.append({
                    "type": "unused_loop_variable",
                    "description": f"Loop variable '{loop_var}' not used in loop body",
                    "line": node.lineno,
                    "confidence": 0.7
                })
        
        self.loops.pop()
    
    def visit_While(self, node):
        """Visit a while loop."""
        self.loops.append(('while', node))
        
        # Check for potential infinite loops
        if isinstance(node.test, ast.Constant) and node.test.value == True:
            has_break = False
            for subnode in ast.walk(node):
                if isinstance(subnode, ast.Break):
                    has_break = True
                    break
            
            if not has_break:
                self.issues.append({
                    "type": "infinite_loop",
                    "description": "Infinite loop (while True without break)",
                    "line": node.lineno,
                    "confidence": 0.9
                })
        
        self.generic_visit(node)
        self.loops.pop()
    
    def visit_If(self, node):
        """Visit an if statement."""
        self.conditionals.append(node)
        
        # Check for constant conditions
        if isinstance(node.test, ast.Constant):
            self.issues.append({
                "type": "constant_condition",
                "description": f"Constant condition in if statement: {node.test.value}",
                "line": node.lineno,
                "confidence": 0.9
            })
        
        # Check for redundant conditions
        if isinstance(node.test, ast.Compare) and len(node.test.ops) == 1:
            if isinstance(node.test.ops[0], (ast.Eq, ast.NotEq)) and len(node.test.comparators) == 1:
                left = node.test.left
                right = node.test.comparators[0]
                
                if (isinstance(left, ast.Name) and isinstance(right, ast.Name) and 
                    left.id == right.id):
                    self.issues.append({
                        "type": "redundant_condition",
                        "description": f"Comparing variable '{left.id}' with itself",
                        "line": node.lineno,
                        "confidence": 0.9
                    })
        
        self.generic_visit(node)
        self.conditionals.pop()
    
    def visit_Compare(self, node):
        """Visit a comparison operation."""
        # Check for off-by-one errors in comparisons
        if len(node.ops) == 1 and isinstance(node.ops[0], (ast.Lt, ast.Gt)):
            if isinstance(node.comparators[0], ast.Constant) and isinstance(node.comparators[0].value, int):
                self.issues.append({
                    "type": "potential_off_by_one",
                    "description": "Potential off-by-one error in comparison",
                    "line": node.lineno,
                    "confidence": 0.6
                })
        
        self.generic_visit(node)
    
    def visit_BinOp(self, node):
        """Visit a binary operation."""
        # Check for division by zero
        if isinstance(node.op, ast.Div) and isinstance(node.right, ast.Constant):
            if node.right.value == 0:
                self.issues.append({
                    "type": "division_by_zero",
                    "description": "Division by zero",
                    "line": node.lineno,
                    "confidence": 0.99
                })
        
        self.generic_visit(node)
    
    def visit_Module(self, node):
        """Visit the module (root of the AST)."""
        self.generic_visit(node)
        
        # Check for unused variables
        unused_vars = self.defined_variables - self.used_variables
        for var in unused_vars:
            if not var.startswith('_'):  # Ignore variables starting with underscore
                self.issues.append({
                    "type": "unused_variable",
                    "description": f"Variable '{var}' is defined but never used",
                    "line": 0,  # We don't know the line number here
                    "confidence": 0.8
                })
        
        # Check for undefined variables
        undefined_vars = self.used_variables - self.defined_variables
        for var in undefined_vars:
            if not var in __builtins__ and not var.startswith('_'):  # Ignore builtins and variables starting with underscore
                self.issues.append({
                    "type": "undefined_variable",
                    "description": f"Variable '{var}' is used but not defined",
                    "line": 0,  # We don't know the line number here
                    "confidence": 0.8
                })

class OptimizationVisitor(ast.NodeVisitor):
    """
    AST visitor that detects potential optimization opportunities in Python code.
    """
    
    def __init__(self):
        """Initialize the optimization visitor."""
        self.opportunities = []
        self.loops = []
        self.functions = {}
        self.function_calls = []
    
    def visit_For(self, node):
        """Visit a for loop."""
        self.loops.append(('for', node))
        
        # Check for nested loops
        if len(self.loops) > 1:
            self.opportunities.append({
                "type": "nested_loop",
                "description": f"Nested loop with depth {len(self.loops)}, consider optimizing",
                "line": node.lineno,
                "confidence": 0.7
            })
        
        # Check for list comprehension opportunities
        if len(node.body) == 1 and isinstance(node.body[0], ast.Expr):
            if isinstance(node.body[0].value, ast.Call) and isinstance(node.body[0].value.func, ast.Attribute):
                if node.body[0].value.func.attr == 'append':
                    self.opportunities.append({
                        "type": "list_comprehension_opportunity",
                        "description": "For loop with append can be converted to list comprehension",
                        "line": node.lineno,
                        "confidence": 0.8
                    })
        
        self.generic_visit(node)
        self.loops.pop()
    
    def visit_While(self, node):
        """Visit a while loop."""
        self.loops.append(('while', node))
        
        # Check for nested loops
        if len(self.loops) > 1:
            self.opportunities.append({
                "type": "nested_loop",
                "description": f"Nested loop with depth {len(self.loops)}, consider optimizing",
                "line": node.lineno,
                "confidence": 0.7
            })
        
        self.generic_visit(node)
        self.loops.pop()
    
    def visit_FunctionDef(self, node):
        """Visit a function definition."""
        self.functions[node.name] = node
        self.generic_visit(node)
    
    def visit_Call(self, node):
        """Visit a function call."""
        # Record function calls
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            self.function_calls.append((func_name, node))
            
            # Check for recursive calls without base case
            if func_name in self.functions:
                # This is a recursive call
                if all(not isinstance(subnode, ast.Return) for subnode in ast.walk(self.functions[func_name])):
                    self.opportunities.append({
                        "type": "recursive_no_base_case",
                        "description": f"Recursive function '{func_name}' might be missing a base case",
                        "line": node.lineno,
                        "confidence": 0.7
                    })
        
        self.generic_visit(node)
    
    def visit_BinOp(self, node):
        """Visit a binary operation."""
        # Check for string concatenation in loops
        if isinstance(node.op, ast.Add) and (isinstance(node.left, ast.Str) or isinstance(node.right, ast.Str)):
            for loop_type, loop_node in self.loops:
                self.opportunities.append({
                    "type": "string_concatenation_in_loop",
                    "description": "String concatenation in loop, consider using join()",
                    "line": node.lineno,
                    "confidence": 0.8
                })
                break
        
        self.generic_visit(node)
    
    def visit_Module(self, node):
        """Visit the module (root of the AST)."""
        self.generic_visit(node)
        
        # Check for duplicate function calls
        function_call_counts = {}
        for func_name, call_node in self.function_calls:
            # Create a simple representation of the arguments
            args_repr = str([ast.dump(arg) for arg in call_node.args])
            key = (func_name, args_repr)
            
            if key not in function_call_counts:
                function_call_counts[key] = []
            function_call_counts[key].append(call_node)
        
        # Report functions called multiple times with the same arguments
        for (func_name, args_repr), calls in function_call_counts.items():
            if len(calls) > 1:
                self.opportunities.append({
                    "type": "repeated_function_call",
                    "description": f"Function '{func_name}' called {len(calls)} times with the same arguments",
                    "line": calls[0].lineno,
                    "confidence": 0.8
                })

class CoherenceVisitor(ast.NodeVisitor):
    """
    AST visitor that analyzes code for phi-harmonic coherence patterns.
    """
    
    def __init__(self, phi=1.618034):
        """Initialize the coherence visitor."""
        self.phi = phi
        self.patterns = []
        self.function_lengths = {}
        self.class_methods = {}
        self.imports = []
        self.constants = []
        self.function_complexity = {}
    
    def visit_FunctionDef(self, node):
        """Visit a function definition."""
        # Calculate function length
        end_lineno = max(getattr(n, 'lineno', 0) for n in ast.walk(node)) if node.body else node.lineno
        length = end_lineno - node.lineno + 1
        self.function_lengths[node.name] = length
        
        # Calculate cyclomatic complexity
        complexity = 1  # Base complexity
        for subnode in ast.walk(node):
            if isinstance(subnode, (ast.If, ast.While, ast.For)):
                complexity += 1
            elif isinstance(subnode, ast.BoolOp) and isinstance(subnode.op, (ast.And, ast.Or)):
                complexity += len(subnode.values) - 1
        
        self.function_complexity[node.name] = complexity
        
        # Check for phi-harmonic function length
        phi_resonance = abs((length / self.phi) % 1)
        if phi_resonance < 0.1 or phi_resonance > 0.9:
            self.patterns.append({
                "type": "phi_harmonic_function_length",
                "description": f"Function '{node.name}' has phi-harmonic length of {length}",
                "line": node.lineno,
                "phi_resonance": phi_resonance,
                "confidence": 0.7
            })
        
        self.generic_visit(node)
    
    def visit_ClassDef(self, node):
        """Visit a class definition."""
        methods = {}
        for subnode in node.body:
            if isinstance(subnode, ast.FunctionDef):
                methods[subnode.name] = subnode
        
        self.class_methods[node.name] = methods
        
        # Check for phi-harmonic method count
        method_count = len(methods)
        phi_resonance = abs((method_count / self.phi) % 1)
        if phi_resonance < 0.1 or phi_resonance > 0.9:
            self.patterns.append({
                "type": "phi_harmonic_method_count",
                "description": f"Class '{node.name}' has phi-harmonic method count of {method_count}",
                "line": node.lineno,
                "phi_resonance": phi_resonance,
                "confidence": 0.7
            })
        
        self.generic_visit(node)
    
    def visit_Import(self, node):
        """Visit an import statement."""
        for name in node.names:
            self.imports.append(name.name)
        self.generic_visit(node)
    
    def visit_ImportFrom(self, node):
        """Visit an import from statement."""
        for name in node.names:
            self.imports.append(f"{node.module}.{name.name}")
        self.generic_visit(node)
    
    def visit_Assign(self, node):
        """Visit an assignment."""
        # Check for constants (uppercase variables)
        for target in node.targets:
            if isinstance(target, ast.Name):
                if target.id.isupper():
                    self.constants.append(target.id)
        
        self.generic_visit(node)
    
    def visit_Module(self, node):
        """Visit the module (root of the AST)."""
        self.generic_visit(node)
        
        # Analyze overall structure for phi-harmonic patterns
        total_functions = len(self.function_lengths)
        total_classes = len(self.class_methods)
        total_imports = len(self.imports)
        total_constants = len(self.constants)
        
        # Check for phi-harmonic ratios in code structure
        if total_functions > 0 and total_classes > 0:
            ratio = total_functions / total_classes
            phi_resonance = abs((ratio / self.phi) % 1)
            if phi_resonance < 0.1 or phi_resonance > 0.9:
                self.patterns.append({
                    "type": "phi_harmonic_function_class_ratio",
                    "description": f"Phi-harmonic ratio of functions to classes: {ratio:.2f}",
                    "line": 0,
                    "phi_resonance": phi_resonance,
                    "confidence": 0.6
                })

class EvolutionVisitor(ast.NodeVisitor):
    """
    AST visitor that analyzes code for evolutionary patterns and self-improvement capabilities.
    """
    
    def __init__(self):
        """Initialize the evolution visitor."""
        self.patterns = []
        self.self_modifying_code = []
        self.file_operations = []
        self.dynamic_code_execution = []
        self.meta_programming = []
    
    def visit_Call(self, node):
        """Visit a function call."""
        # Check for file operations
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name in ['open', 'read', 'write']:
                self.file_operations.append({
                    "type": "file_operation",
                    "name": func_name,
                    "line": node.lineno
                })
        
        # Check for dynamic code execution
        if isinstance(node.func, ast.Name) and node.func.id in ['eval', 'exec', 'compile']:
            self.dynamic_code_execution.append({
                "type": "dynamic_code_execution",
                "name": node.func.id,
                "line": node.lineno
            })
            
            self.patterns.append({
                "type": "self_modifying_capability",
                "description": f"Dynamic code execution using {node.func.id}()",
                "line": node.lineno,
                "confidence": 0.9
            })
        
        # Check for imports of meta-programming modules
        if isinstance(node.func, ast.Attribute):
            if isinstance(node.func.value, ast.Name):
                module = node.func.value.id
                if module in ['ast', 'inspect', 'types', 'importlib']:
                    self.meta_programming.append({
                        "type": "meta_programming",
                        "module": module,
                        "function": node.func.attr,
                        "line": node.lineno
                    })
                    
                    self.patterns.append({
                        "type": "meta_programming_capability",
                        "description": f"Meta-programming using {module}.{node.func.attr}()",
                        "line": node.lineno,
                        "confidence": 0.8
                    })
        
        self.generic_visit(node)
    
    def visit_Import(self, node):
        """Visit an import statement."""
        for name in node.names:
            if name.name in ['ast', 'inspect', 'types', 'importlib', 'sys']:
                self.meta_programming.append({
                    "type": "meta_programming_import",
                    "module": name.name,
                    "line": node.lineno
                })
        
        self.generic_visit(node)
    
    def visit_ImportFrom(self, node):
        """Visit an import from statement."""
        if node.module in ['ast', 'inspect', 'types', 'importlib', 'sys']:
            for name in node.names:
                self.meta_programming.append({
                    "type": "meta_programming_import",
                    "module": f"{node.module}.{name.name}",
                    "line": node.lineno
                })
        
        self.generic_visit(node)
    
    def visit_Module(self, node):
        """Visit the module (root of the AST)."""
        self.generic_visit(node)
        
        # Analyze overall self-modification capabilities
        has_file_ops = len(self.file_operations) > 0
        has_dynamic_exec = len(self.dynamic_code_execution) > 0
        has_meta_programming = len(self.meta_programming) > 0
        
        if has_file_ops and (has_dynamic_exec or has_meta_programming):
            self.patterns.append({
                "type": "self_evolution_capability",
                "description": "Code has potential for self-evolution (file operations + dynamic execution/meta-programming)",
                "line": 0,
                "confidence": 0.7
            })
