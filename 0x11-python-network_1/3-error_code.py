#!/usr/bin/python3
"""
This module takes in a URL,
Sends a request to the URL
Displays the body of the response (decoded in utf-8)
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    """prevents code from executing if imported"""
    request = Request(argv[1])
    try:
        with urlopen(request) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except HTTPError as e:
        print("Error code:", e.code)
