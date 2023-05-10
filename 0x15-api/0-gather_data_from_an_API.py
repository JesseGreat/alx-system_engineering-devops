#!/usr/bin/python3
"""
Script that uses this REST API, for a given employee ID, to gather information
about his/her TODO list progress.
"""
import requests
import sys


if __name__ == '__main__':
    # Get employee ID from command line arguments
    employee_id = sys.argv[1]

    # Get employee information
    employee_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    ).json()

    # Get employee's to-do list
    todo_lists = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format
        (employee_id)).json()

    # Count number of tasks completed
    num_tasks_completed = sum(
        task['completed'] for task in todo_lists
    )

    # Print progress report
    print('Employee {} is done with tasks({}/{}):'.format(
        employee_info['name'], num_tasks_completed, len(todo_lists)
    ))

    for task in todo_lists:
        if task['completed']:
            print('\t {}'.format(task['title']))
