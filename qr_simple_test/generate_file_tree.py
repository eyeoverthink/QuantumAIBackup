#!/usr/bin/env python3
"""
Generate a file tree of the QuantumAI project and save it to FILE_STATUS.TXT
"""

import os
import sys

# Directories to exclude
EXCLUDE_DIRS = [
    '__pycache__',
    '.venv',
    'env',
    'venv',
    'node_modules',
    '.git',
    'qr_dna_env'
]

def generate_file_tree(start_path, output_file):
    """Generate a file tree and write it to the specified output file."""
    with open(output_file, 'w') as f:
        f.write(f"File Tree for: {os.path.abspath(start_path)}\n")
        f.write("=" * 80 + "\n\n")
        
        for root, dirs, files in os.walk(start_path):
            # Skip excluded directories
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            
            # Calculate the level for indentation
            level = root.replace(start_path, '').count(os.sep)
            indent = '│   ' * level
            
            # Write directory name
            rel_path = os.path.relpath(root, start_path)
            if rel_path == '.':
                f.write(f"📁 {os.path.basename(os.path.abspath(start_path))}\n")
            else:
                f.write(f"{indent}├── 📁 {os.path.basename(root)}\n")
            
            # Write files
            sub_indent = '│   ' * (level + 1)
            for i, file in enumerate(sorted(files)):
                if i == len(files) - 1 and len(dirs) == 0:
                    f.write(f"{sub_indent}└── 📄 {file}\n")
                else:
                    f.write(f"{sub_indent}├── 📄 {file}\n")

if __name__ == "__main__":
    # Use the current directory as the starting point
    start_path = '.'
    output_file = 'FILE_STATUS.TXT'
    
    generate_file_tree(start_path, output_file)
    print(f"File tree generated and saved to {output_file}")
