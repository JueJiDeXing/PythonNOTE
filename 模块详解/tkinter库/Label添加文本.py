import tkinter as tk

# 创建窗口
window = tk.Tk()

# 设置窗口标题
window.title("This is demo")
# 设置窗口尺寸
window.geometry("500x300")  # 设置窗口尺寸 长x宽


##### 新增
l = tk.Label(window, text="This is a demo", bg="green", font=("Arial", 12), width=20, height=3)
l.pack()











#####
# 窗口主循环
window.mainloop()
