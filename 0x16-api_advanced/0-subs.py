#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Custom User Agent"}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        if "data" in data and "subscribers" in data["data"]:
            return data["data"]["subscribers"]
    return 0
