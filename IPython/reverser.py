# /home/user/Documents/stuff/Python/Python_For_DevOps/IPython/reverser.py
# 
"""
How to use : 
    In [1]: %load_ext reverser

    In [2]: %reverse Hello World
    Out[2]: 'dlroW olleH'

"""


from IPython.core.magic import register_line_magic

def load_ipython_extension(ipython):
    
    @register_line_magic("reverse")
    def lmagic(line):
        "line magic to reverse a string"
        return line[::-1]


# del lmagic