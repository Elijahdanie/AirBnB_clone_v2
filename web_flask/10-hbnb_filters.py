#!/usr/bin/python3

"""
This module starts a flask applicaiton
and serves list of States and cities
"""

from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
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
    return render_template('8-cities_by_states.html', states=state)


@app.route('/states', strict_slashes=False)
def states():
    """
    this returns a list of states
    """
    return list_states()


@app.route('/states/<id>', strict_slashes=False)
def statesid(id):
    """
    This returns a state Object
    rendered html page
    """
    allstate = storage.all(State)
    if id in allstate.keys():
        stateObject = allstate[id]
    else:
        stateObject = 'None'
    return render_template('9-states.html', state=stateObject)


@app.teardown_appcontext
def teardown(self):
    """Closes the current Sqlalchemy session"""
    storage.close()

@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    This returns a page with
    State cities and amenities
    """
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    data_dict = {'states':states, 'amenities':amenities}
    return render_template('10-hbnb_filters.html', **data_dict)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
