from tkinter import *

#Создаем окно
window = Tk()
window.title('Сектора, дуги и сегменты')

#Создаем холст
c = Canvas(window, width=350, height=200)
c.pack()
р
#Рисуем круг
c.create_oval((10, 10), (190, 190), fill = 'lightgrey', outline = 'white')

#Рисуем сектор размером 60 градусов из точки 0 градусов
c.create_arc((10, 10), (190, 190), start = 0,
extent = 60, fill='blue')

#Рисуем сектор размером 30 градусов из точки 160 градусов
c.create_arc((10, 10), (190, 190), start = 160,
extent = 30, fill='red')

#Рисуем дугу размером 50 градусов из точки 140 градусов
c.create_arc((10, 10), (190, 190), start = 140,
extent = -50, style = ARC, outline='darkgreen', width = 4)


#Рисуем сегмент размером 90 градусов из точки 240 градусов
c.create_arc((10, 10), (190, 190), start = 240,
extent = 90, style = CHORD, fill ='orange')


window.mainloop()