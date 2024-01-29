#!/usr/bin/python3
""" Script to gather data from API for given employee ID. """


import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <emploi_id>".format(argv[0]))
        exit(1)

    employee_id = argv[1]

    base_url = "https://jsonplaceholder.typicode.com/"
    user_url = "{}users/{}".format(base_url, employee_id)
    todo_url = "{}todos?userId={}".format(base_url, employee_id)

    # Fetch user data
    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200:
        print("Error: Unable to fetch user data.")
        exit(1)

    if todo_response.status_code != 200:
        print("Error: Unable to fetch TODO list.")
        exit(1)

    # Parse JSON data
    user_data = user_response.json()
    todo_data = todo_response.json()

    # Extract relevant information
    employee_name = user_data.get('name')
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
