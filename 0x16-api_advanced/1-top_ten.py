#!/usr/bin/python3
""" TOP TEN """
import requests


def top_ten(subreddit):
    """
    Queries Reddit API and prints titles of first 10 hot post listed.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?show="all"&limit=10'.format(
            subreddit)
    headers = {'User-Agent': 'My Reddit API Client by /u/lelaabk'}
    response = requests.get(url, headers=headers)
    try:
        data = response.json()
        top_ten = data['data']['children']
        for post in top_ten:
            print(post['data']['title'])
    except KeyError:
        print("None")
