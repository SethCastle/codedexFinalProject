#To-Do List
list = []
quit = "N"
while quit == "N":
    print("To do list: ", list)
    quit = input("Quit: Y/N ?: ").upper()
    choice = input("What would you like to do?(add, remove): ")
    if choice == "add":
        new_task = input("Add new task: ")
        list.append(new_task)
        continue
    elif choice == "remove":
        removed_task = input("Remove task: ")
        list.remove(removed_task)
        continue