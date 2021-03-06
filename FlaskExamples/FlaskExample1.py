#https://techwithtim.net/tutorials/flask/a-basic-website/
#micro web framework. pip3 install Flask.
from flask import Flask , redirect , url_for #import packages and some functions.

app = Flask(__name__)   #start a instance 
 
#define a function that will represent each page and set its URL/Path. Defining the home page of our site
# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
	return "Hello! this is the main page <h1>HELLO</h1>"  # some basic inline html

#This essentially allows us to route any url that matches a specific pattern to a specific web page.
#To define a dynamic path you simply put a variable name inside of . http://127.0.0.1:5000/sidney example.
@app.route("/<name>") #new web page, using dynamic url/path. 
def user(name):      
    return f"Hello {name}!"

'''Redirect users to other pages from within your python code. The url_for function takes an argument that is 
the name of the function that you want to redirect to. "home", the name of the home page, has been written 
to direct to the main page. When "/ admin" is visited, it is directed to "home". '''
@app.route("/newadmin")    #another web page called admin.
def newadmin():
    return redirect(url_for("home"))

#To the "name" parameter defined in the "user" page, "Admin!" value is assigned.
#When we go to /admin we will redirect to user with the argument "Admin!"
@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))  

if __name__ == "__main__":
    app.run()
