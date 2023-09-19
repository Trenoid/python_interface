from tkinter import *
window = Tk() #Создаем окно
window.title("Вывод текста") #Создаем заголовок окна
window.geometry("500x300") #Задаем размеры окна

#Создаем метку
label = Label(window, bg = "blue" , fg = "yellow",  text = "СПБГАСУ", font = "Arial 16") #Задаем шрифт как строку

#Размещаем метку в окне по вертикали — вверху, по горизонтали — посередине


label.pack()
#Размещаем метку в окне по вертикали — посередине, по горизонтали — посередине
label.pack(expand = 1)

#Заполняем всё пространство по горизонтали
label.pack(expand = 1, fill = X)

#Заполняем всё пространство по обеим осям
label.pack(expand = 1, fill = BOTH)

#Размещаем метку с текстом в левом верхнем углу
label.pack(anchor = NW)

#Цикл обработки событий окна
window.mainloop()