import gradio as gr
import random

def random_name():
    names = ["毛鑫", "王艺芸", "赵启", "侯绍伟", "董鉴欣"]
    return random.choice(names)

iface = gr.Interface(
    fn=random_name,
    inputs=None,  # 不需要输入
    outputs="text",
    title="Random Name Selector",
    description="Click 'Random' to select a name randomly from the list.",
    live=True  # 使用 live=True 来自动触发函数执行
)

# 添加一个按钮，当点击时，触发 random_name 函数
iface.add_component(gr.components.Button("Random"), "output")

if __name__ == "__main__":
    iface.launch()
