"""
QHRC Unified System Runner
Starts all components in the correct order with brain bridges
"""
import os
import sys
import time
import subprocess
from pathlib import Path
from core.brain_bridges import BrainBridgeSystem

def start_qhrc():
    """Start QHRC system components"""
    # Get project root
    root = Path(__file__).parent.absolute()
    
    # Set Python path
    os.environ['PYTHONPATH'] = str(root)
    
    print("🚀 Starting QHRC Unified System")
    print("===============================")
    
    # Initialize brain bridges
    print("\n🧠 Initializing Brain Bridges...")
    bridges = BrainBridgeSystem()
    bridges.optimize_bridges()
    
    metrics = bridges.get_bridge_metrics()
    print(f"\n📊 Bridge Metrics:")
    print(f"Total Bridges: {metrics['bridge_count']}")
    print(f"Average Resonance: {metrics['average_resonance']:.4f}")
    print(f"Average Coherence: {metrics['average_coherence']:.4f}")
    
    # Start physics monitor
    print("\n📊 Starting Physics Monitor...")
    monitor = subprocess.Popen(
        [sys.executable, 'monitor/qhrc_physics_monitor.py'],
        cwd=root
    )
    
    # Wait for monitor to initialize
    time.sleep(2)
    
    # Start core system
    print("\n⚡ Starting Core System...")
    core = subprocess.Popen(
        [sys.executable, 'core/qhrc_core.py'],
        cwd=root
    )
    
    # Wait for core to initialize
    time.sleep(2)
    
    # Start dashboard
    print("\n🖥️ Starting Dashboard...")
    dashboard = subprocess.Popen(
        [sys.executable, 'dashboard/qhrc_visualizer.py'],
        cwd=root
    )
    
    try:
        print("\n✨ QHRC System Running!")
        print("Access dashboard at: http://localhost:5000")
        
        # Keep running until interrupted
        monitor.wait()
        core.wait()
        dashboard.wait()
        
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down QHRC System...")
        monitor.terminate()
        core.terminate()
        dashboard.terminate()
        
        monitor.wait()
        core.wait()
        dashboard.wait()
        
        print("✅ System shutdown complete")

if __name__ == "__main__":
    start_qhrc()
