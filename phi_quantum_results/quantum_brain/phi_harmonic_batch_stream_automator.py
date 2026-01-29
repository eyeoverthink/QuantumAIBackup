#!/usr/bin/env python3
"""
Phi-Harmonic Batch/Streaming Workflow Automator

Automates batch and streaming analysis for multiple datasets or real-time data.
- Batch: process a directory or list of files, aggregate results.
- Streaming: watch a directory or data source, process new files as they arrive.

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import os
import sys
import argparse
import time
from glob import glob
from phi_harmonic_workflow_automator import main as workflow_main

# --- Batch Mode ---
def batch_mode(input_dir, features=None, results_root=None):
    files = glob(os.path.join(input_dir, '*.csv'))
    for f in files:
        print(f"Processing {f}")
        args = ["--input", f]
        if features:
            args += ["--features"] + features
        if results_root:
            args += ["--results_dir", os.path.join(results_root, os.path.splitext(os.path.basename(f))[0] + "_results")]
        sys.argv = [sys.argv[0]] + args
        workflow_main()

# --- Streaming Mode ---
def streaming_mode(watch_dir, features=None, results_root=None, poll_interval=10):
    seen = set()
    print(f"Watching {watch_dir} for new files...")
    while True:
        files = set(glob(os.path.join(watch_dir, '*.csv')))
        new_files = files - seen
        for f in new_files:
            print(f"Processing new file: {f}")
            args = ["--input", f]
            if features:
                args += ["--features"] + features
            if results_root:
                args += ["--results_dir", os.path.join(results_root, os.path.splitext(os.path.basename(f))[0] + "_results")]
            sys.argv = [sys.argv[0]] + args
            workflow_main()
        seen.update(new_files)
        time.sleep(poll_interval)

# --- Main CLI Entrypoint ---
def main():
    parser = argparse.ArgumentParser(description="Phi-Harmonic Batch/Streaming Automator")
    parser.add_argument("--batch_dir", help="Directory of CSV files for batch processing")
    parser.add_argument("--stream_dir", help="Directory to watch for streaming processing")
    parser.add_argument("--features", nargs="*", help="List of feature columns to use")
    parser.add_argument("--results_root", default=None, help="Root directory to save results")
    parser.add_argument("--stream", action="store_true", help="Enable streaming mode (default: batch)")
    parser.add_argument("--poll_interval", type=int, default=10, help="Streaming poll interval (seconds)")
    args = parser.parse_args()
    if args.stream:
        streaming_mode(args.stream_dir, features=args.features, results_root=args.results_root, poll_interval=args.poll_interval)
    else:
        batch_mode(args.batch_dir, features=args.features, results_root=args.results_root)

if __name__ == "__main__":
    main()
