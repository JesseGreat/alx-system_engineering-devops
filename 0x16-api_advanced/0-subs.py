#!/usr/bin/python3

"""
This module contains a function to query the Reddit API and return the number
of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers for a given
    subreddit.
    If the subreddit is invalid, return 0.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if invalid.

    Raises:
        None
    """
    # Set custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'JesseGreat/0.1'}
    # Send GET request to the subreddit API endpoint
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers)
    # If the request was successful, return the number of subscribers
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
