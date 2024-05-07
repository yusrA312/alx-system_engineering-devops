#!/usr/bin/python3
"""This is the request """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """A function that queries the Reddit API and returns a list containing
    the titles of all hot articles for a given subreddit. If no results
    are found for the given subreddit, the function should return None
    """
    url = f'http://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': '0x16-api_advanced:project:v1.0.0'}
    params = {'limit': 100}
    if after is not None:
        params['after'] = after

    try:
        r = requests.get(url, headers=headers, params=params)
        r.raise_for_status()
        data = r.json().get('data', {})
        posts = data.get('children', [])
        if not posts:
            return hot_list
        hot_list.extend([post['data']['title'] for post in posts])
        new_after = data.get('after')
        return recurse(subreddit, hot_list, new_after)
    except requests.RequestException:
        return None
