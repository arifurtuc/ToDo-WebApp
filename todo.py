import streamlit as st
import functions

# Set the title and introduction text
st.title("ToDo App")
st.write("This app will help you to increase your productivity.")

# Display checkboxes for existing tasks
todos = functions.get_todos()
for todo in todos:
    st.checkbox(todo)


# Provide an input field to add new tasks
st.text_input(label="", placeholder="Add new todo")
