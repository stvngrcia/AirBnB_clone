#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from models import storage, classes
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(excep):
    """After each request you must remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list')
def states_list():
    """display Hello HBNB!"""
    states = storage.all(classes["State"]).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run()
