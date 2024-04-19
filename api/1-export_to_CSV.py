#!/usr/bin/python3
"""This script export data in CSV format"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]

    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/", params={"id": employee_id}).json()
    tasks = requests.get(url + "todos/", params={"userId": employee_id}).json()

    username = user[0].get("username") if len(user) > 0 else None
    rows = [[employee_id, username, task.get('completed'), task.get('title')]
            for task in tasks]

    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        # useless comment
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        writer.writerows(rows)
