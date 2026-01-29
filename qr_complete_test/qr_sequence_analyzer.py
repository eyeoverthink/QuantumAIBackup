#!/usr/bin/env python3
"""
QR Sequence Analyzer
By Vaughn Scott & Cascade

Non-intrusive helper utility (lego-style) that decodes a generated QR flip-book
sequence, reconstructs the original payload(s), and optionally executes Python
content through the existing qr_task_executor sandbox.

This file DOES NOT modify or replace any core modules; it simply imports them.
"""

import os
import sys
import json
import base64
import zlib
import argparse
from pathlib import Path
from typing import List, Dict, Any

from PIL import Image
import pyzbar.pyzbar as pyzbar

# Local helper – use the same chunker implementation for (de)compression
from qr_sequence_chunker import QRSequenceChunker
# Task sandbox for safe execution
from qr_task_executor import QRTaskExecutor

chunker = QRSequenceChunker()

def decode_frame(img_path: Path) -> str:
    """Return raw (possibly compressed / encrypted) QR payload from an image."""
    decoded = pyzbar.decode(Image.open(img_path))
    if not decoded:
        raise ValueError(f"No QR code found in {img_path}")
    return decoded[0].data.decode("utf-8")

def decrypt_if_needed(raw: str) -> str:
    """Handle ENCRYPTED:<b64> prefix if present. Uses same key file as other tools."""
    if not raw.startswith("ENCRYPTED:"):
        return raw
    payload_enc = base64.b64decode(raw.split(":", 1)[1])
    from cryptography.fernet import Fernet
    key_path = Path("qr_encryption.key")
    if not key_path.exists():
        raise RuntimeError("Encryption key not found; cannot decrypt.")
    f = Fernet(key_path.read_bytes())
    return f.decrypt(payload_enc).decode()

def decompress_if_needed(raw: str) -> str:
    """Delegate to QRSequenceChunker for COMPRESSED payloads or plain b64."""
    return chunker.decompress_payload(raw)

def analyse_sequence(seq_dir: Path, execute: bool = False, verbose: bool = True):
    frames = sorted(seq_dir.glob("qr_frame_*.png"))
    if not frames:
        print(f"No frames found in {seq_dir}")
        return

    print(f"\n🔍 Analysing {len(frames)} QR frames in '{seq_dir.name}' …\n")

    executor = QRTaskExecutor(timeout=10) if execute else None

    for img_path in frames:
        try:
            raw = decode_frame(img_path)
            decrypted = decrypt_if_needed(raw)
            payload_json = decompress_if_needed(decrypted)
            try:
                payload: Dict[str, Any] = json.loads(payload_json)
            except json.JSONDecodeError:
                print(f"Frame {img_path.name}: not JSON payload\n   Raw first 120 chars: {payload_json[:120]}…")
                continue
        except Exception as e:
            print(f"⚠️  Failed to decode {img_path.name}: {e}")
            continue

        # Pretty summary
        sid = payload.get("session_id", "-")
        fno = payload.get("frame_number", "-")
        ttype = payload.get("task_type", payload.get("type", "-"))
        print(f"Frame {fno}: task_type={ttype}, session_id={sid}")

        content_display = payload.get("content", "")
        print("   content snippet:")
        for line in content_display.splitlines()[:5]:
            print("      ", line[:120])
        if len(content_display.splitlines()) > 5:
            print("      …")

        # Optional execution
        if execute and ttype == "execute_python":
            print("   ▶ Executing in sandbox …")
            success, stdout, stderr = executor.execute_python(content_display)
            print("   • success:", success)
            if stdout:
                print("   • stdout:\n", stdout.strip())
            if stderr:
                print("   • stderr:\n", stderr.strip())
            print()

    print("\n✅ Analysis complete\n")


def main():
    p = argparse.ArgumentParser(description="Decode & analyse a QR flip-book sequence")
    p.add_argument("sequence_dir", nargs="?", default="qr_sequence", help="Directory with qr_frame_*.png images")
    p.add_argument("--execute", action="store_true", help="Execute python tasks in sandbox")
    args = p.parse_args()

    analyse_sequence(Path(args.sequence_dir), execute=args.execute)

if __name__ == "__main__":
    main()
