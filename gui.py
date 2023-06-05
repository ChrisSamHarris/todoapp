import functions
import PySimpleGUI as pg

label = pg.Text("Type in a TODO:")
input_box = pg.InputText(tooltip="Enter TODO")
add_button = pg.Button("Add")

window = pg.Window('My TODO Application', layout=[[label], [input_box, add_button]])
# laout needs to go into another set of square [] brackets -> Layout expects a list of list(s) (further lists to be used as arguments): Inner square brackets will be placed in one row (each row needs a square bracket)
window.read()
window.close()