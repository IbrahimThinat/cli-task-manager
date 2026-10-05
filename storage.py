import json
import os

DB_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(DB_FILE, "w") as file:
        json.dump(tasks, file, indent=4)