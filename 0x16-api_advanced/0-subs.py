#!/usr/bin/python3
"""
This module queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit
    Args:
        subreddit: the name of the subreddit to get subscriber
        count for.
    """
    # Get the subreddit's JSON data from the Reddit API.
    url = 'https://api.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, allow_redirects=False)
    # Check the response status code.
    if response.status_code == 200:
        # The number of subscribers is in the "subscribers" key.
        return response.json()['data']['subscribers']
    # Invalid subreddits
    return 0
