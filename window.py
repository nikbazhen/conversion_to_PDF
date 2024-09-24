from tkinter import *
from button.choice_file import handler_choose_file_button
from button.save_way import handler_save_way_button
from loader import window


def program_window() -> None:
    window.title("Convertion to PDF")
    window.geometry('800x450')

    greeting_widget = Label(window, text="Добро пожаловать в Convertion to PDF!")
    description_widget = Label(window, text="Данная программа позволяет конвертировать "
                                            "файлы в форматах Word, Excel и PowerPoint в PDF.")
    choice_file_button = Button(text="Выбрать файл", command=handler_choose_file_button)
    information_about_saving_widget = Label(window, text="Внимание! Если вы хотите сохранить файл в той папке, "
                                                         "где находится выбранный файл, то папку для "
                                                         "сохранения можете не выбирать.",
                                            font=("Arial", 7), fg='blue')
    save_way_button = Button(text="Выбрать папку для сохранения", command=handler_save_way_button)
    greeting_widget.grid(sticky="W")
    description_widget.grid(sticky="W")
    choice_file_button.grid(sticky="W")
    information_about_saving_widget.grid(sticky="W")
    save_way_button.grid(sticky="W")

    window.mainloop()

