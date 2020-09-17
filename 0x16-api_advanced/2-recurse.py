#!/usr/bin/python3
""" Write a recursive function that queries the Reddit
API and returns a list containing the titles of
all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[]):
    uri = uri = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "holberton"}
    data = requests.get(uri, headers=headers).json().get("data")
    count = data.get("dist")
    idx = 0

    while data.get("after") != None:
        params = {"after": data.get("after")}
        data = requests.get(
            uri,
            headers=headers,
            params=params).json().get("data")
        count += data.get("dist")
    return range(0, count)
