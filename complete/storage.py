import os
import json
from datetime import datetime

path = os.path.join(os.path.dirname(__file__), "..", "file", "tasks.json")


def load_default_tasks():
    file = open(path, "r+")
    data = json.load(file)
    return data


def sort_tasks_by_due_date(tasks):
    def get_due(task):
        try:
            return datetime.strptime(task.get("due_date", ""), "%H:%M %d-%m-%Y")
        except ValueError:
            return datetime.max

    return sorted(tasks, key=get_due)


def add_task(task: str, category: str, due_date: str):
    with open(path, "r+") as file:
        data = json.load(file)
        due_date = due_date or datetime.now().strftime("%H:%M %d-%m-%Y")

        new_task = {
            "task": task,
            "category": category,
            "due_date": due_date,
            "done": False,
        }

        data["default_tasks"].append(new_task)
        data["default_tasks"] = sort_tasks_by_due_date(data["default_tasks"])

        file.seek(0)
        json.dump(data, file, indent=2)
        file.truncate()


def delete_task(position: int):
    with open(path, "r+") as file:
        data = json.load(file)

        data["default_tasks"].pop(position - 1)

        file.seek(0)
        json.dump(data, file, indent=2)
        file.truncate()


def update_task(position: int, task: str, category: str, due_date: str):
    with open(path, "r+") as file:
        data = json.load(file)
        old_task = data["default_tasks"][position - 1]

        updated_task = {
            "task": task or old_task["task"],
            "category": category or old_task["category"],
            "done": old_task["done"],
            "due_date": due_date or old_task["due_date"],
        }

        data["default_tasks"][position - 1] = updated_task
        data["default_tasks"] = sort_tasks_by_due_date(data["default_tasks"])

        file.seek(0)
        json.dump(data, file, indent=2)
        file.truncate()


def toggle_task(position: int):
    with open(path, "r+") as file:
        data = json.load(file)
        old_task = data["default_tasks"][position - 1]

        task = old_task["task"]
        category = old_task["category"]
        due_date = old_task["due_date"]
        done = old_task["done"]

        data["default_tasks"][position - 1] = {
            "task": task,
            "category": category,
            "due_date": due_date,
            "done": not done,
        }

        file.seek(0)
        json.dump(data, file, indent=2)
        file.truncate()
