
import os
file_path = os.path.join(r"qr_progressive_test/workspace", "hello_world.py")
content = """#!/usr/bin/env python3
# Hello World - Created by QR Code 1

def main():
    print("Hello, World!")
    print(f"I was created by QR Code 1")

if __name__ == "__main__":
    main()
"""
with open(file_path, 'w') as f:
    f.write(content)
print(f"Created {file_path}")
