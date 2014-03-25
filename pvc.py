#!/usr/bin/python
# Filename: pv.py

import sys
import os
import time

def initpyfile():
    '''This is a method to init a python file quickly.

    Mainly generate the header of a python script file.'''
    if len(sys.argv) < 2:
        print 'python script creator, need an argument as filename'
        return
    else:
        filename = sys.argv[1]
        if not filename.endswith('.py'):
            filename = filename + '.py'
        if os.path.exists(filename):
            print 'already have a file named', filename
            os.system('vim '+filename)
        else:
            with open(filename, 'w') as f:
                f.write(r'#!/usr/bin/python')
                f.write(os.linesep)
                f.write(r'# Filename: ' + filename)
                f.write(os.linesep)
                f.write(r'# author: ' + os.getenv('USER'))
                f.write(os.linesep)
                f.write(r'# history: ' +time.strftime('%Y-%m-%d %H:%M:%S'))
                f.write(os.linesep)
                f.write(os.linesep)

        os.system('vim + '+filename)


initpyfile()
