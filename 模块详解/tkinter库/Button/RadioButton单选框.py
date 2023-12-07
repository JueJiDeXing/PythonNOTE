import tkinter as tk

window = tk.Tk()

window.title("radio button")
window.geometry("500x300")

var = tk.StringVar()  # 获取选项值


def select():
    print(f'get {var.get()}')


r1 = tk.Radiobutton(window, text="A", variable=var, value=1, command=select)
r1.pack()
r2 = tk.Radiobutton(window, text="B", variable=var, value=2, command=select)
r2.pack()

window.mainloop()
