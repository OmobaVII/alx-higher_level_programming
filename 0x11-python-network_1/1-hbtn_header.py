#!/usr/bin/python3
"""
This module takes in a URL,
Sends a request to the URL
Displays the Value of the X-Request-Id Variable
"""
from urllib.request import Request, urlopen
from sys import argv


if __name__ == "__main__":
    """makes the script unexecuted when imported"""
    request = Request(argv[1])
    with urlopen(request) as response:
        print(response.getheader("X-Request-Id"))
