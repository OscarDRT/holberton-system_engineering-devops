#!/usr/bin/python3
"""Use API"""

import json
import requests

if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()

    all_user = {}
    list_dict = []
    data = {}

    for item in users:
        response = requests.get(
                        "https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(item['id'])).json()
        for task in response:
            data['username'] = item['username']
            data['task'] = task['title']
            data['completed'] = task['completed']
            list_dict.append(data)
            data = {}
        all_user[item['id']] = list_dict
        list_dict = []

    all_user = json.dumps(all_user)
    with open('todo_all_employees.json', 'w', newline='') as file:
        file.write(all_user)
