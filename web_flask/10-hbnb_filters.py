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


@app.route('/hbnb_filters')
def hbnb_filters():
    """display states id"""
    states = storage.all(classes["State"]).values()
    amenities = storage.all(classes["Amenity"]).values()
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


if __name__ == "__main__":
    app.run()
