import gradio as gr
import random

def random_name():
    names = ["毛鑫", "王艺芸", "赵启", "侯绍伟", "董鉴欣"]
    return random.choice(names)

# 定义Gradio界面
iface = gr.Interface(
    fn=random_name,
    inputs=None,
    outputs="text",
    title="Random Name Selector",
    description="Click 'Random' to select a name randomly from the list.",
    # 添加一个动作按钮，用户点击时触发random_name函数
    live=False
).add_component(
    gr.components.Button("Random"), 
    "output" # 指定点击按钮后的输出位置
)

if __name__ == "__main__":
    iface.launch()
