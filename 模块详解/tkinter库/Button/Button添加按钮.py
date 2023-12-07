import tkinter as tk

# 创建主窗口
window = tk.Tk()

# 设置窗口标题
window.title("This is demo1")
# 设置窗口尺寸
window.geometry("500x300")
##### 变化
var = tk.StringVar()  # 可变化文本
count1 = 0
l = tk.Label(window, textvariable=var, bg="green", font=("Arial", 12), width=20, height=3)
l.pack()


def hit_me():
    global count1
    count += 1
    var.set(f"you hit me {count}")  # 设置文本
    print(count)


b = tk.Button(window, text="hit me", font=("Arial", 12), width=10, height=1, command=hit_me)  # command调用函数
b.pack()
####
window.mainloop()
