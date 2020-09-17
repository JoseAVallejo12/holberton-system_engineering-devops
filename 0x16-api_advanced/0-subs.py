#!/usr/bin/python3
"""Write a function that queries the Reddit API
and returns the number of subscribers."""
import requests


def number_of_subscribers(subreddit):
    """Get number of suscriptor in redit
    Args:
        subreddit (str): subreddit or topic to search subs
    Returns:
        [int]: Number subscriber or 0 else not exist
    """
    uri = 'https://api.reddit.com/r/{}/about'.format(subreddit)
    headers = {"User-Agent": "holberton"}
    res = requests.get(uri, headers=headers)
    return res.json().get('data', {}).get("subscribers", 0)
