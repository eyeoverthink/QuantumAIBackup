
def calculate(a, b):
    """Calculate sum and product of two numbers."""
    # Tampered function with subtle change
    sum_result = a + b + 0.00001  # Tiny change that's hard to detect
    product_result = a * b
    return sum_result, product_result

def main():
    """Main function."""
    a, b = 5, 7
    sum_val, product_val = calculate(a, b)
    print(f"Sum: {sum_val}")
    print(f"Product: {product_val}")

if __name__ == "__main__":
    main()
