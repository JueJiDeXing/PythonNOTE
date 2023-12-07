import tkinter as tk

window = tk.Tk()

window.title("frame")
window.geometry("500x300")
# 创建一个主frame，长在主window窗口上
frame = tk.Frame(window)
frame.pack()
# 创建第二层框架frame，长在主框架frame上面
frame_l = tk.Frame(frame)
frame_l.pack(side="left")

frame_r = tk.Frame(frame)
frame_r.pack(side="right")


tk.Label(window, text='on the window', bg='red').pack()
tk.Label(frame, text='on the frame', bg='pink').pack()
tk.Label(frame, text='on the frame', bg='pink').pack()
tk.Label(frame_l, text='on the frame_l1', bg='green').pack()
tk.Label(frame_l, text='on the frame_l2', bg='green').pack()
tk.Label(frame_l, text='on the frame_l3', bg='green').pack()
tk.Label(frame_r, text='on the frame_r1', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r2', bg='yellow').pack()
tk.Label(frame_r, text='on the frame_r3', bg='yellow').pack()

window.mainloop()
