#!/usr/bin/env python3
#answer to the question 1 ^^^^

import os
import json

print("Content-Type: application/json")
print()
print(json.dumps(dict(os.environ), indent=2))
#q1: OS.environ, it is a dictionary that contains all the environment variables
os.environ['QUERY_STRING'] = "query=hello&something&anything"
print(f"<p>HTTP_USER_AGENT: {os.environ['HTTP_USER_AGENT']}</p>")
print(f"<p>QUERY_STRING: {os.environ['QUERY_STRING']}</p>")

#q2: query string ?query=hello&something&anything pass the string to the

#q3: HTTP_User_Agent

