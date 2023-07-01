#!/usr/bin/python3
"""
Takes 2 arguments
1 respository name
2 owner name
"""
import requests
from sys import argv


if __name__ == "__main__":
    """codes wont run if imported"""
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    response = requests.get(url)
    response = response.json()

    for commits in response[0:10]:
        print(commits.get("sha"), end=": ")
        print(commits.get("commit").get("author").get("name"))
