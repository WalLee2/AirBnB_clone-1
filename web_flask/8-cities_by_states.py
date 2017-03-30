#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from os import getenv
from models.state import State
from models.city import City
app = Flask(__name__)


def show_state():
    my_list = storage.all("State").values()
    return render_template('7-states_list.html', my_list=my_list)


@app.route('/cities_by_states')
def cities_by_states_html():
    my_list = storage.all("State").values()
    return render_template('8-cities_by_states.html', my_list=my_list)


@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
