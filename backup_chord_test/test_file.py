#!/usr/bin/env python3
# Test file for backup functionality

def phi():
    """Return the golden ratio."""
    return 1.618034

def fibonacci(n):
    """Return the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
