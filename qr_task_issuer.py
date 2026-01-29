import qrcode
import json
import uuid
import os
import datetime
import base64
from PIL import Image # For displaying the image
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.serialization import load_pem_public_key

# Generate or load encryption key
def get_encryption_key(key_path="qr_encryption.key"):
    """Generate or load a Fernet encryption key"""
    if os.path.exists(key_path):
        with open(key_path, "rb") as key_file:
            key = key_file.read()
    else:
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        print(f"New encryption key generated and saved to {key_path}")
    return key

def create_task_qr(content, task_type="script", input_data=None, image_path="task_qr.png", expiry_hours=24, encrypt=True):
    """
    Creates a QR code containing a JSON payload for a task with enhanced security.
    
    Args:
        content: Script content or list of script steps for multi-task
        task_type: Type of task ("script", "execute_sh", "multi")
        input_data: Dictionary of input data for the script
        image_path: Path to save the QR code image
        expiry_hours: Hours until this task expires
        encrypt: Whether to encrypt the payload
    """
    task_id = str(uuid.uuid4())
    
    # Set expiration time
    valid_until = (datetime.datetime.now() + 
                  datetime.timedelta(hours=expiry_hours)).isoformat()
    
    # Create appropriate payload based on task_type
    if task_type == "multi":
        # Content should be a list of step dictionaries
        payload = {
            "task_id": task_id,
            "task_type": "multi",
            "steps": content,
            "valid_until": valid_until,
            "used": False,
            "input_data": input_data if input_data is not None else {}
        }
    else:
        # Single script or shell execution
        payload = {
            "task_id": task_id,
            "task_type": task_type,
            "script_content": content,
            "valid_until": valid_until,
            "used": False,
            "input_data": input_data if input_data is not None else {}
        }
    # Convert payload to JSON
    json_payload = json.dumps(payload)
    
    # Encrypt the payload if requested
    if encrypt:
        key = get_encryption_key()
        f = Fernet(key)
        encrypted_payload = f.encrypt(json_payload.encode('utf-8'))
        # Convert to base64 string for QR code
        final_payload = base64.b64encode(encrypted_payload).decode('utf-8')
        # Add a marker to indicate encryption
        final_payload = "ENCRYPTED:" + final_payload
    else:
        final_payload = json_payload

    # Generate QR code
    qr_img = qrcode.make(final_payload)
    
    # Save the QR code image
    try:
        qr_img.save(image_path)
        print(f"Task QR code saved to {os.path.abspath(image_path)} with task_id: {task_id}")
    except Exception as e:
        print(f"Error saving QR code image: {e}")
        return

    # Display the QR code image
    try:
        img_to_show = Image.open(image_path)
        img_to_show.show()
        print(f"Displaying QR code. Close the image viewer to continue or stop this script.")
    except Exception as e:
        print(f"Error displaying QR code image: {e}")
        print(f"Please open {os.path.abspath(image_path)} manually.")

if __name__ == "__main__":
    print("QR Task Issuer started.")
    print("This script will generate a QR code for a task and display it.")
    print("The 'worker' machine should scan this QR code from the screen.")
    
    # Ask user which type of task to create
    print("\nSelect task type:")
    print("1. Python script")
    print("2. Shell script")
    print("3. Multi-step task")
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        # --- Python script example ---
        example_script = """
print(f"Executing Python task on worker...")
if 'message' in task_inputs:
    print(f"Message from issuer: {task_inputs['message']}")
if 'value' in task_inputs:
    result = task_inputs['value'] * task_inputs.get('multiplier', 1)
    print(f"Calculation: {task_inputs['value']} * {task_inputs.get('multiplier', 1)} = {result}")
"""
        example_data = {
            "message": "Hello from Vaughn Scott on June 26th, at 12:22pm Pacific Time (on my MacAir)!",
            "value": 42,
            "multiplier": 2
        }
        create_task_qr(example_script, "script", example_data, "task_qr_python.png")
        
    elif choice == "2":
        # --- Shell script example ---
        shell_script = """#!/bin/bash
echo "Shell script execution started"
echo "Current time: $(date)"
echo "Hello from Vaughn Scott" > hello_output_$(date +%Y-%m-%d_%H-%M-%S).txt
echo "Shell script completed"
"""
        create_task_qr(shell_script, "execute_sh", None, "task_qr_shell.png")
        
    elif choice == "3":
        # --- Multi-step example ---
        multi_steps = [
            {"type": "shell", "content": "echo \"Starting multi-step task...\""}, 
            {"type": "python", "content": "print('Step 2: Python code executing')\nprint('Current time:', __import__('datetime').datetime.now())"}, 
            {"type": "shell", "content": "echo \"Final step completed\" > multi_task_$(date +%Y-%m-%d_%H-%M-%S).txt"}
        ]
        create_task_qr(multi_steps, "multi", None, "task_qr_multi.png")
        
    else:
        print("Invalid choice. Exiting.")
        exit(1)
    
    print("\nQR Task Issuer finished. You can now run the worker script on the other machine.")
    print("If the image viewer for the QR code is still open, you may need to close it manually.")
