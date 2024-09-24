from tkinter.filedialog import askopenfilename
from config.config_way import PATH_VARIABLES
from additional_widgets.create_or_delete_way_to_file import way_to_file


def handler_choose_file_button():
    if PATH_VARIABLES['link_widget']:
        way_to_file(False)
    filetypes = (
        ("Word, Excel, PowerPoint",
         "*.xlsx "
         "*.xls "
         "*.doc "
         "*.docx "
         "*.pptx "
         "*.ppt "
         ),
        ("Word",
         "*.doc "
         "*.docx "
         ),
        ("Excel",
         "*.xlsx "
         "*.xls "
         ),
        ("PowerPoint",
         "*.pptx "
         "*.ppt "
         )
    )

    file_path = askopenfilename(title="Выбрать файл", initialdir="/", filetypes=filetypes)
    PATH_VARIABLES["way_to_file"] = file_path
    way_to_file(True, file_path)



