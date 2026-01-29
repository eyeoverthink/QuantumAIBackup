#!/bin/bash
# φ-Dimensional Temporal Paradox Test
# Runs both ψ₁ and ψ₂ nodes to demonstrate noncausal communication
# φ^∞ © 2025 Vaughn Scott - All Rights Reserved in All Realities

echo "=== φ-DIMENSIONAL TEMPORAL PARADOX TEST ==="
echo "This test will demonstrate noncausal communication through the φ-Net temporal loop"
echo "ψ₁ will receive a message from ψ₂ before ψ₂ sends it"
echo

# Ensure log directory exists
mkdir -p phi_temporal_logs

# Make sure our script is executable
chmod +x phi_temporal_paradox.py

# Clear previous logs
echo "Clearing previous logs..."
rm -f phi_temporal_logs/phi_temporal_psi*

# Run ψ₁ node in a separate terminal
echo "Starting ψ₁ (receiver) in a new terminal..."
osascript -e 'tell application "Terminal" to do script "cd \"'$(pwd)'\" && python phi_temporal_paradox.py --node psi1"'

# Wait a moment before starting ψ₂
echo "Waiting 3 seconds before starting ψ₂..."
sleep 3

# Run ψ₂ node in this terminal
echo "Starting ψ₂ (sender) in this terminal..."
python phi_temporal_paradox.py --node psi2

# Note: When complete, check the logs in phi_temporal_logs/
echo
echo "When complete, check the timestamp trails in phi_temporal_logs/"
echo "Look for evidence of the paradox where ψ₁ received the message before ψ₂ sent it"
