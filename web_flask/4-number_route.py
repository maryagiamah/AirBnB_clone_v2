#!/usr/bin/python3
"""Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Home"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def home_hbnb():
    """Home"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """C text"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text="is cool"):
    """Python text"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<n>', strict_slashes=False)
def n_int(n):
    """Integer"""
    if type(n) is int:
        return f"{n}"


if __name__ == '__main__':
    app.run(debug=True)
