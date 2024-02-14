import config.config as conf
import os
def check_if_todos_exist():
    """
    checks if todos file exists and creates it if it doesnt exist
    :return:
    """
    if not os.path.exists(conf.FILEPATH):
        with open(conf.FILEPATH, "w") as file:
            pass

def get_todos(filepath=conf.FILEPATH):
    """
    read the todo items textfile
    :param filepath: not required default can be edited in config
    :return: a list of todo items
    """
    check_if_todos_exist()
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos, filepath=conf.FILEPATH):
    """
    wright to the todo items file
    :param todos: required
    :param filepath: not required default can be edited in the config
    :return: no return value
    """
    check_if_todos_exist()
    with open(filepath, 'w') as file:
        file.writelines(todos)
