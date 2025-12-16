import function
import FreeSimpleGUI as sg


label = sg.Text("Type in your todo: ")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", button_color="blue", size=10)
edit_button = sg.Button("Edit", button_color="blue", size=10)
list_box = sg.Listbox(values=function.get_todos(), key="todos",
                       enable_events=True, size=[45, 10])
complete_button = sg.Button("Complete", button_color="green", size=10)

window = sg.Window("My Todo-App", layout=[
    [label],
    [input_box, add_button], [list_box, edit_button, complete_button]]
) 
while True: 
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = function.get_todos()
            new_todo = value["todo"] + "\n"
            todos.append(new_todo)
            function.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = value["todos"][0]
            new_todo = value["todo"] + "\n"
            todos = function.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            function.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=value["todos"][0])
        case "Complete":
            todo_to_complete = value["todos"][0]
            todos = function.get_todos()
            todos.remove(todo_to_complete)
            function.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exist":
            break
        case sg.WIN_CLOSED:
            break

window.close()

