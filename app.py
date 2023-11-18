from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/eusha")
def eusha():
    return "This is a page"


if __name__ == "__main__":
    app.run(debug=True)


