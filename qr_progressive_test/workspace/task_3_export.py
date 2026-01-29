
import os
import json

source_file = os.path.join(r"qr_progressive_test/workspace", "hello_world.py")
export_file = os.path.join(r"qr_progressive_test/workspace", "code_analysis.json")

try:
    with open(source_file, 'r') as f:
        content = f.read()

    analysis = {
        'file_name': os.path.basename(source_file),
        'line_count': len(content.splitlines()),
        'char_count': len(content),
        'functions': [line.split('(')[0].replace('def ','') for line in content.splitlines() if line.strip().startswith('def ')]
    }

    with open(export_file, 'w') as f:
        json.dump(analysis, f, indent=2)
    print(f"Exported analysis to {export_file}")
except FileNotFoundError:
    print(f"Error: Source file not found at {source_file}")
    # Create an empty error file to signal failure
    with open(export_file + '.error', 'w') as f:
        f.write(f"Could not find {source_file}")
