from functions import add_todo, show_todos, edit_todo, complete_todo

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
            try:
                edit_todo(int(parts[1]))
            except:
                print("Invalid command. Use: edit <number>")

        elif command == "show":
            show_todos()

        elif command == "complete":
            try:
                complete_todo(int(parts[1]))
            except:
                print("Invalid command. Use: complete <number>")

        elif command == "exit":
            print("Bye see ya!")
            break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()