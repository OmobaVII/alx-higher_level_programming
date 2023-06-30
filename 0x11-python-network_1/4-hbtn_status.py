#!/usr/bin/python3
"""
This module fetches the status of `https://alx-intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    """prevent the code below from being executed if imported"""
    response = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type:", type(response.text))
    print("\t- content:", response.text)
