from tkinter import *

#Создаем окно
window = Tk()
window.title('Прямоугольники')

#Создаем холст
c = Canvas(window, width=300, height=200)
c.pack()

#Создаем прямоугольники
c.create_rectangle(20, 20, 280, 40, outline = 'red')

c.create_rectangle(100, 60, 200, 180,
fill='yellow', outline='green', width=3, activedash=(5, 4))



window.mainloop()