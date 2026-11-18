from taskmanager import TaskManager


def read_id():
    raw = input("Task ID: ").strip()
    return int(raw) if raw.isdigit() else None


def show(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
    for task in tasks:
        mark = "x" if task["done"] else " "
        print(f"[{mark}] {task['id']}. {task['title']}")


def main():
    manager = TaskManager()
    while True:
        print()
        print("1. Add  2. Show  3. Complete  4. Delete  5. Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                manager.add_task(input("Title: "))
                print("Task added.")
            except ValueError as error:
                print(error)
        elif choice == "2":
            show(manager)
        elif choice == "3":
            result = manager.complete_task(read_id())
            print("Done." if result else "No task with that ID.")
        elif choice == "4":
            result = manager.delete_task(read_id())
            print("Deleted." if result else "No task with that ID.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
