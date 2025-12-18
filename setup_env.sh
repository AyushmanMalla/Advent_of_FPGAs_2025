#!/bin/bash

echo "Setting up the environment..."

# Check for Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 could not be found. Please install Python3."
    exit 1
fi

# Install Python requirements
echo "Installing Python dependencies from requirements.txt..."
pip install -r requirements.txt

# Install Icarus Verilog
echo "Checking for Icarus Verilog..."
if ! command -v iverilog &> /dev/null; then
    echo "Icarus Verilog not found. Installing..."
    if [ -x "$(command -v apt)" ]; then
        sudo apt update
        sudo apt install -y iverilog
    elif [ -x "$(command -v dnf)" ]; then
        sudo dnf install -y iverilog
    elif [ -x "$(command -v brew)" ]; then
        brew install iverilog
    elif [ -x "$(command -v pacman)" ]; then
        sudo pacman -S iverilog
    else
        echo "Supported package manager (apt, dnf, brew, pacman) not found. Please install Icarus Verilog manually."
        exit 1
    fi
else
    echo "Icarus Verilog is already installed."
fi

echo "Setup complete!"
