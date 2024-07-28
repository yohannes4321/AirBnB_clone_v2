#!/usr/bin/python3
"""
Starts a Flask web application.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text_file(text):
    # Replace underscores with spaces
    return f"C {text.replace('_', ' ')}"


@app.route("/python/<text_>", strict_slashes=False)
def python_file(text_):
    # Replace underscores with spaces
    return f"Python {text_.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
