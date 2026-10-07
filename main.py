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
    notes = []
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            text = input("Note text: ")
            add_note(notes, text)
        elif choice == "2":
            list_notes(notes)
        elif choice == "3":
            index = input("Note number to delete: ")
            delete_note(notes, index)
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()