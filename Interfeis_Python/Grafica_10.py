from tkinter import *

#Создаем окно
window = Tk()
window.title('Использование идентификаторов')

#Создаем холст
can = Canvas(window, width=400, height=200)
can.pack()

#Создаем фигуры
circ ть = can.create_oval((150,75),(250,125), fill = 'yellow')
rect = can.create_rectangle((50,25),(150,75), fill = 'green')
trial = can.create_polygon((350, 20), (310, 80),
                           (390, 80), fill="blue", outline="yellow")


# Функции меняют изображение фигур на текст
def change_circ(event):
    can.delete(circ)
    can.create_text((200, 100), text='Эллипс', fill="red")


def change_rect(event):
    can.delete(rect)
    can.create_text((100, 50),text='Прямоугольник', fill="red")


def change_trial(event):
    can.delete(trial)
    can.create_text((350, 40), text='Треугольник', fill="red")


can.tag_bind(circ, '<Button-1>', change_circ)
can.tag_bind(rect, '<Button-1>', change_rect)
can.tag_bind(trial, '<Button-1>', change_trial)



window.mainloop()