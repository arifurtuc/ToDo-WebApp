import streamlit as st

# Set the title and introduction text
st.title("ToDo App")
st.write("This app will help you to increase your productivity.")

# Display checkboxes for existing tasks
st.checkbox("Todo 1")
st.checkbox("Todo 2")
st.checkbox("Todo 3")
st.checkbox("Todo 4")

# Provide an input field to add new tasks
st.text_input(label="", placeholder="Add new todo")