#!/bin/bash

# Clear the terminal for a fresh view
clear

# Print header
echo "🚀 Launching News Sentiment Analysis Pipeline 🚀"
echo "--------------------------------------------"

# Step 0: Check Python Version (at least 3.8 recommended)
REQUIRED_PYTHON="3.8"
CURRENT_PYTHON=$(python3 --version 2>&1 | awk '{print $2}')

if [[ "$(printf '%s\n' "$REQUIRED_PYTHON" "$CURRENT_PYTHON" | sort -V | head -n1)" != "$REQUIRED_PYTHON" ]]; then
    echo "❌ Python $REQUIRED_PYTHON or higher is required. You have $CURRENT_PYTHON."
    exit 1
else
    echo "✅ Python version $CURRENT_PYTHON detected."
fi

# Step 0.1: Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip is not installed. Please install pip to proceed."
    exit 1
else
    echo "✅ pip is installed."
fi

# Step 1: Check if requirements are installed
echo "🔍 Checking Python dependencies..."

pip3 install --quiet -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ All dependencies installed successfully."
else
    echo "❌ Failed to install dependencies. Please check your Python environment."
    exit 1
fi

# Step 2: Run the main Python script
echo "⚙️ Running the pipeline..."
python3 src/main.py

# Step 3: Goodbye message
echo "--------------------------------------------"
echo "✅ Pipeline complete!"
