import gradio as gr

def test_function():
    return "Hello, Gradio!"

iface = gr.Interface(
    fn=test_function,
    inputs=[],
    outputs="text",
    title="Test Interface",
    description="This is a test to see if Gradio runs correctly."
)

if __name__ == "__main__":
    iface.launch()
