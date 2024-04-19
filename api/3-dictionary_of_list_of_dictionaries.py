#!/usr/bin/python3
"""Script to get and export todo list in JSON of an employee with REST API"""
import json
import requests


def export_all_JSON():
    """export all data to JSON"""
    url = "https://jsonplaceholder.typicode.com"
    req = requests.get("{}/users".format(url))
    data = req.json()
    user_task = {}
    for user in data:
        tasks = requests.get(
            "{}/users/{}/todos".format(url, user['id'])).json()

        user_task[user["id"]] = []
        for task in tasks:
            task_dictionnary = {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            user_task[user["id"]].append(task_dictionnary)
    with open("todo_all_employees.json", "w") as file:
        json.dump(user_task, file)


if __name__ == "__main__":
    export_all_JSON()