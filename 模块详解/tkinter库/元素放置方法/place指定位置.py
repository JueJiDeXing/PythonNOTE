import tkinter as tk

window = tk.Tk()

window.title("place")
window.geometry("500x300")

tk.Label(window, text="P", font=("Arial", 20)).place(x=25, y=100, anchor="nw")

window.mainloop()
