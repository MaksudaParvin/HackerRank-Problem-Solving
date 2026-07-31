"""
------------------------------------------------------------
Problem    : Python If-Else
Platform   : HackerRank
Domain     : Python
Category   : Introduction
Difficulty : Easy
Language   : Python 3

Description:
Given an integer n, print "Weird" or "Not Weird" based on
the given conditional rules.

Problem Link:
https://www.hackerrank.com/challenges/py-if-else/problem
------------------------------------------------------------
"""

n=int(input())

if not n%2==0:
    print("Weird")
    
elif n%2==0 and 2<= n <=5:
    print("Not Weird")
        
elif n%2==0 and 6<= n <=20:
    print("Weird")
        
elif n%2==0 and n>20:
    print("Not Weird")
