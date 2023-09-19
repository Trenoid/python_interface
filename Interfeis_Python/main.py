from tkinter import *


window = Tk() #Создаем окно

window.title("Вывод текста") #Создаем заголовок окна
window.geometry("500x300") #Задаем размеры окна




############################################################################Основа#############################################




# Создаем четыре метки
lab_1 = Label(width=8, height=3, bg='yellow',
text="1")
lab_2 = Label(width=8, height=3, bg='red',
text="2")
lab_3 = Label(width=8, height=3,
bg='lightgreen', text="3")
lab_4 = Label(width=8, height=3,
bg='lightblue', text="4")

#Располагаем метки вертикально сверху вниз
lab_1.pack()
lab_2.pack()
lab_3.pack()
lab_4.pack()

#Комбинированное расположение меток
lab_1.pack(side = BOTTOM)
lab_2.pack(side = TOP)
lab_3.pack(side = LEFT)
lab_4.pack(side = RIGHT)






####################################################################################################################


#Цикл обработки событий окна
window.mainloop()