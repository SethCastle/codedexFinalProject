#To-Do List
list = []
quit = "N"
while quit == "N":
    print("\033[92mTo do list: ", list)
    
    choice = input("\033[0mWhat would you like to do?(add, remove): ")
    if choice == "add":
        new_task = input("Add new task: ")
        list.append(new_task)
        continue
    elif choice == "remove":
        removed_task = input("Remove task: ")
        if removed_task in list:
            list.remove(removed_task)
        else:
            print("\033[31mTask does not exist!!!!\033[0m")
        continue
    quit = input("Quit: Y/N ?: ").upper()
