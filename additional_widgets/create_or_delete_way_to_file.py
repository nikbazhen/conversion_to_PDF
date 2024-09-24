from tkinter import Label
from loader import window
from config.config_way import PATH_VARIABLES


def way_to_file(bool_create_or_delete: bool, path=''):
    if not PATH_VARIABLES['link_widget']:
        PATH_VARIABLES['link_widget'] = Label(window, text=path)
    if bool_create_or_delete:
        PATH_VARIABLES['link_widget'].place(x=215, y=43)
    else:
        PATH_VARIABLES['link_widget'].destroy()
        PATH_VARIABLES['link_widget'] = None
        PATH_VARIABLES['way_to_file'] = None


