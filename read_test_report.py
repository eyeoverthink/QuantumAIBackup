#!/usr/bin/env python3
"""
Read the latest quantum cohesion test report.
"""

import os
import glob
import json
from datetime import datetime

def find_latest_report():
    """Find the latest test report in the results directory."""
    # Look for MD reports
    md_reports = glob.glob("quantum_cohesion_test/results/QUANTUM_COHESION_REPORT_*.md")
    # Look for JSON results
    json_reports = glob.glob("quantum_cohesion_test/results/cohesion_test_*.json")
    
    all_reports = md_reports + json_reports
    if not all_reports:
        print("No test reports found.")
        return None
    
    # Sort by modification time (newest first)
    latest_report = max(all_reports, key=os.path.getmtime)
    return latest_report

def read_report(report_path):
    """Read and display the report content."""
    print(f"Reading report: {report_path}")
    print("-" * 80)
    
    if report_path.endswith('.json'):
        try:
            with open(report_path, 'r') as f:
                data = json.load(f)
            print(f"Success rate: {data.get('success_rate', 0) * 100:.2f}%")
            print(f"Phi-harmonic coherence: {data.get('phi_harmonic_coherence', 0):.6f}")
            print("\nTest results:")
            for test_name, test_result in data.get('tests', {}).items():
                status = "✅" if test_result.get('success', False) else "❌"
                print(f"{status} {test_name}: {test_result.get('message', '')}")
                if 'error' in test_result:
                    print(f"   Error: {test_result['error']}")
        except Exception as e:
            print(f"Error reading JSON report: {e}")
    else:
        try:
            with open(report_path, 'r') as f:
                content = f.read()
            print(content)
        except Exception as e:
            print(f"Error reading report: {e}")

if __name__ == "__main__":
    report_path = find_latest_report()
    if report_path:
        read_report(report_path)
    else:
        print("No test reports found.")
