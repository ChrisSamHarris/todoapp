import functions
import greeting as hello

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
persistent_filepath = "files/todos.txt"

menu_items = ['Add','Complete','Show', 'Edit', 'Quit']
menu_string = " | ".join(f"{index}. {i}" for index, i in enumerate(menu_items, 1))

hello.greet()

# print('############## User Guide #############')
def main(): 
    while True:
        user_action = input(f"----------------------------------------\n##########  Main Menu ##########\n{menu_string}\n\nPlease type an option: ").lower()
        print('\n')

        if user_action.startswith('add') or user_action[0] in ('a', '1'):
            todos = functions.read_todos(persistent_filepath)

            try: 
                if len(user_action.split()) >= 2:
                    new_todo = functions.extract_todo(user_action)
                    functions.append_and_write_todo(todos, new_todo)

                    print(f"Task '{new_todo}' added to TODO list.\n")

                elif len(user_action.split()) < 2:
                    print("""\n#############################################\nEntering ADD mode...\npress 'b' at any time to return to the Main Menu.\n""")

                    while True:
                        todo = input("Enter a TODO task: ")
                        if todo.lower().strip() in ('back', 'b', 'quit', 'q'):
                            print("Returning to Main Menu...\n")
                            break
                        else:
                            todo = todo.title().strip()
                            functions.append_and_write_todo(todos, new_todo)
                            
                            print(f"Task '{todo}' added.\n")
            except ValueError:
                print('Your command is not valid.')
                continue
            # continue will break out of the lopp and go back a level to ask for the input

        # elif 'complete' in user_action[:9] or user_action[0] in ('c', '2'):
        elif user_action.startswith('complete') or user_action[0] in ('c', '2'):
            todos = functions.read_todos()
            
            if len(user_action.split()) >= 2:
                number_check_a = user_action.split()
                complete_number = number_check_a[1]

                if complete_number.isdigit():
                    try: 
                        complete_todo = complete_number 
                        if int(complete_todo) <= len(todos):
                            index_num = int(complete_todo)-1
                            removed_value = todos[index_num].strip('\n')
                            print(f'Task {removed_value} successfully completed. Removed from TODO list.')
                            todos.pop(int(complete_todo)-1)

                            functions.write_todos(todos)
                        else: 
                            print('\n ############# Invalid task number provided! ############# ')
                    except IndexError:
                        print('\n ############# Invalid task number provided! ############# ')
                        continue

                else: 
                    complete_todo = functions.extract_todo(user_action)

                    if complete_todo + '\n' in todos:
                        item_ix = todos.index(complete_todo + '\n')
                        todos.pop(item_ix)
                        functions.write_todos(todos)

                        print(f'Task {complete_todo} successfully completed. Removed from TODO list.\n')
                    
                    else:
                        print('Syntax error. Item highlighted for completion is not in the TODO list')


            elif len(user_action.split()) < 2:
                print("\n#############################################\nEntering COMPLETE mode...\npress 'b' at any time to return to the Main Menu.\n")
                while True:
                    todo_list = [str(item[:-1]) for item in todos]
                    print("Current items in TODO list: " + " | ".join(todo_list) + "\n")
                    complete_todo = input("Which item has been completed? ").title().strip()
                    if complete_todo.lower().strip() in ('back', 'b', 'quit', 'q'):
                            print("Returning to Main Menu...\n")
                            break
                    elif complete_todo + '\n' in todos:
                        item_ix = todos.index(complete_todo + '\n')
                        todos.pop(item_ix)

                        functions.write_todos(todos)
                        
                        complete_todo = complete_todo.strip('\n')
                        print(f'Task {complete_todo} successfully completed. Removed from TODO list.\n')
                    
                    elif complete_todo.isdigit(): 
                        if int(complete_todo) <= len(todos):
                            index_num = int(complete_todo)-1
                            removed_value = todos[index_num].strip('\n')
                            print(f'Task {removed_value} successfully completed. Removed from TODO list.')
                            todos.pop(int(complete_todo)-1)

                            functions.write_todos(todos)

                        else: 
                            print('Invalid task number provided!')

                    else:
                        print('Item not in todo list!')
                        print(f"Current items: {todos}\n")


        elif user_action.startswith('show') or user_action[0] in ('s', '3'):
            print('------------------------------------------')
            todos = functions.read_todos()

            if len(todos) < 1:
                print('TODO list is currently empty!')
            else: 
                print("Current jobs on the TODO list:")
                for index, item in enumerate(todos, 1):
                    item = item.strip('\n')
                    print(f'{(index)}. {item}')


        elif user_action.startswith('edit') or user_action[0] in ('e', '4'):
            todos = functions.read_todos()

            todo_list = [str(item[:-1]) for item in todos]

            print("Current items in TODO list: " + " | ".join(todo_list) + "\n")


            if len(user_action.split()) >= 2:
                number_check_b = user_action.split()
                edit_number = number_check_b[1]

                if edit_number.isdigit():
                    try:
                        item_ix = int(edit_number) -1
                        old_todo = todos[item_ix]

                        new_todo = input("Enter your new TODO: ").title().strip() +'\n'
                        todos[item_ix] = new_todo

                        functions.write_todos(todos)

                        todos = functions.read_todos()

                        todo_list = [str(item[:-1]) for item in todos]

                        print(f"\nTODO '{old_todo}' replaced with '{new_todo[:-1]}'.\nCurrent TODO list: " + " | ".join(todo_list) + "\n")

                    except IndexError:
                        print('Invalid task number provided!')
                        continue

                else:
                    edit_todo = functions.extract_todo(user_action)

                    item_ix = todos.index(edit_todo + '\n')
                    new_todo = input("Enter your new TODO: ").title().strip() +'\n'
                    todos[item_ix] = new_todo

                    functions.write_todos(todos)

                    todos = functions.read_todos()

                    todo_list = [str(item[:-1]) for item in todos]
                    print(f"TODO '{edit_todo}' replaced with '{new_todo[:-1]}'.\n\nCurrent TODO list: " + " | ".join(todo_list) + "\n")

            elif len(user_action.split()) < 2:
                print("\n#############################################\nEntering EDIT mode...\npress 'b' at any time to return to the Main Menu.\n")
                while True:
                    edit_item = input("Which item would you like to edit? ").title().strip()

                    if edit_item.lower().strip() in ('back', 'b', 'quit', 'q'):
                        print("Returning to Main Menu...\n")
                        break

                    elif edit_item + '\n' in todos:
                        item_ix = todos.index(edit_item + '\n')
                        new_todo = input("Enter your new TODO: ").title().strip() +'\n'
                        todos[item_ix] = new_todo

                        functions.write_todos(todos)

                        todos = functions.read_todos()

                        todo_list = [str(item[:-1]) for item in todos]
                        print(f"TODO '{edit_item}' replaced with '{new_todo[:-1]}'.\nCurrent TODO list: " + " | ".join(todo_list) + "\n")

                    else:
                        print('Item not in todo list!')
                        todos = functions.read_todos()
                        print("Current items in TODO list: " + " | ".join(todo_list) + "\n")

        elif user_action.split() == 'quit' or user_action[0] in ('q', '5'):
            exit('Quitting Application...\n')

        else:
            print("You entered an incorrect command!\n")

if __name__ == "__main__":
    main()

    
