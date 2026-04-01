FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    try:
        with open(filepath, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def write_todos(todos, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos)

def show_todos():
    todos = get_todos()
    print(f"\nTotal number of tasks: {len(todos)}")

    if not todos:
        print("No tasks found.\n")
        return

    for index, todo in enumerate(todos, start=1):
        print(f"{index}. {todo.strip()}")
    print()

def add_todo(todo_text):
    if not todo_text:
        print("Cannot add an empty todo.")
        return

    todos = get_todos()
    todos.append(todo_text + "\n")
    write_todos(todos)
    print(f"Added: {todo_text}")

def edit_todo(number, new_text=None):
    todos = get_todos()

    if number < 1 or number > len(todos):
        print("No such todo item.")
        return

    if new_text is None:
        new_text = input("Enter new todo: ").strip()
    if not new_text:
        print("Todo cannot be empty.")
        return

    todos[number - 1] = new_text + "\n"
    write_todos(todos)
    print("Todo updated.")

def complete_todo(number):
    todos = get_todos()

    if number < 1 or number > len(todos):
        print("No such todo item.")
        return

    removed = todos.pop(number - 1).strip()
    write_todos(todos)
    print(f"Todo '{removed}' was removed from the list.")