#!/usr/bin/python3

"""


Usage : 
    $ PYTHONSTARTUP=pythonstartup.py python

Result :
    >>> helpers
    <module 'helpers'>
    >>> helpers.uuid4
    UUID('3deb0204-a834-4642-9e55-fee51ed54591')

"""


import types
import uuid

helpers = types.ModuleType('helpers')
helpers.uuid4 = uuid.uuid4()
