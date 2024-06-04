#!/usr/bin/python3
import requests


def top_ten(subreddit):
    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code == 200:
        [print(child.get('data').get('title'))
            for child in sub_info.json().get('data').get('children')]
