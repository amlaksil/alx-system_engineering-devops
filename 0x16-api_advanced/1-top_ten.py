#!/usr/bin/python3
"""
This module prints the tittle of the first
10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts """
    headers = {
            'User-Agent': 'Mozilla/5.0'
            }
    params = {
            'limit': 10
            }
    # Get the subreddit's JSON data from the Reddit API.
    url = 'https://api.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        items = response.json()['data']['children']
        if len(items) == 0:
            print(None)
        else:
            for item in items:
                print(item['data']['title'])
    else:
        print(None)
