#!/usr/bin/python3
""" Count """
import requests


def count_words(subreddit, word_list, hot_list=[], count=0, after=''):
    """
    Queries Reddit Api and prints a sorted count of given keywords.
    """
    site = 'https://www.reddit.com/'
    endpoint = 'r/{}/hot.json'.format(subreddit)
    query = '?show="all"&limit=100&count={}'.format(count)
    if after:
        query += '&after={}'.format(after)
    url = site + endpoint + query
    headers = {'User-Agent': 'My Reddit API Client by /u/lelaabk'}
    response = requests.get(url, headers=headers,
                            allow_redirects=False)

    if not response.ok:
        return None

    data = response.json()['data']
    for post in data['children']:
        hot_list.append(post['data']['title'])
    after = data.get('after')
    dist = data['dist']
    if after:
        count_words(subreddit, word_list, hot_list, count + dist, after)

    if count == 0:
        result = {}
        word_list = [word.lower() for word in word_list]
        hot_words = ' '.join(hot_list).lower().split(' ')
        for hot_word in hot_words:
            for search_word in word_list:
                if hot_word == search_word:
                    result.setdefault(search_word, 0)
                    result[search_word] += 1
        for word, count in sorted(result.items()):
            print("{}: {}".format(word, count))
