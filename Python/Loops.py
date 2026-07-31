"""
------------------------------------------------------------
Problem    : Loops
Platform   : HackerRank
Domain     : Python
Category   : Introduction
Difficulty : Easy
Language   : Python 3

Description:
Read an integer n and print the square of each
non-negative integer less than n, with one result
per line.

Problem Link:
https://www.hackerrank.com/challenges/python-loops/problem
------------------------------------------------------------
"""

n = int(input())

for i in range(0,n):
    print(i**2)
