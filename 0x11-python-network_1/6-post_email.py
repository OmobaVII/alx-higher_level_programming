#!/usr/bin/python3
"""
This module takes in a URL and an email
Sends a POST request to the URL
with the email as the parameter
Displays the body of the response
"""
import requests
from sys import argv


if __name__ == "__main__":
    """the codes in this block will not be executed"""
    email = {"email": argv[2]}
    response = requests.post(argv[1], data=email)
    print(response.text)
