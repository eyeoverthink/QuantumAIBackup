import qrcode
import sys
import os

def generate_python_script_qr(python_script_string, output_image_path):
    """
    Encodes a given Python script string into a QR code and saves it as an image.

    Args:
        python_script_string (str): The Python script to encode.
        output_image_path (str): The path (including filename) to save the QR code image.
                                     Example: 'hello_world_qr.png'
    """
    try:
        print(f"Encoding Python script: '{python_script_string[:50]}...' into {output_image_path}")
        
        # Create QR code instance
        qr = qrcode.QRCode(
            version=None,  # Let the library choose the version based on data size
            error_correction=qrcode.constants.ERROR_CORRECT_L, # L = Low (7% correction)
            box_size=10,    # Size of each box in pixels
            border=4,       # Thickness of the border (in boxes)
        )
        
        # Add data (the Python script string)
        qr.add_data(python_script_string)
        qr.make(fit=True)
        
        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save the image
        img.save(output_image_path)
        print(f"Successfully saved QR code to {output_image_path}")
        
    except Exception as e:
        print(f"Error generating QR code: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python qr_script_encoder.py \"<python_script_string>\" <output_image_filename.png>")
        print("Example: python qr_script_encoder.py \"print('Hello, World!')\" hello_world_qr.png")
        sys.exit(1)
    
    script_to_encode = sys.argv[1]
    output_filename = sys.argv[2]
    
    # Ensure the output filename has a .png extension if not provided
    if not output_filename.lower().endswith('.png'):
        output_filename += '.png'
        
    # For simplicity, save in the same directory as the script
    # In a more structured project, this might go to a 'generated_qrs' subdirectory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    full_output_path = os.path.join(script_dir, output_filename)
        
    generate_python_script_qr(script_to_encode, full_output_path)
