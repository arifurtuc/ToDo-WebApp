import streamlit as st

# Define the file path for the todos file
FILEPATH = 'files/todos.txt'


def get_todos(filepath=FILEPATH):
    """
    Retrieve a list of todos from a text file.

    :param filepath: The path to the text file containing todos.
    :return: A list of todos.
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
        return todos


def write_todos(todos, filepath=FILEPATH):
    """
    Write a list of todos to a text file.

    :param todos: A list of todos to write to the file.
    :param filepath: The path to the text file where todos will be written.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos)


def add_todo():
    """
    Add a new todo to the list of existing todos.

    The new todo is obtained from the Streamlit session state.
    """
    # Retrieve the current list of todos
    todos = get_todos()

    # Get the new todo from the Streamlit session state and append it to the list
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)

    # Write the updated list of todos back to the file
    write_todos(todos)

    # Clear the text input field value
    st.session_state["new_todo"] = ""
