"""
Note-handling functions, kept separate from main.py on purpose
so you have two files to practice conflicts/merges with.
"""


def add_note(notes, text):
    notes.append(text)
    print(f"Added: {text}")


def list_notes(notes):
    if not notes:
        print("No notes yet.$$")
        return
    for i, note in enumerate(notes, start=1):
        print(f"{i}. {note}")


def delete_note(notes, index):
    try:
        i = int(index) - 1
        removed = notes.pop(i)
        print(f"Deleted: {removed}")
    except (ValueError, IndexError):
        print("Invalid note number.")