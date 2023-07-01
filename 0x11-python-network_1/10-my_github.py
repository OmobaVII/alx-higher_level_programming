#!/usr/bin/python3
"""
Takes your github credentials
Uses the Github API to display your id
"""
from sys import argv
import requests


if __name__ == "__main__":
    """prevents from being executed when imported"""
    url = "https://api.github.com/user"
    username = argv[1]
    password = argv[2]
    credentials = (username, password)
    response = requests.get(url, auth=credentials)
    response = response.json()
    print(response.get('id'))
