#!/usr/bin/python
# Filename: ab.py
import pickle as p
import os
import sys


datafile = "ab.data"
try:
    f = file(datafile)

    if os.path.exists(datafile):
        ab = p.load(f)
    else:
        ab = {}
finally:
    f.close()

def printUsage():
    '''This is a address book program in command line.'''
 
    print r'python ab.py [add|delete|update|list|find] [content]'
    print r'example: python ab.py add linnan 15210xxxxxx'

def verifyArgv():
    '''This method is to validate arguments of program.'''
    
    if len(sys.argv) < 2:
        printUsage()
        sys.exit()

def addContact():
    '''Add one contact to the address book '''
    if len(sys.argv) < 4:
        return
    name = sys.argv[2]
    number = sys.argv[3]
    ab[name] = number

def delContact():
    '''Remove one contact from address book'''
    if len(sys.argv) < 3:
        return
    if ab.has_key(name):
        del ab[name]

def listContact():
    '''List all the contact in the address book'''
    for key in ab:
        print 'Name: %s \t No.:%s' % (key, ab[key])

def updateContact():
    '''Update the contact in the address book.

    actually, you can do this with [add] option.'''
    if len(sys.argv) < 4:
        return
    if ab.has_key(sys.argv[2]):
        ab[sys.argv[2]] = argv[3]

def findContact():
    '''Search the contact in the address book.'''
    if len(sys.argv) < 3:
        return
    name = sys.argv[2]
    for i in (n for n in ab.keys() if name in n):
        print 'Name: %s \t No.:%s' % (i, ab[i])

def main():
    
    verifyArgv()
    if sys.argv[1].lower() == 'add':
        addContact()
    if sys.argv[1].lower() == 'list':
        listContact()
    if sys.argv[1].lower() == 'del':
        delContact()
    if sys.argv[1].lower() == 'update':
        updateContact()
    if sys.argv[1].lower() == 'find':
        findContact()
main()
try:
    f = file(datafile, "w")
    p.dump(ab, f)
finally:
    f.close()
