# install request library: pip/pip3 install requests or conda install requests

import requests  # import python library for making requests and working with APIs

response1 = requests.get("http://api.open-notify.org/this-api-doesnt-exist") # To make a ‘GET’ request

print(response.status_code) # to receive the status code for your request

# this returns data about astronauts currently in space, there is no need authentication.
response2 = requests.get("http://api.open-notify.org/astros.json")

print(response2.status_code) # to receive the status code for your request

print(response.json()) # see the data you received back from the API


