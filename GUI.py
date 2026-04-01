import FreeSimpleGUI as sg

import functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window(
    "My To-Do App",
    layout=[[label],
            [input_box, add_button],
            [list_box, edit_button, complete_button],
            [exit_button]],
    font=("Helvetica", 20))

while True:
    event, values = window.read()
    match event:
        case "todos":
            if values['todos']:
                window['todo'].update(value=values['todos'][0].strip())
        case "Add":
            new_todo = values['todo'].strip()
            if new_todo:
                todos = functions.get_todos()
                todos.append(new_todo + "\n")
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
        case "Edit":
            if not values['todos']:
                sg.popup("Please select a to-do to edit.")
                continue
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'].strip()
            if not new_todo:
                sg.popup("Input cannot be empty.")
                continue
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo + "\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Complete":
            if not values['todos']:
                sg.popup("Please select a to-do to complete.")
                continue
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Exit" | sg.WINDOW_CLOSED:
            break

window.close()
