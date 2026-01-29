"""
logic_reference.py
Modular, canonical logic and math reference for QuantumAI Orchestrator logic healing.
Follows phi-harmonic, quantum, and golden ratio principles. Import-only, never modifies core files.
"""

# --- LOGIC GATES ---
def AND(a, b):
    """Logical AND gate."""
    return bool(a) and bool(b)

def OR(a, b):
    """Logical OR gate."""
    return bool(a) or bool(b)

def NOT(a):
    """Logical NOT gate."""
    return not bool(a)

def XOR(a, b):
    """Logical XOR gate."""
    return bool(a) != bool(b)

def NAND(a, b):
    """Logical NAND gate."""
    return not (AND(a, b))

def NOR(a, b):
    """Logical NOR gate."""
    return not (OR(a, b))

def XNOR(a, b):
    """Logical XNOR gate."""
    return not XOR(a, b)

# --- MATH OPERATIONS ---
def ADD(a, b):
    """Addition."""
    return a + b

def SUB(a, b):
    """Subtraction."""
    return a - b

def MUL(a, b):
    """Multiplication."""
    return a * b

def DIV(a, b):
    """Division, returns None if division by zero."""
    try:
        return a / b
    except ZeroDivisionError:
        return None

def MOD(a, b):
    """Modulo, returns None if division by zero."""
    try:
        return a % b
    except ZeroDivisionError:
        return None

def EXP(a, b):
    """Exponentiation."""
    return a ** b

# --- SYMBOLIC ALPHABETS & TRANSFORMS ---
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
DIGITS = '0123456789'
SYMBOLS = '!@#$%^&*()-_=+[]{}|;:,.<>?/`~'

# --- TRUTH TABLES ---
TRUTH_TABLES = {
    'AND': {(0,0):0, (0,1):0, (1,0):0, (1,1):1},
    'OR':  {(0,0):0, (0,1):1, (1,0):1, (1,1):1},
    'XOR': {(0,0):0, (0,1):1, (1,0):1, (1,1):0},
    'NAND':{(0,0):1, (0,1):1, (1,0):1, (1,1):0},
    'NOR': {(0,0):1, (0,1):0, (1,0):0, (1,1):0},
    'XNOR':{(0,0):1, (0,1):0, (1,0):0, (1,1):1},
}

# --- PHI-HARMONIC EXTENSIONS ---
from math import sqrt, pi, e, log

PHI = (1 + sqrt(5)) / 2
PHI_INV = PHI - 1

# Example: phi-harmonic scaling

def PHI_SCALE(x):
    """Linear scaling by golden ratio."""
    return PHI * x

def PHI_MOD(x):
    """Phi-harmonic resonance mod 1."""
    return (PHI * x) % 1

# --- QUANTUM EXTENSIONS (STUBS) ---
def QUBIT_NOT(q):
    """Quantum NOT (X) gate stub."""
    return 1-q if q in (0,1) else None

def QUBIT_HADAMARD(q):
    """Quantum Hadamard gate stub (returns superposition placeholder)."""
    return 'superposition' if q in (0,1) else None

# --- UTILITY: Validate logic gate by truth table ---
def validate_gate(gate_name, a, b=None):
    """Validate gate output against canonical truth table."""
    table = TRUTH_TABLES.get(gate_name.upper())
    if table is None:
        raise ValueError(f'Unknown gate: {gate_name}')
    key = (int(bool(a)), int(bool(b))) if b is not None else (int(bool(a)),)
    return table.get(key)

# --- END MODULE ---
