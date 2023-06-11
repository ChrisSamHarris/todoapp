import functions
import PySimpleGUI as pg

label = pg.Text("Type in a TODO:")
input_box = pg.InputText(tooltip="Enter TODO", key="user_todo", do_not_clear=False)
add_button = pg.Button("Add")

window = pg.Window('My TODO Application',
                    layout=[[label], [input_box, add_button]], 
                    font=('Helvetica', 20))
# laout needs to go into another set of square [] brackets -> Layout expects a list of list(s) (further lists to be used as arguments): Inner square brackets will be placed in one row (each row needs a square bracket)

while True: 
    event, values = window.read()
    # Output can be broken down due to data being a dictionary: ('Add', {'user_todo': 'test2'})
    print(event)
    print(values)
    print(window.read())
    match event:
        case "Add":
            todos = functions.read_todos()
            new_todo = values['user_todo'] + '\n'
            todos.append(new_todo.strip().title())
            functions.write_todos(todos)
        case "Edit":
            print('edit')
        case pg.WIN_CLOSED:
            break

window.close()