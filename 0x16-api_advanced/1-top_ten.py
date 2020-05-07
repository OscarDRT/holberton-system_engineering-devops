#!/usr/bin/python3


import requests

def top_ten(subreddit):

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    head = {'User-Agent': 'oscar@gmail.com'}
    par = {'limit': 10}

    response = requests.get(url, headers=head, params=par, allow_redirects=False)

    if response.status_code == 200:
        response = response.json()
        data = response.get('data')
        data = data.get('children')
        for item in data:
            name = item.get('data')
            title = name.get('title')
            print(title)
    else:
        print(None)