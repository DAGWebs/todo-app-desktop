import config.config as conf

def get_todos(filepath=conf.FILEPATH):
    """
    read the todo items textfile
    :param filepath: not required default can be edited in config
    :return: a list of todo items
    """
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
    with open(filepath, 'w') as file:
        file.writelines(todos)

print(get_todos())