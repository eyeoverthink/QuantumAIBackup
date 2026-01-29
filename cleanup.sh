#!/bin/bash

# Simple cleanup script to free disk space
echo "Starting disk cleanup..."

# Try to remove large temporary directories
echo "Removing temporary files..."

# Clean deep_learning checkpoints and history
if [ -d "/Users/vaughnscott/CascadeProjects/QuantumAI/deep_learning/checkpoints" ]; then
  echo "Cleaning checkpoints directory..."
  /bin/rm -rf /Users/vaughnscott/CascadeProjects/QuantumAI/deep_learning/checkpoints/*
fi

if [ -d "/Users/vaughnscott/CascadeProjects/QuantumAI/deep_learning/evolution_history" ]; then
  echo "Cleaning evolution history directory..."
  /bin/rm -rf /Users/vaughnscott/CascadeProjects/QuantumAI/deep_learning/evolution_history/*
fi

# Clean brain data directories
if [ -d "/Users/vaughnscott/CascadeProjects/QuantumAI/brain_metrics" ]; then
  echo "Cleaning brain metrics directory..."
  /bin/rm -rf /Users/vaughnscott/CascadeProjects/QuantumAI/brain_metrics/*
fi

if [ -d "/Users/vaughnscott/CascadeProjects/QuantumAI/brain_states" ]; then
  echo "Cleaning brain states directory..."
  /bin/rm -rf /Users/vaughnscott/CascadeProjects/QuantumAI/brain_states/*
fi

# Clean agent data
if [ -d "/Users/vaughnscott/CascadeProjects/QuantumAI/agent_data" ]; then
  echo "Cleaning agent data directory..."
  /bin/rm -rf /Users/vaughnscott/CascadeProjects/QuantumAI/agent_data/*
fi

echo "Cleanup completed. You should now have enough space to restore your files."
