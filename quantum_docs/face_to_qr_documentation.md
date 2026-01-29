# Face Image to QR Code Integration

This system allows encoding a facial image into a QR code and subsequently decoding and displaying it.

## 1. QR Code Generation (`generate_face_qr.py`)

This script takes an image file as input, processes it, and encodes it into a QR code.

**Features:**
-   **Image Input**: Accepts a path to an image file (e.g., JPEG, PNG).
-   **Processing**: 
    -   Resizes the image to a small, configurable dimension (default 96x96 pixels) to manage data size.
    -   Converts the image to grayscale to further reduce data.
    -   Encodes the processed image as PNG bytes.
-   **Base64 Encoding**: The image bytes are base64 encoded to be safely embedded in a JSON payload.
-   **JSON Payload**: The base64 image string is wrapped in a JSON structure with `task_type: "display_face_image"` and other metadata like `task_id`, phi-harmonic `timestamp`, original filename, processed size, and image format.
-   **QR Code Output**: Generates a QR code image (`.png`) containing this JSON payload.

**Usage:**
```bash
python generate_face_qr.py --image /path/to/your_face.jpg --output my_face_qr.png --size_px 64
```
-   `--image`: (Required) Path to the input image.
-   `--output`: (Optional) Path to save the generated QR code. Defaults to `user_face_qr.png`.
-   `--size_px`: (Optional) The width and height in pixels for the downscaled image. Defaults to 96. Smaller sizes result in smaller QR codes but lower image quality.

## 2. QR Code Task Worker (`qr_task_worker_from_file.py` - To Be Updated)

The `qr_task_worker_from_file.py` script will be updated to handle the `display_face_image` task type.

**Functionality (Proposed):**
-   **Task Detection**: Identifies tasks with `"task_type": "display_face_image"`.
-   **Data Extraction**: Retrieves the `image_data_base64` string from the payload.
-   **Decoding**: Base64 decodes the string back into image bytes.
-   **Image Reconstruction**: Loads the image bytes using Pillow.
-   **Output**: Saves the reconstructed image to a file (e.g., `decoded_face_[timestamp].png`) and prints the file path to the console.

## 3. Data Flow

1.  User provides an image to `generate_face_qr.py`.
2.  The script processes the image (resize, grayscale, PNG format) and base64 encodes it.
3.  A JSON payload containing the base64 image data and task type `display_face_image` is created.
4.  This JSON is encoded into a QR code image.
5.  The `qr_task_worker_from_file.py` (when it processes this QR code):
    a.  Parses the JSON payload.
    b.  Identifies the `display_face_image` task.
    c.  Decodes the base64 data.
    d.  Saves the image and outputs its path.

## Important Considerations

-   **QR Code Capacity**: The primary limitation is the data capacity of QR codes. Larger images or higher fidelity (e.g., color, less compression) will result in QR codes that are too dense to be practical or decodable. The current approach uses resizing, grayscaling, and PNG compression (via Pillow) to manage this.
-   **Image Quality**: The reconstructed image will be small and grayscale due to the necessary processing.
-   **Error Correction**: The QR code generation uses medium error correction (`ERROR_CORRECT_M`) as a balance between data capacity and robustness.
