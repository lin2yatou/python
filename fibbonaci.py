#!/usr/bin/python
# Filename: fibbonaci.py

def fibbonaci(index):
    if (index == 1):
        return 1
    elif (index == 2):
        return 1
    else:
        return fibbonaci(index-1) + fibbonaci(index-2)

for i in range(1,7):
    print fibbonaci(i)

