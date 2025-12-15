from function import get_todos, write_todos

user_prompt = "Type add, show or Exit "
todos = []
while True:
    user_action = input(user_prompt)
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"
        #todos.append(todo)
        """file = open("todos.txt", "a")
        file.writelines(todo)
        file.close()"""

        with open("todos.txt", "a") as file:
            file.writelines(todo)
    elif user_action.startswith("show"): 
        todos = get_todos("todos.txt")
        for index, item in enumerate(todos):
            print(f" {index +1} - {item}")
    elif user_action.startswith("edit"):
        try:
            todos = get_todos("todos.txt")
            for todo in todos:
                print(f"{todos.index(todo) + 1}. {todo}")
            number = int(user_action[5:])
            number = number - 1
            new_todo = input("Enter the new todo: ") + "\n"
            todos[number] = new_todo
            write_todos("todos.txt", todos)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith("complete"):
        try:    
            todos = get_todos("todos.txt")
        
            for index, todo in enumerate(todos):
                print(f"{index +1} - {todo}")
            complete_todo = int(user_action[9:])
            todos.pop(complete_todo - 1)
            write_todos("todos.txt", todos)
        except IndexError:
            print("No item with that number.")
            continue
    elif user_action.startswith("exit"):
        break        
    else:
        print("Unknown command. Please type add, show or Exit.")
        

print("Goodbye!")
