#!/usr/bin/python3
"""This is the request """
import requests


def recurse(subreddit, hot_list=[], yy=None):
    """A function"""
    U = f"http://www.reddit.com/r/{subreddit}/hot.json"
    head = {"User-Agent": "0x16-api_advanced:project:v1.0.0"}
    params = {"limit": 100}
    if yy is not None:
        params["yy"] = yy

    try:
        r = requests.get(U, head=head, params=params)
        r.raise_for_status()
        data = r.json().get("data", {})
        posts = data.get("children", [])
        if not posts:
            return hot_list
        hot_list.extend([post["data"]["title"] for post in posts])
        new_yy = data.get("yy")
        return recurse(subreddit, hot_list, new_yy)
    except requests.RequestException:
        return None
