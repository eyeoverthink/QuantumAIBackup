#!/bin/bash

# Run Face QR Test with Aggressive Optimization
# This script runs the face image to QR code test with more aggressive optimization settings
# to ensure the QR code fits within version limits (≤ 40)

# Note: If you get a "permission denied" error, run this command first:
# chmod +x run_face_qr_test.sh

# Make the extension file executable if it exists
if [ -f "qr_task_worker_extension.py" ]; then
    chmod +x qr_task_worker_extension.py
    echo "Made qr_task_worker_extension.py executable"
fi

# Make this script executable
chmod +x "$0"

echo "=== Face Image to QR Code Test with Aggressive Optimization ==="
echo "Using: 24px size, 50% JPEG quality"

# Run the test with aggressive optimization
python test_face_qr_system.py --image face.jpg --size_px 24 --jpeg_quality 50
RESULT1=$?

# If that fails, try more aggressive settings
if [ $RESULT1 -ne 0 ]; then
    echo -e "\n\n=== First attempt failed, trying with more aggressive settings ==="
    echo "Using: 16px size, 40% JPEG quality"
    python test_face_qr_system.py --image face.jpg --size_px 16 --jpeg_quality 40
    RESULT2=$?
    
    # If that still fails, try the most aggressive settings
    if [ $RESULT2 -ne 0 ]; then
        echo -e "\n\n=== Second attempt failed, trying with most aggressive settings ==="
        echo "Using: 12px size, 30% JPEG quality"
        python test_face_qr_system.py --image face.jpg --size_px 12 --jpeg_quality 30
        RESULT3=$?
        
        if [ $RESULT3 -ne 0 ]; then
            echo -e "\n\n=== All attempts failed ==="
            echo "Try manually adjusting the settings or using a smaller face image"
            exit 1
        fi
    fi
fi

echo -e "\nTest complete successfully!"
exit 0
