"""
QHRC Levitation Animation Generator
Patent #19/071,497
"""

import imageio.v2 as imageio
import glob

# Load all frames
frames = []
for filename in sorted(glob.glob('levitation_*.png')):
    frames.append(imageio.imread(filename))

# Create GIF with φ-based timing
duration = 1.618034 / len(frames)  # φ-based frame duration
imageio.mimsave('qhrc_levitation.gif', frames, duration=duration)
