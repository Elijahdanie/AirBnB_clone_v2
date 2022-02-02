#!/usr/bin/python3

"""
This module starts a flask applicaiton
and serves list of States and cities
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """
    returns a list of all the states
    """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    This returns a html page of
    list of cities by states
    """
    state = storage.all(State).values()
    return render_template()

@app.teardown_appcontext
def teardown(self):
    """Closes the current Sqlalchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)