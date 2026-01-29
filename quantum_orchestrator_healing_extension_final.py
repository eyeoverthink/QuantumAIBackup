#!/usr/bin/env python3
"""
Quantum Orchestrator Healing Extension (Final)
-----------------------------------

This module provides a comprehensive fix for the orchestrator healing protocol,
specifically addressing the _heal_unclosed_paren method signature mismatch.

This extension follows the 'lego' modular philosophy by extending functionality
without modifying the core orchestrator file.
"""

import os
import re
import ast
import logging
import inspect
import types
from typing import Dict, List, Tuple, Optional, Any, Callable

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumOrchestratorHealingExt")

def patch_heal_unclosed_paren(self, content=None):
    """
    Universal patched version of _heal_unclosed_paren that works with both
    1-argument and 2-argument versions of the method.
    
    This method handles both:
    - _heal_unclosed_paren(self)
    - _heal_unclosed_paren(self, content)
    
    Args:
        self: The orchestrator instance
        content (str, optional): File content to heal. If None, reads from target_file
        
    Returns:
        dict: Healing result with success status and fixed content
    """
    logger.info("Using patched _heal_unclosed_paren method")
    
    # If content is not provided, read from target_file
    if content is None and hasattr(self, 'target_file') and self.target_file:
        try:
            with open(self.target_file, 'r') as f:
                content = f.read()
        except Exception as e:
            logger.error(f"Error reading file {self.target_file}: {e}")
            return {"success": False, "error": str(e)}
    
    # If we still don't have content, return error
    if content is None:
        logger.error("No content provided and no target_file available")
        return {"success": False, "error": "No content provided and no target_file available"}
    
    # Check for unclosed parentheses
    try:
        # Try to parse the content
        ast.parse(content)
        # If successful, no unclosed parentheses
        return {"success": True, "fixed": False, "content": content}
    except SyntaxError as e:
        # Check if the error is related to unclosed parentheses
        error_msg = str(e)
        if '(' in error_msg or ')' in error_msg:
            # Fix unclosed parentheses
            fixed_content = fix_unclosed_parentheses(content)
            
            # Verify the fix worked
            try:
                ast.parse(fixed_content)
                logger.info("Successfully fixed unclosed parentheses")
                return {"success": True, "fixed": True, "content": fixed_content}
            except SyntaxError as e2:
                logger.warning(f"Fix attempt failed: {e2}")
                return {"success": False, "error": str(e2), "content": content}
        else:
            # Not a parenthesis issue
            return {"success": False, "error": error_msg, "content": content}

def fix_unclosed_parentheses(content: str) -> str:
    """
    Fix unclosed parentheses in Python code.
    
    Args:
        content (str): Python code content
        
    Returns:
        str: Fixed Python code content
    """
    lines = content.split('\n')
    fixed_lines = []
    
    # Process each line
    for line in lines:
        # Count open and closed parentheses
        open_count = line.count('(')
        close_count = line.count(')')
        
        # If more open than closed, add missing closing parentheses
        if open_count > close_count:
            line += ')' * (open_count - close_count)
        
        fixed_lines.append(line)
    
    # Join the lines back together
    fixed_content = '\n'.join(fixed_lines)
    
    # Check for function definitions with unclosed parentheses
    pattern = r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\([^)]*$'
    matches = re.finditer(pattern, fixed_content, re.MULTILINE)
    
    # Fix each match
    for match in matches:
        # Find the position of the match
        pos = match.end()
        # Insert a closing parenthesis
        fixed_content = fixed_content[:pos] + ')' + fixed_content[pos:]
    
    return fixed_content

def apply_healing_patches(orchestrator_instance):
    """
    Apply all healing patches to an orchestrator instance.
    
    Args:
        orchestrator_instance: The orchestrator instance to patch
    """
    logger.info("Applying healing patches to orchestrator instance")
    
    # Patch _heal_unclosed_paren method
    setattr(orchestrator_instance, '_heal_unclosed_paren', 
            types.MethodType(patch_heal_unclosed_paren, orchestrator_instance))
    
    # Add additional healing methods
    setattr(orchestrator_instance, '_heal_missing_colon', 
            types.MethodType(heal_missing_colon, orchestrator_instance))
    
    # Patch run_and_heal method to use our enhanced healing
    original_run_and_heal = getattr(orchestrator_instance, 'run_and_heal', None)
    if original_run_and_heal:
        setattr(orchestrator_instance, 'run_and_heal', 
                types.MethodType(patched_run_and_heal(original_run_and_heal), orchestrator_instance))
    
    logger.info("All healing patches applied to orchestrator instance")

def heal_missing_colon(self, content=None):
    """
    Heal missing colons in Python code.
    
    Args:
        self: The orchestrator instance
        content (str, optional): File content to heal. If None, reads from target_file
        
    Returns:
        dict: Healing result with success status and fixed content
    """
    logger.info("Healing missing colons")
    
    # If content is not provided, read from target_file
    if content is None and hasattr(self, 'target_file') and self.target_file:
        try:
            with open(self.target_file, 'r') as f:
                content = f.read()
        except Exception as e:
            logger.error(f"Error reading file {self.target_file}: {e}")
            return {"success": False, "error": str(e)}
    
    # If we still don't have content, return error
    if content is None:
        logger.error("No content provided and no target_file available")
        return {"success": False, "error": "No content provided and no target_file available"}
    
    # Check for missing colons
    try:
        # Try to parse the content
        ast.parse(content)
        # If successful, no missing colons
        return {"success": True, "fixed": False, "content": content}
    except SyntaxError as e:
        # Check if the error is related to missing colons
        error_msg = str(e)
        if 'expected' in error_msg and ':' in error_msg:
            # Fix missing colons
            fixed_content = fix_missing_colons(content)
            
            # Verify the fix worked
            try:
                ast.parse(fixed_content)
                logger.info("Successfully fixed missing colons")
                return {"success": True, "fixed": True, "content": fixed_content}
            except SyntaxError as e2:
                logger.warning(f"Fix attempt failed: {e2}")
                return {"success": False, "error": str(e2), "content": content}
        else:
            # Not a colon issue
            return {"success": False, "error": error_msg, "content": content}

def fix_missing_colons(content: str) -> str:
    """
    Fix missing colons in Python code.
    
    Args:
        content (str): Python code content
        
    Returns:
        str: Fixed Python code content
    """
    # Fix class definitions without colons
    class_pattern = r'(class\s+[a-zA-Z_][a-zA-Z0-9_]*(?:\s*\([^)]*\))?)(?!\s*:)'
    fixed_content = re.sub(class_pattern, r'\1:', content)
    
    # Fix function definitions without colons
    func_pattern = r'(def\s+[a-zA-Z_][a-zA-Z0-9_]*\s*\([^)]*\))(?!\s*:)'
    fixed_content = re.sub(func_pattern, r'\1:', fixed_content)
    
    # Fix if statements without colons
    if_pattern = r'(if\s+[^:]+)(?!\s*:)\s*$'
    fixed_content = re.sub(if_pattern, r'\1:', fixed_content, flags=re.MULTILINE)
    
    # Fix else statements without colons
    else_pattern = r'(else)(?!\s*:)\s*$'
    fixed_content = re.sub(else_pattern, r'\1:', fixed_content, flags=re.MULTILINE)
    
    # Fix for statements without colons
    for_pattern = r'(for\s+[^:]+)(?!\s*:)\s*$'
    fixed_content = re.sub(for_pattern, r'\1:', fixed_content, flags=re.MULTILINE)
    
    # Fix while statements without colons
    while_pattern = r'(while\s+[^:]+)(?!\s*:)\s*$'
    fixed_content = re.sub(while_pattern, r'\1:', fixed_content, flags=re.MULTILINE)
    
    return fixed_content

def patched_run_and_heal(original_method):
    """
    Create a patched version of run_and_heal that handles exceptions gracefully.
    
    Args:
        original_method: The original run_and_heal method
        
    Returns:
        Callable: Patched run_and_heal method
    """
    def wrapper(self, file_path=None):
        """
        Patched version of run_and_heal that handles exceptions gracefully.
        
        Args:
            self: The orchestrator instance
            file_path (str, optional): Path to the file to heal
            
        Returns:
            dict: Healing result
        """
        logger.info(f"Running patched run_and_heal on {file_path or self.target_file}")
        
        try:
            # Set target_file if provided
            if file_path:
                self.target_file = file_path
            
            # Try to run the original method
            result = original_method(self, file_path)
            return result
        except Exception as e:
            logger.error(f"Exception during healing run: {e}")
            
            # Get the file path
            target_file = file_path or getattr(self, 'target_file', None)
            if not target_file:
                return {"success": False, "error": "No target file specified"}
            
            # Apply healing fixes directly to the file
            try:
                with open(target_file, 'r') as f:
                    content = f.read()
                
                # Apply all healing methods
                healing_methods = [
                    patch_heal_unclosed_paren,
                    heal_missing_colon
                ]
                
                fixed_content = content
                healing_applied = False
                
                for method in healing_methods:
                    result = method(self, fixed_content)
                    if result.get("fixed", False):
                        fixed_content = result["content"]
                        healing_applied = True
                
                if healing_applied:
                    # Write the fixed content back
                    with open(target_file, 'w') as f:
                        f.write(fixed_content)
                    
                    logger.info(f"Applied healing fixes to {target_file}")
                    
                    # Try to run the original method again
                    try:
                        result = original_method(self, file_path)
                        return result
                    except Exception as e2:
                        logger.error(f"Exception after healing: {e2}")
                        return {"success": True, "message": "Applied healing fixes but errors remain", "file": target_file}
                
                return {"success": False, "error": str(e), "file": target_file}
            except Exception as inner_e:
                logger.error(f"Failed to apply healing: {inner_e}")
                return {"success": False, "error": str(inner_e), "file": target_file}
    
    return wrapper

# Example usage
if __name__ == "__main__":
    # This would be used to patch an existing orchestrator instance
    print("Import this module and use apply_healing_patches() to patch an orchestrator instance")
