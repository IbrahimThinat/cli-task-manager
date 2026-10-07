"""
Tiny CLI Notes App — built on purpose to practice Git.
Run it with: python main.py
"""

from notes import add_note, list_notes, delete_note


def print_menu():
    print("\n=== Notes App ===")
    print("1. Add note ##")
    print("2. List notes")
    print("3. Delete note")
    print("4. Quit")


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