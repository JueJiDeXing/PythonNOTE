import tkinter as tk

window = tk.Tk()

window.title("grid")
window.geometry("500x300")

for i in range(3):
    for j in range(3):
        tk.Label(window, text=1).grid(row=i, column=j, padx=10, pady=10, ipadx=10, ipady=10)
# padx就是单元格左右间距,pady就是单元格上下间距,ipadx是单元格内部元素与单元格的左右间距,ipady是单元格内部元素与单元格的上下间距
window.mainloop()
