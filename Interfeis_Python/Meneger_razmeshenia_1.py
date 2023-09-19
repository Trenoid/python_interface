from tkinter import *

window = Tk()
window.title( 'Электрички' )
window.resizable(0,0) #Деактивируем кнопкуизменения размеров окна

#Размещаем в ячейке (0,0) метку с текстом
Label(text="Введите номер станции назначения:").grid(row=0, column=0, sticky=N+W,pady=10, padx=10)

#Размещаем в ячейке (0,1) однострочное текстовое поле
station_numb = Entry(width = 3)
station_numb.grid(row=0, column=1,sticky=N+W,
pady=10, padx=10 ) #Размещаем в ячейке (0,2) поле со списком

#объединяем ячейки (0,2),(0,3) и (0,4)
station_list = Listbox(window, width = 50)
station_list.grid(row=0, column=2, columnspan = 5,padx=10)

#Размещаем в ячейке (1,0) метку с текстом
Label(text="Минимальное время в пути до станции №:").grid(row=1, column=0, sticky=W, pady=10, padx=10)

#Размещаем в ячейке (1,1) однострочное текстовое поле
station_numb = Entry(width = 3)
station_numb.grid(row=1, column=1, sticky=W,
pady=10, padx=10 )

#Размещаем в ячейке (1,2) метку с текстом
Label(text="составляет").grid(row=1, column=2, sticky=W, pady=10, padx=10)

#Размещаем в ячейке (1,3) однострочное текстовое поле
station_numb = Entry(width = 5)
station_numb.grid(row=1, column=3, sticky=W,
pady=10, padx=10 )

#Размещаем в ячейке (1,4) метку с текстом
Label(text="минут").grid(row=1, column=4, sticky=W, pady=10, padx=10)

#Размещаем в ячейке (2,0) кнопку "Подобрать вариант"
btn_1 = Button(window, text = "Подобрать вариант", bg = "lightgreen")

btn_1.grid(row=2, column=0, sticky=S, pady=30, padx=10)

#Размещаем в ячейке (2,2) кнопку "Очистить"
btn_2 = Button(window, text = "Очистить", bg = "orange", width = 20)

btn_2.grid(row=2, column=2, sticky=S, pady=30, padx=10)

#Размещаем в ячейке (2,4) кнопку "Выход"
btn_3 = Button(window, text = "Выход", bg = "red", width = 20)

btn_3.grid(row=2, column=4, sticky=S, pady=30, padx=10)



window.mainloop()