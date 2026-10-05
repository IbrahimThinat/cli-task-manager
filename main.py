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
        print(f"[{t['id']}] -> {status} Task: {t['title']}")
    print()

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [add <title> | list]")
        return

    command = sys.argv[1].lower()
    if command == "add" and len(sys.argv) > 2:
        title = " ".join(sys.argv[2:])
        add_task(title)
    elif command == "list":
        list_tasks()
    else:
        print("Unknown or incomplete command.") 

if __name__ == "__main__":
    main()
    ##iby 