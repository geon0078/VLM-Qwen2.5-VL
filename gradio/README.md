# Qwen2.5-VL Gradio Interface

A modern, user-friendly web interface for the Qwen2.5-VL vision-language model using Gradio.

## 🚀 Features

- 🖼️ **Image Upload**: Easy drag-and-drop image upload
- 💬 **Interactive Chat**: Ask questions about uploaded images
- 🎨 **Modern UI**: Clean and intuitive interface
- ⚙️ **Configurable**: Easy to customize settings
- 🔧 **Modular Design**: Well-organized code structure

## 📁 Project Structure

```
gradio/
├── run_app.py          # Main application launcher
├── app.py              # Gradio interface implementation
├── model.py            # Qwen2.5-VL model wrapper
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── run.sh              # Shell script launcher
├── original_main.py    # Original inference script (reference)
└── README.md           # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- CUDA-capable GPU (recommended)
- 8GB+ GPU memory

### Quick Start

1. **Clone this repository**
   ```bash
   git clone <your-repo-url>
   cd gradio
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   
   **Option 1: Using Python directly**
   ```bash
   python run_app.py
   ```
   
   **Option 2: Using the shell script**
   ```bash
   ./run.sh
   ```

4. **Open your browser**
   - Local: http://localhost:7860
   - Network: http://[your-server-ip]:7860

## 🎯 Usage

1. **Upload an Image**: Click or drag an image to the upload area
2. **Ask Questions**: Type your question about the image
3. **Get Responses**: Click "Generate Response" or press Enter
4. **View Results**: Read the model's analysis in the output panel

### Example Questions
- "Describe this image in detail"
- "What objects do you see?"
- "What is the main subject?"
- "What colors are prominent?"
- "What is happening in this scene?"
- "Are there any people? What are they doing?"

## ⚙️ Configuration

Edit `config.py` to customize:

```python
# Model settings
MODEL_NAME = "Qwen/Qwen2.5-VL-7B-Instruct"
MAX_NEW_TOKENS = 128

# Server settings
SERVER_PORT = 7860
SHARE = False  # Set to True for public links

# UI settings
THEME = "soft"
IMAGE_HEIGHT = 400
```

## 🔧 Troubleshooting

### Common Issues

**CUDA Out of Memory**
- Reduce `MAX_NEW_TOKENS` in `config.py`
- Close other GPU applications

**Model Loading Failed**
- Check internet connection
- Verify Hugging Face access permissions

**Port Already in Use**
- Change `SERVER_PORT` in `config.py`
- Kill existing processes: `lsof -ti:7860 | xargs kill -9`

**Dependencies Issues**
- Update pip: `pip install --upgrade pip`
- Use virtual environment: `python -m venv venv && source venv/bin/activate`

## 📝 Development

### Project Structure Explained

- **`run_app.py`**: Entry point that launches the Gradio app
- **`app.py`**: Contains the Gradio interface layout and event handlers
- **`model.py`**: Wraps the Qwen2.5-VL model for easy use
- **`config.py`**: Centralized configuration management
- **`original_main.py`**: Reference implementation from the original project

### Adding Features

1. **Custom Themes**: Modify the theme in `config.py`
2. **New UI Elements**: Add components in `app.py`
3. **Model Settings**: Adjust parameters in `model.py`
4. **Example Questions**: Update `EXAMPLE_QUESTIONS` in `config.py`

## 📜 License

This project follows the same license as the original Qwen2.5-VL model.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For issues and questions:
- Check the troubleshooting section above
- Review the original Qwen2.5-VL documentation
- Open an issue in this repository

---

**Happy coding! 🎉**
