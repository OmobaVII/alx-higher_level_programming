#i/bin/bash
# Makes a request to a server that cuases the server to respond with a message
curl -sL -X PUT -d "user_id=98" -H "Origin: School" -L 0.0.0.0:5000/catch_me_2
