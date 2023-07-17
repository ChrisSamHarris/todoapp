import PySimpleGUI as pg
from archive_backend import extract_archive

pg.theme('Black')

label1 = pg.Text("Select archive:")
input1 = pg.Input()
choose_button1 = pg.FileBrowse('Choose', key='archive')

label2 = pg.Text("Destination folder:")
input2 = pg.Input()
choose_button2 = pg.FolderBrowse('Choose', key='folder')

extract_button = pg.Button("Extract")
output_label = pg.Text(key="output", text_color="green")

window = pg.Window('Archive Extractor',
                    layout=[[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [extract_button, output_label]], 
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print("Event:", event)
    print("Values:", values)
    archive_path = values["archive"]
    dest_dir = values["folder"]
    try: 
        extract_archive(archive_path, dest_dir)
        window["output"].update(value="Extraction Successful!")
    except Exception as e:
        print(f"Error, extraction unsuccessful: {e}")

window.close()


