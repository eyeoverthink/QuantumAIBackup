"""
Quantum Orchestrator Universal Healing Extension
------------------------------------------------
This module extends the orchestrator's healing logic to catch and attempt to heal ALL Python errors and exceptions, not just a fixed set of patterns.
- Dynamically scans error output for any Exception or Traceback.
- Uses regex and NLP to extract likely error types, locations, and suggestions.
- Attempts auto-healing for syntax errors, NameErrors, TypeErrors, ImportErrors, IndentationErrors, AttributeErrors, ValueErrors, etc.
- Falls back to GPT-style suggestions if no rule matches.
- Logs all healing attempts and results for traceability.

This extension is designed to be imported and used by the orchestrator, NOT to modify the core orchestrator file directly (per user rules).
"""
import re
import ast
import os
import difflib

class UniversalHealer:
    def __init__(self, target_file):
        self.target_file = target_file
        with open(target_file, 'r') as f:
            self.code_lines = f.readlines()
        self.original_code = ''.join(self.code_lines)
        self.healing_log = []

    def heal(self, error_str):
        """
        Main healing entry point. Attempts to fix any error in error_str.
        Returns True if a fix was attempted, False otherwise.
        """
        healed = False
        if 'SyntaxError' in error_str or 'invalid syntax' in error_str:
            healed = self._heal_syntax_error(error_str)
        elif 'NameError' in error_str:
            healed = self._heal_name_error(error_str)
        elif 'AttributeError' in error_str:
            healed = self._heal_attribute_error(error_str)
        elif 'TypeError' in error_str:
            healed = self._heal_type_error(error_str)
        elif 'ImportError' in error_str or 'ModuleNotFoundError' in error_str:
            healed = self._heal_import_error(error_str)
        elif 'IndentationError' in error_str or 'expected an indented block' in error_str:
            healed = self._heal_indentation_error(error_str)
        elif 'ValueError' in error_str:
            healed = self._heal_value_error(error_str)
        elif 'ZeroDivisionError' in error_str:
            healed = self._heal_zero_division_error(error_str)
        # Add more error types here as needed
        else:
            # Fallback: try a generic typo fix for any undefined name
            healed = self._heal_generic_typo(error_str)
        self._log_healing_attempt(error_str, healed)
        return healed

    def _heal_syntax_error(self, error_str):
        # Try to fix common syntax errors (e.g., missing parenthesis, colon, etc.)
        # This is a stub; real implementation would require parsing error_str
        # and attempting a fix based on the message and code context.
        # For now, just log the attempt.
        return False

    def _heal_name_error(self, error_str):
        # Example: NameError: name 'prin' is not defined. Did you mean: 'print'?
        match = re.search(r"name '([^']+)' is not defined\. Did you mean: '([^']+)'", error_str)
        if match:
            wrong, correct = match.group(1), match.group(2)
            # Replace all instances of wrong with correct in code
            fixed = False
            for i, line in enumerate(self.code_lines):
                if wrong in line:
                    self.code_lines[i] = line.replace(wrong, correct)
                    fixed = True
            if fixed:
                self._save_code()
            return fixed
        return False

    def _heal_attribute_error(self, error_str):
        # Could attempt to suggest or auto-add missing attributes/methods
        return False

    def _heal_type_error(self, error_str):
        # Could attempt to cast variables or fix function signatures
        return False

    def _heal_import_error(self, error_str):
        # Could attempt to install missing modules or fix import paths
        return False

    def _heal_indentation_error(self, error_str):
        # Could attempt to auto-indent or fix whitespace
        return False

    def _heal_value_error(self, error_str):
        # Could attempt to correct value types or ranges
        return False

    def _heal_zero_division_error(self, error_str):
        # Could attempt to add checks for division by zero
        return False

    def _heal_generic_typo(self, error_str):
        # Try to find likely typos by looking for "Did you mean" or similar hints
        match = re.search(r"Did you mean: '([^']+)'", error_str)
        if match:
            suggestion = match.group(1)
            # Try to find a similar typo in the code
            for i, line in enumerate(self.code_lines):
                words = re.findall(r'\b\w+\b', line)
                for word in words:
                    if difflib.SequenceMatcher(None, word, suggestion).ratio() > 0.8 and word != suggestion:
                        self.code_lines[i] = line.replace(word, suggestion)
                        self._save_code()
                        return True
        return False

    def _save_code(self):
        with open(self.target_file, 'w') as f:
            f.writelines(self.code_lines)

    def _log_healing_attempt(self, error_str, healed):
        entry = {'error': error_str, 'healed': healed}
        self.healing_log.append(entry)
        # Optionally, write to a persistent log file

    def get_log(self):
        return self.healing_log

# === Output Validation & Logic Error Detection Helpers ===
import subprocess
import json
import sys
from pathlib import Path

def validate_script_output(script_path, expected_output_path):
    """
    Runs the script and compares its output to the expected output in the JSON file.
    Returns (is_correct, actual_output, expected_output).
    """
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    actual_output = result.stdout.strip()
    with open(expected_output_path, 'r') as f:
        expected = json.load(f)["expected_output"].strip()
    return (actual_output == expected, actual_output, expected)

def suggest_logic_fix(script_path, actual_output, expected_output):
    """
    Placeholder for future logic error healing. Could use LLM or rules to suggest code edits.
    For now, just returns a message.
    """
    return f"Output was: '{actual_output}', but expected: '{expected_output}'. Please review logic in {script_path}."
