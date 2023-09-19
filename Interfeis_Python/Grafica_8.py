from tkinter import *

#Создаем окно
window = Tk()
window.title('Идентификаторы объектов')
#Создаем холст
can = Canvas(window, width=400, height=200)
can.focus_set()
can.pack()

#Создаем прямоугольник
rect = can.create_rectangle((150,75),(250,125),
fill = 'blue')

#Функция изменяет цвет и размер прямоугольника
def change(event):
    can.itemconfig(rect, fill='green')
    can.coords(rect, 50, 50, 300, 150)
can.bind('<Return>',change)

window.mainloop()