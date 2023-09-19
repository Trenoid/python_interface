from tkinter import * #Создаем окно


window = Tk()
window.title('Структура инвестиционного портфеля')

#Создаем холст
c = Canvas(window, width=500, height=200)
c.pack()

#Рисуем сектор размером 72 градуса из точки 0 градусов
c.create_arc((10, 10), (190, 190), start = 0, extent = 72, fill='blue')

#Рисуем сектор размером 288 градусов из точки 72 градуса
c.create_arc((10, 10), (190, 190), start = 72,
extent = 288, fill='red')

#Рисуем два прямоугольника
c.create_rectangle((250,100),(300,120), fill =
'blue')
c.create_rectangle((250,150),(300,170), fill =
'red')

#Добавляем текст
c.create_text((350,50), text = "Круговая диаграмма", justify = CENTER,  fill = "green", font = "Times 14 bold")
c.create_text((325,110), text = "Лукойл - 20%", anchor = W,
            fill = "darkgreen", font = "Times 10 bold")
c.create_text((325,160), text = "Сбербанк - 80%", anchor = W,
fill = "darkgreen", font = "Times 10 bold")


window.mainloop()