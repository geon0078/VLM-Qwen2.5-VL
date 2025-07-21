import gradio as gr
from model import Qwen2_5VLChat
from config import *
from PIL import Image
import numpy as np

def create_gradio_interface():
    """Create and configure the Gradio interface"""
    
    # Initialize the chat model
    qwen_chat = Qwen2_5VLChat()
    
    # Create Gradio interface
    with gr.Blocks(title="Qwen2.5-VL 챗", theme=getattr(gr.themes, THEME.capitalize())()) as demo:
        gr.Markdown(
            """
            # 🤖 Qwen2.5-VL 챗 인터페이스
            
            이미지를 업로드하고 질문을 해보세요! 모델이 이미지를 설명하고, 질문에 답변하며, 시각적 대화를 할 수 있습니다.
            """
        )
        
        with gr.Row():
            with gr.Column(scale=1):
                image_input = gr.Image(
                    type="pil",
                    label="이미지 업로드",
                    height=IMAGE_HEIGHT
                )
                
                text_input = gr.Textbox(
                    label="질문 입력",
                    placeholder="이미지에 대해 궁금한 점을 입력하세요... (예: '이 이미지를 설명해줘', '무엇이 보이나요?')",
                    lines=3
                )
                
                submit_btn = gr.Button("답변 생성", variant="primary", size="lg")
                clear_btn = gr.Button("초기화", variant="secondary")
                
            with gr.Column(scale=1):
                output_text = gr.Textbox(
                    label="모델 답변",
                    lines=OUTPUT_LINES,
                    max_lines=OUTPUT_MAX_LINES,
                    show_copy_button=True
                )
        
        # 예시 질문 섹션
        gr.Markdown("### 📝 예시 질문:")
        examples_text = "\n".join([f"- {q}" for q in EXAMPLE_QUESTIONS])
        gr.Markdown(examples_text)
        
        # 이벤트 핸들러
        submit_btn.click(
            fn=qwen_chat.generate_response,
            inputs=[image_input, text_input],
            outputs=[output_text]
        )
        
        text_input.submit(
            fn=qwen_chat.generate_response,
            inputs=[image_input, text_input],
            outputs=[output_text]
        )
        
        clear_btn.click(
            fn=lambda: [None, "", ""],
            outputs=[image_input, text_input, output_text]
        )
    
    return demo

def main():
    """Main function to launch the Gradio app"""
    demo = create_gradio_interface()
    
    # Launch the app
    demo.launch(
        server_name=SERVER_NAME,  # Allow external access
        server_port=SERVER_PORT,  # Default Gradio port
        share=SHARE,              # Set to True if you want a public link
        debug=DEBUG,
        show_error=True
    )


if __name__ == "__main__":
    main()