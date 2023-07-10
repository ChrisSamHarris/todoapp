import functions
import PySimpleGUI as pg
import time

pg.theme('Dark Amber')

label_dt = pg.Text(time.strftime("%b %d, %Y %H:%M"), key='clock')
label = pg.Text("Type in a TODO:")
input_box = pg.InputText(tooltip="Enter TODO", key="user_todo", do_not_clear=False)
add_button = pg.Button("Add")
list_box = pg.Listbox(values=functions.read_todos(), key='todo_edit', enable_events=True, size=[45, 10])

edit_button = pg.Button("Edit")
complete_button = pg.Button("Complete")
exit_button = pg.Button("Exit")

window = pg.Window('My TODO Application',
                    layout=[[label_dt], [label], [input_box, add_button], [list_box, edit_button, complete_button],[exit_button]], 
                    font=('Helvetica', 20))
# layout needs to go into another set of square [] brackets -> Layout expects a list of list(s) (further lists to be used as arguments): Inner square brackets will be placed in one row (each row needs a square bracket)

while True: 
    event, values = window.read()
    # event, values = window.read(timeout=10) = While loop runs every 10 milliseconds - useful if you want the seconds on the GUI i.e. time.strftime("%b %d, %Y %H:%M:%S")
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M"))

    # Output can be broken down due to data being a dictionary: ('Add', {'user_todo': 'test2'})
    # print(1, window.read()) -> DO NOT USE this is a blocking operation that waits for an event to occur so you would have to click 'Edit' twice for example - When window.read() is called, it pauses the execution of your program and waits for one of these events to happen.
    print("Event:", event)
    print("Values:", values)
    # print(4, values['todo_edit'])
    match event:
        case "Add":
            todo_list = functions.read_todos()
            new_todo = values['user_todo'] 
            todo_list.append(new_todo.title().strip()+ '\n')
            functions.write_todos(todo_list)

            window['todo_edit'].update(values=todo_list)

        case "Edit":
            try: 
                todo_list = functions.read_todos()
                todo_to_edit = values['todo_edit'][0]
                raw_index = todo_list.index(todo_to_edit)
                new_todo = values['user_todo']
                # print(f'New TODO = \'{new_todo}\', replaces {todo_list[raw_index]}.')
                todo_list[raw_index] = new_todo.title().strip() + '\n'
                # print(f'todo_list = {todo_list}')

                functions.write_todos(todo_list)
                window['todo_edit'].update(values=todo_list)
            
            except IndexError: 
                print("Please select an item first!")
                pg.popup("Please select an item first!", font=("Helvetica", 20))

        case "todo_edit":
            window['user_todo'].update(value=values['todo_edit'][0])
            #widgets can be accessed with window['<WIDGET_KEY>'] -> Values can be updated using the ".update(values=<NEW_VAL>)" method

        case "Complete":
            try: 
                todo_to_complete = values['user_todo']
                todos = functions.read_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todo_edit'].update(values=todos)
                window['user_todo'].update(values='')
                print(f"\'{todo_to_complete}\' successfully removed from TODO list.")
            
            except IndexError:
                pg.popup("Please select an item first!", font=("Helvetica", 20))

        
        case "Exit":
            break

        case pg.WIN_CLOSED:
            break

window.close()