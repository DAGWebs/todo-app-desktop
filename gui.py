import functions
import PySimpleGUI as gui

gui.theme("DarkTeal6")
label = gui.Text("Type in a To-Do Item: ")
input_box = gui.InputText(tooltip="Enter A To-Do Item", key="todo")
add_button = gui.Button('➕ Add Item')

list_box = gui.Listbox(values=functions.get_todos(), key='todos', enable_events=True, size=[45, 10])
edit_button = gui.Button("✏ Edit")

complete_button = gui.Button("✔ Complete")

layout =[
        [label],
        [input_box, add_button],
        [list_box, edit_button],
        [complete_button]
    ],

window = gui.Window(
    "To-Do Application",
    layout,
    font=('Helvetica', 20)
)
while True:
    event, values = window.read()
    match event:
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "➕ Add Item":
            values['todo'].strip("\n")
            if values['todo'] != "" and values['todo'] != '\n' and values['todo'] != " ":
                todos = functions.get_todos()
                todos.append(values['todo'] + "\n")
                functions.write_todos(todos)
                window['todo'].update(value="")
                window['todos'].update(values=todos)
        case "✏ Edit":
            try:
                todo = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                gui.popup("You must select one of your todo list items.", font=('Helvetica', 20))
        case "✔ Complete":
            try:
                todo = values['todos'][0]
                todos = functions.get_todos()
                index = todos.index(todo)
                todos.pop(index)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                gui.popup("You must select one of your todo list items.", font=('Helvetica', 20))
        case gui.WIN_CLOSED:
            break

window.close()