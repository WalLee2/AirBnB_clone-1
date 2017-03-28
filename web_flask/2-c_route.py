#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def display_Hello():
    return 'Hello HBNB!'

@app.route('/hbnb')
def display_HBNB():
    return 'HBNB'

@app.route('/c/<text>')
def replace_(text):
    if "_" in text:
        text = text.replace("_", " ")
        return 'C %s' % text
    else:
        return 'C %s' % text

if __name__ == "__main__":
    app.run(host='0.0.0.0')
