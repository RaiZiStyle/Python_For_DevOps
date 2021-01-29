#!/usr/bin/python3

"""
Description:
    - Command-line tool using fire

Usage : 
    $ ./fire_example.py ships --help 
    $ ./fire_example.py ships --help
    $ ./fire_example.py ships sail
    $ ./fire_example.py sailors Hiya Karl -- --interactive


"""
import fire

class Ships(): 
    def sail(self):
        ship_name = 'Your ship'
        print(f"{ship_name} is setting sail")

    def list(self):
        ships = ['John B', 'Yankee Clipper', 'Pequod']
        print(f"Ships: {','.join(ships)}")

def sailors(greeting, name): 
    message = f'{greeting} {name}'
    print(message)

class Cli(): 

    def __init__(self):
        self.sailors = sailors
        self.ships = Ships()

if __name__ == '__main__':
    fire.Fire(Cli)
    sailors('hello', 'fred')