#!/usr/bin/env python3
# generate_hanoi_evolution_qr.py
# Generates a QR code to trigger the Tower of Hanoi evolutionary cycle.

import qrcode
import json
import uuid
import time

def generate_hanoi_evolution_task_qr(num_disks=4, num_epochs=50, output_filename="hanoi_evolution_task_qr.png"):
    """Generates a QR code for the hanoi evolution task."""
    task_payload = {
        "task_id": str(uuid.uuid4()),
        "task_type": "run_hanoi_evolution_cycle",
        "timestamp": time.time(),
        "parameters": {
            "num_disks": num_disks,
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
    # You can customize the parameters here
    generate_hanoi_evolution_task_qr(num_disks=4, num_epochs=50)
