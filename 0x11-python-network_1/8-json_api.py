#!/usr/bin/python3
"""
Takes in a letter and sends a POST
request to `http://0.0.0.0:5000/search_user
with the letter as parameter
"""
import requests
from sys import argv


if __name__ == "__main__":
    """makes it unexcutable if imported"""
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) <= 1:
        letter = ""
    else:
        letter = argv[1]
    payload = {"q": letter}
    response = requests.post(url, data=payload)
    try:
        result = response.json()
        if len(result) >= 1:
            print("[{}] {}".format(result.get("id"), result.get("name")))
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")
