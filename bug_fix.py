# my_answer = input("What is your answer?")
# answers = ['Yes', 'No', 'Yes', 'No', my_answer]

#################


# greeting = 'hello'
# print(greeting.upper())


#################


# countries = []
 
# while True:
#     country = input("Enter the country: ")
#     if country == "q":
#         break
#     else:
#         countries.append(country)
#         print(countries)

#################

# elements = ['a', 'b', 'c']
# print(elements[1])

#################

# elements = ['a', 'b', 'c']
# new = 'x'
# elements[1] = new
# print(elements)

###################

# def calculate_time(h, g=9.80665):
#     t = (2 * h / g) ** 0.5
#     return t
    
    
# time = calculate_time(100)
# print(time)

###################

# The following program (which we developed in today's coding exercise) ends with an error if the user presses the Convert button without supplying any values in the input boxes first. 
# Please modify the above program so that instead of ending, the program should show a popup window telling the user to enter numbers in the input boxes ^ 

import PySimpleGUI as sg
    
def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters
    
    
sg.theme("Black")
    
feet_label = sg.Text("Enter feet: ")
feet_input = sg.Input(key="feet")
    
inches_label = sg.Text("Enter inches: ")
inches_input = sg.Input(key="inches")
    
button = sg.Button("Convert")
output_label = sg.Text("", key="output")
exit_button = sg.Button("Exit")
    
window = sg.Window("Convertor",
                    layout=[[feet_label, feet_input],
                            [inches_label, inches_input],
                            [button, exit_button, output_label]])
    
while True:
    event, values = window.read()
    match event:
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break
    try: 
        feet = float(values["feet"])
        inches = float(values["inches"])
        result = round(float(convert(feet, inches)),2)
        window["output"].update(value=f"{result} m", text_color="white")

    except ValueError:
        sg.popup("Please enter a value for both feet and inches first.", font=("Helvetica", 20))
    
window.close()

