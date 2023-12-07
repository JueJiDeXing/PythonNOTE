import tkinter as tk

window = tk.Tk()

window.title("This is demo4")
window.geometry("500x300")

var_l = tk.StringVar()
l = tk.Label(window, textvariable=var_l, font=("Arial", 14), width=10, height=3)
l.pack()


def show():
    select = lb.curselection()  # 检测鼠标光标选中项
    print("select", select, type(select))
    if not select:
        return
    value = lb.get(select)
    print("value", value, type(value))
    var_l.set(value)


b = tk.Button(window, text="show select", command=show)
b.pack()
##### 新增
var = tk.StringVar()
var.set((1, 2, 3, 4))
lb = tk.Listbox(window, listvariable=var)

# 插入选项
lb.insert(1, "s1")  # 在index=1处插入"s1"
lb.insert(2, "s2")
lb.insert("end", "se")  # 1 s1 s2 2 3 4 se

lb.pack()
#####
window.mainloop()
