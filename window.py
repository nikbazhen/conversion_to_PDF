from tkinter import *
from button.choice_file import handler_choose_file_button
from button.save_way import handler_save_way_button

def program_window() -> None:
    window = Tk()
    window.title("Convertion to PDF")
    window.geometry('800x450')

    lbl_greeting = Label(window, text="Добро пожаловать в Convertion to PDF!")
    lbl_description = Label(window, text="Данная программа позволяет конвертировать "
                                         "файлы в форматах Word, Excel и PowerPoint в PDF.")


    # text_way = Label(window, text='Выберите или введите путь до файла:')
    # input_way = Entry(window, width=30)
    # btn = Button(window, text="нажимать")
    lbl_greeting.grid(sticky="W")
    lbl_description.grid(sticky="W")
    # text_way.grid(sticky="W", row=3)
    # input_way.place(x=215, y=43)
    # btn.place(x=410, y=40)
    choice_file_button = Button(text="Выбрать файл", command=handler_choose_file_button)
    save_way_button = Button(text="Выбрать папку для сохранения", command=handler_save_way_button)
    choice_file_button.grid(sticky='W')
    save_way_button.grid(sticky='W')


    window.mainloop()
