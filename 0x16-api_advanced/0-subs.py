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
    response = requests.get(
      'https://api.reddit.com/r/{}/about'.format(subreddit))
    # Check the response status code.
    if response.status_code == 200:
        data = response.json()
        # The number of subscribers is in the "subscribers" key.
        return data['subscribers']
    # Invalid subreddits
    return None
