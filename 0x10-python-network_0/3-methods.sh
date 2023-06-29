#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept the last - is to include everything after ' '
curl -sI "$1" | grep 'Allow' | cut -d' ' -f2-
