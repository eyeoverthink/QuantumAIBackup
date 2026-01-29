#!/usr/bin/env python3
"""
Test file with low phi-harmonic coherence for MoA integration testing.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, value):
        self.result += value
    
    def subtract(self, value):
        self.result -= value
    
    def multiply(self, value):
        self.result *= value
    
    def divide(self, value):
        self.result /= value
    
    def clear(self):
        self.result = 0
    
    def get_result(self):
        return self.result

if __name__ == "__main__":
    calc = Calculator()
    calc.add(5)
    calc.multiply(2)
    calc.subtract(3)
    calc.divide(2)
    print(f"Result: {calc.get_result()}")
