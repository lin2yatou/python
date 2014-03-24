#!/urs/bin/python
# Filename: diamond.py

import sys

if len(sys.argv) < 2:
    print 'Please input the size of the diamond'
    sys.exit()

length = sys.argv[1]
if not length.isdigit():
    print 'The second argument must be a digit to specify the size of the diamond'
    sys.exit()

count = int(length) * 2 - 1
for i in range(count):
    numofblank = abs(int(length) - i - 1)
    numofstar = (-2) * abs(i - int(length) + 1) + 2 * int(length) - 1
    print (' ' * numofblank) + '*' * numofstar
