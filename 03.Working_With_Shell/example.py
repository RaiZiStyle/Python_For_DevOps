#!/usr/bin/python3

"""
Description:
    - Example of class and SubProcess

Usage : 
    $ ./example.py 

"""

import sys
import os
import subprocess


class MyOtherClass():
    def __init__(self, name):
        self.name = name



def say_it():
    greeting = 'Hello'
    target = 'Joe'
    message = f'{greeting} {target}'
    print(message)



if __name__ == '__main__':
    print("In this {0}, we are in {1}, with a python version {2}.{3}".format(sys.platform, sys.byteorder, sys.version_info.major, sys.version_info.minor))
    myOtherObject = MyOtherClass('Sammy')
    print("Example of class : {}".format(myOtherObject.name))


    # Checking Version of Python
    if sys.version_info.major < 3:
        print("You need to update your Python version")
    elif sys.version_info.minor < 7:
        print("You are not running the latest version of Python")
    else:
        print("You'r good to go")

    # Simple subProcess
    cp = subprocess.run(['ls', '-l'],
                        capture_output=True,
                        universal_newlines=True)
    print(cp.stdout)

    # Handle error in subProcess
    try:
        cp3 = subprocess.run(['ls', '/dontexiste'],
                            capture_output=True,
                            universal_newlines=True,
                            check=True)
    except:
        print("Error in subProcess : ")
        print(cp3.stderr)