from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
 

# my app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/info")
def info():
    return render_template("info.html")

@app.route("/thebest")
def thebest():
    return "Allan (yep this is a dead end)"


if __name__ in "__main__":
    app.run(debug=True)