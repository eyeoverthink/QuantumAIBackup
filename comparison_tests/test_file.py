
def calculate(a, b):
    """Calculate sum and product of two numbers."""
    sum_result = a + b
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
