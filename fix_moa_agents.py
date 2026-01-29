#!/usr/bin/env python3
"""
Fix for quantum_moa_agents.py syntax errors
"""

import re

def fix_coherence_agent_header():
    """Fix the syntax errors in the CoherenceAgent's docstring header."""
    with open('/Users/vaughnscott/CascadeProjects/QuantumAI/quantum_moa_agents.py', 'r') as file:
        content = file.read()
    
    # Fix the header array syntax error
    pattern = r"""header = \[\s*"{6}",\s*"Phi-Harmonic Module",\s*"------------------",\s*"",\s*"This module is designed with phi-harmonic coherence principles.",\s*"Coherence Target: \{:.6f\}".format\(target_coherence\),\s*"{6}"\s*\]"""
    replacement = """header = f\"\"\"
                    Phi-Harmonic Module
                    ------------------
                    
                    This module is designed with phi-harmonic coherence principles.
                    Coherence Target: {target_coherence:.6f}
                    \"\"\""""
    content = re.sub(pattern, replacement, content)
    
    # Fix the header insertion
    pattern = r"""# Insert after any shebang or encoding declarations\s*insert_pos = 0\s*for i, line in enumerate\(lines\):\s*if line\.startswith\('\#!'\):\s*insert_pos = i \+ 1\s*elif line\.startswith\('\# -\*- coding:'\):\s*insert_pos = i \+ 1\s*\s*for i, line in enumerate\(header\):\s*lines\.insert\(insert_pos \+ i, line\)"""
    replacement = """# Insert after any shebang or encoding declarations
                insert_pos = 0
                for i, line in enumerate(lines):
                    if line.startswith('#!'):
                        insert_pos = i + 1
                    elif line.startswith('# -*- coding:'):
                        insert_pos = i + 1
                
                lines.insert(insert_pos, header)"""
    content = re.sub(pattern, replacement, content)
    
    # Remove duplicated _enhance_evolution method
    pattern = r"""return '\\n'\.join\(lines\), enhancements\s*"{3}\s*Enhance code's self-evolution capabilities\.\s*\s*Args:\s*code: The original code\s*patterns: List of detected evolution patterns\s*evolution_targets: List of evolution capabilities to enhance\s*\s*Returns:\s*Tuple of \(evolved_code, number_of_enhancements\)\s*"{3}\s*if not patterns:\s*return code, 0\s*\s*lines = code\.split\('\\n'\)\s*enhancements = 0\s*\s*# Add evolution capabilities based on patterns and targets\s*has_class = any\(line\.strip\(\)\.startswith\('class '\) for line in lines\)\s*has_meta_learning = 'meta_learning' in evolution_targets\s*has_self_healing = 'self_healing' in evolution_targets\s*\s*if has_class:\s*# Find the main class\s*class_indices = \[i for i, line in enumerate\(lines\) if line\.strip\(\)\.startswith\('class '\)\]"""
    replacement = """return '\\n'.join(lines), enhancements"""
    content = re.sub(pattern, replacement, content)
    
    # Write the fixed content back to the file
    with open('/Users/vaughnscott/CascadeProjects/QuantumAI/quantum_moa_agents.py', 'w') as file:
        file.write(content)
    
    print("Fixed syntax errors in quantum_moa_agents.py")

if __name__ == "__main__":
    fix_coherence_agent_header()
