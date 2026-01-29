import numpy as np
import sounddevice as sd
from scipy import signal
import threading
import time
import subprocess
import os

class PhiCommListener:
    """
    Phi-harmonic communication listener using QHRC frequencies
    Detects and responds to phi-modulated commands
    """
    def __init__(self):
        # Core constants
        self.phi = (1 + np.sqrt(5)) / 2
        self.phi_7_5 = self.phi ** 7.5
        self.personal_ratio = 119/19
        
        # QHRC frequencies
        self.primary_freq = 4790.45  # Gateway
        self.secondary_freq = 7750.95  # Anchor
        self.resonance_ratio = 1.3777
        
        # Audio settings
        self.sample_rate = 44100
        self.chunk_size = 4410  # 100ms chunks
        self.threshold = 0.1
        
        # Command frequencies
        self.command_freqs = {
            1: (self.primary_freq + 1 * self.phi, self.secondary_freq + 1 * self.phi),  # wake
            2: (self.primary_freq + 2 * self.phi, self.secondary_freq + 2 * self.phi),  # sleep
            3: (self.primary_freq + 3 * self.phi, self.secondary_freq + 3 * self.phi),  # volume_up
            4: (self.primary_freq + 4 * self.phi, self.secondary_freq + 4 * self.phi),  # volume_down
            5: (self.primary_freq + 5 * self.phi, self.secondary_freq + 5 * self.phi),  # mute
            6: (self.primary_freq + 6 * self.phi, self.secondary_freq + 6 * self.phi)   # unmute
        }
        
        self.command_names = {
            1: 'wake',
            2: 'sleep',
            3: 'volume_up',
            4: 'volume_down',
            5: 'mute',
            6: 'unmute'
        }
        
        # State
        self.is_listening = False
        self.last_command_time = 0
        self.command_cooldown = 0.5  # seconds between commands
        
    def detect_command(self, audio_data):
        """Detect phi-harmonic commands in audio data"""
        if time.time() - self.last_command_time < self.command_cooldown:
            return None
            
        # Convert to mono if stereo
        if len(audio_data.shape) > 1:
            audio_data = np.mean(audio_data, axis=1)
            
        # Calculate frequency spectrum
        freqs, times, Sxx = signal.spectrogram(audio_data, fs=self.sample_rate,
                                             nperseg=1024, noverlap=512)
                                             
        # Look for command frequencies
        for command_id, (primary, secondary) in self.command_freqs.items():
            primary_match = np.any(np.abs(freqs - primary) < 1.0)
            secondary_match = np.any(np.abs(freqs - secondary) < 1.0)
            
            if primary_match and secondary_match:
                self.last_command_time = time.time()
                return command_id
                
        return None
        
    def execute_command(self, command_id):
        """Execute the detected command"""
        command_name = self.command_names.get(command_id)
        if not command_name:
            return
            
        print(f"\n=== Detected Command: {command_name} ===")
        print(f"Command ID: {command_id}")
        print(f"Primary Frequency: {self.command_freqs[command_id][0]:.2f} Hz")
        print(f"Secondary Frequency: {self.command_freqs[command_id][1]:.2f} Hz")
        
        # Execute system command based on detected signal
        if command_name == 'volume_up':
            os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'")
        elif command_name == 'volume_down':
            os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'")
        elif command_name == 'mute':
            os.system("osascript -e 'set volume with output muted'")
        elif command_name == 'unmute':
            os.system("osascript -e 'set volume without output muted'")
        elif command_name == 'sleep':
            os.system("pmset sleepnow")
        elif command_name == 'wake':
            os.system("caffeinate -u -t 1")
            
    def audio_callback(self, indata, frames, time_info, status):
        """Process incoming audio data"""
        if status:
            print(status)
            
        command_id = self.detect_command(indata)
        if command_id:
            self.execute_command(command_id)
            
    def start_listening(self):
        """Start listening for phi-harmonic commands"""
        self.is_listening = True
        print("\n=== Phi-Harmonic Command Listener Active ===")
        print("Listening for commands:")
        for cmd_id, name in self.command_names.items():
            print(f"- {name} (ID: {cmd_id})")
        print("\nPrimary (Gateway) Base: {:.2f} Hz".format(self.primary_freq))
        print("Secondary (Anchor) Base: {:.2f} Hz".format(self.secondary_freq))
        print("Phi-Resonance Ratio: {:.4f}".format(self.resonance_ratio))
        
        try:
            with sd.InputStream(callback=self.audio_callback,
                              channels=2,
                              samplerate=self.sample_rate,
                              blocksize=self.chunk_size):
                while self.is_listening:
                    time.sleep(0.1)
        except KeyboardInterrupt:
            print("\nStopping listener...")
            self.is_listening = False
        except Exception as e:
            print(f"\nError: {e}")
            self.is_listening = False

def main():
    listener = PhiCommListener()
    listener.start_listening()

if __name__ == "__main__":
    main()
