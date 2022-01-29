#!/usr/bin/python3

"""
This module creates a flask application
that returns Hello world when called
"""

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function returns Hello HBNB
    """
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    This function returns HBNB
    """
    return 'HBNB'



if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
