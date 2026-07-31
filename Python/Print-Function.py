"""
------------------------------------------------------------
Problem    : Print Function
Platform   : HackerRank
Domain     : Python
Category   : Introduction
Difficulty : Easy
Language   : Python 3

Description:
Read an integer n and print the integers from 1 to n
as a continuous sequence without spaces or new lines.

Problem Link:
https://www.hackerrank.com/challenges/python-print/problem
------------------------------------------------------------
"""

n = int(input())

for i in range(1,n+1):
    print(i,end="")
