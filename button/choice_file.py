from tkinter.filedialog import askopenfilename


def handler_choose_file_button():
    filetypes = (
        ("Word, Excel, PowerPoint",
         "*.xlsx "
         "*.xls "
         "*.xltx "
         "*.xlt "
         "*.xlsm "
         "*.xltm "
         "*.xlsb "
         "*.doc "
         "*.docm "
         "*.docx "
         "*.dot "
         "*.dotm "
         "*.dotx "
         "*.pptx "
         "*.ppt "
         "*.pptm "
         "*.potx "
         "*.potm "
         "*.ppsx"
         ),
        ("Word",
         "*.doc "
         "*.docm "
         "*.docx "
         "*.dot "
         "*.dotm "
         "*.dotx"
         ),
        ("Excel",
         "*.xlsx "
         "*.xls "
         "*.xltx "
         "*.xlt "
         "*.xlsm "
         "*.xltm "
         "*.xlsb"
         ),
        ("PowerPoint",
         "*.pptx "
         "*.ppt "
         "*.pptm "
         "*.potx "
         "*.potm "
         "*.ppsx"
         )
    )

    filename = askopenfilename(title="Выбрать файл", initialdir="/", filetypes=filetypes)
