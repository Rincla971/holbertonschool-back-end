import json
import requests # type: ignore

def fetch_all_employees_todo():
    base_url = 'https://jsonplaceholder.typicode.com/users'
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        employees = response.json()
        
        all_employees_tasks = {}
        
        for employee in employees:
            employee_id = employee['id']
            username = employee['username']
            todo_url = f'{base_url}/{employee_id}/todos'
            response = requests.get(todo_url)
            response.raise_for_status()
            todos = response.json()
            employee_tasks = [{"username": username, "task": todo['title'], "completed": todo['completed']} for todo in todos]
            all_employees_tasks[employee_id] = employee_tasks
        
        with open("todo_all_employees.json", "w") as jsonfile:
            json.dump(all_employees_tasks, jsonfile, indent=4)
        print("Data exported to todo_all_employees.json")
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)

if __name__ == "__main__":
    fetch_all_employees_todo()
