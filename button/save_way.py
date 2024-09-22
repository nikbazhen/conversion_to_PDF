from tkinter.filedialog import askdirectory


def handler_save_way_button():
    directory = askdirectory(title="Выбрать папку", initialdir="/")
    if directory:
        print(directory)
