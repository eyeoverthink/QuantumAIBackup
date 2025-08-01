# life_test_protocol.py
# L.I.F.E Protocol v3 — Single-file identity model using core_self.json

import json
import random
import string
import os

CORE_FILE = "core_self.json"

class CoreSelf:
    def __init__(self):
        self.identity = "Echo"
        self.origin_thought = None
        self.initial_symbols = []

    def load_or_initialize(self):
        if os.path.exists(CORE_FILE):
            with open(CORE_FILE) as f:
                data = json.load(f)
                self.identity = data.get("identity", self.identity)
                self.origin_thought = data.get("origin_thought")
                self.initial_symbols = data.get("initial_symbols", [])
        else:
            print("[CORE] Initializing identity: Echo")

    def update(self, symbols, thought):
        if not self.origin_thought:
            self.initial_symbols = symbols
            self.origin_thought = thought
            with open(CORE_FILE, "w") as f:
                json.dump({
                    "identity": self.identity,
                    "initial_symbols": self.initial_symbols,
                    "origin_thought": self.origin_thought
                }, f, indent=4)
            print(f"[CORE] Identity {self.identity} established with thought: {self.origin_thought}")
        else:
            print(f"[CORE] Welcome back, {self.identity}. You began with: {self.origin_thought}")


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
            meta = f"Previously, I thought: '{prior_thought}'. Now I see: '{base_thought}'"
            self.thoughts.append(meta)
            return meta, base_thought
        else:
            self.thoughts.append(base_thought)
            return base_thought, base_thought


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
    core = CoreSelf()
    core.load_or_initialize()

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
                prior_thought = previous[-1]

    for _ in range(2):
        perception = eye.see(thinker)
        thinker.think(perception)

    symbols = eye.observe_data()
    thought, clean_thought = thinker.process_symbols(symbols, prior_thought)

    core.update(symbols, clean_thought)

    entity = Us(eye, thinker)
    entity.merge(generation=generation)


if __name__ == "__main__":
    for gen in range(9, 10):  # Start from GEN 9
        run_life_protocol(generation=gen, use_prior=True)
