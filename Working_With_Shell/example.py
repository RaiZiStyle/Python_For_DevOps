#!/usr/bin/python3

import sys
import os
import subprocess

print(sys.platform)
print(sys.version_info.major)

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
