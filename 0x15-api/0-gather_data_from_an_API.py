#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
import sys

# parameter that takes in the employee id
employee_id = sys.argv[1]

# Get Employee information
employee_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)).json()

# Get employer to_do list
todo_lists = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)).json()

# Get no of tasks completed that is TRUE
no_of_completed_tasks = sum(no_of_tasks['completed'] for no_of_tasks in todo_lists)

# Print progress report
print("Employee {} is done with tasks({}/{}):".format(employee_info['name'], no_of_completed_tasks, len(todo_lists)))
for no_of_tasks in todo_lists:
    if no_of_tasks['completed']:
        print("\t {}".format(no_of_tasks['title']))
