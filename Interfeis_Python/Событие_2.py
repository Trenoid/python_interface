from tkinter import *

#Функции-обработчики различных событий
def mouse_left(event):
    window.title("Левая кнопка мыши")

def mouse_right(event):
    window.title("Правая кнопка мыши")

def mouse_move(event):
    x = event.x
    y = event.y
    ss = "Движение мышью {0}x{1}".format(x, y)
    window.title(ss)

window = Tk()

window.minsize(width = 600, height = 300)
window.bind('<Button-1>', mouse_left)
window.bind('<Button-3>', mouse_right)
window.bind('<Motion>', mouse_move)


window.mainloop()