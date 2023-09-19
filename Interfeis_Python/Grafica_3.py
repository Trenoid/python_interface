from tkinter import *

#Создаем окно
window = Tk()
window.title('Многоугольники произвольной формы')

#Создаем холст
c = Canvas(window, width=450, height=250)
c.pack()

#Создаем фигуры произвольной формы
#Рисуем ромб
c.create_polygon((180, 10), (100, 90), (260, 90),
fill = 'yellow', outline = 'red')

#Рисуем трапецию
c.create_polygon((40, 110), (160, 110), (190,
180), (10, 180),
 fill='orange', outline='green', width=3)

#Рисуем параллелепипед
c.create_polygon((300, 230), (300, 180), (400,
180), (400, 230), fill='red', outline = 'blue')
c.create_polygon((300, 180), (330, 150), (430,
150), (400, 180), fill='red', outline = 'blue')
c.create_polygon((400, 230), (400, 180), (430,
150), (430, 200), fill='red', outline = 'blue')
c.create_line((300, 230), (330, 200), fill =
'blue', dash = (2,2))
c.create_line((330, 150), (330, 200), fill =
'blue', dash = (2,2))
c.create_line((330, 200), (430, 200), fill =
'blue', dash = (2,2))


window.mainloop()