from tkinter import *

window = Tk()
window.geometry("400x200")
window.title( 'Метод place()' )

#Размещаем метку по абсолютным координатам
Label(text="Введите номер станции назначения:").place(x=50, y = 20)

#Размещаем однострочное текстовое поле по абсолютным координатам

station_numb = Entry(width = 3)
station_numb.place(x = 315, y = 20)

#Размещаем кнопку "Подобрать вариант" по относительным координатам
btn = Button(window, text = "Подобрать вариант",
bg = "lightgreen")
btn.place(relx=0.25, rely=0.75)

window.mainloop()