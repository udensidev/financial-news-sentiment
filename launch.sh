#!/bin/bash

# Clear the terminal for a fresh view
clear

# Print header
echo "🚀 Launching News Sentiment Analysis Pipeline 🚀"
echo "--------------------------------------------"

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
