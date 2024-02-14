#!/usr/bin/python3
""" Recurse """
import requests


def recurse(subreddit, hot_list=[], count=0, after='i'):
    """
    Queries Reddit Api and returns list containing titles of all hot articles.
    """
    site = "https://www.reddit.com"
    endpoint = 'r/{}/hot.json'.format(subreddit)
    query = '?show="all"&limit=100&count={}'.format(count)
    if after:
        query += '&after={}'.format(after)
    url = site + endpoint + query
    headers = {'User-Agent': 'My Reddit API Client by /u/lelaabk'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    if (not response.ok):
        if len(hot_list) == 0:
            return None
        else:
            return hot_list

    data = response.json()['data']
    for post in data['children']:
        hot_list.append(post['data']['title'])
    after = data.get('after')
    dist = data['dist']
    if after:
        recurse(subreddit, hot_list, count + dist, after)

    if len(hot_list) == 0:
        return None
    else:
        return hot_list
