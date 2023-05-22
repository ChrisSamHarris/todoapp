# Organising the code into Modules.
persistent_filepath = "files/todos.txt"

def read_todos(filepath=persistent_filepath):
    """Reads the existing/persistant TODO file and updates the variable"""
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local

def append_and_write_todo(todo_list, new_todo):
    """Updates todos with the new todo value and recreates the TODO.txt file with the new todo appended onto the list"""
    todo_list.append(new_todo.title().strip() + '\n')
    write_todos(todo_list)

def write_todos(todo_list, filepath=persistent_filepath):
    """Recreates the TODO.txt file with current todos list"""
    with open(filepath, 'w') as file:
        file.writelines(todo_list)

def extract_todo(user_action):
    """Extracts the subject TODO if the given user argument in longer than one word - only operates from the Main Menu"""
    user_action = user_action.split()
    todo_words = user_action[1:]
    todo_item = ' '.join(todo_words).title().strip()
    return todo_item

if __name__ == "__main__":
    # Will only run when functions.py is EXPLICTLY ran. 
    print('Functions loaded successfully.')