while True:
    user_action = input("Type add, show, edit, or exit: ")
    user_action = user_action.strip()
    FILEPATH = "to do 2.txt"
    if user_action.startswith("add"):
        todo = user_action[4:].strip() + "\n"
        with open(FILEPATH, "r") as file:
            todos = file.readlines()
        todos.append(todo)
        with open(FILEPATH, "w") as file:
            file.writelines(todos)
    elif user_action.startswith("show"):
        with open(FILEPATH, 'r') as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1} - {item}")
    elif user_action.startswith("edit"):
       try:
        number = int(user_action[5:].strip()) - 1

        with open(FILEPATH, "r") as file:
            todos = file.readlines()

        new_todo = input("Enter a new todo: ").strip() + "\n"
        todos[number] = new_todo

        with open(FILEPATH, "w") as file:
            file.writelines(todos)

        print("Task updated successfully.")

       except ValueError:
           print("Please provide a number. Example: edit 2")
       except IndexError:
           print("There is no task with that number.")

    elif user_action == "exit":
        break
    else:
        print("Command is not valid")
print("Bye!")
