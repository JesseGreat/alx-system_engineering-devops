#!/usr/bin/python3
# This script prints out an employee to do list progress.

import requests
import sys

# parameter that takes in the employee id
employee_id = sys.argv[1]

# Get Employee information
employee_info = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()

# Get employer to_do list
todo_lists = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}').json()

# Get no of tasks completed that is TRUE
no_of_completed_tasks = sum(no_of_tasks['completed']
        for no_of_tasks in todo_lists)

# Print progress report
print(f"Employee {employee_info['name']} is done with {no_of_completed_tasks}/{len(todo_lists)} tasks:")
for no_of_tasks in todo_lists:
    if no_of_tasks['completed']:
        print(f"\t{no_of_tasks['title']}")
