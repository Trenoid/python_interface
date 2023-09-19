from tkinter import *

#Функции-обработчики различных событий
def close_win(event):
 window.destroy()

def text_to_Label(event):
    s = t.get()
    lbl.configure(text=s)
def select_All(event):
    window.after(10,select_all,event.widget)
def select_all(widget):
    widget.selection_range(0,END)
    widget.icursor(END)

window = Tk()

t = Entry(width = 50)
t.focus_set() #Устанавливаем фокус в текстовое поле

t.pack()
#Создаем метку
lbl = Label(height = 4, fg = 'orange', bg = 'darkblue', font = 'Times 16 bold')
lbl.pack(fill = X)
t.bind('<Return>', text_to_Label)
t.bind('<Control-t>', select_All)
window.bind('<Control-q>', close_win)
window.mainloop()
