#!/usr/bin/env python3
# Fibonacci sequence generator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Print first 20 Fibonacci numbers
for i, num in enumerate(fibonacci(20)):
    print(f"F({i}) = {num}")
