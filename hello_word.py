from tkinter import *


window = Tk()
window.title("Convertion to PDF")
window.geometry('800x450')
lbl_greeting = Label(window, text="Добро пожаловать в Convertion to PDF!")
lbl_description = Label(window, text="Данная программа позволяет конвертировать "
                                     "файлы в форматах Word, Excel и PowerPoint в PDF.")
lbl_greeting.grid()
lbl_description.grid()
window.mainloop()
