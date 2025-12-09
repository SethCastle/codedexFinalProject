#To-Do List
#list = []
try:
# Read file todo.txt and populate list
    with open('todo.txt', 'r') as file:
        list = file.read().splitlines()
except FileNotFoundError:
    print("\033[31mtodo.txt does not exist!!!!\033[0m")

quit = "N"
while quit == "N":
    print("\033[92mTo do list: ", list)
    
    choice = input("\033[0mWhat would you like to do?(add, remove): ")
    if choice == "add":
        new_task = input("Add new task: ")
        list.append(new_task.lower())
        #continue
    elif choice == "remove":
        removed_task = input("Remove task: ").lower()
        if removed_task in list:
            list.remove(removed_task)
        else:
            print("\033[31mTask does not exist!!!!\033[0m")
        #continue
    else:
        print("\033[31mCommand does not exist!!!!\033[0m")
    quit = input("Quit: Y/N ?: ").upper()
    if quit != "Y" or quit != "N":
        print("\033[31mYou have entered an invalid answer!!!! SETTING TO QUIT!!!!\033[0m")
        quit = "Y"
#save the list into a todo.txt
with open("todo.txt", "w") as file:
    for items in list:
        file.write(items + "\n")
