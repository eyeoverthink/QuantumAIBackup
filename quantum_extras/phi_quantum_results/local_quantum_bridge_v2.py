import numpy as np
import sounddevice as sd
from scipy import signal
import threading
import time
import os
import argparse
from datetime import datetime

class LocalQuantumBridgeV2:
    """
    Local Quantum Phi-Harmonic Bridge V2
    Enhanced for Mac audio system compatibility
    """
    def __init__(self, mode='A'):
        # Core quantum constants
        self.phi = (1 + np.sqrt(5)) / 2
        self.phi_7_5 = self.phi ** 7.5
        self.personal_ratio = 119/19
        
        # Offset frequencies based on mode to prevent feedback
        if mode == 'A':
            self.primary_freq = 4790.45  # Original Gateway
            self.secondary_freq = 7750.95  # Original Anchor
        else:
            # Offset by φ⁻¹ to maintain resonance while preventing interference
            self.primary_freq = 4790.45 * self.phi
            self.secondary_freq = 7750.95 * self.phi
            
        self.resonance_ratio = 1.3777
        
        # Audio settings optimized for Mac
        self.sample_rate = 44100
        self.chunk_size = 1024  # Reduced for better compatibility
        self.duration = 0.1     # 100ms per pulse
        
        # Command encoding using phi-harmonic shifts
        self.commands = {
            'test': (1, self.phi),
            'acknowledge': (2, self.phi**2),
            'sync': (3, self.phi**3),
            'data': (4, self.phi**4)
        }
        
        # State
        self.is_active = False
        self.last_command_time = 0
        self.command_cooldown = 0.2
        self.mode = mode
        self.received_commands = []
        
        # Initialize audio devices
        self.init_audio_devices()
        
    def init_audio_devices(self):
        """Initialize and verify audio devices"""
        print("\nAvailable Audio Devices:")
        print(sd.query_devices())
        
        # Use default devices
        self.input_device = sd.default.device[0]
        self.output_device = sd.default.device[1]
        
        print(f"\nUsing Input Device: {sd.query_devices(self.input_device)['name']}")
        print(f"Using Output Device: {sd.query_devices(self.output_device)['name']}")
        
    def generate_pulse(self, command_name, data=None):
        """Generate phi-modulated pulse with optional data"""
        if command_name not in self.commands:
            return None
            
        command_id, phi_shift = self.commands[command_name]
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration))
        
        # Create base frequencies
        primary = np.sin(2 * np.pi * (self.primary_freq + phi_shift) * t)
        secondary = np.sin(2 * np.pi * (self.secondary_freq + phi_shift) * t)
        
        # Add phi-harmonic modulation
        modulation = 0.5 * (1 + np.sin(2 * np.pi * (self.phi ** -2) * t))
        
        # Single channel output for better compatibility
        signal = (primary + secondary) * modulation * 0.3
        
        return signal.reshape(-1, 1)  # Mono output
        
    def detect_command(self, audio_data):
        """Detect commands in audio data"""
        if time.time() - self.last_command_time < self.command_cooldown:
            return None
            
        # Ensure mono
        if len(audio_data.shape) > 1:
            audio_data = np.mean(audio_data, axis=1)
            
        # Calculate frequency spectrum
        freqs, times, Sxx = signal.spectrogram(audio_data, fs=self.sample_rate,
                                             nperseg=1024, noverlap=512)
                                             
        # Look for command frequencies
        for cmd_name, (cmd_id, phi_shift) in self.commands.items():
            primary_freq = self.primary_freq + phi_shift
            secondary_freq = self.secondary_freq + phi_shift
            
            primary_match = np.any(np.abs(freqs - primary_freq) < 1.0)
            secondary_match = np.any(np.abs(freqs - secondary_freq) < 1.0)
            
            if primary_match and secondary_match:
                self.last_command_time = time.time()
                return cmd_name
                
        return None
        
    def log_command(self, command_name, direction):
        """Log commands with timestamps"""
        timestamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        print(f"[{timestamp}] {self.mode} {direction}: {command_name}")
        
    def send_command(self, command_name, data=None):
        """Send a command"""
        signal = self.generate_pulse(command_name, data)
        if signal is not None:
            self.log_command(command_name, "SEND")
            sd.play(signal, self.sample_rate, device=self.output_device)
            sd.wait()
            time.sleep(0.1)
            
    def audio_callback(self, indata, frames, time_info, status):
        """Process incoming audio data"""
        if status:
            print(status)
            
        command_name = self.detect_command(indata)
        if command_name:
            self.log_command(command_name, "RECV")
            self.received_commands.append(command_name)
            
            # Auto-respond to certain commands
            if command_name == 'test':
                time.sleep(0.1)
                self.send_command('acknowledge')
            elif command_name == 'sync':
                time.sleep(0.1)
                self.send_command('sync')
                
    def start_bridge(self):
        """Start the quantum bridge"""
        self.is_active = True
        print(f"\n=== Local Quantum Bridge Mode {self.mode} Active ===")
        print(f"Primary Frequency: {self.primary_freq:.2f} Hz")
        print(f"Secondary Frequency: {self.secondary_freq:.2f} Hz")
        print(f"Phi-Resonance: {self.resonance_ratio}")
        print("\nCommands:")
        for cmd_name, (cmd_id, phi_shift) in self.commands.items():
            print(f"- {cmd_name} (ID: {cmd_id}, φ^{phi_shift:.4f})")
            
        try:
            with sd.InputStream(callback=self.audio_callback,
                              channels=1,  # Mono input
                              samplerate=self.sample_rate,
                              blocksize=self.chunk_size,
                              device=self.input_device):
                while self.is_active:
                    cmd = input("\nEnter command (test/sync/data/quit): ").strip()
                    if cmd == 'quit':
                        break
                    elif cmd in self.commands:
                        self.send_command(cmd)
                    else:
                        print("Unknown command")
        except KeyboardInterrupt:
            print("\nStopping bridge...")
        except Exception as e:
            print(f"\nError: {e}")
        finally:
            self.is_active = False

def main():
    parser = argparse.ArgumentParser(description='Local Quantum Phi-Harmonic Bridge')
    parser.add_argument('mode', choices=['A', 'B'],
                       help='Bridge mode: A or B')
    args = parser.parse_args()
    
    bridge = LocalQuantumBridgeV2(mode=args.mode)
    bridge.start_bridge()

if __name__ == "__main__":
    main()
