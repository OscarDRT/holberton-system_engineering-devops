#!/usr/bin/python3
"""Module to display the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """ Function that will take the first 10 hot posts
    from a subreddit """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    h = {'User-Agent': 'oscar@gmail.com'}
    par = {'limit': 10}
    response = requests.get(url,
                            headers=h,
                            allow_redirects=False,
                            params=par)

    if response.status_code == 200:
        response = response.json()
        data = response.get('data')
        children = data.get('children')
        if data and children:
            for post in children:
                post_data = post.get('data')
                title = post_data.get('title')
                print(title)
    else:
        print(None)
