while True:
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:]

        with open('todo.txt','r') as file:
            todos = file.readlines()

        todos.append(todo + '\n')

        with open('todo.txt','w') as file:
            file.writelines(todos)

    elif 'edit' in user_action:
        number = int(user_action[5:])
        print(number)

        number = number - 1

        with open('todo.txt','r') as file:
            todos = file.readlines()

        new_todo = input('Enter new todo: ')
        todos[number] = new_todo + '\n'

        with open('todo.txt','w') as file:
            file.writelines(todos)

    elif 'show' in user_action or 'display' in user_action:
        with open('todo.txt','r') as file:
            todos = file.readlines()

        new_todos = [item.strip('\n') for item in todos]

        print("Total number of tasks:", len(todos))
        for index, item in enumerate(new_todos):
            row = f"{index+1}. {item}"
            print(row)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('todo.txt','r') as file:
            todos = file.readlines()

        todos.pop(number-1)

        with open('todo.txt','w') as file:
            file.writelines(todos)

    elif 'exit' in user_action:
        break
    else:
        print('Invalid Command')

print("Bye see ya!")