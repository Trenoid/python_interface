from tkinter import *
import tkinter.messagebox as box

window = Tk() #Создаем окно
window.title("Ввод данных") #Создаем заголовок окна

frame = Frame(window)#Создаем фрейм, в который бу-дет размещено поле для ввода

entry = Entry(frame) #Создаем поле ввода и привязываем его к фрейму

#Функция для отображения данных, считанных из поля ввода

def dialog():
    box.showinfo("Приветствие", "Привет, " + entry.get())

#Создаем кнопку, которая будет вызывать функцию
btn = Button(frame, text = "Ввод", command = dialog)

#Создаем метку с поясняющим текстом
lb = Label(frame, text = "Введите имя: ")

#Добавляем все виджеты на фрейм
lb.pack(side = LEFT)
entry.pack(side = LEFT)
btn.pack(side = RIGHT, padx = 5)
frame.pack(padx = 20, pady = 20)
#Цикл обработки событий окна
window.mainloop()