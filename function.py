def get_todos(filepath):
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local
def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("This is a module for todo functions.")