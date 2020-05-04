#!/usr/bin/python3
"""Use API"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(
                            "https://jsonplaceholder.typicode.com/todos?userId={}"
                            .format(argv[1])).json()

    user_response = requests.get(
                                "https://jsonplaceholder.typicode.com/users/{}"
                                .format(argv[1])).json()


    username = user_response['username']
    user_id = argv[1]
    list_dict = []
    data = {}

    for item in response:
        data['task'] = item['title']
        data['completed'] = item['completed']
        data['username'] = username
        list_dict.append(data)
        data = {}

    data[user_id] = list_dict


    data = json.dumps(data)

    with open(user_id + '.json', 'w', newline='') as file:
        file.write(data)
