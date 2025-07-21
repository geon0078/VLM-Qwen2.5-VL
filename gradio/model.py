"""
Qwen2.5-VL Model wrapper for Gradio interface
"""

from transformers import Qwen2_5_VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info
from config import MODEL_NAME, MAX_NEW_TOKENS
import torch

class Qwen2_5VLChat:
    def __init__(self):
        self.model = None
        self.processor = None
        self.load_model()
    
    def load_model(self):
        """Load the Qwen2.5-VL model and processor"""
        print("🔄 Loading Qwen2.5-VL model...")
        
        # Load the model on the available device(s)
        self.model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
            MODEL_NAME, 
            torch_dtype="auto", 
            device_map="auto"
        )
        
        # Load processor
        self.processor = AutoProcessor.from_pretrained(MODEL_NAME)
        
        print("✅ Model loaded successfully!")
    
    def generate_response(self, image, text_input):
        """Generate response from image and text input"""
        if image is None:
            return "❌ Please upload an image."
        
        if not text_input.strip():
            text_input = "Describe this image."
        
        try:
            # Prepare messages in the required format
            messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image",
                            "image": image,
                        },
                        {"type": "text", "text": text_input},
                    ],
                }
            ]
            
            # Preparation for inference
            text = self.processor.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
            image_inputs, video_inputs = process_vision_info(messages)
            inputs = self.processor(
                text=[text],
                images=image_inputs,
                videos=video_inputs,
                padding=True,
                return_tensors="pt",
            )
            inputs = inputs.to("cuda")
            
            # Inference: Generation of the output
            generated_ids = self.model.generate(**inputs, max_new_tokens=MAX_NEW_TOKENS)
            generated_ids_trimmed = [
                out_ids[len(in_ids) :] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
            ]
            output_text = self.processor.batch_decode(
                generated_ids_trimmed, skip_special_tokens=True, clean_up_tokenization_spaces=False
            )
            
            return output_text[0] if output_text else "No response generated."
            
        except Exception as e:
            return f"❌ Error generating response: {str(e)}"
