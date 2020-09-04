# https://www.dataquest.io/blog/python-api-tutorial/
# install request library: pip/pip3 install requests or conda install requests

import requests  # import python library for making requests and working with APIs

response1 = requests.get("http://api.open-notify.org/this-api-doesnt-exist") # To make a ‘GET’ request

print(response.status_code) # to receive the status code for your request

# this returns data about astronauts currently in space, there is no need authentication.
response2 = requests.get("http://api.open-notify.org/astros.json")

print(response2.status_code) # to receive the status code for your request

print(response2.json()) # see the data you received back from the API

#-----------------------------------------------------------------------------------------------------------|

# The dumps() function can be used to print a formatted string that makes JSON output easier to understand.
import json
def jprint(obj):
# create a formatted string of the Python JSON object
text = json.dumps(obj, sort_keys=True, indent=4)
print(text)
jprint(response2.json())

#------------------------------------------------------------------------------------------------------------|
# Understanding the Pass Times. 
# They are in a format known as timestamp or epoch. These times are difficult to understand.
pass_times = response2.json()['response']
jprint(pass_times)

# use a loop to extract just the five risetime values.
risetimes = []
for d in pass_times:
time = d['risetime']
risetimes.append(time)
print(risetimes)

# Python datetime.fromtimestamp() method to convert these into easier to understand times.
from datetime import datetime
times = []
for rt in risetimes:
time = datetime.fromtimestamp(rt)
times.append(time)
print(time)
