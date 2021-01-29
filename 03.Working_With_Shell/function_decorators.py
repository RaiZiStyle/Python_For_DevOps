#!/usr/bin/python3
 
"""
Description:
    - Example of decorator

Usage : 
    $ ./function_decorators.py
"""

def some_decorator(wrapped_function):
    def wrapped():
        print('Do something before calling wrapped function')
        wrapped_function()
        print('Do something after calling wrapped function')
    return wrapped

def foobat():
    print('foobat')

@some_decorator
def batfoo():
    print('batfoo')

if __name__ == '__main__':
    f = some_decorator(foobat)
    # print(f())
    f()
    batfoo()