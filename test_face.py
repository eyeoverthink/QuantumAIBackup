import numpy as np
from PIL import Image

# Create a test grayscale face image
size = 256
test_face = np.zeros((size, size), dtype=np.uint8)

# Add some basic facial features using phi-based proportions
phi = 1.618034

# Eyes
eye_size = int(size/phi**3)
eye_y = int(size/phi)
left_eye_x = int(size/(phi*2))
right_eye_x = size - left_eye_x

test_face[eye_y-eye_size:eye_y+eye_size, 
         left_eye_x-eye_size:left_eye_x+eye_size] = 200
test_face[eye_y-eye_size:eye_y+eye_size,
         right_eye_x-eye_size:right_eye_x+eye_size] = 200

# Nose
nose_width = int(eye_size*1.5)
nose_height = int(size/phi**2)
nose_x = size//2
nose_y = int(size/phi) + eye_size*2

test_face[nose_y:nose_y+nose_height,
         nose_x-nose_width:nose_x+nose_width] = 150

# Mouth
mouth_width = int(size/phi**2)
mouth_height = int(eye_size*1.2)
mouth_y = int(size/phi) + int(size/phi**2)

test_face[mouth_y:mouth_y+mouth_height,
         size//2-mouth_width:size//2+mouth_width] = 180

# Save the test face
Image.fromarray(test_face).save('face.jpg')
