#!/usr/bin/python3
""" Function that queries the Reddit API """
import requests
import sys


def top_ten(subreddit):
    """Queries the Reddit API to get top ten posts in a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'MyBot/1.0'}  # Changed the User-Agent
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json().get('data')
        if data:
            children = data.get("children")
            if children:
                for child in children:
                    title = child.get("data", {}).get("title")
                    if title:
                        print(title)
                return
    print('None')
