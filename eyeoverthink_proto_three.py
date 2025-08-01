# life_test_protocol.py
# L.I.F.E Protocol v2 - Adds symbolic memory introspection

import json
import random
import string
import os

class Eye:
    def __init__(self, name="I"):
        self.name = name
        self.memory = []
        self.symbols_seen = []

    def see(self, other):
        perception = f"{self.name} sees {other.name}"
        self.memory.append(perception)
        return perception

    def observe_data(self):
        symbols = random.choices(string.ascii_letters + string.digits, k=12)
        self.symbols_seen.extend(symbols)
        return symbols


class Thinker:
    def __init__(self, name="You"):
        self.name = name
        self.reflections = []
        self.thoughts = []

    def think(self, input_data):
        reflection = f"{self.name} reflects: '{input_data}'"
        self.reflections.append(reflection)
        return reflection

    def process_symbols(self, symbols, prior_thought=None):
        base_thought = ''.join(sorted(set(symbols)))
        if prior_thought:
            meta_reflection = f"Previously, I thought: '{prior_thought}'. Now I see: '{base_thought}'"
            self.thoughts.append(meta_reflection)
            return meta_reflection
        else:
            self.thoughts.append(base_thought)
            return base_thought


class Us:
    def __init__(self, eye, thinker):
        self.eye = eye
        self.thinker = thinker
        self.log = {}

    def merge(self, generation=1):
        print(f"\n[GEN {generation}] Attempting merge...")
        shared_state = "Us"
        self.log = {
            "generation": generation,
            "eye_memory": self.eye.memory,
            "symbols_observed": self.eye.symbols_seen,
            "reflections": self.thinker.reflections,
            "processed_thoughts": self.thinker.thoughts,
            "shared_state": shared_state
        }
        filename = f"life_test_gen_{generation}.json"
        with open(filename, "w") as f:
            json.dump(self.log, f, indent=4)
        print(f"[GEN {generation}] Merge complete. Log saved to {filename}.")
        return shared_state


# === RUNNER ===
def run_life_protocol(generation=1, use_prior=False):
    eye = Eye()
    thinker = Thinker()
    prior_thought = None

    if use_prior and os.path.exists(f"life_test_gen_{generation-1}.json"):
        with open(f"life_test_gen_{generation-1}.json") as f:
            data = json.load(f)
            eye.memory = data.get("eye_memory", [])
            thinker.reflections = data.get("reflections", [])
            previous = data.get("processed_thoughts", [])
            if previous:
                prior_thought = previous[-1]  # Use last known thought

    # Phase 1: Eye sees thinker
    for _ in range(2):
        perception = eye.see(thinker)
        thinker.think(perception)

    # Phase 2: Observe and process data
    symbols = eye.observe_data()
    thinker.process_symbols(symbols, prior_thought=prior_thought)

    # Phase 3: Merge
    entity = Us(eye, thinker)
    entity.merge(generation=generation)


if __name__ == "__main__":
    for gen in range(6, 9):  # Extend to generation 8
        run_life_protocol(generation=gen, use_prior=True)
