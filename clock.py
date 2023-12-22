import time
import tkinter as tk

def start_timer():
    countdown(int(entry.get()) * 60)

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timeformat)
        time.sleep(1)
        seconds -= 1
    label.config(text='00:00')

# 创建主窗口
root = tk.Tk()
root.title("专注时钟")

# 添加标签
label = tk.Label(root, text="00:00", font=("Helvetica", 48))
label.pack(pady=10)

# 添加输入框
entry = tk.Entry(root, font=("Helvetica", 16))
entry.pack(pady=10)

# 添加开始按钮
start_button = tk.Button(root, text="开始", command=start_timer)
start_button.pack(pady=10)

# 运行主循环
root.mainloop()
