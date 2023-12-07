import tkinter as tk


def quit_new():
    global new_w
    windows.remove(new_w)
    new_w.destroy()
    new_w = None


def quit_all():
    for w in windows:
        w.destroy()


def new_window():
    global new_w
    if not new_w:
        new_w = tk.Tk()
        windows.insert(0, new_w)

        new_w.title("new window")
        new_w.geometry("400x300")
        tk.Label(new_w, text="This is new window", bg="red").pack()
        new_w.protocol("WM_DELETE_WINDOW", quit_new)
        new_w.mainloop()


windows = []
window = tk.Tk()
new_w = None  # 新窗口
windows.append(window)

window.title("window")
window.geometry("500x300")

tk.Button(window, text="new window", command=new_window).pack()

window.protocol("WM_DELETE_WINDOW", quit_all)
window.mainloop()
