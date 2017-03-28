#!/usr/bin/python3
from flask import Flask, url_for, render_template
app = Flask(__name__)


@app.route('/')
def display_Hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def display_HBNB():
    return 'HBNB'


@app.route('/c/(<text>)')
def replace_c(text):
    if "_" in text:
        text = text.replace("_", " ")
        return 'C %s' % text
    else:
        return 'C %s' % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>')
def replace_py(text="is cool"):
    if "_" in text:
        text = text.replace("_", " ")
        return 'Python %s' % text
    else:
        return 'Python %s' % text


@app.route('/number/<int:n>', strict_slashes=False)
def only_num(n):
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_odd(n):
    return render_template('6-number_odd_or_even.html', n=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
