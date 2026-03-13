import tkinter as tk

from core.security_analyzer import analyze_password
from core.password_generator import generate_passphrase


def analyze():

    password = entry.get()

    result = analyze_password(password)

    output_text.set(
        f"""
Entropy: {result['entropy']}
Strength: {result['strength']}
Patterns: {result['patterns'] if result['patterns'] else 'None'}
Breach: {'FOUND' if result['breach'] else 'Not Found'}
"""
    )


def generate():

    password = generate_passphrase()

    entry.delete(0, tk.END)
    entry.insert(0, password)


# 创建窗口
root = tk.Tk()
root.title("Password Security Analyzer")
root.geometry("400x300")


# 标题
title = tk.Label(root, text="Password Security Analyzer", font=("Arial", 16))
title.pack(pady=10)


# 输入框
entry = tk.Entry(root, width=30)
entry.pack(pady=10)


# 分析按钮
analyze_button = tk.Button(root, text="Analyze Password", command=analyze)
analyze_button.pack(pady=5)


# 生成按钮
generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.pack(pady=5)


# 输出文本
output_text = tk.StringVar()

output_label = tk.Label(root, textvariable=output_text, justify="left")
output_label.pack(pady=20)


root.mainloop()