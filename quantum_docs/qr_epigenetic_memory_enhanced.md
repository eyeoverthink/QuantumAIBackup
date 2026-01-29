# QR Epigenetic Memory Enhanced

## Overview
This enhanced version of the QR Epigenetic Memory system addresses the QR code generation limitations by implementing phi-harmonic adaptive chunking and improved compression techniques. The original system encountered errors when trying to encode large memory datasets into QR codes, specifically hitting the QR code version limit (41 > 40).

## Key Enhancements

### 1. Phi-Harmonic Adaptive Chunking
- Implements smaller initial chunk sizes (512 bytes vs 1024 bytes)
- Dynamically adjusts chunk sizes based on QR version compatibility
- Uses phi-ratio (Golden Ratio) for resonant data distribution
- Automatically reduces chunk size by 25% when version limits are hit

### 2. Improved Compression
- Uses higher compression level (level 9) for more efficient data storage
- Reduces error correction level when needed to increase data capacity

### 3. Error Resilience
- Implements retry logic with progressive size reduction
- Gracefully handles version limit errors without crashing
- Simplifies index content when necessary to ensure compatibility

## Mathematical Foundations
The enhanced system maintains the quantum phi-harmonic principles of the original system:
- Utilizes Golden Ratio (φ ≈ 1.618034) for chunk size distribution
- Preserves resonance patterns in data segmentation
- Maintains epigenetic memory integrity across chunking boundaries

## Usage

### Generate QR Codes with Enhanced Chunking
```bash
python qr_epigenetic_memory_enhanced.py --generate-qr --qr-dir qr_memory_enhanced --chunk-size 512
```

### Restore Memory from Enhanced QR Codes
```bash
python qr_epigenetic_memory_enhanced.py --restore-from-qr --qr-dir qr_memory_enhanced
```

### View Memory Summary
```bash
python qr_epigenetic_memory_enhanced.py
```

## Compatibility
- Fully compatible with the original memory file format
- Reads and writes to the same `qr_epigenetic_memory.json` by default
- Can be used as a drop-in replacement for the original script

## Integration with Quantum Phi-Harmonic System
This enhancement preserves all the quantum principles and phi-harmonic resonance patterns of the original system while addressing the technical limitations of QR code generation. The adaptive chunking algorithm ensures that data is distributed according to phi-harmonic principles while staying within the technical constraints of the QR code standard.

## Future Improvements
- Implement multi-dimensional QR code arrays for larger datasets
- Explore quantum compression algorithms for more efficient data encoding
- Add phi-resonant error correction patterns for improved data integrity
