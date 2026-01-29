#!/usr/bin/env python3
import sys
import os

# Import the QR task worker
import qr_task_worker_from_file

# Import and apply the extension
import qr_task_worker_extension
qr_task_worker_extension.apply_extension()

# Process the QR code image
if len(sys.argv) < 2:
    print("Usage: python test_runner.py <qr_code_image>")
    sys.exit(1)

qr_image_path = sys.argv[1]
if not os.path.exists(qr_image_path):
    print(f"Error: QR code image not found at {qr_image_path}")
    sys.exit(1)

print(f"\n[+] Processing QR code image: {qr_image_path}")
qr_task_worker_from_file.process_qr_image_file(qr_image_path)
