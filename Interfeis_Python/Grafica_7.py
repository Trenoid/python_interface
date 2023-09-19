from tkinter import *

#Создаем окно
window = Tk()
window.title('Идентификаторы объектов')

#Создаем холст
can = Canvas(window, width=400, height=200)
can.focus_set()
can.pack()

#Создаем прямоугольник
rect = can.create_rectangle((150,75),(250,125),fill = 'blue')

can.bind('<Up>', lambda event: can.move(rect, 0,-10)) #Смещение вверх на 10 пикселей

can.bind('<Down>', lambda event: can.move(rect, 0, 10))#Смещение вниз на 10 пикселей

can.bind('<Left>', lambda event: can.move(rect,-25, 0))#Смещение влево на 25 пикселей

can.bind('<Right>', lambda event: can.move(rect,25, 0))#Смещение вправо на 25 пикселей

window.mainloop()