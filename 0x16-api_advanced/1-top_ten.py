#!/usr/bin/python3
"""
function that queries the Reddit API 

"""
import requests


def top_ten(subreddit):
    """
     function that queries the Reddit API and prints the titles
     of the first 10 hot posts listed for a given subreddit.

    """
    data = {
        'User-agent': 'Iamabot',
    }
    r = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                     .format(subreddit),
                     headers=data,
                     allow_redirects=False
                     )
    if r.status_code != 200:
        print(None)
    else:
        posts = r.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
