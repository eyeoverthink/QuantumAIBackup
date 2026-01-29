import qrcode
import json
import uuid
from datetime import datetime, timedelta
import base64
import os
from cryptography.fernet import Fernet

def get_encryption_key(key_path="qr_encryption.key"):
    """Loads or generates an encryption key."""
    if os.path.exists(key_path):
        with open(key_path, "rb") as key_file:
            return key_file.read()
    else:
        print(f"Warning: Encryption key not found at {key_path}. A new key will be used for this session, but decryption will fail if the runner does not have it.")
        key = Fernet.generate_key()
        # In a real scenario, this key would need to be securely distributed.
        # For this demo, we assume the runner can find it or has it.
        with open(key_path, "wb") as key_file:
            key_file.write(key)
        return key

def generate_task_qr(task_payload, output_filename, encrypt=False):
    """
    Generates a QR code from a task payload.

    Args:
        task_payload (dict): The JSON payload for the task.
        output_filename (str): The path to save the QR code image.
        encrypt (bool): Whether to encrypt the payload.
    """
    payload_text = json.dumps(task_payload, indent=4)

    if encrypt:
        print("Encrypting payload...")
        key = get_encryption_key()
        f = Fernet(key)
        encrypted_data = f.encrypt(payload_text.encode('utf-8'))
        payload_text = "ENCRYPTED:" + base64.b64encode(encrypted_data).decode('utf-8')

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(payload_text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_filename)
    print(f"Successfully generated QR code: {output_filename}")

def main():
    """Main function to generate a specific refactoring task QR code."""
    print("Generating Meta-Refactorer Task QR Code...")

    refactor_script_content = """
import sys
import os
sys.path.append(os.getcwd())

from qr_phi_meta_refactorer_v2 import QuantumPhiMetaRefactorer

print("Executing meta-refactorer task...")

target_file = task_inputs.get('target_file')

if not target_file:
    print("Error: 'target_file' not found in task_inputs.")
else:
    print(f"Target file for refactoring: {target_file}")
    if os.path.exists(target_file):
        refactorer = QuantumPhiMetaRefactorer()
        results = refactorer.load_and_refactor_file(target_file)
        
        print("\\n--- Refactoring Summary ---")
        print(f"Refactorings made: {results['refactorings_made']}")
        print(f"File saved to: {results['output_path']}")
        print("---------------------------\\n")
    else:
        print(f"Error: Target file {target_file} does not exist.")
"""

    task_payload = {
        "session_id": str(uuid.uuid4()),
        "frame_number": 1,
        "task_type": "execute_python",
        "content": "from qr_phi_meta_refactorer_v2 import QuantumPhiMetaRefactorer\nimport os\nprint('Meta-refactorer executing...')\nif os.path.exists('test_subject.py'):\n    r = QuantumPhiMetaRefactorer()\n    res = r.load_and_refactor_file('test_subject.py')\n    print(f'Done: {res[\"refactorings_made\"]} refactorings, saved to {res[\"output_path\"]}')\nelse:\n    print('test_subject.py not found')",
        "valid_until": (datetime.now() + timedelta(hours=1)).isoformat()
    }

    output_filename = "qr_refactor_task.png"
    
    generate_task_qr(task_payload, output_filename, encrypt=False)

if __name__ == "__main__":
    main()
