#!/usr/bin/python3
""" Write a recursive function that queries the Reddit
API and returns a list containing the titles of
all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], params={}):
    """recurse functions"""
    uri = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "holberton"}
    data = requests.get(uri, headers=headers, params=params).json().get("data")
    params = {"after": data.get("after")}
    hot_list.append(data.get("dist"))
    if data.get("after") is not None:
        recurse(subreddit, hot_list, params)
    if sum(hot_list) is not 0:
        return range(0, sum(hot_list))
    else:
        return None
