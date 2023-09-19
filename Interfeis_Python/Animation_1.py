from tkinter import *

#Создаем окно
window = Tk()
window.title('Простая анимация')

#Создаем холст
can = Canvas(window, width=400, height=200)
can.pack()
width = can.winfo_reqwidth()-4 #Вычисляем ширину холста

#Создаем круг
ball = can.create_oval((0,100),(50,150), fill = 'blue')

print(can.coords(ball)[0],can.coords(ball)[1],
can.coords(ball)[2])

#Функция для реализации движения
def motion():
    can.move(ball, 5, 0)
    if can.coords(ball)[2] < width:
        window.after(100, motion)
    else:
        can.delete(ball)
motion()
window.mainloop()

#  Метод after() в качестве аргументов получает интервал времени
#  (в данном случае это 10 миллисекунд) и функцию, которую нужно
#  вызывать через этот интервал (функция motion()).