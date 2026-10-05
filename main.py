import sys
from storage import load_tasks, save_tasks

def add_task(title):
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "status": "pending"
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Added task #{new_task['id']}: '{title}'")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour Tasks:")
    for t in tasks:
        status = "[x]" if t["status"] == "done" else "[ ]"
        print(f"{t['id']}. {status} {t['title']}")
    print()

def complete_task(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = "done"
            save_tasks(tasks)
            print(f"Marked task #{task_id} as completed!")
            return
    print(f"Task #{task_id} not found.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [add <title> | list | complete <id>]")
        return

    command = sys.argv[1].lower()
    if command == "add" and len(sys.argv) > 2:
        title = " ".join(sys.argv[2:])
        add_task(title)
    elif command == "list":
        list_tasks()
    elif command == "complete" and len(sys.argv) > 2:
        try:
            task_id = int(sys.argv[2])
            complete_task(task_id)
        except ValueError:
            print("Error: Task ID must be a number.")
    else:
        print("Unknown or incomplete command.")

if __name__ == "__main__":
<<<<<<< HEAD
    main()
=======
    main()
        
>>>>>>> 2c6d07e (resolve conflict between format a and foramt b)
