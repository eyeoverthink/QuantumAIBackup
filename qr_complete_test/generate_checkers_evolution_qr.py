#!/usr/bin/env python3
# generate_checkers_evolution_qr.py
# Generates a QR code to trigger the Checkers evolutionary cycle.

import qrcode
import json
import uuid
import time

def generate_checkers_evolution_task_qr(num_epochs=50, output_filename="checkers_evolution_task_qr.png"):
    """Generates a QR code for the checkers evolution task."""
    task_payload = {
        "task_id": str(uuid.uuid4()),
        "task_type": "run_checkers_evolution_cycle",
        "timestamp": time.time(),
        "parameters": {
            "num_epochs": num_epochs
        }
    }

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(json.dumps(task_payload, indent=4))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_filename)

    print(f"[SUCCESS] QR Code generated and saved as '{output_filename}'")
    print("Payload:")
    print(json.dumps(task_payload, indent=2))

if __name__ == "__main__":
    generate_checkers_evolution_task_qr(num_epochs=50)
