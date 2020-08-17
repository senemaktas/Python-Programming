'''Cookie , Sessions , Message Flashing'''

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__) 

#for session identify 
app.secret_key = "hello"

#define for  session permanat time : days, minutes etc.
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    return render_template("Example3index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True  # <--- makes the permanent session
        user = request.form["nm"]
        session["user"] = user
        flash("Login succesful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
  
        return render_template("login.html")        

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    #message flashing and give category
    flash("You have been logged out!","info")
    #session closing
    session.pop("user", None)
    return redirect(url_for("login"))        

if __name__ == "__main__":
    app.debug = True
    app.run()