# Функция, переключающая цвет окна с желтого на зе-леный и обратно


def color_switch():
    if window.cget("bg") == "yellow":  # Получаем цвет фона с помощью метода cget()
        window.configure(bg="green")  # Цвет фона зеленый(используем метод configure())

    else:
        window['bg'] = "yellow"  # Цвет фона желтый (используем "терминологию" словаря)




from tkinter import *

window = Tk()  # Создаем окно
window.title("Работа с кнопками")  # Создаем заголовок окна
window.geometry("500x300")  # Задаем размеры окна

# Создаем кнопку для выхода из программы
btn_exit = Button(window, text="Выход",
                  bg = "#ff0000", fg = "green",
                  width = 12, command = exit)

# Создаем кнопку для изменения цвета фона
btn_switch = Button(window, text="Цвет окна",
                    bg="blue", fg="red",
                    width=15,
                    font=("Arial",16, "bold"),
                    command = color_switch)

btn_switch.pack(padx = 150, pady = 50) #Размещаем  обе кнопки в окне
btn_exit.pack(padx = 150, pady = 20)

#Цикл обработки событий окна
window.mainloop()