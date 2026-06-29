tasks = []

while True:
    print("\n TO-DO LIST ")
    print("1. View tasks")
    print("2. Add task")
    print("3. Update task")
    print("4. Delete task")
    print("5. Exit")

    option = input("Enter option: ")

    if option == "1":
        if len(tasks) == 0:
            print("No tasks")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif option == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task updated")

    elif option == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            num = int(input("Enter task number to update: "))
            if num >= 1 and num <= len(tasks):
                new_task = input("Enter new task: ")
                tasks[num-1] = new_task
                print("Task updated")
            else:
                print("Invalid number.")

    elif option == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            num = int(input("Enter task number to delete: "))
            if num >= 1 and num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid")

    elif option == "5":
        print("thank you")
        break

    else:
        print("Invalid")
