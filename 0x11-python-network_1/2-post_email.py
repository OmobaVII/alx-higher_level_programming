#!/usr/bin/python3
"""
This module takes in a URL and an email
sends a POST request to the URL
with the email as the parameter
Displays the body of the response(decoded in utf-8)
"""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    """makes this part of the code not to be executed"""
    url = argv[1]
    email = {'email': argv[2]}
    data = urlencode(email)
    data = data.encode('ascii')  # this line makes the data to be bytes
    request = Request(url, data)
    with urlopen(request) as response:
        content = response.read()
    print(content.decode('utf-8'))
