import tkinter as tk

window = tk.Tk()

window.title("Menu")
window.geometry("500x300")


def job1():
    print("do job1")


# 创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
menubar = tk.Menu(window)
# 创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
filemenu = tk.Menu(menubar, tearoff=0)
# 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
menubar.add_cascade(label="File", menu=filemenu)

# 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作
filemenu.add_command(label="New", command=job1)
filemenu.add_command(label="Open", command=job1)
filemenu.add_command(label="Save", command=job1)
filemenu.add_separator()  # 添加一条分隔线
filemenu.add_command(label="Exit", command=window.quit)
# 创建第二级菜单，即菜单项里面的菜单
submenu = tk.Menu(filemenu)
filemenu.add_cascade(label="Import", menu=submenu)
submenu.add_command(label="do1", command=job1)

# 创建菜单栏完成后，配置让菜单栏menubar显示出来
window.config(menu=menubar)

window.mainloop()
