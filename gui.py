import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


sg.theme("Black")
clock = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key="todo")
add_button = sg.Button("Add")
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
list_box = sg.Listbox(functions.get_todos(), key="todos", enable_events=True, size=(45, 10))
window = sg.Window("My to-do App",
                   [[clock],
                    [label],
                    [input_box, add_button],
                    [list_box, edit_button, complete_button],
                    [exit_button]],
                   font=("Helvetica", 10))
while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please Select an item first", font=("Helvetica", 20))
        case "Complete":
            try:
                todos_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todos_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Please Select an item first", font=("Helvetica", 20))
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break
window.close()
