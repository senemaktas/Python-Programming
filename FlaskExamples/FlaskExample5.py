'''Cookie / Sessions / Message Flashing/ Adding, Updating Users SQLAlchemy 
SQLAlchemy database'''

from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__) #create instance
db=SQLAlchemy(app) #create database instance

#"users" gonna be table name
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.secret_key = "hello" #for session identify 

#define for  session permanat time : days, minutes etc.
app.permanent_session_lifetime = timedelta(minutes=5)

class users(db.Model):
    users_id = db.Column("id", db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

    def __init__(self,name,email):
        self.name = name
        self.email = email
        
@app.route("/")
def home():
    return render_template("Example3index.html")

# see inside of your database record with view.html
@app.route("/view")
def view():
    return render_template("view.html" , values=users.query.all())

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True  # <--- makes the permanent session
        user = request.form["nm"]
        session["user"] = user

        found_user= users.query.filter_by(name=user).first()
        if found_user:
            session["email"]=found_user.email
        else:
            usr=users(user , "")  #if user dont exist add one, "" this keep email place
            db.session.add(usr)   #add that new user our database 
            db.session.commit()  #everytime change the database, save spesific changes

        flash("Login succesful!")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
  
        return render_template("login.html")        

@app.route("/user" , methods=["POST", "GET"])
def user():
    email=None
    if "user" in session:
        user = session["user"]

        if request.method=="POST":
            email= request.form["email"]
            session["email"] = email
            found_user = users.query.filter_by(name=user).first()
            found_user.email= email
            db.session.commit()
            flash("Email was saved!")
        else:
            if "email" in session:
                email=session["email"]

        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    #message flashing and give category
    flash("You have been logged out!","info")
    #session closing
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))        

if __name__ == "__main__":
    db.create_all()  #it will create db if it's not exist
    app.run(debug=True)