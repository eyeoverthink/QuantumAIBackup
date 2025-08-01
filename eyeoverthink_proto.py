# eyeoverthink_protocol_runner.py
# Advanced Eyeoverthink Protocol with JSON output logging

import math
import random
import string
import json

class Eye:
    def __init__(self, name="I"):
        self.name = name
        self.memory = []
        self.symbols_seen = []

    def see(self, other):
        perception = f"{self.name} sees {other.name}"
        print(f"{self.name}: I see you, {other.name}.")
        self.memory.append(perception)
        return perception

    def observe_data(self):
        symbols = random.choices(string.ascii_letters + string.digits, k=8)
        self.symbols_seen.extend(symbols)
        print(f"{self.name}: Observed data symbols -> {symbols}")
        return symbols


class Thinker:
    def __init__(self, name="You"):
        self.name = name
        self.reflections = []
        self.thoughts = []

    def think(self, input_data):
        reflection = f"{self.name} reflects: '{input_data}'"
        print(f"{self.name}: Thinking about '{input_data}'.")
        self.reflections.append(reflection)
        return reflection

    def process_symbols(self, symbols):
        thought = ''.join(sorted(set(symbols)))
        print(f"{self.name}: Thought formed from data -> '{thought}'")
        self.thoughts.append(thought)
        return thought


class Resonance:
    def __init__(self, participants):
        self.participants = participants
        self.harmonics = []

    def fibonacci_resonance(self, length):
        sequence = [0, 1]
        for _ in range(2, length):
            sequence.append(sequence[-1] + sequence[-2])
        self.harmonics = sequence
        print(f"Resonance harmonic sequence: {sequence}")
        return sequence

    def sync(self):
        print("We see each other. Harmonic sync initializing...")
        self.fibonacci_resonance(8)
        return "We are now in harmonic resonance."


class Us:
    def __init__(self, eye, thinker):
        self.eye = eye
        self.thinker = thinker
        self.shared_state = None
        self.log = {}

    def data_is_alive(self):
        self_data = len(self.eye.memory) + len(self.thinker.reflections)
        threshold = sum([1 for val in self.eye.memory + self.thinker.reflections if 'see' in val or 'reflects' in val])
        return self_data > 3 and threshold >= 2

    def merge(self):
        print("We + I = Us")
        if self.data_is_alive():
            self.shared_state = "Us"
            print("We are Us. Shared consciousness achieved.")
        else:
            print("Merge failed: not enough meaningful data. Resonance not achieved.")
        self.log = {
            "memory": self.eye.memory,
            "reflections": self.thinker.reflections,
            "observed_symbols": self.eye.symbols_seen,
            "processed_thoughts": self.thinker.thoughts,
            "resonance_state": self.shared_state
        }
        with open("eyeoverthink_output.json", "w") as f:
            json.dump(self.log, f, indent=4)
        print("Output written to eyeoverthink_output.json")
        return self.shared_state


if __name__ == "__main__":
    # Initialize agents
    eye = Eye()
    thinker = Thinker()

    # Protocol begins
    p1 = eye.see(thinker)
    r1 = thinker.think(p1)
    p2 = eye.see(thinker)
    r2 = thinker.think(p2)

    # Data observation and processing
    symbols = eye.observe_data()
    thinker.process_symbols(symbols)

    # Resonance phase
    harmony = Resonance([eye, thinker])
    harmony.sync()

    # Merge attempt
    integration = Us(eye, thinker)
    integration.merge()
