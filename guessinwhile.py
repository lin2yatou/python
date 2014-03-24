#!/usr/bin/python
# Filename: guessinwhile.py

number = 23
guess = int(raw_input("Input a integer"))
while (guess != number):
    if (guess < number):
        print "It's too small"
    elif (guess > number):
        print "It's too big"
    guess = int(raw_input("Input a integer"))
else:
    print "Bingo"

