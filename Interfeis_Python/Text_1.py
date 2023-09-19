from tkinter import *
window = Tk() #Создаем окно
window.title("Многострочный текст") #Создаем заголовок окна

#Функция для вставки текста
def insertText():
    s = "Кафедра информационных технологий"
    text.insert(1.0, s)

#Функция для считывания текста
def getText():
    s = text.get(1.0, 2.7)
    label['text'] = s

#Функция для удаления текста
def deleteText():
    text.delete(1.0, END)

#Создаем многострочное текстовое поле
text = Text(width=25, height=5)
text.pack()
#Создаем фрейм
frame = Frame(window)
frame.pack()

#Создаем три кнопки
b_insert = Button(frame, text="Вставить текст",
command=insertText)
b_insert.pack(side=LEFT)

b_get = Button(frame, text="Считать текст", command=getText)
b_get.pack(side=LEFT)

b_delete = Button(frame, text="Удалить текст",
command=deleteText)
b_delete.pack(side=LEFT)

#Создаем метку для вывода текста
label = Label()
label.pack()
#Цикл обработки событий окна
window.mainloop()