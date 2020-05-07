#!/usr/bin/python3

import requests



def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    head = {'User-Agent': 'oscar@gmail.com'}

    response = requests.get(url, headers=head, allow_redirects=False)

    if response.status_code == 200:

        response = response.json()
        data = response['data']
        data = data['subscribers']
        return(data)
    else:
        return(0)
