tasks = []

def add_task(task):
    tasks.append(task)
    print("Task",task," added to your To-DO List.")

def update_task(index, new_task):
    if 1 <= index <= len(tasks):
        tasks[index - 1] = new_task
        print("Task",index," updated to", new_task)
    else:
        print("Invalid task index.")

def display_task():
    if tasks:
        print("To-Do List:")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
    else:
        print("To-Do List is empty.")


def delete_task(index, task):
    try:
        del tasks[index -1]
        #tasks.save_task()
    except IndexError:
        print("invalid task number.")
        

def main():
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Update task")
        print("3. Display tasks")
        print("4. Delete tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == "2":
            index = int(input("Enter the task number to update: "))
            new_task = input("Enter the new task: ")
            update_task(index, new_task)
        elif choice == "3":
            display_task()
        elif choice == "4":
            index = int(input("Enter the task number to delete: "))
            del_task = input("Enter the del task: ")
            delete_task(index, del_task)
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid choice")


if __name__== "__main__":
    main()










