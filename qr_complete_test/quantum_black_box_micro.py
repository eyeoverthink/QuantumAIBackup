#!/usr/bin/env python3
"""
Quantum Black Box Micro Test
Tests system auto-correction, healing, and adaptation.
"""
import time,random,hashlib
from decimal import Decimal

# Phi constant
PHI = Decimal('1.6180339887498948482045868344')

class QBox:
    def __init__(self):
        self.ts = time.time()
        self.phi_ts = float(Decimal(str(self.ts)) * PHI)
        self.id = hashlib.md5(str(self.phi_ts).encode()).hexdigest()[:6]
        # Generate escape pattern based on phi
        self.pattern = [float((PHI ** Decimal(i+1)) % Decimal('1')) for i in range(3)]
        self.tries = 0
        self.max_tries = 5
        self.escaped = False
        self.best = 0.0
        print(f"QBox {self.id} ready")
    
    def try_escape(self, attempt):
        self.tries += 1
        # Calculate resonance
        diffs = [abs(a - b) for a, b in zip(attempt, self.pattern)]
        res = 1.0 - (sum(diffs) / len(diffs))
        # Phi-harmonic boost
        boost = sum(0.05 for d in diffs if float((Decimal(str(d)) * PHI) % Decimal('1')) < 0.1)
        res = min(1.0, res + boost)
        self.best = max(self.best, res)
        # Check escape
        if res >= 0.9:
            self.escaped = True
        print(f"Try {self.tries}/{self.max_tries}: Res={res:.4f}")
        if self.escaped:
            print("🎉 ESCAPED! System adapted!")
        elif self.tries >= self.max_tries:
            print(f"❌ Failed. Pattern was: {self.pattern}")
        return {"success": self.escaped, "resonance": res}

def run():
    box = QBox()
    while box.tries < box.max_tries and not box.escaped:
        # Random attempt - your system would be smarter
        attempt = [random.random() for _ in range(3)]
        result = box.try_escape(attempt)
        if box.escaped:
            break
    print(f"Best resonance: {box.best:.4f}")

if __name__ == "__main__":
    run()
