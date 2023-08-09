#!/usr/bin/python3
"""
This module prints the tittle of the first
10 hot posts listed for a given subreddit
"""
import sys


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts """
    hot_posts = reddit.subreddit(subreddit).hot(limit=10)
    # Get the titles of the host posts
    titles = [post.title for post in hot_posts]
    return titles


if __name__ == '__main__':
    top_ten(sys.argv[2])
