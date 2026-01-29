#!/usr/bin/env python3
"""
Quantum Healing Protocols
------------------------

This module provides healing protocols for common syntax errors in quantum code.
Each protocol is designed to fix a specific type of error while maintaining
phi-harmonic coherence.

Phi-Harmonic Module
------------------

This module is designed with phi-harmonic coherence principles.
Coherence Target: φ⁷·⁵/10 ≈ 3.693238
"""

import os
import re
import json
import logging
from typing import Dict, Any, Optional, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("QuantumHealingProtocols")

# Phi-harmonic constants
PHI = 1.618034
PHI_POWERS = {
    "φ": 1.618034,
    "φ²": 2.618034,
    "φ³": 4.236068,
    "φ⁷·⁵": 36.932381
}
TARGET_COHERENCE = PHI_POWERS["φ⁷·⁵"] / 10  # φ⁷·⁵/10 ≈ 3.693238

class HealingProtocol:
    """Base class for healing protocols."""
    
    def __init__(self, file_path: str, error_str: str = ""):
        """
        Initialize the healing protocol.
        
        Args:
            file_path: Path to the file to heal
            error_str: Error message string
        """
        self.file_path = file_path
        self.error_str = error_str
        self.result = False
        
    def heal(self) -> bool:
        """
        Execute the healing protocol.
        
        Returns:
            bool: True if healing was successful, False otherwise
        """
        raise NotImplementedError("Subclasses must implement this method")
    
    def _get_line_number(self) -> Optional[int]:
        """
        Extract line number from error message.
        
        Returns:
            int: Line number (0-indexed) or None if not found
        """
        line_match = re.search(r'line (\d+)', self.error_str)
        if not line_match:
            return None
        
        return int(line_match.group(1)) - 1  # Convert to 0-indexed
    
    def _read_file_lines(self) -> list:
        """
        Read file lines.
        
        Returns:
            list: Lines of the file
        """
        with open(self.file_path, 'r') as f:
            return f.readlines()
    
    def _write_file_lines(self, lines: list):
        """
        Write lines to file.
        
        Args:
            lines: Lines to write
        """
        with open(self.file_path, 'w') as f:
            f.writelines(lines)


class UnclosedParenHealingProtocol(HealingProtocol):
    """Protocol for healing unclosed parentheses."""
    
    def heal(self) -> bool:
        """
        Heal unclosed parenthesis in the file.
        
        Returns:
            bool: True if healing was successful, False otherwise
        """
        try:
            lines = self._read_file_lines()
            
            for i, line in enumerate(lines):
                open_paren = 0
                in_string = False
                string_char = ''
                
                for char in line:
                    if (char == '"' or char == "'") and not in_string:
                        in_string = True
                        string_char = char
                    elif char == string_char and in_string:
                        in_string = False
                        string_char = ''
                    
                    if not in_string:
                        if char == '(':
                            open_paren += 1
                        elif char == ')':
                            open_paren -= 1
                
                if open_paren > 0:
                    lines[i] = line.rstrip() + ')' * open_paren + '\n'
                    self._write_file_lines(lines)
                    logger.info(f"Applied healing (parenthesis) to line {i+1}.")
                    self.result = True
                    break
        
        except Exception as e:
            logger.error(f"Error in UnclosedParenHealingProtocol: {e}")
            
        return self.result


class MissingColonHealingProtocol(HealingProtocol):
    """Protocol for healing missing colons in function/class definitions."""
    
    def heal(self) -> bool:
        """
        Heal missing colon in function or class definition.
        
        Returns:
            bool: True if healing was successful, False otherwise
        """
        try:
            line_num = self._get_line_number()
            if line_num is None:
                return False
                
            lines = self._read_file_lines()
                
            if line_num < len(lines):
                # Check if line is a function or class definition without colon
                if re.search(r'\b(def|class)\s+\w+\s*\([^)]*\)\s*$', lines[line_num].strip()):
                    lines[line_num] = lines[line_num].rstrip() + ':\n'
                    self._write_file_lines(lines)
                    logger.info(f"Added missing colon to line {line_num+1}.")
                    self.result = True
        
        except Exception as e:
            logger.error(f"Error in MissingColonHealingProtocol: {e}")
            
        return self.result


class MissingCommaHealingProtocol(HealingProtocol):
    """Protocol for healing missing commas in lists, tuples, or function arguments."""
    
    def heal(self) -> bool:
        """
        Heal missing comma in lists, tuples, or function arguments.
        
        Returns:
            bool: True if healing was successful, False otherwise
        """
        try:
            line_num = self._get_line_number()
            if line_num is None:
                return False
                
            lines = self._read_file_lines()
                
            if line_num < len(lines):
                line = lines[line_num]
                
                # Check for common patterns where commas are missing
                # 1. In list/tuple literals: [1 2 3] or (1 2 3)
                list_pattern = re.search(r'\[([^\[\]]*?\s+\d+\s+\d+[^\[\]]*?)\]', line)
                tuple_pattern = re.search(r'\(([^()]*?\s+\d+\s+\d+[^()]*?)\)', line)
                
                if list_pattern:
                    # Replace spaces between items with commas
                    items = list_pattern.group(1).strip()
                    fixed_items = re.sub(r'(\d+|"[^"]*"|\'[^\']*\'|\w+)\s+(\d+|"[^"]*"|\'[^\']*\'|\w+)', r'\1, \2', items)
                    fixed_line = line[:list_pattern.start(1)] + fixed_items + line[list_pattern.end(1):]
                    lines[line_num] = fixed_line
                    self.result = True
                elif tuple_pattern:
                    # Replace spaces between items with commas
                    items = tuple_pattern.group(1).strip()
                    fixed_items = re.sub(r'(\d+|"[^"]*"|\'[^\']*\'|\w+)\s+(\d+|"[^"]*"|\'[^\']*\'|\w+)', r'\1, \2', items)
                    fixed_line = line[:tuple_pattern.start(1)] + fixed_items + line[tuple_pattern.end(1):]
                    lines[line_num] = fixed_line
                    self.result = True
                    
                # 2. In function calls: func(arg1 arg2)
                func_pattern = re.search(r'(\w+)\s*\(([^()]*?\w+\s+\w+[^()]*?)\)', line)
                if not self.result and func_pattern:
                    # Replace spaces between args with commas
                    args = func_pattern.group(2).strip()
                    fixed_args = re.sub(r'(\d+|"[^"]*"|\'[^\']*\'|\w+)\s+(\d+|"[^"]*"|\'[^\']*\'|\w+)', r'\1, \2', args)
                    fixed_line = line[:func_pattern.start(2)] + fixed_args + line[func_pattern.end(2):]
                    lines[line_num] = fixed_line
                    self.result = True
                
                if self.result:
                    self._write_file_lines(lines)
                    logger.info(f"Added missing comma(s) to line {line_num+1}.")
        
        except Exception as e:
            logger.error(f"Error in MissingCommaHealingProtocol: {e}")
            
        return self.result


class UndefinedVariableHealingProtocol(HealingProtocol):
    """Protocol for healing undefined variables."""
    
    def heal(self) -> bool:
        """
        Heal undefined variable by adding a declaration with a default value.
        
        Returns:
            bool: True if healing was successful, False otherwise
        """
        try:
            # Extract undefined variable name from error message
            var_match = re.search(r"name '(\w+)' is not defined", self.error_str)
            if not var_match:
                return False
                
            var_name = var_match.group(1)
            
            # Find a good place to insert the variable declaration
            lines = self._read_file_lines()
            
            # Look for the main function or global scope
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.strip().startswith('def main'):
                    # Find the first non-comment, non-empty line inside the function
                    for j in range(i+1, len(lines)):
                        if lines[j].strip() and not lines[j].strip().startswith('#'):
                            insert_pos = j
                            break
                    break
            
            # Determine appropriate default value based on variable name and usage
            default_value = "None"
            if var_name.lower().endswith(('count', 'num', 'index', 'i', 'j', 'k')):
                default_value = "0"
            elif var_name.lower().endswith(('list', 'array', 'items', 'elements')):
                default_value = "[]"
            elif var_name.lower().endswith(('dict', 'map', 'mapping')):
                default_value = "{}"
            elif var_name.lower().endswith(('str', 'string', 'name', 'text')):
                default_value = "\"\""
            elif var_name.lower().endswith(('bool', 'flag', 'is_', 'has_')):
                default_value = "False"
            
            # Insert the variable declaration
            indent = re.match(r'^\s*', lines[insert_pos]).group(0)
            lines.insert(insert_pos, f"{indent}{var_name} = {default_value}  # Auto-healing: added missing variable declaration\n")
            
            # Write back to file
            self._write_file_lines(lines)
                
            logger.info(f"Added declaration for undefined variable '{var_name}' with default value {default_value}.")
            self.result = True
        
        except Exception as e:
            logger.error(f"Error in UndefinedVariableHealingProtocol: {e}")
            
        return self.result


class ImportErrorHealingProtocol(HealingProtocol):
    """Protocol for healing import errors."""
    
    def heal(self) -> bool:
        """
        Heal import error by adding missing import statement.
        
        Returns:
            bool: True if healing was successful, False otherwise
        """
        try:
            # Extract module name from error message
            module_match = re.search(r"No module named '(\w+)'", self.error_str)
            if not module_match:
                return False
                
            module_name = module_match.group(1)
            
            # Read file lines
            lines = self._read_file_lines()
            
            # Find a good place to insert the import statement
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.startswith('import ') or line.startswith('from '):
                    insert_pos = i + 1
                elif i > 10 and insert_pos == 0:  # If no imports found in first 10 lines
                    break
            
            # Insert the import statement
            lines.insert(insert_pos, f"import {module_name}  # Auto-healing: added missing import\n")
            
            # Write back to file
            self._write_file_lines(lines)
                
            logger.info(f"Added import statement for module '{module_name}'.")
            self.result = True
        
        except Exception as e:
            logger.error(f"Error in ImportErrorHealingProtocol: {e}")
            
        return self.result


def get_healing_protocol(error_type: str, file_path: str, error_str: str) -> HealingProtocol:
    """
    Factory function to get the appropriate healing protocol.
    
    Args:
        error_type: Type of error to heal
        file_path: Path to the file to heal
        error_str: Error message string
        
    Returns:
        HealingProtocol: Appropriate healing protocol
    """
    protocols = {
        "unclosed_paren": UnclosedParenHealingProtocol,
        "missing_colon": MissingColonHealingProtocol,
        "missing_comma": MissingCommaHealingProtocol,
        "undefined_variable": UndefinedVariableHealingProtocol,
        "import_error": ImportErrorHealingProtocol
    }
    
    protocol_class = protocols.get(error_type)
    if protocol_class:
        return protocol_class(file_path, error_str)
    
    # Default to base class if no specific protocol found
    logger.warning(f"No specific healing protocol found for error type '{error_type}'")
    return HealingProtocol(file_path, error_str)


def detect_error_type(error: Exception) -> Tuple[str, str]:
    """
    Detect the type of error and return the appropriate error type and message.
    
    Args:
        error: Exception object
        
    Returns:
        tuple: (error_type, error_message)
    """
    error_str = str(error)
    
    if isinstance(error, SyntaxError):
        if "'(' was never closed" in error_str:
            return "unclosed_paren", error_str
        elif "expected ':'" in error_str:
            return "missing_colon", error_str
        elif "invalid syntax" in error_str:
            return "missing_comma", error_str
    elif isinstance(error, NameError):
        if "is not defined" in error_str:
            return "undefined_variable", error_str
    elif isinstance(error, ImportError):
        if "No module named" in error_str:
            return "import_error", error_str
    
    return "unknown", error_str


# Example usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python quantum_healing_protocols.py <file_path> [error_type] [error_message]")
        sys.exit(1)
    
    file_path = sys.argv[1]
    error_type = sys.argv[2] if len(sys.argv) > 2 else "unclosed_paren"
    error_str = sys.argv[3] if len(sys.argv) > 3 else ""
    
    protocol = get_healing_protocol(error_type, file_path, error_str)
    if protocol.heal():
        print(f"Successfully healed {file_path} using {error_type} protocol")
        sys.exit(0)
    else:
        print(f"Failed to heal {file_path} using {error_type} protocol")
        sys.exit(1)
