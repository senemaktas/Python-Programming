#With blueprint we can create our project in parts so that we can make project management easier.

from flask import Blueprint , render_template

blueVariable=Blueprint("Useblueprint" , __name__ , static_folder="static",template_folder="templates")

@blueVariable.route("/home")
@blueVariable.route("/")
def home():
    return render_template("homeblueprint.html")

@blueVariable.route("/test")
def test():
    return "<h1>testtttt</h1>"