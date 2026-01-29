import json
import qrcode
import uuid
from PIL import Image, ImageDraw, ImageFont
import os

# Configuration
QR_CODE_FILENAME = "generic_task_qr.png"

def display_qr_code(data_string, filename="qr_code.png"):
    """Generates and saves a QR code, then tries to display it."""
    qr = qrcode.QRCode(
        version=None,  # Let the library choose the smallest fitting version
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data_string)
    try:
        qr.make(fit=True)
    except qrcode.exceptions.DataOverflowError:
        print("Error: Data too long for QR code. Consider reducing payload size.")
        # Attempt to make a larger version if possible, though this might still fail
        # For very large data, other strategies are needed (compression, splitting, etc.)
        qr.best_fit(start=21) # Try starting from a larger version
        try:
            qr.make(fit=True)
        except qrcode.exceptions.DataOverflowError as e:
            print(f"Critical Error: Data still too long even after trying best_fit. {e}")
            return False

    img = qr.make_image(fill_color="black", back_color="white")
    img_path = os.path.join(os.getcwd(), filename)
    img.save(img_path)
    print(f"Task QR code saved to {img_path}")

    try:
        # Try to open the image (platform-dependent)
        if os.name == 'nt': # Windows
            os.startfile(img_path)
        elif os.uname().sysname == 'Darwin': # macOS
            os.system(f'open "{img_path}"')
        else: # Linux
            os.system(f'xdg-open "{img_path}"')
        return True
    except Exception as e:
        print(f"Error displaying QR code image: {e}")
        print(f"Please open {img_path} manually.")
        return False # Indicates display error, but QR was saved


def main():
    print("Generic QR File Creator/Reader Task Issuer started.")

    # 1. Define the worker script to be embedded
    # This script will be executed on the target machine by qr_task_worker_from_file.py
    worker_script_content = """
import json
import os

print(\"W: File Creator/Reader Script Started\")
filename_on_target = \"created_by_qr_task.txt\"
content_to_write = \"Hello from the QR task initiated on another Mac!\\nThis file confirms the remote execution worked.\"

# Determine file path in the CWD of the worker script on the target machine
file_path_on_target = os.path.join(os.getcwd(), filename_on_target)

try:
    print(f\"W: Attempting to create and write to: {file_path_on_target}\")
    with open(file_path_on_target, \"w\") as f:
        f.write(content_to_write)
    print(f\"W: Successfully wrote to {filename_on_target}\")

    print(f\"W: Attempting to read back {filename_on_target}\")
    read_content = \"\"
    with open(file_path_on_target, \"r\") as f:
        read_content = f.read()
    print(f\"W: Content read from {filename_on_target}:\")
    print(\"---------------------------\")
    print(read_content)
    print(\"---------------------------\")
    print(\"W: File read back successfully.\")

except Exception as e:
    print(f\"W: Error during file operation: {e}\")

print(\"W: File Creator/Reader Script Finished\")
"""

    # 2. Define minimal task metadata
    task_meta_data = {
        "type": "GenericFileCreateReadTask",
        "description": "Creates a file, writes to it, and reads it back.",
        "version": "1.0"
    }

    # 3. Create the task payload for the QR code
    task_id = str(uuid.uuid4())
    task_payload_dict = {
        "task_id": task_id,
        "task_meta": task_meta_data,
        "script": worker_script_content,
        "input_data": {
            "task_meta_info": task_meta_data.copy() # Pass metadata to script if needed
        } # No specific fraymus_capsule for this generic task
    }

    json_task_payload = json.dumps(task_payload_dict)
    print(f"Task payload created for task_id: {task_id}")

    # 4. Generate and display the QR code
    print(f"\nGenerating QR Code ({QR_CODE_FILENAME})...")
    if display_qr_code(json_task_payload, QR_CODE_FILENAME):
        print("QR Code generated and display attempted successfully.")
    else:
        print("QR Code generated, but display failed. Check console for path.")

    print("\nGeneric QR File Creator/Reader Task Issuer finished.")

if __name__ == "__main__":
    main()

