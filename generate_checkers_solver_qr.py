import qrcode
import json

def generate_solver_qr_code(output_filename='checkers_solver_task_qr.png'):
    """Generates a QR code to trigger the checkers puzzle solver."""
    task_data = {
        'task_type': 'run_checkers_solver',
        'description': 'A task to execute the self-evolving checkers puzzle solver.'
    }

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(json.dumps(task_data))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_filename)
    print(f"[SUCCESS] Checkers solver QR code saved to '{output_filename}'")

if __name__ == '__main__':
    generate_solver_qr_code()
