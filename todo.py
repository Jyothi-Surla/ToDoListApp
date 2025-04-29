TASKS_FILE = "todo.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def show_tasks(tasks):
    if not tasks:
        print("\n✅ No tasks yet!")
    else:
        print("\n📋 Your To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added!")

def mark_task_completed(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            number = int(input("\nEnter task number to mark as completed: "))
            if 1 <= number <= len(tasks):
                tasks[number - 1] = "[DONE] " + tasks[number - 1]
                save_tasks(tasks)
                print("✅ Task marked as completed!")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def delete_task(tasks):
    show_tasks(tasks)
    if tasks:
        try:
            number = int(input("\nEnter task number to delete: "))
            if 1 <= number <= len(tasks):
                removed_task = tasks.pop(number - 1)
                save_tasks(tasks)
                print(f"🗑️ Task '{removed_task}' deleted!")
            else:
                print("⚠️ Invalid task number.")
        except ValueError:
            print("⚠️ Please enter a valid number.")

def clear_all_tasks(tasks):
    confirm = input("\n⚠️ Are you sure you want to delete all tasks? (yes/no): ")
    if confirm.lower() in ("yes", "y"):
        tasks.clear()
        save_tasks(tasks)
        print("🧹 All tasks cleared!")
    else:
        print("❎ Cancelled.")

def main():
    tasks = load_tasks()

    while True:
        print("\n📝 To-Do List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Clear All Tasks")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            clear_all_tasks(tasks)
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    main()

