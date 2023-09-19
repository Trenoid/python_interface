from tkinter import *

window = Tk()
window.title( 'Работа с изображением' )

#Создаем объект-изображение
img = PhotoImage( file = 'null.gif' )

#Уменьшаем полученное изображение в два раза
small_img = PhotoImage.subsample( img , x = 2 , y = 2 )

#Создаем метку с изображением
label = Label( window , image = img , bg ='yellow' )

#Создаем кнопку с изображением
btn = Button( window , bg = 'red', image = small_img )

#Создаем текстовое поле с изображением
txt = Text( window , width = 25 , height = 7, fg = 'darkgreen' )
txt.image_create( '1.0' , image = small_img )
txt.insert( '1.1', 'Python is Fun!' )

#Создаем холст с изображением
can = Canvas( window , width = 100 , height = 100 , bg = 'cyan' )

can.create_image( ( 50 , 50 ), image = small_img )
can.create_line( 0 , 0 , 100 , 100, width = 25 , fill = 'yellow' )

#Размещаем созданные виджеты в окне приложения
label.pack( side = TOP )
btn.pack( side = LEFT , padx = 10 )
txt.pack( side = LEFT )
can.pack( side = LEFT, padx = 10 )


window.mainloop()