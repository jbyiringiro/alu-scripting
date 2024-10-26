#!/usr/bin/python3
"""
Function that queries the 'Reddit API'
and prints the titles of the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url ="https://reddit.com/r/{}.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

     if response.status_code == 200:
        data = response.json()['data']
        for post in data['children'][:10]:
            print(post['data']['title'])

    else:
        print(None)

