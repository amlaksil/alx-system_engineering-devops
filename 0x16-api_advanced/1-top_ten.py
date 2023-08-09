#!/usr/bin/python3
"""
This module prints the tittle of the first
10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts """
    params = {
            'limit': 10
            }
    # Get the subreddit's JSON data from the Reddit API.
    url = 'https://api.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url, params=params, allow_redirects=False)
    # Check the response status code.
    if response.status_code != 200:
        print(None)
        return
    dic = response.json()
    hot_posts = dic['data']['children']
    if len(hot_posts) is 0:
        print(None)
    else:
        for post in hot_posts:
            print(post['data']['title'])
