import json
import requests # type: ignore
import sys

def fetch_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = f'{base_url}/{employee_id}/todos'

    try:
        response = requests.get(todo_url)
        response.raise_for_status()
        todos = response.json()
        if todos:
            employee_name = todos[0]['username']
            total_tasks = len(todos)
            completed_tasks = sum(1 for todo in todos if todo['completed'])

            print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
            for todo in todos:
                print(f"\t{todo['title']} ({'Completed' if todo['completed'] else 'Incomplete'})")

            # Exporting to JSON
            json_data = {
                "USER_ID": [{"task": todo['title'], "completed": todo['completed'], "username": todo['username']} for todo in todos]
            }
            with open(f"{employee_id}.json", "w") as jsonfile:
                json.dump(json_data, jsonfile, indent=4)
                print(f"Data exported to {employee_id}.json")
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("Employee ID should be an integer.")
        sys.exit(1)

    fetch_employee_todo_progress(employee_id)
