#!/usr/bin/python3

"""
Description:
    - Example of class and SubProcess

Usage : 
    $ FLASK_APP=small.py flask run
    $ molotov load_test.py
"""


from flask import Flask, redirect, request

app = Flask("basic app")


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        redirect('https://www.google.com/search?q=%s' % request.args['q'])
    else:
        return '<h1>GET request from Flask! </h1>'
