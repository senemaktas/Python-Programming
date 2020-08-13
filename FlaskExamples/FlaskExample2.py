#source: https://techwithtim.net/tutorials/flask/html-templates/

'''  It works with "index.html" file. what you want to do is enable debug mode so Flask will
actually tell you what the error is. (And you get the added benefit of flask reloading every 
time you modify code!)'''

#render_template : this function grab the html file and render that as web page.
from flask import Flask ,redirect ,url_for , render_template #import packages

app = Flask(__name__) #instance

#Create an html file (FlaskAndHTML.html). Make sure to put it in the templates folder! Rendering HTML
@app.route("/<name>")
def home(name):
    return render_template("FlaskExample2.html",content=name,test=["option1","option2","option3"])

if __name__ == "__main__":
    app.debug = True
    app.run()


