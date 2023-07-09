import PySimpleGUI as pg
import zip_creator as fzip

label1 = pg.Text("Select files to compress:")
input1 = pg.Input()
choose_button1 = pg.FilesBrowse("Choose", key="files")

label2 = pg.Text("Select destination folder")
input2 = pg.Input()
choose_button2 = pg.FolderBrowse("Choose", key='folder')

# label3 = pg.Text("Enter a Filename:")
# input_box = pg.InputText(tooltip="Enter Filename", key="new_filename")

output_label = pg.Text(key="output")

compress_button = pg.Button("Compress")



window = pg.Window("File Compressor", 
                   layout=[[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [compress_button, output_label]
                            ])

while True:
    event, values = window.read()
    if event == pg.WINDOW_CLOSED:
        break

    if event == "Compress":
        print(event, values)
        filepaths = values['files'].split(";")
        folder = values['folder']
        # new_filename = values['new_filename']
        fzip.zip_the_files(filepaths, folder)
        window["output"].update(value="Compression Completed.")

window.close()