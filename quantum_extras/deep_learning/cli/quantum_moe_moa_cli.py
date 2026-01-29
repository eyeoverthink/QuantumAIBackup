#!/usr/bin/env python3
import argparse
import sys
import os
from pathlib import Path
import json
import asyncio
import numpy as np
from datetime import datetime

# Add the project root to Python path
project_root = str(Path(__file__).parent.parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from deep_learning.quantum_moe_moa import QuantumMoEMoA
from deep_learning.integrations.quantum_moe_moa_integration import QuantumMoEMoAIntegration

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description='QuantumMoEMoA CLI Tool')
    
    # Create subparsers for different commands
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Process command
    process_parser = subparsers.add_parser('process', help='Process a query')
    process_parser.add_argument('query', type=str, help='Query to process')
    process_parser.add_argument('--brain-type', type=str, default='Standard', 
                               help='Brain type (Standard or Creative)')
    
    # Evaluate command
    evaluate_parser = subparsers.add_parser('evaluate', help='Evaluate the model')
    
    # Visualize command
    visualize_parser = subparsers.add_parser('visualize', help='Generate a visualization')
    visualize_parser.add_argument('query', type=str, help='Query to visualize')
    
    # Benchmark command
    benchmark_parser = subparsers.add_parser('benchmark', help='Run a benchmark')
    benchmark_parser.add_argument('--num-queries', type=int, default=5, 
                                 help='Number of queries to run in the benchmark')
    
    # Learn command
    learn_parser = subparsers.add_parser('learn', help='Run the learning process')
    learn_parser.add_argument('--urls', type=str, nargs='+', 
                             help='URLs to learn from')
    learn_parser.add_argument('--duration', type=int, default=1, 
                             help='Duration in hours to run the learning process')
    
    # Status command
    status_parser = subparsers.add_parser('status', help='Get system status')
    
    return parser.parse_args()

async def main():
    """Main function"""
    args = parse_args()
    
    if not args.command:
        print("Error: No command specified. Use --help for usage information.")
        return
    
    # Initialize the quantum system
    quantum_moe_moa = QuantumMoEMoA()
    integration = QuantumMoEMoAIntegration()
    
    if args.command == 'process':
        print(f"Processing query: {args.query}")
        result = integration.process_query(args.query, args.brain_type)
        print("\nResults:")
        print(f"Combined score: {result['combined_metrics']['combined_score']}")
        print("\nQuantum AI Metrics:")
        for key, value in result['quantum_ai_result'].get('metrics', {}).items():
            print(f"  {key}: {value}")
        print("\nMoE/MoA Metrics:")
        print(f"  Expert utilization: {np.mean(result['moe_moa_result'].get('expert_utilization', [0]))}")
        print(f"  Temperature: {result['moe_moa_result'].get('temperature', 'N/A')}")
        
    elif args.command == 'evaluate':
        print("Evaluating model...")
        metrics = quantum_moe_moa.evaluate_model()
        print("\nEvaluation metrics:")
        for key, value in metrics.items():
            print(f"  {key}: {value}")
            
    elif args.command == 'visualize':
        print(f"Generating visualization for query: {args.query}")
        viz_path = integration.generate_enhanced_visualization(args.query)
        print(f"Visualization saved to: {viz_path}")
        
        # Display the visualization
        with open(viz_path, 'r') as f:
            print("\n" + f.read())
            
    elif args.command == 'benchmark':
        print(f"Running benchmark with {args.num_queries} queries...")
        benchmark_results = integration.run_benchmark(args.num_queries)
        print("\nBenchmark results:")
        print(f"  Number of queries: {benchmark_results['num_queries']}")
        print(f"  Total duration: {benchmark_results['total_duration_seconds']:.2f} seconds")
        print(f"  Average time per query: {benchmark_results['avg_time_per_query']:.2f} seconds")
        print(f"  Average combined score: {benchmark_results['avg_combined_score']}")
        
    elif args.command == 'learn':
        if not args.urls:
            # Default URLs if none provided
            args.urls = [
                "https://arxiv.org/list/quant-ph/recent",
                "https://quantum-computing.ibm.com/docs",
                "https://quantum.country",
                "https://qiskit.org/documentation"
            ]
            
        print(f"Starting learning process with {len(args.urls)} URLs for {args.duration} hour(s)...")
        print(f"URLs: {', '.join(args.urls)}")
        
        # Create a task to run for the specified duration
        start_time = datetime.now()
        end_time = start_time + datetime.timedelta(hours=args.duration)
        
        try:
            # Run the learning process for a single iteration
            await quantum_moe_moa.learn_from_web(args.urls)
            quantum_moe_moa.evolve_architecture()
            
            print(f"Learning process completed at {datetime.now()}")
            print(f"Total duration: {(datetime.now() - start_time).total_seconds() / 60:.2f} minutes")
            
        except KeyboardInterrupt:
            print("\nLearning process interrupted by user.")
            
    elif args.command == 'status':
        print("QuantumMoEMoA System Status:")
        print(f"  Timestamp: {datetime.now().isoformat()}")
        print(f"  Device: {quantum_moe_moa.device}")
        print(f"  Model configuration:")
        for key, value in quantum_moe_moa.config['model'].items():
            print(f"    {key}: {value}")
        print(f"  Training configuration:")
        for key, value in quantum_moe_moa.config['training'].items():
            print(f"    {key}: {value}")
        print(f"  Evolution configuration:")
        for key, value in quantum_moe_moa.config['evolution'].items():
            print(f"    {key}: {value}")
        print(f"  Scraping configuration:")
        for key, value in quantum_moe_moa.config['scraping'].items():
            print(f"    {key}: {value}")

if __name__ == '__main__':
    asyncio.run(main())
