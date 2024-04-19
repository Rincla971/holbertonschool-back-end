#!/usr/bin/python3
"""Script to export data in the JSON format."""

import json
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]

    api = "https://jsonplaceholder.typicode.com/"
    user = requests.get(api + "users/", params={"id": employee_id}).json()
    tasks = requests.get(api + "todos/", params={"userId": employee_id}).json()

    username = user[0].get("username") if len(user) > 0 else None
    task_list = [{"task": task.get('title'),
                  "completed": task.get('completed'),
                  "username": username} for task in tasks]

    with open("{}.json".format(employee_id), "w", newline="") as jsonfile:
        # useless comment again
        json.dump({employee_id: task_list}, jsonfile)
