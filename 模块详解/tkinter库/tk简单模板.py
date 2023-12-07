import tkinter as tk

# 创建窗口
window = tk.Tk(className="绝迹的星")#可传参设置标题,也可单独写window.title("绝迹的星")

# 设置窗口尺寸
window.geometry("500x300")  # 设置窗口尺寸 长x宽
# window.resizable(width=False, height=False) # 设置窗口大小无法改变


# 窗口主循环
window.mainloop()
