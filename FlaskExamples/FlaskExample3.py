from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Example3index.html")

@app.route("/test")
def test():
    return render_template("Example3newindex.html", content="testing")

if __name__ == "__main__":
    app.run(debug=True)