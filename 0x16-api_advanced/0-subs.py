#!/usr/bin/python3
"""xxxxxxxxx"""
import requests


def number_of_subscribers(subreddit):
    """
        Returns the number of subscribers to a specified subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    head = {'User-Agent': 'oscar@gmail.com'}

    response = requests.get(url, headers=head, allow_redirects=False)

    if response.status_code == 200:

        response = response.json()
        data = response.get('data')
        subscribers = data.get('subscribers')
        if data and subscribers:
            return(subscribers)
    return(0)
