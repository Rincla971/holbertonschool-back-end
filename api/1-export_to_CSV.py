#!/usr/bin/python3
"""Script to get and export todo list of an employee with REST API"""
import csv
import requests
from sys import argv


def export_csv(id):
    """export data in CSV"""
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    req = requests.get(url, params={"_expand": "user"})
    data = req.json()
    USERNAME = data[0]["user"]["username"]

    with open("{}.csv".format(id), "w", newline="") as file:
        filewriter = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in data:
            filewriter.writerow(
                [id, USERNAME, str(task["completed"]), task["title"]])


if __name__ == "__main__":
    """Main function"""
    if len(argv) != 2:
        print("Usage: python3 {} (int)id_employe".format(__file__))
        exit(1)
    export_csv(argv[1])