#!/usr/bin/python3
""" Script to export data in json format for tasks owned by given employee. """


import json
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
    user_id = user_data.get('id')
    username = user_data.get('username')
    json_filename = "{}.json".format(user_id)

    json_data = {str(user_id): [{"task": task.get('title'), "completed":
                 task.get('completed'), "username": username} for task in
                 todo_data]}

    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)

    print("Employee {} tasks exported to {}".format(username, json_filename))
