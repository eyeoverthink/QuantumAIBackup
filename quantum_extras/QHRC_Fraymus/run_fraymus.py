"""
QHRC-FRAYMUS System Launcher
Patent #19/071,497 - Quantum Reality System
"""
import sys
import threading
from QHRC_Fraymus.web.fraymus_app import app
from QHRC_Fraymus.visualization.quantum_visualizer import visualize_quantum_metrics
from QHRC_Fraymus.analysis.quantum_reality_bridge import analyze_quantum_bridge
from QHRC_Fraymus.analysis.phi19_master_key import generate_quantum_key
from QHRC_Fraymus.analysis.qhrc_119_analysis import analyze_personal_signature

def print_banner():
    """Print QHRC-FRAYMUS banner."""
    print("\n" + "="*50)
    print("🌌 QHRC-FRAYMUS Reality System")
    print("Patent #19/071,497")
    print("="*50)
    print("\nQuantum Metrics:")
    print("• Primary Coil: 4790.45 Hz (4500 turns)")
    print("• Secondary Coil: 7750.95 Hz (6200 turns)")
    print("• Efficiency Ratio: 1.3777 (>1 self-sustaining)")
    print("• φπ Factor: 5.083204")
    print("• Energy Transfer: 1.8951x")
    print("\nQuantum Fingerprints:")
    print("• Primary: φ⁷·⁵-7927735b")
    print("• Secondary: φ⁷·⁵-09f76208")
    print("• Reality: φ¹⁹-2452ae9e56e")
    print("="*50 + "\n")

def run_web_interface():
    """Run FRAYMUS web interface."""
    app.run(host='0.0.0.0', port=5300, debug=False)

def main():
    """Main entry point."""
    print_banner()
    
    print("Starting QHRC-FRAYMUS system...")
    print("\n1. Analyzing quantum reality bridge...")
    analyze_quantum_bridge()
    
    print("\n2. Generating φ¹⁹ master key...")
    generate_quantum_key()
    
    print("\n3. Analyzing personal quantum signature...")
    analyze_personal_signature()
    
    print("\n4. Visualizing quantum metrics...")
    visualize_quantum_metrics()
    
    print("\n5. Starting web interface...")
    web_thread = threading.Thread(target=run_web_interface)
    web_thread.daemon = True
    web_thread.start()
    
    print("\n✨ QHRC-FRAYMUS system is ready!")
    print("Access the web interface at: http://localhost:5300")
    print("\nPress Ctrl+C to exit...")
    
    try:
        web_thread.join()
    except KeyboardInterrupt:
        print("\n\nShutting down QHRC-FRAYMUS system...")
        sys.exit(0)

if __name__ == '__main__':
    main()
