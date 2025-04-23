import os
import json


def load_default_tasks():
    path = os.path.join(os.path.dirname(__file__), "..", "file", "tasks.json")
    file = open(path,"r+")
    data = json.load(file)
    return data

load_default_tasks()