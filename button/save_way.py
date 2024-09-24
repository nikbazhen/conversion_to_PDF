from tkinter.filedialog import askdirectory
from additional_widgets.create_or_delete_way_to_file import way_to_file
from config.config_way import PATH_VARIABLES


def handler_save_way_button():
    directory = askdirectory(title="Выбрать папку", initialdir="/")

