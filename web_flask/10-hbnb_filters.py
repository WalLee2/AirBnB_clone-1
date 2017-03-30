#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/hbnb_filters")
def filters():
    states_list = storage.all("State").values()
    amenities_list = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states_list=states_list,
                           amenities_list=amenities_list)

@app.teardown_appcontext
def teardown(self):
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
