#!/usr/bin/python3
"""
Function to cout  subreddit.
"""

import requests


def count_words(subreddit, word_list, after="", word_frequency=None):
    """A function that queries the Reddit API recursively, parses the title of
    all hot articles, and prints a sorted count of given keywords.
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
        posts = data.get("children", [])
        after = data.get("after")

        for post in posts:
            post_title = post["data"]["title"]
            words = post_title.lower().split()
            for word in word_list:
                word_frequency[word.lower()] += words.count(word.lower())

    except requests.RequestException:
        return None
    except Exception:
        return None

    count_words(subreddit, word_list, after, word_frequency)
