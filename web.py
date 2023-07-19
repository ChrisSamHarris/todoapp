# Ran with: streamlit run web.py 
import functions
import streamlit as st
# https://docs.streamlit.io/library/cheatsheet#build-chat-based-apps


todo_list = functions.read_todos()
def add_todo():
    # session_state = Almost a dictionary of data - useful for debugging
    new_todo = st.session_state["new_todo"]
    print(new_todo)
    todo_list.append(new_todo.strip() + '\n')
    functions.write_todos(todo_list)

# def complete_todo():
#     completed_todo = 

st.title("My TODO App")
st.write("This is an Application designed to increase your productivity.")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        print(index, todo)
        todo_list.pop(index)
        functions.write_todos(todo_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text('\n')
st.text_input(label='new_todo', label_visibility='hidden',  key='new_todo', placeholder='Enter a new TODO...', on_change=add_todo)
print(st.session_state)

# item needs a key in order to display in the session state
# st.session_state

