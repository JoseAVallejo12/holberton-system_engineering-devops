#!/usr/bin/python3
""" Write a function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    """query the last ten post

    Args:
        subreddit (str): subredit to find
    """
    uri = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "holberton"}
    size_query = {"limit": 10}
    res = requests.get(uri, params=size_query, headers=headers)
    children = res.json().get("data", {}).get("children", None)

    if children:
        for topic in children:
            print(topic.get("data").get("title"))
    else:
        print("None")
