import os

def calljed(self,filename, linenum):
    "My editor hook calls the jed editor directly."
    print "Calling my own editor, jed ..."
    if os.system('jed +%d %s' % (linenum,filename)) != 0:
        raise TryNext()

def load_ipython_extension(ip):
    ip.set_hook('editor', calljed)