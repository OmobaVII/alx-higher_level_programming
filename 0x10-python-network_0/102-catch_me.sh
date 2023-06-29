#!/bin/bash
# Makes a request to a server that cuases the server to respond with a message
curl -sL http://0.0.0.0:5000/catch_me -X PUT -d "You got me!"
