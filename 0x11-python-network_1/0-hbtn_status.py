#!/usr/bin/python3
"""
This module fetches `https://alx-intranet.hbtn.io/status`
"""
import urllib.request


with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    html = response.read()

print('Body response:')
print('    - type:', type(html))
print('    - content:', html)
print('    - utf8 content:', html.decode('utf-8'))

if __name__ == "__main__":
