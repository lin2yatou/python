#!/usr/bin/python
# Filename: pv.py

import sys
import os

def initpyfile():
    '''This is a method to init a python file quickly.

    Mainly generate the header of a python script file.'''
    if len(sys.argv) < 2:
        return
    else:
        filename = sys.argv[1]
        if not filename.endswith('.py'):
            filename = filename + '.py'
        if os.path.exists(filename):
            print 'already have a file named', filename
        else:
            try:
                f = file(filename, 'w')
                f.write(r'#!/usr/bin/python')
                f.write(os.linesep)
                f.write(r'# Filename: '+filename)
                f.write(os.linesep)
            finally:
                f.close()

        os.system('vim '+filename)


initpyfile()
