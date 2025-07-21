"""
Configuration settings for Qwen2.5-VL Gradio interface
"""

# Model settings
MODEL_NAME = "Qwen/Qwen2.5-VL-7B-Instruct"
MAX_NEW_TOKENS = 128

# Gradio interface settings
SERVER_NAME = "0.0.0.0"
SERVER_PORT = 7860
SHARE = False
DEBUG = True

# UI settings
THEME = "soft"
IMAGE_HEIGHT = 400
OUTPUT_LINES = 15
OUTPUT_MAX_LINES = 20

# Example questions
EXAMPLE_QUESTIONS = [
    "Describe this image in detail",
    "What objects do you see in this image?",
    "What is the main subject of this image?",
    "What colors are prominent in this image?",
    "What is happening in this scene?",
    "Can you identify any text in this image?",
    "What is the mood or atmosphere of this image?",
    "Are there any people in this image? What are they doing?"
]
