from tkinter import *
window = Tk()
window.title("Обработка разных событий")

#Функция обработчик (одна функция для нескольких событий)

def change_color(col):
    lb['fg'] = col

#Создаем метку
lb = Label(text = "Обработка разных событий")
lb.pack()

#Создаем кнопку, окрашивающую текст в синий цвет, и сразу размещаем ее
Button(command = lambda col = 'blue':
    change_color(col)).pack()
#Создаем кнопку, окрашивающую текст в красный цвет, и сразу размещаем ее

Button(command = lambda col = 'red':
    change_color(col)).pack()
window.mainloop()