from flask import Flask ,render_template
from Useblueprint import blueVariable #import your blueprint python page and variable name from there

app=Flask(__name__)
app.register_blueprint(blueVariable, url_prefix="/admin")

@app.route("/")
def test():
    return "<h1>test blueprint</h1>"

if __name__=="__main__":
    app.run(debug=True)
