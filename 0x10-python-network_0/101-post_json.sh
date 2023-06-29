#!/bin/bash
# Sends a JSON POST request to a URL passed as the first argument and displays the body of the response
curl -sX POST -sH "Content-Type: application/json" -sd @"$2" "$1"
