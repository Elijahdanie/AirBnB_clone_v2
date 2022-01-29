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

@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """
    This function returns c
    followed by valule of text
    """
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """
    This function returns
    Python followd by value of text
    """
    text = 'is cool' if text is None else text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    This function returns
    Python followd by value of text
    """
    return '{} is a number'.format(n)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)
