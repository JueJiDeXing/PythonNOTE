import tkinter as tk

cell_size = 20
cell_number = 20
window_size = cell_size * cell_number

window = tk.Tk()
window.title('snake_tk')
window.geometry(f'{window_size}x{window_size}')
window.resizable(True, True)
label = tk.Label(window)
label.focus_set()
label.pack()

canvas = tk.Canvas(window, bg='white', height=window_size, width=window_size)
# rect= canvas.create_rectangle(0*cell_size, 0*cell_size, cell_size, cell_size, fill='black')
# 黑白相间
for i in range(cell_number):
    for j in range(cell_number):
        if (i + j) % 2 == 0:
            color = 'white'
        else:
            color = 'black'
        rect = canvas.create_rectangle(j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size,
                                       fill=color)
canvas.pack()


def func(event):
    print()
    print("event.char =", event.char)
    print("event.keycode =", event.keycode)
    print(event)
    print(type(event))

# <Key> 响应所有的按键，但是不响应Mac的触控板输入
label.bind("<Key>", func)

window.mainloop()
