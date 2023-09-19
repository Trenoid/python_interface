from tkinter import *
import tkinter.messagebox as box


# Функция по выводу диалогового окна
def dialog():
    box.showinfo("Выбор языка", "Вы выбрали язык " +  listbox.get(listbox.curselection()))




window = Tk()  # Создаем окно
window.title("Работа со списком")  # Создаем заголовок окна


# Создаем фрейм для виджетов
frame = Frame(window)

# Создаем виджет Listbox
listbox = Listbox(frame)

# Заполняем список
for i in ('Java', 'C++', 'Python', 'C#', 'JavaScript', 'PHP'):
    listbox.insert(END, i)
listbox.insert(3, "FORTRAN")

# Создаем кнопку
btn = Button(frame, text="Выберите язык", bg=
"lightgreen", command=dialog)

# Размещаем виджеты
btn.pack(side=RIGHT, padx=15)
listbox.pack(side = LEFT)
frame.pack(padx=30, pady=30)

#Цикл обработки событий окна
window.mainloop()