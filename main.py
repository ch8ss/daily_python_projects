FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """Read todos from file and return them as a list."""
    try:
        with open(filepath, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def write_todos(todos, filepath=FILEPATH):
    """Write the todo list to file."""
    with open(filepath, "w") as file:
        file.writelines(todos)


def show_todos():
    """Display all todos with numbering."""
    todos = get_todos()
    print(f"\nTotal number of tasks: {len(todos)}")

    if not todos:
        print("No tasks found.\n")
        return

    for index, todo in enumerate(todos, start=1):
        print(f"{index}. {todo.strip()}")
    print()


def add_todo(todo_text):
    """Add a new todo item."""
    if not todo_text:
        print("Cannot add an empty todo.")
        return

    todos = get_todos()
    todos.append(todo_text + "\n")
    write_todos(todos)
    print(f"Added: {todo_text}")


def edit_todo(number):
    """Edit an existing todo item."""
    todos = get_todos()

    if number < 1 or number > len(todos):
        print("No such todo item.")
        return

    new_todo = input("Enter new todo: ").strip()
    if not new_todo:
        print("Todo cannot be empty.")
        return

    todos[number - 1] = new_todo + "\n"
    write_todos(todos)
    print("Todo updated.")


def complete_todo(number):
    """Remove a completed todo item."""
    todos = get_todos()

    if number < 1 or number > len(todos):
        print("No such todo item.")
        return

    removed = todos.pop(number - 1).strip()
    write_todos(todos)
    print(f"Todo '{removed}' was removed from the list.")


def main():
    while True:
        user_action = input("Type add, edit, show, complete or exit: ").strip()

        if not user_action:
            print("Please enter a command.")
            continue

        parts = user_action.split(maxsplit=1)
        command = parts[0].lower()

        if command == "add":
            if len(parts) < 2:
                print("Usage: add <todo>")
                continue
            add_todo(parts[1].strip())

        elif command == "edit":
            if len(parts) < 2:
                print("Usage: edit <number>")
                continue
            try:
                number = int(parts[1])
                edit_todo(number)
            except ValueError:
                print("Invalid command. Use: edit <number>")

        elif command == "show":
            show_todos()

        elif command == "complete":
            if len(parts) < 2:
                print("Usage: complete <number>")
                continue
            try:
                number = int(parts[1])
                complete_todo(number)
            except ValueError:
                print("Invalid command. Use: complete <number>")

        elif command == "exit":
            print("Bye see ya!")
            break

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()