#!/usr/bin/python3
"""
Application listening on 0.0.0.0, port 5000
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def rmSession():
    storage.close()


@app.route('/states_list', strict_slahes=False)
def states_list(states_list):
    return render_template('7-states_list.html', states_list=states_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
