
import os
import json

source_file = os.path.join(r"qr_progressive_test/workspace", "code_analysis.json")
output_file = os.path.join(r"qr_progressive_test/workspace", "analysis_report.md")

try:
    with open(source_file, 'r') as f:
        data = json.load(f)

    report = f"""# Analysis Report for {data.get('file_name', 'N/A')}

- **Line Count:** {data.get('line_count', 0)}
- **Character Count:** {data.get('char_count', 0)}
- **Functions:**
"""
    for func in data.get('functions', []):
        report += f"  - `{func}`
"

    with open(output_file, 'w') as f:
        f.write(report)
    print(f"Generated analysis report at {output_file}")

except (FileNotFoundError, json.JSONDecodeError) as e:
    print(f"Error processing analysis file: {e}")
    with open(output_file + '.error', 'w') as f:
        f.write(f"Could not process {source_file}. Error: {e}")
