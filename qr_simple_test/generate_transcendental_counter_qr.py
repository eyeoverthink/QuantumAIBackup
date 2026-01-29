"""
Generates a QR code to trigger the Quantum Transcendental Counter.

The QR code contains a JSON payload with:
- task_type: "run_transcendental_counter"
- duration: (Optional) The number of seconds the counter should run.
"""
import qrcode
import json
import os
import argparse
import uuid

DEFAULT_OUTPUT_FILENAME = "transcendental_counter_task_qr.png"

def generate_qr_for_transcendental_counter(duration=None, output_filename=DEFAULT_OUTPUT_FILENAME):
    """
    Generates a QR code for the transcendental counter task.

    Args:
        duration (int, optional): The duration in seconds for the counter to run.
                                  If None, the worker will use its default.
        output_filename (str): The filename for the generated QR code image.

    Returns:
        str: The absolute path to the generated QR code image.
    """
    task_id = str(uuid.uuid4())
    task_payload = {
        "task_type": "run_transcendental_counter",
        "task_id": task_id,
        "timestamp": time.time() # Added timestamp similar to other generators
    }

    if duration is not None:
        task_payload["duration"] = int(duration)
    
    # For fraymus_qr_module compatibility, nest under 'task_data'
    fraymus_payload = {
        "issuer_id": "generate_transcendental_counter_qr",
        "task_data": task_payload
    }

    qr_data_string = json.dumps(fraymus_payload, indent=4)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data_string)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Ensure the output directory exists (if specified in output_filename)
    output_dir = os.path.dirname(output_filename)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")

    img.save(output_filename)
    abs_path = os.path.abspath(output_filename)
    print(f"Generated QR code for transcendental counter task (ID: {task_id}) with data:")
    print(qr_data_string)
    print(f"QR code saved to: {abs_path}")
    return abs_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a QR code to run the Quantum Transcendental Counter.")
    parser.add_argument(
        "--duration", 
        type=int, 
        help="(Optional) Duration in seconds for the counter to run.",
        default=None
    )
    parser.add_argument(
        "--output", 
        type=str, 
        default=DEFAULT_OUTPUT_FILENAME, 
        help=f"Output filename for the QR code image (default: {DEFAULT_OUTPUT_FILENAME})"
    )

    args = parser.parse_args()

    # Add timestamp for uniqueness if not included, helps with fraymus structure
    import time # Ensure time is imported if not already for the main block

    generate_qr_for_transcendental_counter(duration=args.duration, output_filename=args.output)
