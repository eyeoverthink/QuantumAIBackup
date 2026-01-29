import qrcode
import json
import uuid

# --- Task Configuration ---
TASK_PAYLOAD = {
    "task_id": str(uuid.uuid4()),
    "task_type": "run_hanoi_solver",
    "timestamp": __import__('time').time(),
    "parameters": {
        "num_disks": 3
    }
}

# --- QR Code Generation ---
qr_data = json.dumps(TASK_PAYLOAD, indent=4)
qr_img = qrcode.make(qr_data)

# --- Save the QR Code ---
output_filename = 'hanoi_solver_task_qr.png'
qr_img.save(output_filename)

print(f"[SUCCESS] QR Code generated and saved as '{output_filename}'")
print("Payload:")
print(qr_data)
