#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states')
def cities():
    my_list = storage.all("State").values()
    return render_template('9-states.html', my_id="no_need", my_ids=my_list)

@app.route('/states/<id>')
def city_ids(id):
    my_list = storage.all("State").values()
    for x in my_list:
        if str(x.id) == id:
            found = x
            return render_template('9-states.html', my_id=found, my_ids=x)
    return render_template('9-states.html', my_id="None", my_ids=x)

@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
