import PySimpleGUI as pg

feet_label = pg.Text("Enter Feet:")
feet_input_box = pg.InputText(tooltip="Enter Feet", key="user_feet")
inch_label = pg.Text("Enter Inches:")
inch_input_box = pg.InputText(tooltip="Enter Inches", key="user_inches")
convert_button = pg.Button("Convert")

output_label = pg.Text(key="output")

layout = [[feet_label, feet_input_box], [inch_label, inch_input_box], [convert_button, output_label]]

window = pg.Window('Converter',
                    layout=layout, 
                    font=('Helvetica', 20))

while True: 
    event, values = window.read()
    match event:
        case "Convert":
            print('Convert')
            feet = int(values['user_feet'])
            inches = int(values['user_inches'])

            feet_to_m = feet * 0.3048
            inches_to_m = inches * 0.0254
            meters = round(feet_to_m + inches_to_m, 3)

            window["output"].update(value=f"{meters} meters")
            print(meters)

        case pg.WIN_CLOSED:
            break

