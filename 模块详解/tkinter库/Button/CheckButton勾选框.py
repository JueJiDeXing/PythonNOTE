import tkinter as tk

window = tk.Tk()

window.title("check button")
window.geometry("500x300")


def check_selection():
    print(f"value {var1.get()}")


var1 = tk.IntVar()
c1 = tk.Checkbutton(window, text="option1", variable=var1, onvalue=1, offvalue=0, command=check_selection)
c1.pack()

window.mainloop()
