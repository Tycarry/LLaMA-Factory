# -*- coding: utf-8 -*-
"""
@file: deploy.py
@author： ty
@time: 2024/11/25 17:16
"""
import os
import sys

# 获取当前工作目录
current_path = os.getcwd()

# 拼接当前工作目录和src目录的路径
src_path = os.path.join(current_path, 'src')

# 将src目录的路径添加到sys.path的开头
sys.path.insert(0, src_path)

from llamafactory.chat import ChatModel
from llamafactory.extras.misc import torch_gc

torch_gc()
args = dict(
    model_name_or_path="unsloth/Qwen2-7B-Instruct-bnb-4bit",  # 使用 4 bit量化版 Qwen2-7B-Instruct 模型
    adapter_name_or_path="qwen2_lora",  # 加载之前保存的 LoRA 适配器
    template="qwen",  # 和训练保持一致
    finetuning_type="lora",  # 和训练保持一致
)
chat_model = ChatModel(args)

messages = []
print("使用 `clear` 清除对话历史，使用 `exit` 退出程序。")
while True:
    query = input("\n用户: ")
    if query.strip() == "exit":
        break
    if query.strip() == "clear":
        messages = []
        torch_gc()
        print("对话历史已清除")
        continue

    messages.append({"role": "user", "content": query})
    print("BajiGo: ", end="", flush=True)

    response = ""
    for new_text in chat_model.stream_chat(messages):
        print(new_text, end="", flush=True)
        response += new_text
    print()
    messages.append({"role": "assistant", "content": response})
