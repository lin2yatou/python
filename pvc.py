#!/usr/bin/python
# Filename: pvc.py

import sys
import os

if len(sys.argv) < 2:
    sys.exit()

filename=sys.argv[1]
if not os.path.exists(filename):
    try:
        f = file(filename, 'w')
        f.write(r'#!/usr/bin/python')
        f.write(os.linesep)
        f.write(r'# Filename: ' + filename)
        f.write(os.linesep)
        f.write(os.linesep)
    finally:
        f.close()

os.system('vim + ' + filename)
sys.exit()

