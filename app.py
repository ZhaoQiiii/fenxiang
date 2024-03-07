import gradio as gr
import random

def random_name():
    names = ["毛鑫", "王艺芸", "赵启", "侯绍伟", "董鉴欣"]
    return random.choice(names)

iface = gr.Interface(
    fn=random_name,
    inputs=gr.components.Button(label="Random"),
    outputs="text",
    title="Random Name Selector",
    description="Click 'Random' to select a name randomly from the list."
)

if __name__ == "__main__":
    iface.launch()
