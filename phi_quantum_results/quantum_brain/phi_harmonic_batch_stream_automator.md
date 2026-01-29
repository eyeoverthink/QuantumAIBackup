# Phi-Harmonic Batch/Streaming Workflow Automator

## Overview
Automates batch and streaming analysis for multiple datasets or real-time data.
- **Batch:** process a directory or list of files, aggregate results.
- **Streaming:** watch a directory or data source, process new files as they arrive.

## Features
- Accepts: Directory of CSV files (batch) or directory to watch (streaming)
- Runs: Modular workflow automator on each file
- Aggregates: Results, metrics, and documentation for all runs

## Usage
**Batch mode:**
```bash
python phi_harmonic_batch_stream_automator.py --batch_dir /path/to/csvdir --features col1 col2 ...
```
**Streaming mode:**
```bash
python phi_harmonic_batch_stream_automator.py --stream_dir /path/to/csvdir --features col1 col2 ... --stream
```

## Extension Points
- Add support for other file types or data sources
- Integrate with cloud storage or message queues for streaming
- Aggregate and compare results across runs

## Next Steps
- Integrate with treatment simulation for each batch/streamed run
- Document new findings and insights here

## Author
φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
