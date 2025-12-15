import function
import FreeSimpleGUI as sg


label = sg.Text("Type in your todo: ")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", button_color="blue", size=10)
window = sg.Window("My Todo-App", layout=[
    [label],
    [input_box, add_button]
])  
window.read()
window.close()

