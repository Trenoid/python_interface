from tkinter import *

window = Tk()
window.title("Многоуровневое меню")

#Создаем меню в главном окне
mainmenu = Menu(window)
window.config(menu=mainmenu)

#Создаем пункты подменю для пункта меню "Файл"
filemenu = Menu(mainmenu, tearoff=0) #Создаем еще один объект Menu
filemenu.add_command(label="Открыть...")

#Добавляем в него пункты меню
filemenu.add_separator()#Добавляем линию-разделитель
filemenu.add_command(label="Новый")

filemenu.add_separator()#Добавляем линию-разделитель
filemenu.add_command(label="Сохранить...")

filemenu.add_separator()#Добавляем линию-разделитель
filemenu.add_command(label="Выход")

#Создаем пункт подменю "Помощь" для пункта меню "Справка"
helpmenu = Menu(mainmenu, tearoff=0) #Создаем еще один объект Menu

#Добавляем еще один уровень меню к пункту подменю "Помощь"
helpmenu1 = Menu(helpmenu, tearoff=0)
helpmenu1.add_command(label="Локальная справка")

helpmenu1.add_separator()#Добавляем линию-разделитель
helpmenu1.add_command(label="На сайте")

#Связываем два созданных пункта меню с пунктом подменю "Помощь"
helpmenu.add_cascade(label="Помощь",menu=helpmenu1)

helpmenu.add_separator()#Добавляем линию-разделитель

#Создаем пункт подменю "О программе" для пункта меню "Справка"
helpmenu.add_command(label="О программе")

#Связываем два созданных меню с главным меню
mainmenu.add_cascade(label="Файл", menu=filemenu)
mainmenu.add_cascade(label="Справка",menu=helpmenu)


window.mainloop()