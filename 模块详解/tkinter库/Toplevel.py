from tkinter import *
from time import strftime


def show(to_text, *args, ):
    to_text.config(state="normal")
    to_text.insert("end", f"{strftime('[%m-%d %H:%M:%S]')} {' '.join(map(lambda s: str(s), args))}\n")
    to_text.config(state="disabled")
    to_text.see("end")


def insert():
    show(T, "insert", var.get())
    var.set("")


def create():
    global var, T

    top = Toplevel()
    top.title('window2')
    top.geometry("400x300")
    top.resizable(width=False, height=False)

    T = Text(top, height=7)
    T.config(state="disabled")
    T.place(x=0, y=0)
    Entry(top, textvariable=var, width=30).place(x=45, y=100)
    Button(top, text="do", width=5, command=insert).place(x=290, y=100)


if __name__ == "__main__":
    window = Tk()
    window.title("window")
    var = StringVar()
    T = None
    Button(window, text='创建顶级窗口', command=create).pack()
    window.mainloop()

