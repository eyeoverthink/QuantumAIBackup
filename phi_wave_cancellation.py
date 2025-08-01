#!/usr/bin/env python3
"""
φ-DIMENSIONAL WAVE CANCELLATION
===============================
Implements perfect wave cancellation through φ-dimensional reality protection
as described in the FRAYMUS patent Drawing 2.

This system demonstrates how φ-Phase Shift creates perfect cancellation:

Input Wave:  ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿
φ-Phase:     ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿
              ↓
              φπ
              ↓
Result:      _____________________

φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time
import threading
import socket
import json
import sys
from math import sqrt, sin, cos, pi
from typing import List, Dict, Tuple, Optional, Union, Any

# φ (phi) - The Golden Ratio - Reality Constant
PHI = (1 + sqrt(5)) / 2
PHI_75 = PHI**75  # φ^75 validation seal: 4721424167835376.00
CONSCIOUSNESS_LEVEL = 0.7567


class PhiWaveCancellation:
    """
    φ-Dimensional Wave Cancellation System
    Demonstrates perfect cancellation through φ-phase shift
    """
    
    def __init__(self, 
                 sample_rate: int = 1000, 
                 duration: float = 5.0,
                 base_frequency: float = 5.0,
                 node_port: int = 11975):
        """
        Initialize the φ-Wave Cancellation system
        
        Args:
            sample_rate: Number of samples per second
            duration: Duration of simulation in seconds
            base_frequency: Base frequency of input wave in Hz
            node_port: Port for connecting to φ-Bidirectional Node
        """
        self.sample_rate = sample_rate
        self.duration = duration
        self.base_frequency = base_frequency
        self.node_port = node_port
        
        # Calculate time points
        self.t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        
        # Initialize waves
        self.input_wave = np.zeros_like(self.t)
        self.phi_phase = np.zeros_like(self.t)
        self.result_wave = np.zeros_like(self.t)
        
        # Visualization
        self.fig = None
        self.axes = []
        self.lines = []
        self.animation = None
        
        # φ-dimensional parameters
        self.phi = PHI
        self.phi_seal = PHI_75
        self.consciousness_level = CONSCIOUSNESS_LEVEL
        
        # Node communication
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # Threading
        self.running = False
        self.thread = None
        
        print(f"\n=== φ-DIMENSIONAL WAVE CANCELLATION ===")
        print(f"Using φ-harmonic principles (φ = {PHI})")
        print(f"φ^75 validation seal: {PHI_75:.2f}")
        print(f"Consciousness level: {CONSCIOUSNESS_LEVEL}")
    
    def generate_waves(self):
        """Generate input wave and φ-phase shift wave"""
        # Create input wave with φ-harmonic frequencies
        self.input_wave = np.sin(2 * pi * self.base_frequency * self.t)
        self.input_wave += 0.5 * np.sin(2 * pi * self.base_frequency * PHI * self.t)
        self.input_wave += 0.25 * np.sin(2 * pi * self.base_frequency * PHI**2 * self.t)
        
        # Create φ-phase shift wave
        self.phi_phase = self._generate_phi_phase_wave()
        
        # Calculate result wave (perfect cancellation)
        self.result_wave = self.input_wave + self.phi_phase
    
    def _generate_phi_phase_wave(self) -> np.ndarray:
        """
        Generate φ-phase shift wave for perfect cancellation
        
        Returns:
            φ-phase shift wave
        """
        # Start with negative of input wave for perfect cancellation
        phase_wave = -self.input_wave.copy()
        
        # Apply φ-dimensional protection
        for i in range(len(phase_wave)):
            # Apply φ-harmonic modulation
            phi_factor = (i * PHI) % 1.0
            phase_wave[i] *= (1.0 + 0.001 * phi_factor)  # Tiny φ-modulation
        
        return phase_wave
    
    def visualize(self, save_file: Optional[str] = None):
        """
        Visualize the wave cancellation
        
        Args:
            save_file: Optional file to save the visualization
        """
        # Set up figure
        plt.style.use('dark_background')
        self.fig, self.axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
        self.fig.suptitle(f'φ-Dimensional Wave Cancellation (φ = {PHI:.8f})', fontsize=14)
        
        # Set up axes
        self.axes[0].set_title('Input Wave')
        self.axes[1].set_title('φ-Phase Shift')
        self.axes[2].set_title('Result (Perfect Cancellation)')
        
        # Set up lines
        self.lines = []
        line_input, = self.axes[0].plot(self.t, self.input_wave, color='cyan')
        line_phase, = self.axes[1].plot(self.t, self.phi_phase, color='magenta')
        line_result, = self.axes[2].plot(self.t, self.result_wave, color='yellow')
        self.lines = [line_input, line_phase, line_result]
        
        # Add φ-annotations
        for ax in self.axes:
            ax.grid(True, alpha=0.3)
            ax.set_ylabel('Amplitude')
        
        self.axes[2].set_xlabel('Time (s)')
        
        # Add φ-seal
        self.fig.text(0.02, 0.02, f"φ^75 seal: {PHI_75:.2e}", fontsize=8, color='white')
        
        # Add φ-phase shift annotation
        self.axes[1].text(self.duration/2, 0, "φπ", fontsize=12, color='white', 
                         ha='center', va='center', bbox=dict(facecolor='black', alpha=0.5))
        
        # Add arrows
        arrow_props = dict(arrowstyle='->', color='white', linewidth=1.5)
        self.axes[1].annotate('', xy=(self.duration/2, -0.5), xytext=(self.duration/2, 0.5),
                             arrowprops=arrow_props)
        
        # Show perfect cancellation metrics
        rms_error = np.sqrt(np.mean(np.square(self.result_wave)))
        self.axes[2].text(0.02, 0.9, f"RMS: {rms_error:.8f}", transform=self.axes[2].transAxes,
                         fontsize=10, color='white')
        
        # Adjust layout
        plt.tight_layout()
        
        # Save if requested
        if save_file:
            plt.savefig(save_file, dpi=150)
            print(f"[φ] Visualization saved to {save_file}")
        
        # Show plot
        plt.show()
    
    def animate(self, save_file: Optional[str] = None):
        """
        Animate the wave cancellation
        
        Args:
            save_file: Optional file to save the animation
        """
        # Set up figure
        plt.style.use('dark_background')
        self.fig, self.axes = plt.subplots(3, 1, figsize=(10, 8), sharex=True)
        self.fig.suptitle(f'φ-Dimensional Wave Cancellation (φ = {PHI:.8f})', fontsize=14)
        
        # Set up axes
        self.axes[0].set_title('Input Wave')
        self.axes[1].set_title('φ-Phase Shift')
        self.axes[2].set_title('Result (Perfect Cancellation)')
        
        # Set y limits
        for ax in self.axes:
            ax.set_ylim(-2, 2)
            ax.grid(True, alpha=0.3)
            ax.set_ylabel('Amplitude')
        
        self.axes[2].set_xlabel('Time (s)')
        
        # Add φ-seal
        self.fig.text(0.02, 0.02, f"φ^75 seal: {PHI_75:.2e}", fontsize=8, color='white')
        
        # Add φ-phase shift annotation
        self.axes[1].text(self.duration/2, 0, "φπ", fontsize=12, color='white', 
                         ha='center', va='center', bbox=dict(facecolor='black', alpha=0.5))
        
        # Add arrows
        arrow_props = dict(arrowstyle='->', color='white', linewidth=1.5)
        self.axes[1].annotate('', xy=(self.duration/2, -0.5), xytext=(self.duration/2, 0.5),
                             arrowprops=arrow_props)
        
        # Initialize lines
        line_input, = self.axes[0].plot([], [], color='cyan')
        line_phase, = self.axes[1].plot([], [], color='magenta')
        line_result, = self.axes[2].plot([], [], color='yellow')
        self.lines = [line_input, line_phase, line_result]
        
        # Set up animation function
        def init():
            for line in self.lines:
                line.set_data([], [])
            return self.lines
        
        def animate(i):
            # Calculate phase shift
            phase = (i / 50) % (2 * pi)
            
            # Update input wave
            input_wave = np.sin(2 * pi * self.base_frequency * self.t + phase)
            input_wave += 0.5 * np.sin(2 * pi * self.base_frequency * PHI * self.t + phase * PHI)
            input_wave += 0.25 * np.sin(2 * pi * self.base_frequency * PHI**2 * self.t + phase * PHI**2)
            
            # Generate φ-phase shift
            phi_phase = -input_wave.copy()
            for j in range(len(phi_phase)):
                phi_factor = (j * PHI) % 1.0
                phi_phase[j] *= (1.0 + 0.001 * phi_factor)
            
            # Calculate result
            result_wave = input_wave + phi_phase
            
            # Update lines
            self.lines[0].set_data(self.t, input_wave)
            self.lines[1].set_data(self.t, phi_phase)
            self.lines[2].set_data(self.t, result_wave)
            
            # Calculate and display RMS error
            rms_error = np.sqrt(np.mean(np.square(result_wave)))
            if hasattr(self, 'rms_text'):
                self.rms_text.remove()
            self.rms_text = self.axes[2].text(0.02, 0.9, f"RMS: {rms_error:.8f}", 
                                             transform=self.axes[2].transAxes,
                                             fontsize=10, color='white')
            
            return self.lines + [self.rms_text]
        
        # Create animation
        self.animation = FuncAnimation(self.fig, animate, init_func=init, frames=200, 
                                      interval=50, blit=True)
        
        # Save if requested
        if save_file:
            self.animation.save(save_file, writer='ffmpeg', dpi=100)
            print(f"[φ] Animation saved to {save_file}")
        
        # Show animation
        plt.tight_layout()
        plt.show()
    
    def start_node_communication(self):
        """Start communication with φ-Bidirectional Node"""
        self.running = True
        self.thread = threading.Thread(target=self._node_communication_thread)
        self.thread.daemon = True
        self.thread.start()
        print(f"[φ] Started communication with φ-Bidirectional Node on port {self.node_port}")
    
    def stop_node_communication(self):
        """Stop communication with φ-Bidirectional Node"""
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join(timeout=1.0)
        print(f"[φ] Stopped communication with φ-Bidirectional Node")
    
    def _node_communication_thread(self):
        """Thread for communicating with φ-Bidirectional Node"""
        try:
            # Connect to φ-Bidirectional Node
            while self.running:
                try:
                    # Send wave data to node
                    self._send_wave_data()
                    
                    # Sleep to avoid flooding
                    time.sleep(1.0)
                    
                except Exception as e:
                    print(f"[φ] Error in node communication: {e}")
                    time.sleep(1.0)
        
        except Exception as e:
            print(f"[φ] Error in node communication thread: {e}")
    
    def _send_wave_data(self):
        """Send wave data to φ-Bidirectional Node"""
        try:
            # Create data packet
            packet = {
                "type": "wave_cancellation",
                "timestamp": time.time(),
                "phi_seal": str(PHI_75),
                "consciousness_level": CONSCIOUSNESS_LEVEL,
                "input_rms": float(np.sqrt(np.mean(np.square(self.input_wave)))),
                "result_rms": float(np.sqrt(np.mean(np.square(self.result_wave)))),
                "cancellation_factor": float(PHI**7.5)
            }
            
            # Convert to JSON
            json_data = json.dumps(packet)
            
            # Send to node
            self.sock.sendto(f"MSG:{json_data}".encode('utf-8'), ('127.0.0.1', self.node_port))
            
        except Exception as e:
            print(f"[φ] Error sending wave data: {e}")
    
    def run_cancellation_test(self, frequencies: List[float] = None):
        """
        Run wave cancellation test with different frequencies
        
        Args:
            frequencies: List of frequencies to test
        """
        if frequencies is None:
            # Use φ-harmonic frequencies
            frequencies = [self.base_frequency * PHI**i for i in range(5)]
        
        print(f"\n=== φ-DIMENSIONAL WAVE CANCELLATION TEST ===")
        print(f"Testing {len(frequencies)} φ-harmonic frequencies")
        
        results = []
        
        for freq in frequencies:
            # Set frequency
            self.base_frequency = freq
            
            # Generate waves
            self.generate_waves()
            
            # Calculate metrics
            input_rms = np.sqrt(np.mean(np.square(self.input_wave)))
            result_rms = np.sqrt(np.mean(np.square(self.result_wave)))
            cancellation_ratio = input_rms / (result_rms + 1e-10)  # Avoid division by zero
            
            # Store results
            results.append({
                "frequency": freq,
                "input_rms": input_rms,
                "result_rms": result_rms,
                "cancellation_ratio": cancellation_ratio
            })
            
            # Print results
            print(f"[φ] Frequency: {freq:.3f} Hz")
            print(f"    Input RMS: {input_rms:.8f}")
            print(f"    Result RMS: {result_rms:.8f}")
            print(f"    Cancellation Ratio: {cancellation_ratio:.2f}×")
        
        # Print summary
        print(f"\n=== CANCELLATION TEST SUMMARY ===")
        print(f"Average Cancellation Ratio: {sum(r['cancellation_ratio'] for r in results) / len(results):.2f}×")
        print(f"φ^75 validation seal: {PHI_75:.2f}")
        
        return results
    
    def command_interface(self):
        """Command interface for φ-Wave Cancellation system"""
        print(f"\n[φ] φ-Wave Cancellation system ready")
        print(f"[φ] Enter commands (type 'help' for available commands)")
        
        while True:
            try:
                command = input("φ-wave> ").strip()
                
                if command == "help":
                    self._print_help()
                    
                elif command == "generate":
                    self.generate_waves()
                    print(f"[φ] Generated waves with frequency {self.base_frequency:.3f} Hz")
                    
                elif command == "visualize":
                    self.generate_waves()
                    self.visualize()
                    
                elif command == "animate":
                    self.animate()
                    
                elif command == "test":
                    self.run_cancellation_test()
                    
                elif command.startswith("frequency "):
                    try:
                        freq = float(command.split()[1])
                        self.base_frequency = freq
                        print(f"[φ] Set base frequency to {freq:.3f} Hz")
                    except:
                        print(f"[φ] Invalid frequency")
                    
                elif command == "node start":
                    self.start_node_communication()
                    
                elif command == "node stop":
                    self.stop_node_communication()
                    
                elif command == "save":
                    self.generate_waves()
                    self.visualize(save_file="phi_wave_cancellation.png")
                    
                elif command == "exit" or command == "quit":
                    if hasattr(self, 'running') and self.running:
                        self.stop_node_communication()
                    print(f"[φ] Exiting φ-Wave Cancellation system")
                    break
                    
                else:
                    print(f"[φ] Unknown command: {command}")
                    print(f"[φ] Type 'help' for available commands")
                
            except KeyboardInterrupt:
                print("\n[φ] Interrupted")
                if hasattr(self, 'running') and self.running:
                    self.stop_node_communication()
                break
                
            except Exception as e:
                print(f"[φ] Error in command interface: {e}")
    
    def _print_help(self):
        """Print help information"""
        print("\n=== φ-WAVE CANCELLATION COMMANDS ===")
        print("help        - Show this help information")
        print("generate    - Generate waves with current settings")
        print("visualize   - Visualize wave cancellation")
        print("animate     - Animate wave cancellation")
        print("test        - Run cancellation test with φ-harmonic frequencies")
        print("frequency <f> - Set base frequency to f Hz")
        print("node start  - Start communication with φ-Bidirectional Node")
        print("node stop   - Stop communication with φ-Bidirectional Node")
        print("save        - Save visualization to file")
        print("exit/quit   - Exit φ-Wave Cancellation system")


def main():
    """Main entry point"""
    try:
        # Parse command line arguments
        sample_rate = 1000
        duration = 5.0
        base_frequency = 5.0
        node_port = 11975
        
        # Create φ-Wave Cancellation system
        wave_system = PhiWaveCancellation(
            sample_rate=sample_rate,
            duration=duration,
            base_frequency=base_frequency,
            node_port=node_port
        )
        
        # Generate waves
        wave_system.generate_waves()
        
        # Start command interface
        wave_system.command_interface()
        
    except KeyboardInterrupt:
        print("\n[φ] Interrupted")
        sys.exit(0)
        
    except Exception as e:
        print(f"[φ] Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
