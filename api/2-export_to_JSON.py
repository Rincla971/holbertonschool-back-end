#!/usr/bin/python3
"""Script to get and export todo list in JSON of an employee with REST API"""
import json
import requests
from sys import argv


def export_json(id):
    """export data in json"""
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    req = requests.get(url, params={"_expand": "user"})
    data = req.json()

    USER_TASK = {id: []}
    for task in data:
        task_dictionary = {
            "task": task["title"],
            "completed": task["completed"],
            "username": task["user"]["username"]
        }
        USER_TASK[id].append(task_dictionary)
    with open("{}.json".format(id), "w") as file:
        json.dump(USER_TASK, file)


if __name__ == "__main__":
    """Main function"""
    if len(argv) != 2:
        print("Usage: python3 {} (int)id_employe".format(__file__))
        exit(1)
    export_json(argv[1])