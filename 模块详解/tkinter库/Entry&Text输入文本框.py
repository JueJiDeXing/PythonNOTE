import tkinter as tk

window = tk.Tk()
window.title("This is demo2")
window.geometry("500x300")

# 显示明文
e1 = tk.Entry(window, show=None, font=("Arial", 14))
# 显示密文
e2 = tk.Entry(window, show="*", font=("Arial", 14))

e1.pack()
e2.pack()
##########################

e = tk.Entry(window, show=None)  # 输入框
e.pack()


def insert_point():
    var = e.get()
    t.insert("insert", var)


def insert_end():
    var = e.get()
    t.insert("end", var)
    # 插入文本后是窗口聚焦到末尾
    t.see("end")


b1 = tk.Button(window, text="insert", width=10, height=1, command=insert_point)
b2 = tk.Button(window, text="insert end", width=10, height=1, command=insert_end)

b1.pack()
b2.pack()

# 创建并放置一个多行文本框text用以显示，指定height=3为文本框是三个字符高度
t = tk.Text(window, height=3)
t.pack()

#
window.mainloop()
