from tkinter import *

class My_Button:

#Конструктор с аргументами
    def __init__(self, mwindow, mtext = "Цвет окна", mwidth = 15, mheight = 3, mbg = "blue", mfg = "red", mpdx = 150, mpdy = 50):

#Создаем кнопку с параметрами по умолчанию
        self.btn = Button(mwindow, text = mtext,width = mwidth, height = mheight, bg = mbg, fg = mfg)
        self.btn.pack(padx = mpdx, pady = mpdy)

#Конфигурирование функции обработчика событий
    def setFunc(self, func):
        self.btn['command'] = eval('self.' + func)

#Функция, переключающая цвет окна с желтого на зеленый и обратно
    def color_change(self):
        if window.cget("bg") == "yellow": #Получаем цвет фона с помощью метода cget()
            window.configure(bg = "green") # Цвет фона зеленый (используем метод configure())
        else:
            window['bg'] = "yellow" #Цвет фона  желтый (используем "терминологию" словаря)желтый (используем "терминологию" словаря)

#Функция для выхода из программы
    def m_exit(self):
        exit()
    
window = Tk() #Создаем окно
window.title("Работа с кнопками") #Создаем заголовок окна
window.geometry("500x300") #Задаем размеры окна

#Создаем кнопку для изменения цвета фона
btn_switch = My_Button(window)
btn_switch.setFunc('color_change') #Связываем кнопку с обработчиком (функция color_change)

#Создаем кнопку для выхода из программы
btn_exit = My_Button(window, "Выход", 12,
2,"#ff0000", "green", 150, 20)
btn_exit.setFunc('m_exit')#Связываем кнопку с обработчиком (функция m_exit)

#Цикл обработки событий окна
window.mainloop()