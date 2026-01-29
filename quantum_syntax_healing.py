"""
quantum_syntax_healing.py
Phi-harmonic quantum syntax healing extension for the orchestrator.
Detects and fixes common syntax errors in Python files.
"""

import os
import ast
import logging
import time
import json
import re

# Phi-harmonic coherence value for syntax healing
PHI_COHERENCE = 0.991800

def heal_syntax_errors(file_path):
    """
    Detect and heal common syntax errors in Python files.
    Returns a dict with status and content.
    """
    try:
        # Read the file content
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Try to parse the file to detect syntax errors
        try:
            ast.parse(content)
            return {'status': 'no_errors', 'content': content}
        except SyntaxError as se:
            logging.warning(f"Syntax error detected: {str(se)}")
            
            # Attempt to fix common syntax errors
            fixed_content = content
            error_fixed = False
            
            # Fix 1: Missing closing brackets/parentheses/braces
            if "was never closed" in str(se) or "EOF while scanning" in str(se):
                # Get the line number from the error message
                line_num = None
                line_match = re.search(r'line (\d+)', str(se))
                if line_match:
                    line_num = int(line_match.group(1))
                    logging.info(f"Syntax error detected on line {line_num}")
                
                # Identify which bracket is missing
                if "'['" in str(se) or "[" in str(se):
                    # For unclosed brackets, we need to add it to the end of the line
                    if line_num:
                        lines = fixed_content.split('\n')
                        if line_num <= len(lines):
                            lines[line_num-1] = lines[line_num-1] + "]"  # Add missing closing bracket
                            fixed_content = '\n'.join(lines)
                            logging.info(f"Adding missing closing bracket ] to line {line_num}")
                            error_fixed = True
                    else:
                        # Fallback: add to the end of the file
                        fixed_content = fixed_content + "]"  
                        logging.info("Adding missing closing bracket ] to end of file")
                        error_fixed = True
                elif "'('" in str(se) or "(" in str(se):
                    if line_num:
                        lines = fixed_content.split('\n')
                        if line_num <= len(lines):
                            lines[line_num-1] = lines[line_num-1] + ")"  # Add missing closing parenthesis
                            fixed_content = '\n'.join(lines)
                            logging.info(f"Adding missing closing parenthesis ) to line {line_num}")
                            error_fixed = True
                    else:
                        fixed_content = fixed_content + ")"  
                        logging.info("Adding missing closing parenthesis ) to end of file")
                        error_fixed = True
                elif "'{'" in str(se) or "{" in str(se):
                    if line_num:
                        lines = fixed_content.split('\n')
                        if line_num <= len(lines):
                            lines[line_num-1] = lines[line_num-1] + "}"  # Add missing closing brace
                            fixed_content = '\n'.join(lines)
                            logging.info(f"Adding missing closing brace }} to line {line_num}")
                            error_fixed = True
                    else:
                        fixed_content = fixed_content + "}"  
                        logging.info("Adding missing closing brace } to end of file")
                        error_fixed = True
                elif "string literal" in str(se):
                    # Try to fix unclosed string
                    if "'" in str(se):
                        if line_num:
                            lines = fixed_content.split('\n')
                            if line_num <= len(lines):
                                lines[line_num-1] = lines[line_num-1] + "'"  # Add missing single quote
                                fixed_content = '\n'.join(lines)
                                logging.info(f"Adding missing single quote ' to line {line_num}")
                                error_fixed = True
                        else:
                            fixed_content = fixed_content + "'"  
                            logging.info("Adding missing single quote ' to end of file")
                            error_fixed = True
                    else:
                        if line_num:
                            lines = fixed_content.split('\n')
                            if line_num <= len(lines):
                                lines[line_num-1] = lines[line_num-1] + '"'  # Add missing double quote
                                fixed_content = '\n'.join(lines)
                                logging.info(f"Adding missing double quote \" to line {line_num}")
                                error_fixed = True
                        else:
                            fixed_content = fixed_content + '"'  
                            logging.info("Adding missing double quote \" to end of file")
                            error_fixed = True
            
            if error_fixed:
                # Try to parse again to see if our fix worked
                try:
                    ast.parse(fixed_content)
                    # If we get here, the fix worked
                    with open(file_path, 'w') as f:
                        f.write(fixed_content)
                    logging.info(f"✅ Fixed syntax error in {file_path}")
                    
                    # Save to evolution JSON for tracking
                    try:
                        evolution_file = file_path.replace('.py', '_evolution.json')
                        evolution_data = {}
                        if os.path.exists(evolution_file):
                            with open(evolution_file, 'r') as ef:
                                evolution_data = json.load(ef)
                        
                        # Add syntax healing event to evolution data
                        if 'healing_events' not in evolution_data:
                            evolution_data['healing_events'] = []
                        
                        evolution_data['healing_events'].append({
                            'timestamp': time.time(),
                            'type': 'syntax_healing',
                            'error': str(se),
                            'phi_coherence': PHI_COHERENCE,
                            'quantum_fingerprint': f"φ⁷·⁵-{hash(fixed_content)}"
                        })
                        
                        with open(evolution_file, 'w') as ef:
                            json.dump(evolution_data, ef, indent=2)
                    except Exception as json_err:
                        logging.warning(f"Could not update evolution JSON: {str(json_err)}")
                    
                    return {'status': 'healed', 'content': fixed_content}
                except SyntaxError:
                    # Our simple fix didn't work
                    return {'status': 'failed', 'error': f"Couldn't fix syntax error: {str(se)}"}
            else:
                return {'status': 'failed', 'error': f"Unsupported syntax error type: {str(se)}"}
    except Exception as e:
        logging.warning(f"Syntax healing attempt failed: {str(e)}")
        return {'status': 'failed', 'error': str(e)}

def apply_syntax_healing(file_path):
    """
    Apply syntax healing to a file and return the result.
    This is the main entry point for the orchestrator.
    """
    print(f"🔍 Checking for syntax errors in {file_path}...")
    result = heal_syntax_errors(file_path)
    
    if result['status'] == 'healed':
        print(f"🩹 Syntax healing applied successfully to {file_path}")
    elif result['status'] == 'no_errors':
        print(f"✅ No syntax errors found in {file_path}")
    else:
        print(f"❌ Failed to heal syntax errors in {file_path}: {result.get('error', 'Unknown error')}")
    
    return result
