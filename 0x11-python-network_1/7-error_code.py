#!/usr/bin/python3
"""
This module takes in a URL,
Sends a request to the URL
Displays the body of the response
or the Error code received
"""
import requests
from sys import argv


if __name__ == "__main__":
    """all codes in this block will not be excuted
    if module is imported"""
    try:
        response = requests.get(argv[1])
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException:
        print("Error code:", response.status_code)
