import streamlit as st
import functions
import os

# Set the title and introduction text
st.title("ToDo App")
st.write("This app will help you to increase your productivity.")

# Check if the 'todos.txt' file exists; if not, create an empty file
if not os.path.exists("files/todos.txt"):
    with open("files/todos.txt", 'w') as file:
        pass

# Display checkboxes for existing tasks
todos = functions.get_todos()

# Iterate through the todos, displaying checkboxes and processing user interactions
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]

        # Rerun the Streamlit app to reflect the changes
        st.rerun()


# Provide an input field to add new tasks
st.text_input(label="", placeholder="Add new todo", on_change=functions.add_todo, key="new_todo")
