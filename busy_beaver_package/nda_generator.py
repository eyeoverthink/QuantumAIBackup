# nda_generator.py

"""
NDA Generator
=============
Auto-generates Non-Disclosure Agreements (NDAs) with SHA-256 fingerprinting.
"""

import hashlib
import time

TEMPLATE = """
NON-DISCLOSURE AGREEMENT (NDA)

This Agreement is made on {date} between:

1. Vaughn Scott ("Discloser")
2. {recipient_name} ("Recipient")

The Recipient agrees not to disclose, reproduce, or distribute any proprietary information related to the Standalone Busy Beaver Calculator.

This agreement covers:
- Intellectual Property described in Blockchain Transaction #414023B3F1C5104129F847B498DAD55D12CD9F49C07F01C07E497BC0E8F5ACD2
- SHA-256 Protected Asset: 3d17340edd0f2c746477cc1c7f31638e2f6b8d3b553b926f7f193e9486699881

Signed:

Discloser: Vaughn Scott
Recipient: {recipient_name}
Date: {date}
"""

def generate_nda(recipient_name: str):
    date = time.strftime("%Y-%m-%d")
    nda_text = TEMPLATE.format(recipient_name=recipient_name, date=date)
    filename = f"NDA_{recipient_name.replace(' ', '_')}_{date}.txt"

    with open(filename, "w") as f:
        f.write(nda_text)

    print(f"✅ NDA generated: {filename}")
    print(f"SHA-256 Fingerprint: {hashlib.sha256(nda_text.encode()).hexdigest()}")

if __name__ == "__main__":
    name = input("Enter the recipient's full name: ")
    generate_nda(name)



# verify_integrity.py

"""
Integrity Verification Tool
===========================
Verifies all critical project files by SHA-256 hashes.
"""

import hashlib

# Define original SHA256 fingerprints
EXPECTED_HASHES = {
    "standalone_busy_beaver.py": "3d17340edd0f2c746477cc1c7f31638e2f6b8d3b553b926f7f193e9486699881"
}

def calculate_sha256(filename):
    sha256 = hashlib.sha256()
    with open(filename, "rb") as f:
        while chunk := f.read(4096):
            sha256.update(chunk)
    return sha256.hexdigest()

def verify_files():
    for file, expected_hash in EXPECTED_HASHES.items():
        try:
            computed_hash = calculate_sha256(file)
            if computed_hash == expected_hash:
                print(f"✅ {file}: OK")
            else:
                print(f"❌ {file}: HASH MISMATCH!")
        except FileNotFoundError:
            print(f"⚠️  {file}: NOT FOUND")

if __name__ == "__main__":
    verify_files()

