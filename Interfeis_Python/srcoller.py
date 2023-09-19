from tkinter import *

window = Tk() #Создаем окно
window.title("Полоса прокрутки") #Создаем заголовок окна

#Создаем многострочное поле ввода
text = Text(width=30, height=5, bg = "blue", fg = "yellow", wrap = WORD)
text.pack(side = LEFT)

#Создаем вертикальную полосу прокрутки
scroll = Scrollbar(orient = VERTICAL, command = text.yview)
scroll.pack(side = RIGHT, fill = Y)

#Конфигурируем поле ввода с полосой прокрутки
text.config(yscrollcommand = scroll.set)


#Цикл обработки событий окна
window.mainloop()