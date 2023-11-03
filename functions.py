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
