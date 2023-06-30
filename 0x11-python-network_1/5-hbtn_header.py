#!/usr/bin/python3
"""
This module takes in a URL,
Sends a request to the URL
Displays the Value of the X-Request-Id Variable
"""
import requests
from sys import argv


if __name__ == "__main__":
    """Makes the code not to be executed when imported"""
    response = requests.get(argv[1])
    value = response.headers.get("X-Request-Id")
    print(value)
