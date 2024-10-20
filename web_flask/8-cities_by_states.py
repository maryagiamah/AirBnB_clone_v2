#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """States List"""
    return render_template('7-states_list.html', states=storage.all(State))


@app.teardown_appcontext
def tearDown(self):
    """Close"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
