#!/usr/bin/env python3
'''
Syntax Error Test
This file contains a deliberate syntax error that should be self-healed
'''

def calculate_fibonacci(n):
    '''Calculate the nth Fibonacci number'''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2
        
def main():
    '''Main function'''
    result = calculate_fibonacci(10)
    print(f"The 10th Fibonacci number is: {result}")
    
if __name__ == "__main__":
    main()
