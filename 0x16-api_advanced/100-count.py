#!/usr/bin/python3
""" Module for a function that queries the Reddit API recursively."""

import requests


def count_words(subreddit, word_list, after="", word_frequency=None):
    """A function that queries the Reddit API.
    """
    if word_frequency is None:
        word_frequency = {word.lower(): 0 for word in word_list}

    if after is None:
        sorted_word_frequency = sorted(
            word_frequency.items(), key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_word_frequency:
            if count:
                print(f"{word}: {count}")
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "redquery"}
    params = {"limit": 100, "after": after}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json().get("data", {})
        posy = data.get("children", [])
        after = data.get("after")

    for post in posts:
        title = post["data"]["title"].lower()
        words = title.split()
        word_frequency.update({word.lower(): word_frequency.get(word.lower(), 0) + words.count(word.lower()) for word in word_list})

        
    except requests.RequestException:
        return None
    except Exception:
        return None

    count_words(subreddit, word_list, after, word_frequency)
