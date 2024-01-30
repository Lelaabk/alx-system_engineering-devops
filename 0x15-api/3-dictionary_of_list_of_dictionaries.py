#!/usr/bin/python3
""" Script to export data in json format. """


import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)

    # Fetch user data
    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    # Parse JSON data
    user_data = user_response.json()
    todo_data = todo_response.json()

    # Extract relevant information
    username = user_data.get('username')
    user_dict = {user_id: []}

    for todo in todo_data:
        task_dict = {
            "username": username,
            "task": todo.get('title'),
            "completed": todo.get('completed'),
        }
        user_dict[user_id].append(task_dict)

    with open('{}.json'.format(user_id), 'w') as json_file:
        json.dump(user_dict, json_file)
