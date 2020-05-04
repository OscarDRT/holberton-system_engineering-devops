#!/usr/bin/python3
"""Use API"""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    pa = "https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1])
    response = requests.get(pa).json()

    user_response = requests.get(
                                "https://jsonplaceholder.typicode.com/users/{}"
                                .format(argv[1])).json()

    username = user_response['username']
    user_id = argv[1]

    with open(user_id + '.csv', 'w', newline='') as csvfile:
        for item in response:
            spamwriter = csv.writer(
                                    csvfile, delimiter=',',
                                    quotechar='"',
                                    quoting=csv.QUOTE_ALL)
            spamwriter.writerow(
                                [item['userId']] +
                                [username] +
                                [item['completed']] +
                                [item['title']])
