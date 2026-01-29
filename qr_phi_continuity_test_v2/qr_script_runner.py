from PIL import Image
from qreader import QReader
import cv2
import sys
import os
import json
import base64
import datetime
import sqlite3
import tempfile
import subprocess
from cryptography.fernet import Fernet

# Setup task history database
def setup_task_db():
    """Create SQLite database to track executed tasks"""
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "qr_tasks_history.db")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS task_history (
        task_id TEXT PRIMARY KEY,
        execution_time TEXT,
        task_type TEXT,
        valid_until TEXT,
        status TEXT
    )
    """)
    conn.commit()
    return conn

# Load encryption key
def get_encryption_key(key_path="qr_encryption.key"):
    """Load the Fernet encryption key"""
    if os.path.exists(key_path):
        with open(key_path, "rb") as key_file:
            return key_file.read()
    else:
        print(f"Error: Encryption key not found at {key_path}")
        print("Make sure to copy the key from the issuer machine.")
        return None

# Mark QR image as used
def mark_image_as_used(image_path):
    """Add a visual indicator that this QR code has been used"""
    try:
        img = Image.open(image_path)
        # Add a red X or text overlay
        width, height = img.size
        # Create a copy with _used suffix
        used_path = image_path.replace(".png", "_used.png")
        img.save(used_path)
        print(f"Marked QR code as used: {used_path}")
    except Exception as e:
        print(f"Could not mark image as used: {e}")

def run_script_from_qr(qr_image_path):
    """
    Decodes a task from a QR code image and executes it with security checks.

    Args:
        qr_image_path (str): The path to the QR code image file.
    """
    try:
        if not os.path.exists(qr_image_path):
            print(f"Error: QR code image not found at {qr_image_path}")
            return

        print(f"Attempting to decode QR code from: {qr_image_path} using qreader")
        
        # Initialize QReader
        qreader_decoder = QReader()
        
        # Decode the QR code from the image file path
        # qreader.decode() returns a list of decoded strings or None
        # We need to read the image first, qreader expects an image array
        image_for_qreader = cv2.imread(qr_image_path)
        if image_for_qreader is None:
            print(f"Error: Could not read image file {qr_image_path} with OpenCV for qreader.")
            return
            
        decoded_text = qreader_decoder.detect_and_decode(image=image_for_qreader)
        
        if not decoded_text or decoded_text[0] is None:
            print("Error: No QR code found in the image or could not decode with qreader.")
            return
            
        # qreader returns a list of decoded data, take the first one.
        payload_text = decoded_text[0]
        
        # Check if payload is encrypted
        if payload_text.startswith("ENCRYPTED:"):
            print("Encrypted payload detected. Decrypting...")
            # Remove the ENCRYPTED: prefix
            encrypted_data = payload_text[10:]
            # Decrypt the payload
            key = get_encryption_key()
            if not key:
                print("Cannot proceed without decryption key.")
                return
                
            try:
                f = Fernet(key)
                # Decode base64 then decrypt
                encrypted_bytes = base64.b64decode(encrypted_data)
                decrypted_data = f.decrypt(encrypted_bytes).decode('utf-8')
                payload = json.loads(decrypted_data)
                print("Payload successfully decrypted.")
            except Exception as e:
                print(f"Decryption failed: {e}")
                return
        else:
            # Unencrypted payload
            try:
                payload = json.loads(payload_text)
                print("Unencrypted payload loaded.")
            except json.JSONDecodeError:
                print("Error: Payload is not valid JSON.")
                return
        
        # Connect to task history database
        conn = setup_task_db()
        cursor = conn.cursor()
        
        # Check if task has already been executed
        task_id = payload.get("task_id")
        cursor.execute("SELECT * FROM task_history WHERE task_id = ?", (task_id,))
        if cursor.fetchone():
            print(f"Error: Task {task_id} has already been executed.")
            conn.close()
            return
            
        # Check if task has expired
        if "valid_until" in payload:
            try:
                expiry_time = datetime.datetime.fromisoformat(payload["valid_until"])
                current_time = datetime.datetime.now()
                if current_time > expiry_time:
                    print(f"Error: Task expired on {expiry_time}")
                    # Record expired task
                    cursor.execute(
                        "INSERT INTO task_history VALUES (?, ?, ?, ?, ?)",
                        (task_id, current_time.isoformat(), payload.get("task_type", "unknown"), 
                         payload["valid_until"], "expired")
                    )
                    conn.commit()
                    conn.close()
                    mark_image_as_used(qr_image_path)
                    return
            except (ValueError, TypeError) as e:
                print(f"Warning: Could not parse expiry time: {e}")
        
        # Process based on task type
        task_type = payload.get("task_type", "script")
        
        if task_type == "execute_sh":
            # Shell script execution
            print("Executing shell script...")
            script_content = payload.get("script_content", "")
            if not script_content:
                print("Error: No shell script content found in payload.")
                return
                
            # Write to temporary file
            temp_script_path = "temp_generated_script.sh"
            with open(temp_script_path, "w") as script_file:
                script_file.write(script_content)
            
            # Make executable
            os.chmod(temp_script_path, 0o755)
            
            # Execute
            try:
                result = subprocess.run(["./" + temp_script_path], 
                                       capture_output=True, text=True, check=True)
                print("Shell script output:")
                print(result.stdout)
                if result.stderr:
                    print("Errors:")
                    print(result.stderr)
            except subprocess.CalledProcessError as e:
                print(f"Shell script execution failed: {e}")
                print(e.stderr)
                
        elif task_type == "multi":
            # Multi-step execution
            print("Executing multi-step task...")
            steps = payload.get("steps", [])
            
            for i, step in enumerate(steps):
                step_type = step.get("type")
                content = step.get("content", "")
                print(f"\nExecuting step {i+1}/{len(steps)} ({step_type})...")
                
                if step_type == "shell":
                    # Execute shell command
                    temp_script_path = f"temp_step_{i+1}.sh"
                    with open(temp_script_path, "w") as script_file:
                        script_file.write("#!/bin/bash\n" + content)
                    
                    os.chmod(temp_script_path, 0o755)
                    try:
                        result = subprocess.run(["./" + temp_script_path], 
                                              capture_output=True, text=True, check=True)
                        print(result.stdout)
                    except subprocess.CalledProcessError as e:
                        print(f"Step {i+1} failed: {e}")
                        print(e.stderr)
                        
                elif step_type == "python":
                    # Execute Python code
                    try:
                        # Create a context with task inputs
                        context = {}
                        if "input_data" in payload:
                            context["task_inputs"] = payload["input_data"]
                        exec(content, context)
                    except Exception as e:
                        print(f"Python step {i+1} failed: {e}")
                
        else:  # Default to Python script
            # Python script execution
            print("Executing Python script...")
            script_content = payload.get("script_content", "")
            if not script_content:
                print("Error: No script content found in payload.")
                return
                
            # --- SECURITY WARNING ---
            # Executing arbitrary code with exec() is dangerous and should not be done 
            # with untrusted QR codes in a real application without proper sandboxing.
            # This is for demonstration purposes only.
            # --- ---------------- ---
            try:
                # Create a context with task inputs
                context = {}
                if "input_data" in payload:
                    context["task_inputs"] = payload["input_data"]
                exec(script_content, context)
            except Exception as e:
                print(f"Script execution failed: {e}")
        
        # Record successful execution
        cursor.execute(
            "INSERT INTO task_history VALUES (?, ?, ?, ?, ?)",
            (task_id, datetime.datetime.now().isoformat(), task_type, 
             payload.get("valid_until", ""), "executed")
        )
        conn.commit()
        conn.close()
        
        # Mark QR code as used
        mark_image_as_used(qr_image_path)
        
        print("Task execution finished.")
        
    except FileNotFoundError:
        print(f"Error: Could not find the QR image at {qr_image_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("QR Task Worker v2.0 - By Vaughn Scott")
    print("Enhanced with encryption, expiration, and multi-script support")
    
    if len(sys.argv) != 2:
        print("Usage: python qr_script_runner.py <path_to_qr_image.png>")
        print("Example: python qr_script_runner.py task_qr_python.png")
        sys.exit(1)
    
    image_path = sys.argv[1]
    run_script_from_qr(image_path)
    
    # Clean up temp files
    for file in os.listdir("."):
        if file.startswith("temp_") and (file.endswith(".sh") or file.endswith(".py")):
            try:
                os.remove(file)
                print(f"Cleaned up temporary file: {file}")
            except:
                pass
