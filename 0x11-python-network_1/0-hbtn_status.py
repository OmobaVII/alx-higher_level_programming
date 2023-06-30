#!/usr/bin/python3
"""
This module fetches `https://alx-intranet.hbtn.io/status`
"""
from urllib.request import urlopen


if __name__ == "__main__":
    """Prevents from being executed"""
    with urlopen("https://alx-intranet.hbtn.io/status") as response:
        html = response.read()

    print('Body response:')
    print('\t- type:', type(html))
    print('\t- content:', html)
    print('\t- utf8 content:', html.decode('utf-8'))
