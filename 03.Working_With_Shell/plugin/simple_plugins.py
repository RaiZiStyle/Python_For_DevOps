#!/usr/bin/python3

"""
Description:
    - Command-line tool using fire

Usage : 
    $ ./simple_plugins.py find_and_run_plugins foo_plugin 

"""

import fire
import pkgutil
import importlib

def find_and_run_plugins(plugin_prefix):
    plugins = {}

    # Discover and Load Plugins
    print(f"Discovering plugins with prefix: {plugin_prefix}")
    for _, name, _ in  pkgutil.iter_modules(): 
        if name.startswith(plugin_prefix): 
            module = importlib.import_module(name) 
            plugins[name] = module
        # else:
        #     print("Name of other module :",end='')
        #     print(name)

    # Run Plugins
    for name, module in plugins.items():
        print(f"Running plugin {name}")
        module.run()  

if __name__ == '__main__':
    fire.Fire()