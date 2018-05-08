#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Hero lws
age_of_oldman = 66
n = 0;x = 3

while True:
    if n == 0:
        print("now you have {i} change for guess！".format(i = x))
    elif n < 3:
        print("now you only {i} change for guess！".format(i = x))
        break

    age = int(input("Guess the age of oldman :"))

    if age == age_of_oldman:
        print("yes,you got it!")
        break
    elif age > age_of_oldman and age < 200:
        print("I think it bigger...")
    elif age < age_of_oldman and age >= 1:
        print("I think it smaller...")
    else:
        print("毛病？")

    x-=1
    if x == 0:
        print( "you are a loser...\n")
        change = input("would you like to guess it again?(y/n):")
        if str( change ).upper() == "Y":
            x = 3
            continue
        elif str( change ).upper() == "N":
            break
        else:
            print( r"there only two change: 'y' or 'n',understand?!")
            print( "You are doomed to be a loser! rolling! ")
            break

