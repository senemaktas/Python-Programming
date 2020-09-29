# https://rapidapi.com/blog/how-to-use-an-api-with-python/
# For python 3 , requests that is the de facto standard for making HTTP requests in Python.
import requests

response1=requests.get("https://www.google.com/")
print(response1)  # <Response [200]> 200 – OK. The request was successful.

# simply view the status of the response code by accessing .status_code
print(response1.status_code) # output ->  200

# use Response instance in a conditional expression. It will evaluate to True if the status 
# code was between 200 and 400, and False otherwise.
if response1:
    print("Request is successful!")
else:
    print("Request returned an error !")

''' Endpoint is a specific address (for example, https://weather-in-london.com/forecast), by referring to 
which you get access to certain features/data (in our case – the weather forecast for London). Commonly, 
the name (address) of the endpoint corresponds to the functionality it provides. The Dino Ipsum API is 
used to generate any amount of Lorem Ipsum placeholder text. It is useful when you prototype or test the
interface of your application and want to fill it with any random content. Our app will call the endpoint,
which is located at https://alexnormand-dino-ipsum.p.rapidapi.com/ and will print for us this nice placeholder
text https://rapidapi.com/alexnormand/api/dino-ipsum '''

# import requests

url = "https://alexnormand-dino-ipsum.p.rapidapi.com/"

# format can be text , html , json etc.
querystring = {"format":"text","words":"30","paragraphs":"5"}

headers = {
    'x-rapidapi-host': "alexnormand-dino-ipsum.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

response2 = requests.request("GET", url, headers=headers, params=querystring)

print(response2.text)

''' Often REST API returns a response in JSON format for ease of further processing. The requests library
has a convenient .json() method for this case that converts JSON to a Python object. We can get JSON from
it in response if we specify the format = JSON parameter when accessing dinos list endpoint. '''

url = "https://alexnormand-dino-ipsum.p.rapidapi.com/"

params = {"format":"json","words":"30","paragraphs":"5"}

headers = {
    'x-rapidapi-host': "alexnormand-dino-ipsum.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

response3 = requests.request("GET", url, headers=headers, params=params)

print(type(response3.json()))
print(response3.json())
