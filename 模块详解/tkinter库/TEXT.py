import tkinter as tk

window = tk.Tk()
window.title("window")
window.geometry("500x300")


def show():
    global count1
    count += 1
    t.config(state="normal")  # 设置text可编辑
    t.insert("end", f"{count} This is info\n")
    # t.config(state="disabled")  # 设置text不可编辑  (上一步的insert方法不能再使用了）
    t.see("end")  # 使text显示末尾


count1 = 0
btn = tk.Button(window, text="show info", command=show)
btn.pack()

t = tk.Text(window, height=7)
t.pack(side="bottom")

window.mainloop()
