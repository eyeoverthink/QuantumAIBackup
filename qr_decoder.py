from pyzbar.pyzbar import decode
from PIL import Image
import json

img = Image.open("/Users/vaughnscott/CascadeProjects/QuantumAI/hello_world_qr.png")
data = decode(img)

for obj in data:
    text = obj.data.decode('utf-8')
    try:
        parsed = json.loads(text)
        print(json.dumps(parsed, indent=4))
    except:
        print("Raw text:", text)