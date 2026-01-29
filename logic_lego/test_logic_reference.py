"""
test_logic_reference.py
Unit tests for logic_reference.py (modular, import-only).
Ensures all gates, math ops, and phi-harmonic extensions are cohesive and correct.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from logic_reference import *

def test_logic_gates():
    assert AND(1, 1) == True
    assert AND(1, 0) == False
    assert OR(0, 1) == True
    assert OR(0, 0) == False
    assert NOT(1) == False
    assert NOT(0) == True
    assert XOR(1, 0) == True
    assert XOR(1, 1) == False
    assert NAND(1, 1) == False
    assert NOR(0, 0) == True
    assert XNOR(1, 1) == True
    print('Logic gates: PASS')

def test_math_ops():
    assert ADD(2, 3) == 5
    assert SUB(5, 2) == 3
    assert MUL(3, 4) == 12
    assert DIV(8, 2) == 4
    assert DIV(8, 0) is None
    assert MOD(7, 3) == 1
    assert MOD(7, 0) is None
    assert EXP(2, 3) == 8
    print('Math ops: PASS')

def test_alphabet():
    assert 'A' in ALPHABET
    assert 'z' in ALPHABET
    assert '5' in DIGITS
    assert '@' in SYMBOLS
    print('Alphabets: PASS')

def test_truth_tables():
    assert validate_gate('AND', 1, 1) == 1
    assert validate_gate('AND', 1, 0) == 0
    assert validate_gate('XOR', 1, 0) == 1
    assert validate_gate('XNOR', 1, 1) == 1
    print('Truth tables: PASS')

def test_phi_harmonic():
    x = 2
    assert abs(PHI_SCALE(x) - PHI * x) < 1e-8
    assert 0 <= PHI_MOD(x) < 1
    print('Phi-harmonic: PASS')

def test_quantum_stubs():
    assert QUBIT_NOT(0) == 1
    assert QUBIT_NOT(1) == 0
    assert QUBIT_HADAMARD(0) == 'superposition'
    assert QUBIT_HADAMARD(1) == 'superposition'
    print('Quantum stubs: PASS')

def run_all():
    test_logic_gates()
    test_math_ops()
    test_alphabet()
    test_truth_tables()
    test_phi_harmonic()
    test_quantum_stubs()
    print('\nALL LOGIC REFERENCE TESTS PASSED')

if __name__ == '__main__':
    run_all()
