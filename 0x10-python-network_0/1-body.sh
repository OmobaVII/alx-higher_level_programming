#!/bin/bash
# Takes a URL, sends a GET request to the URL, and displays the body of responses of 200 status code
curl -sL "$1"
