#!/usr/bin/python3
from flask import Flask, url_for
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

if __name__ == "__main__":
    app.run(host='0.0.0.0')
