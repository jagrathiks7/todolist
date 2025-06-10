def show_menu():
    print("\n--- TO-DO LIST ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def main():
    tasks = load_tasks()
    
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            if not tasks:
                print("No tasks yet.")
            else:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter a new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added.")

        elif choice == "3":
            if not tasks:
                print("No tasks to remove.")
                continue
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                index = int(input("Enter the task number to remove: ")) - 1
                removed = tasks.pop(index)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            except (IndexError, ValueError):
                print("Invalid selection.")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
