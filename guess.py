#!/usr/bin/python
# Filename: guess.py
number = 23
guess = int(raw_input('Input a number: '))
if guess == number:
    print "You're right"
elif guess > number:
    print "It's too big"
else:
    print "It's too small"

print "Done"
