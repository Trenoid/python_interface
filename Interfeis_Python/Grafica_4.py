from tkinter import *

#Создаем окно
window = Tk()
window.title('Эллипс и круг')

#Создаем холст
c = Canvas(window, width=250, height=200)
c.pack()

#Рисуем круг
c.create_oval((50, 10), (150, 110), outline =
'red', width = 3)

#Рисуем эллипс
c.create_oval(10, 120, 190, 190, fill='grey80',
outline='white')

window.mainloop()