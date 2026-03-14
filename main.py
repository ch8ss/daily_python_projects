FILEPATH = "todos.txt"


def get_todos(filepath="todos.txt"):
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
    for index, todo in enumerate(todos, start=1):
        print(f"{index}. {todo.strip()}")
    print()


while True:
    user_action = input("Type add, edit, show, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()
        if todo == "":
            print("Cannot add an empty todo.")
            continue

        todos = get_todos()
        todos.append(todo + "\n")
        write_todos(todos)
        print(f"Added: {todo}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:].strip()) - 1
            todos = get_todos()

            if number < 0 or number >= len(todos):
                print("No such todo item.")
                continue

            new_todo = input("Enter new todo: ").strip()
            if new_todo == "":
                print("Todo cannot be empty.")
                continue

            todos[number] = new_todo + "\n"
            write_todos(todos)
            print("Todo updated.")

        except ValueError:
            print("Invalid command. Use: edit <number>")

    elif user_action == "show":
        show_todos()

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:].strip()) - 1
            todos = get_todos()

            if number < 0 or number >= len(todos):
                print("No such todo item.")
                continue

            removed = todos.pop(number).strip()
            write_todos(todos)
            print(f"Todo '{removed}' was removed from the list.")

        except ValueError:
            print("Invalid command. Use: complete <number>")

    elif user_action == "exit":
        break

    else:
        print("Invalid command.")

print("Bye see ya!")