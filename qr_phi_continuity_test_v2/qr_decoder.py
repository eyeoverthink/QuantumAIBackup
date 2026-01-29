from pyzbar.pyzbar import decode
from PIL import Image
import json

img = Image.open("qr_phi_replication/qr_codes/qr_phi_replicator_refactored_gen4_0.293047.png")
data = decode(img)

for obj in data:
    text = obj.data.decode('utf-8')
    try:
        parsed = json.loads(text)
        print(json.dumps(parsed, indent=4))
    except:
        print("Raw text:", text)