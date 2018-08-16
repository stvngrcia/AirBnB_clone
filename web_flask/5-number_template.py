#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def Hello_HBNB():
    """display Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def HBNB():
    """display HBNB"""
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    """display C followed by the value of the text variable"""
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/')
@app.route('/python/<text>')
def python(text="is cool"):
    """display Python, followed by the value of the text variable"""
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """display n is a number onlyif n is an integer"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run()
