from tkinter import *

#Создаем окно
window = Tk()
window.title('Использование тегов')

#Создаем холст
can = Canvas(window, width=400, height=200)
can.focus_set()
can.pack()

#Создаем группу фигур под одним тегом group_1
circ = can.create_oval((150,75),(250,125),fill = 'yellow', tag = "group_1")

rect = can.create_rectangle((50,25),(150,75),fill = 'green',tag = "group_1")

#Функция изменяет цвет всех фигур из группы с тегом group_1

def change_color(event):
    can.itemconfig('group_1', fill='red')

can.bind('<Button-1>', change_color)
window.mainloop()