import functions
import PySimpleGUI as gui

label = gui.Text("Type in a To-Do Item: ")
input_box = gui.InputText(tooltip="Enter A To-Do Item")
add_button = gui.Button('Add Item')

window = gui.Window("To-Do Application", layout=[[label], [input_box, add_button]])

window.read()
window.close()