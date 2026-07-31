"""
------------------------------------------------------------
Problem    : Write a Function
Platform   : HackerRank
Domain     : Python
Category   : Introduction
Difficulty : Medium
Language   : Python 3

Description:
Complete the is_leap(year) function to determine whether
a given year is a leap year according to the Gregorian
calendar and return True or False.

Problem Link:
https://www.hackerrank.com/challenges/write-a-function/problem
------------------------------------------------------------
"""

def is_leap(year):
    leap = False
    if year %400==0:
        leap=True        
    elif year %100==0:
        leap=False
    elif year%4==0:
        leap=True
    else:
        leap=False
    return leap
    

year = int(input())
print(is_leap(year))
