#i/bin/bash
# Makes a request to a server that cuases the server to respond with a message
curl -sL "0.0.0.0:5000/catch_me" -X PUT -H "Origin: School" -d "user_id=98"
