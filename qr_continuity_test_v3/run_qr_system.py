#!/usr/bin/env python3
"""
QR Flipbook DNA System Runner - Main Entry Point
By Vaughn Scott

Orchestrates the complete QR Flipbook DNA system:
- Creates and evolves QR genomes with phi-harmonic principles
- Generates QR code sequences from genomes
- Displays QR flipbooks with phi-harmonic timing
- Captures and executes QR codes via camera
- Maintains epigenetic memory across executions
"""

import os
import sys
import json
import time
import argparse
import numpy as np
from datetime import datetime

# Phi (Golden Ratio) constant
PHI = (1 + np.sqrt(5)) / 2  # Approximately 1.618034

def setup_environment():
    """Setup the environment and check for required dependencies."""
    try:
        # Check for required modules
        import qrcode
        import PIL
        import cv2
        import pygame
        import cryptography
        import numpy
        
        print("✅ All required dependencies are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("\nPlease install required dependencies:")
        print("pip install qrcode[pil] opencv-python pygame cryptography numpy pyzbar")
        return False

def create_genome():
    """Create a new QR genome."""
    from qr_genome_engine import QRGenomeEngine
    from qr_codon_groups import create_basic_genome
    
    print("\n🧬 Creating new QR genome...")
    
    # Create genome engine
    engine = QRGenomeEngine(debug=True)
    
    # Create basic genome
    engine.create_basic_genome()
    
    # Print genome summary
    engine.genome.print_summary()
    
    print("\n✅ Genome created successfully")
    return engine.genome_file

def execute_genome(genome_file="qr_genome.json", memory_file="qr_epigenetic_memory.json"):
    """Execute a QR genome."""
    from qr_genome_engine import QRGenomeEngine
    
    print(f"\n🧬 Executing QR genome from {genome_file}...")
    
    # Create genome engine
    engine = QRGenomeEngine(
        genome_file=genome_file,
        memory_file=memory_file,
        debug=True
    )
    
    # Execute genome
    results = engine.run_genome_execution()
    
    # Print execution summary
    engine.print_execution_summary(results)
    
    print("\n✅ Genome execution complete")
    return results

def evolve_genome(genome_file="qr_genome.json", memory_file="qr_epigenetic_memory.json"):
    """Evolve a QR genome using phi-harmonic principles."""
    from qr_genome_engine import QRGenomeEngine
    
    print(f"\n🧬 Evolving QR genome from {genome_file}...")
    
    # Create genome engine
    engine = QRGenomeEngine(
        genome_file=genome_file,
        memory_file=memory_file,
        debug=True
    )
    
    # Evolve genome
    mutations = engine.evolve_genome()
    
    if mutations > 0:
        print(f"\n✅ Applied {mutations} mutations to genome")
        print(f"✅ Advanced to generation {engine.genome.generation}")
    else:
        print("\n✅ No mutations applied (genome is stable)")
    
    # Print memory summary
    engine.memory.print_memory_summary()
    
    return mutations

def generate_qr_sequence(genome_file="qr_genome.json", output_dir="qr_genome_sequence", frames=20):
    """Generate a QR code sequence from a genome."""
    from qr_genome_engine import QRGenomeEngine
    
    print(f"\n🧬 Generating QR sequence from {genome_file}...")
    
    # Create genome engine
    engine = QRGenomeEngine(
        genome_file=genome_file,
        debug=True
    )
    
    # Generate QR sequence
    sequence_dir = engine.generate_qr_sequence(
        output_dir=output_dir,
        frames=frames
    )
    
    print(f"\n✅ Generated QR sequence in {sequence_dir}")
    return sequence_dir

def display_qr_sequence(sequence_dir="qr_genome_sequence", fullscreen=False):
    """Display a QR code sequence as a flipbook."""
    from qr_display import QRDisplayEngine
    
    print(f"\n📺 Displaying QR sequence from {sequence_dir}...")
    
    # Create display engine
    display = QRDisplayEngine(
        sequence_dir=sequence_dir,
        fullscreen=fullscreen
    )
    
    # Run display
    display.run()
    
    print("\n✅ QR sequence display complete")

def analyze_qr_sequence(sequence_dir="qr_genome_sequence"):
    """Analyze a QR code sequence."""
    from qr_flipbook_analyzer import QRFlipbookAnalyzer
    
    print(f"\n🔍 Analyzing QR sequence in {sequence_dir}...")
    
    # Create analyzer
    analyzer = QRFlipbookAnalyzer(sequence_dir=sequence_dir)
    
    # Analyze sequence
    analysis = analyzer.analyze_sequence()
    
    # Print sequence summary
    analyzer.print_sequence_summary(analysis)
    
    # Visualize phi evolution
    analyzer.visualize_phi_evolution()
    
    print("\n✅ QR sequence analysis complete")
    return analysis

def run_qr_worker(camera_id=1):
    """Run the QR worker to capture and execute QR codes."""
    from qr_worker import QRWorker
    
    print(f"\n👁️ Starting QR worker with camera {camera_id}...")
    
    # Create worker
    worker = QRWorker(camera_id=camera_id)
    
    # Run worker
    worker.run()
    
    print("\n✅ QR worker stopped")

def run_full_cycle():
    """Run a full cycle of the QR Flipbook DNA system."""
    print("\n🔄 Running full QR Flipbook DNA system cycle...")
    
    # Create genome
    genome_file = create_genome()
    
    # Execute genome
    execute_genome(genome_file)
    
    # Evolve genome
    evolve_genome(genome_file)
    
    # Generate QR sequence
    sequence_dir = generate_qr_sequence(genome_file)
    
    # Analyze QR sequence
    analyze_qr_sequence(sequence_dir)
    
    # Display QR sequence
    display_qr_sequence(sequence_dir)
    
    print("\n✅ Full cycle complete")

def print_system_info():
    """Print information about the QR Flipbook DNA system."""
    print("\n" + "="*60)
    print("🧬 QR FLIPBOOK DNA SYSTEM")
    print("By Vaughn Scott")
    print("="*60)
    
    print("\nThis system implements a phi-harmonic, self-evolving code execution")
    print("environment using QR codes as a visual DNA-like medium.")
    
    print("\nCOMPONENTS:")
    print("  • QR Genome Engine - Orchestrates execution of QR DNA")
    print("  • QR Epigenetic Memory - Stores execution history across sessions")
    print("  • QR Codon Groups - Organizes QR frames into functional units")
    print("  • QR Task Executor - Safely executes code fragments")
    print("  • QR Display Engine - Shows QR flipbooks with phi-harmonic timing")
    print("  • QR Flipbook Analyzer - Analyzes QR sequences and evolution")
    print("  • QR Worker - Captures and executes QR codes via camera")
    
    print("\nPHI-HARMONIC PRINCIPLES:")
    print(f"  • Golden Ratio (φ): {PHI}")
    print("  • Complexity Evolution: Code fragments evolve in complexity")
    print("  • Resonance Calculation: 1.0 / (1.0 + abs((x * φ) % 1.0 - 0.5))")
    print("  • Hash Chain Integrity: Each frame validates previous frame")
    
    print("\n" + "="*60)

def main():
    """Main function to run the QR Flipbook DNA system."""
    parser = argparse.ArgumentParser(
        description="QR Flipbook DNA System Runner",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python run_qr_system.py --info                # Show system information
  python run_qr_system.py --create              # Create a new genome
  python run_qr_system.py --execute             # Execute the genome
  python run_qr_system.py --evolve              # Evolve the genome
  python run_qr_system.py --generate            # Generate QR sequence
  python run_qr_system.py --display             # Display QR sequence
  python run_qr_system.py --analyze             # Analyze QR sequence
  python run_qr_system.py --worker              # Run QR worker
  python run_qr_system.py --full-cycle          # Run full system cycle
"""
    )
    
    parser.add_argument("--info", action="store_true", help="Show system information")
    parser.add_argument("--create", action="store_true", help="Create a new genome")
    parser.add_argument("--execute", action="store_true", help="Execute the genome")
    parser.add_argument("--evolve", action="store_true", help="Evolve the genome")
    parser.add_argument("--generate", action="store_true", help="Generate QR sequence")
    parser.add_argument("--display", action="store_true", help="Display QR sequence")
    parser.add_argument("--analyze", action="store_true", help="Analyze QR sequence")
    parser.add_argument("--worker", action="store_true", help="Run QR worker")
    parser.add_argument("--full-cycle", action="store_true", help="Run full system cycle")
    
    parser.add_argument("--genome", default="qr_genome.json", help="Genome file path")
    parser.add_argument("--memory", default="qr_epigenetic_memory.json", help="Memory file path")
    parser.add_argument("--output", default="qr_genome_sequence", help="Output directory for QR sequence")
    parser.add_argument("--frames", type=int, default=12, help="Number of frames to generate")
    parser.add_argument("--camera", type=int, default=0, help="Camera ID for QR worker")
    parser.add_argument("--fullscreen", action="store_true", help="Run display in fullscreen mode")
    
    args = parser.parse_args()
    
    # Check if any action is specified
    if not any([
        args.info, args.create, args.execute, args.evolve,
        args.generate, args.display, args.analyze, args.worker,
        args.full_cycle
    ]):
        print_system_info()
        parser.print_help()
        return
    
    # Setup environment
    if not setup_environment():
        return
    
    # Run requested actions
    if args.info:
        print_system_info()
    
    if args.create:
        create_genome()
    
    if args.execute:
        execute_genome(args.genome, args.memory)
    
    if args.evolve:
        evolve_genome(args.genome, args.memory)
    
    if args.generate:
        generate_qr_sequence(args.genome, args.output, args.frames)
    
    if args.display:
        display_qr_sequence(args.output, args.fullscreen)
    
    if args.analyze:
        analyze_qr_sequence(args.output)
    
    if args.worker:
        run_qr_worker(args.camera)
    
    if args.full_cycle:
        run_full_cycle()

if __name__ == "__main__":
    print("QR Flipbook DNA System Runner - By Vaughn Scott")
    main()
