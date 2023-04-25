#!/usr/bin/python3
"""Script to export data in the JSON format"""
import csv
import requests
import sys
import json

if __name__ == '__main__':
    # Get employee ID from command line arguments
    employee_id = sys.argv[1]

    # Get employee information
    employee_info = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    ).json()

    # Get employee's to-do list
    todo_lists = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(employee_id)
    ).json()

    # Count number of tasks completed
    num_tasks_completed = sum(
        task['completed'] for task in todo_lists
    )

    info = {employee_id: [{'task': task['title'],
                           'completed': task['completed'],
                           'username': employee_info['username']}
                          for task in todo_lists]}

    # Export data to JSON file
    filename = '{}.json'.format(employee_id)
    with open(filename, mode='w') as json_file:
        json.dump(info, json_file)
