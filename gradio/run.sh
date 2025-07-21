#!/bin/bash

# Qwen2.5-VL Gradio App Launcher

echo "🚀 Starting Qwen2.5-VL Gradio Interface..."
echo "📦 Installing/Updating dependencies..."

# Install requirements
pip install -r requirements.txt

echo ""
echo "🔥 Launching Gradio app..."
echo "🌐 The app will be available at: http://localhost:7860"
echo "⏹️  Press Ctrl+C to stop the application"
echo "=================================================="

# Run the Gradio app
python run_app.py
