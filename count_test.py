# # Python script to count from 1 to 10 and back to 1
# def count():
#     for i in range(1, 11):
#         print(i)
#     for i in range(9, 0, -1):
#         print(i)

# count()

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Calculate the first 15 Fibonacci numbers
fibonacci_numbers = [fibonacci(i) for i in range(1, 16)]

# Calculate the 31st Fibonacci number
fibonacci_31 = fibonacci(31)

# Multiply the next 5 Fibonacci numbers by the 31st Fibonacci number
next_5_fibonacci = [fibonacci(i) * fibonacci_31 for i in range(16, 21)]

print("First 15 Fibonacci numbers:", fibonacci_numbers)
print("31st Fibonacci number:", fibonacci_31)
print("Next 5 Fibonacci numbers multiplied by the 31st Fibonacci number:", next_5_fibonacci)