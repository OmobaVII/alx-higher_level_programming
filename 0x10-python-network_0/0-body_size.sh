#!/bin/bash
# Takes a URL, send a request to the URL and displays the size of the body of the response
curl -sI "$1" | grep -oP '(?<=Content-Length: )\d+'
