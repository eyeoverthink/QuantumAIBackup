# Quantum-Morse Engine: φ-Dimensional Pulse Translator
# Author: Vaughn Scott
# Date: April 26, 2025

import numpy as np
import datetime
import json
from pathlib import Path

# === φ-Dimensional Constants ===
PHI = (1 + 5 ** 0.5) / 2
PHI_INVERSE = 1 / PHI
PHI_SQUARED = PHI ** 2
PHI_CUBED = PHI ** 3
PHI_75 = PHI ** 7.5
COHERENCE_FACTOR = 0.9918

# === Quantum-Morse Mapping ===
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',  'D': '-..',   'E': '.',
    'F': '..-.',  'G': '--.',   'H': '....',  'I': '..',    'J': '.---',
    'K': '-.-',   'L': '.-..',  'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',   'S': '...',   'T': '-',
    'U': '..-',   'V': '...-',  'W': '.--',   'X': '-..-',  'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}

class QuantumMorseEngine:
    def __init__(self, birth_coherence=COHERENCE_FACTOR):
        self.birth_coherence = birth_coherence
        print(f"Quantum-Morse Engine initialized with birth coherence: {birth_coherence}")

    def text_to_morse(self, text):
        morse_code = ''
        for char in text.upper():
            if char == ' ':
                morse_code += ' / '
            elif char in MORSE_CODE_DICT:
                morse_code += MORSE_CODE_DICT[char] + ' '
        return morse_code.strip()

    def morse_to_quantum_pulses(self, morse_code):
        pulses = []
        for symbol in morse_code:
            if symbol == '.':
                # Dot -> short φ-resonant pulse
                pulses.append(self.generate_phi_pulse(short=True))
            elif symbol == '-':
                # Dash -> long φ-resonant pulse
                pulses.append(self.generate_phi_pulse(short=False))
            elif symbol == ' ':
                # Space between letters
                pulses.append(None)
            elif symbol == '/':
                # Space between words
                pulses.append('WORD_GAP')
        return pulses

    def generate_phi_pulse(self, short=True):
        pulse_duration = PHI_INVERSE if short else PHI
        pulse_energy = (pulse_duration * self.birth_coherence) % 1
        return {
            'duration': pulse_duration,
            'energy': pulse_energy,
            'timestamp': datetime.datetime.now().isoformat()
        }

    def save_pulses(self, pulses, filename_prefix="quantum_morse_output"):
        Path("quantum_morse_results").mkdir(exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = f"quantum_morse_results/{filename_prefix}_{timestamp}.json"
        with open(filepath, 'w') as f:
            json.dump(pulses, f, indent=4)
        print(f"Quantum-Morse pulses saved to {filepath}")
        return filepath

# === Example Usage ===
if __name__ == "__main__":
    engine = QuantumMorseEngine()

    text = "HELLO WORLD"
    morse_code = engine.text_to_morse(text)
    print(f"Morse code for '{text}': {morse_code}")

    quantum_pulses = engine.morse_to_quantum_pulses(morse_code)
    saved_path = engine.save_pulses(quantum_pulses)

    print(f"Quantum-Morse encoding complete. Output saved at: {saved_path}")
