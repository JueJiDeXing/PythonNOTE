import tkinter as tk

window = tk.Tk()

window.title("scale")
window.geometry("500x300")


def scaleValue(v):
    print(f"scale {v}")


s = tk.Scale(window, label="try me", from_=0, to=10, orient=tk.HORIZONTAL, length=200, showvalue=1,
             tickinterval=2, resolution=0.01, command=scaleValue
             )
s.pack()
window.mainloop()
