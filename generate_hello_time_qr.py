import qrcode
import datetime
import os

def display_qr_code_image(image_path):
    """Displays the QR code image using the default system viewer."""
    try:
        if os.name == 'nt':  # Windows
            os.startfile(image_path)
        elif os.uname().sysname == 'Darwin':  # macOS
            os.system(f'open "{image_path}"')
        else:  # Linux
            os.system(f'xdg-open "{image_path}"')
        print(f"Displaying QR code: {image_path}. Close the image viewer to continue.")
        return True
    except Exception as e:
        print(f"Error displaying QR code: {e}")
        print("Please open the QR code manually from the path: " + os.path.abspath(image_path))
        return False

def create_hello_time_qr():
    # Get the current exact time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    
    # Prepare the text for the QR code
    text_to_encode = f"HELLO WORLD {current_time}"
    
    # Define the output file name
    qr_file_name = "hello_world_time.png"
    qr_full_path = os.path.join(os.getcwd(), qr_file_name) # For clearer print messages
    
    print(f"Generating QR code with text: '{text_to_encode}'")
    
    # Generate the QR code
    # Using a specific version and error correction for consistency, can be adjusted
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text_to_encode)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the QR code image
    img.save(qr_full_path)
    print(f"QR code saved as: {qr_full_path}")
    
    # Display the QR code
    display_qr_code_image(qr_full_path)
    print(f"If the image viewer for the QR code is still open, you may need to close it manually.")

if __name__ == "__main__":
    create_hello_time_qr()
