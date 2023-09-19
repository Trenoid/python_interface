from tkinter import *
import tkinter.messagebox as box

def dialog():
    var = box.askyesno("Выбор действий",
                       "Продолжаем ввод?")
    if var == 1:
        box.showinfo("Продолжение",
                     "Продолжаем...")
    else:
        box.showwarning("Прекращение", "Выход...")


window = Tk()  # Создаем окно
window.title("Вывод сообщений")  # Создаем заголовок окна
window.geometry("500x300")  # Задаем размеры окна

# Создаем кнопку для выхода из программы
btn = Button(window, text="Выбор решения", bg= "red", fg="#00ff00",
                     width=20, font=("Arial", 16, "bold"), command=dialog)

btn.pack(padx=100, pady=100)  # Размещаем кнопку в окне

#Цикл обработки событий окна
window.mainloop()