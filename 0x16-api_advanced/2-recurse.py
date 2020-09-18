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
    if data is None:
        return None
    params = {"after": data.get("after")}

    # fill the host_list
    children = data.get("children", None)
    if children:
        for topic in children:
            hot_list.append(topic.get("data").get("title"))

    # call to recursive funtion if exits more data
    if data.get("after") is not None:
        recurse(subreddit, hot_list, params)

    if len(hot_list) is not 0:
        return hot_list
    else:
        return None
