#!/usr/bin/python3
"""
   recursive function that queries the Reddit API

"""
import requests


def recurse(subreddit, after=None, hot_list=[]):
    """
      recursive function that queries the Reddit API and returns a 
      list containing the titles of all hot articles for a given subreddit

    """
    data = {
        'User-agent': 'Iamabot'
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    if after:i
        url += "?after={}".format(after)
    r = requests.get(url,
                     headers=data,
                     allow_redirects=False
                     )
    if r.status_code != 200:
        return None
    else:
        posts = r.json().get('data').get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))
        if r.json().get('data').get('after'):
            return recurse(
                subreddit,
                after=r.json().get('data').get('after'),
                hot_list=hot_list
            )
        return hot_list
