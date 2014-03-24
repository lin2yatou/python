#!/usr/bin/python
# Filename Person.py
import sys

class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print 'Hi, this is ',self.name

p = Person("Nanan")
p.sayHi()
       
