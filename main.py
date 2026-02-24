Todos = []

while True:
    user_action = input("Type add, edit, show or exit: ")
    user_action = user_action.strip()  # ignores spaces

    match user_action:
        case 'add':
            Todo = input("Add a new task: ")
            Todos.append(Todo)
        case 'edit':
            number = int(input('number of the task to be edited: '))
            number = number - 1  # ensures that the numbering starts from 1, not 0
            new_todo = input('Enter new todo: ')
            Todos[number] = new_todo
        case 'show' | 'display':  # bitwise op. can use either show or display
            for index, item in enumerate(Todos):
                item = item.title()  # capitalizes the first letter
                print(index, '.', item)
        case 'exit':
            break
        case tf:
            print("Invalid")

print("Bye see ya!")


