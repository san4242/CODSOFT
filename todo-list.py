# create an empty list to store the tasks:
tasks = []

# Function for adding a task:
def add_task(task):
    tasks.append(task)
    print("Task added successfully~")

# Function for removing a task:
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully~")
    else:
        print("Task is not present in the list.")

# Function to view all tasks:
def view_tasks():
    if tasks:
        print("Your to-do list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

# Main function
def main():
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == '3':
            view_tasks()
        elif choice == '4':
            print("Have a nice day!")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()
