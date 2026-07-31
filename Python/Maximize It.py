"""
------------------------------------------------------------
Problem    : Maximize It!
Platform   : HackerRank
Domain     : Python
Category   : Itertools
Difficulty : Hard
Language   : Python 3

Description:
Given K lists of integers, choose exactly one element
from each list such that the sum of their squares,
modulo M, is maximized.

Problem Link:
https://www.hackerrank.com/challenges/maximize-it/problem
------------------------------------------------------------
"""
from itertools import product

K, M = map(int, input().split())

lists = []

for i in range(K):
    values = list(map(int, input().split()))

    lists.append(values[1:])

maximum = 0

for combination in product(*lists):

    total = 0

    for number in combination:
        total += number ** 2

    value = total % M

    if value > maximum:
        maximum = value

print(maximum)
