print("1. Add Task")
print("2. View Tasks")
print("3. Remove Task")
print("4. Quit")
tasks = []
choice = int(input("Choice: "))
if choice == 4:
    print("Come back when you're ready")
while choice != 4:
    if choice == 1:
        newTask = input("Enter task: ")
        tasks.append(newTask)
    elif choice == 2:
        print("Tasks: ")
        taskNumber = 1
        for task in tasks:
            print(str(taskNumber) + ".  " + task)
            taskNumber+=1
            print()
    elif choice == 3:
        taskRemove = int(input("Which task do you want to remove? "))
        tasks.pop(taskRemove - 1)
    
