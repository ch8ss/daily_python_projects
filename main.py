def get_todos():
    with open('todos.txt', 'r') as file:
        todos = file.readlines()
    return todos


while True:
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print('Invalid Command')
            continue
        except IndexError:
            print("No such todo item.")
            continue

    elif user_action.startswith('show'):
        todos = get_todos()
        new_todos = [item.strip('\n') for item in todos]

        print("Total number of tasks:", len(todos))
        for index, item in enumerate(new_todos):
            row = f"{index + 1}. {item}"
            print(row)

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todo_to_remove = todos.pop(number - 1).strip('\n')

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

            message = f"Todo '{todo_to_remove}' was removed from the list."
            print(message)

        except ValueError:
            print("Invalid Command")
            continue
        except IndexError:
            print("No such todo item.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print('Invalid Command')

print("Bye see ya!")