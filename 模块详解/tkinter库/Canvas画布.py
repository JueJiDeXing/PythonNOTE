import tkinter as tk  # 使用Tkinter前需要先导入

# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x

# 第4步，在图形界面上创建 500 * 200 大小的画布并放置各种元素
canvas = tk.Canvas(window, bg='green', height=200, width=500)
# 说明图片位置，并导入图片到画布上
# image_file = tk.PhotoImage(file="ee.gif")  # 仅支持GIF和PGM/PPM文件格式
# image = canvas.create_image(250, 0, anchor='n', image=image_file)  # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
# 定义多边形参数，然后在画布上画出指定图形
x0, y0, x1, y1 = 100, 100, 150, 150
line = canvas.create_line(50, 50, 100, 100)  # 画直线(x1,y1)->(x2,y2)->(x3,y3)->...
for i in range(10):
    line = canvas.create_line(50 * i, 0, 50 * i, 200)
for j in range(5):
    line=canvas.create_line(0,50*j,500,50*j)
oval = canvas.create_oval(100, 150, 300, 200, fill='yellow')  # 画椭圆,内切于矩形区域(x1,y1)(x2,y2) 用黄色填充
arc = canvas.create_arc(100, 100, 200, 150, start=0, extent=180)  # 画扇形,同上 从0度打开收到180度结束
rect = canvas.create_rectangle(330, 30, 330 + 20, 30 + 20)  # 画矩形
canvas.pack()


# 第6步，触发函数，用来一定指定图形
def moveit():
    canvas.move(rect, 2, 2)  # 移动正方形rect（也可以改成其他图形名字用以移动一起图形、元素），按每次（x=2, y=2）步长进行移动


# 第5步，定义一个按钮用来移动指定图形的在画布上的位置
tk.Button(window, text='move item', command=moveit).pack()

# 第7步，主窗口循环显示
window.mainloop()
