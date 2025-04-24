import os
import json

path = os.path.join(os.path.dirname(__file__), "..", "file", "tasks.json")


def load_default_tasks():
    file = open(path, "r+")
    data = json.load(file)
    return data


def add_task(task: str, category: str):
    with open(path, "r+") as file:
        data = json.load(file)
        new_task = {"task": task, "category": category, "done": False}

        data["default_tasks"].append(new_task)

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


def update_task(position: int, task: str, category: str):
    with open(path, "r+") as file:
        data = json.load(file)

        data["default_tasks"][position - 1] = {
            "task": task,
            "category": category,
            "done": False,
        }

        file.seek(0)
        json.dump(data, file, indent=2)
        file.truncate()


def toggle_task(position: int):
    with open(path, "r+") as file:
        data = json.load(file)

        task = data["default_tasks"][position - 1]["task"]
        category = data["default_tasks"][position - 1]["category"]
        done = data["default_tasks"][position - 1]["done"]
        data["default_tasks"][position - 1] = {
            "task": task,
            "category": category,
            "done": not done,
        }

        file.seek(0)
        json.dump(data, file, indent=2)
        file.truncate()
