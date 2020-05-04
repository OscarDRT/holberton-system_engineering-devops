#!/usr/bin/python3
"""Use API"""

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(
                        "https://jsonplaceholder.typicode.com/todos?userId={}"
                        .format(argv[1])).json()

    user_response = requests.get(
                                "https://jsonplaceholder.typicode.com/users/{}"
                                .format(argv[1])).json()

    info = {}
    tasks_done = 0
    text_done = ""

    for item in response:
        if item['completed'] is True:
            text_done += "\t {}\n".format(item['title'])
            tasks_done += 1
    number_task = len(response)

    info['EMPLOYEE'] = user_response['name']
    info['DONE_TASKS'] = tasks_done
    info['NUMBER_OF_TASKS'] = number_task

    text = "Employee {} ".format(info['EMPLOYEE'])
    text += "is done with tasks({}/{}):\n" \
        .format(info['DONE_TASKS'], info['NUMBER_OF_TASKS'])
    text += text_done
    print(text, end='')
