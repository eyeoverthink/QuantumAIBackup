import json
import os
import time
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode

class QuantumGene:
    """Handles the encoding and decoding of the system's state into a QR code.

    This class represents the 'DNA' of the orchestrator, capturing its state
    in a portable and resilient format.
    """

    def __init__(self, state_data: dict):
        self.state_data = state_data
        self.timestamp = int(time.time())
        self.state_data['gene_timestamp'] = self.timestamp

    def encode_to_qr(self, output_dir: str = 'quantum_genes') -> str:
        """Encodes the current state data into a QR code image.

        Args:
            output_dir: The directory to save the QR code image.

        Returns:
            The path to the generated QR code image.
        """
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        json_data = json.dumps(self.state_data, indent=4)
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(json_data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        
        file_path = os.path.join(output_dir, f'qgene_{self.timestamp}.png')
        img.save(file_path)
        return file_path

    @staticmethod
    def decode_from_qr(image_path: str) -> dict:
        """Decodes the state data from a QR code image.

        Args:
            image_path: The path to the QR code image file.

        Returns:
            A dictionary containing the decoded state data.
        """
        try:
            decoded_objects = decode(Image.open(image_path))
            if not decoded_objects:
                raise ValueError("No QR code found in the image.")
            
            json_data = decoded_objects[0].data.decode('utf-8')
            return json.loads(json_data)
        except FileNotFoundError:
            raise FileNotFoundError(f"Gene image not found at {image_path}")
        except Exception as e:
            print(f"Error decoding Quantum Gene: {e}")
            return {}
