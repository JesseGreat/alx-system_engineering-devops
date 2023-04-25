#!/usr/bin/python3
"""Script to export data in the CSV format"""
import csv
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
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(employee_id)).json()

    # Count number of tasks completed
    num_tasks_completed = sum(
        task['completed'] for task in todo_lists
    )

    # Export data to CSV file
    filename = '{}.csv'.format(employee_id)
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo_lists:
            writer.writerow([employee_id, employee_info['username'],
                             task['completed'], task['title']])
