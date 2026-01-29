#!/bin/sh
echo "Testing available commands..."
echo "Current directory: $PWD"
echo "Available space:"
/bin/df -h /
echo "Shell: $SHELL"
echo "PATH: $PATH"
