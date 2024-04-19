#!/usr/bin/python3
"""Script to export data in JSON format with all users"""

import json
import requests


if __name__ == "__main__":
    api = "https://jsonplaceholder.typicode.com/"
    users = requests.get(api + "users/").json()
    tasks = requests.get(api + "todos/").json()

    all = {}
    for usr in users:
        # absolutely hate this project
        user_id = usr.get("id")
        task_list = [{"task": task.get('title'),
                      "completed": task.get('completed'),
                      "username": usr.get("username")}
                     for task in tasks if user_id == task.get("userId")]
        all[user_id] = task_list

    with open("todo_all_employees.json", "w", newline="") as jsonfile:
        # useless comment again :)
        json.dump(all, jsonfile)
