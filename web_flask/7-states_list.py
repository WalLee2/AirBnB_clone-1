#!/usr/bin/python3
"""
Application listening on 0.0.0.0, port 5000
"""
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states_list')
def states_list():
    my_list = storage.all("State")
    return render_template('7-states_list.html', my_list=my_list)


@app.teardown_appcontext
def rmSession(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
