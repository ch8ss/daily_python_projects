while True:
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.strip()  # ignores spaces

    match user_action:
        case 'add':
            Todo = input("Add a new task: ") + "\n"
            file = open('todo.txt','r')
            Todos = file.readlines()
            file.close()

            Todos.append(Todo)

            file = open('todo.txt','w')
            file.writelines(Todos)
            file.close()

        case 'edit':
            number = int(input('number of the task to be edited: '))
            number = number - 1  # ensures that the numbering starts from 1, not 0
            new_todo = input('Enter new todo: ')
            Todos[number] = new_todo
        case 'show' | 'display':  # bitwise op. can use either show or display
            print("Total number of tasks:", len(Todos))
            for index, item in enumerate(Todos):
                row = f"{index+1}.{item}"
                print(row)
        case 'complete':
            num = int(input('number of the completed task: '))
            Todos.pop(num-1)

        case 'exit':
            break
        case tf:
            print("Invalid")

print("Bye see ya!")


