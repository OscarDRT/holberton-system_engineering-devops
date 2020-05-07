#!/usr/bin/python3
"""Module to display the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """ Function that will take the first 10 hot posts
    from a subreddit """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    head = {'User-Agent': 'oscar@gmail.com'}
    par = {'limit': 10}
    response = requests.get(url, headers=head, allow_redirects=False, params=par)

    if response.status_code == 200:
        response = response.json()
        data = response.get('data')
        children = data.get('children')
        if data and children:
            for item in children:
                name = item.get('data')
                title = name.get('title')
                print(title)
    else:
        print('None')
