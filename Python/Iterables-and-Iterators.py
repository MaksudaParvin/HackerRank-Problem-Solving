"""
------------------------------------------------------------
Problem    : Iterables and Iterators
Platform   : HackerRank
Domain     : Python
Category   : Itertools
Difficulty : Medium
Language   : Python 3

Description:
Given a list of lowercase letters and an integer K,
calculate the probability that at least one selected
combination of size K contains the letter 'a'.

Problem Link:
https://www.hackerrank.com/challenges/iterables-and-iterators/problem
------------------------------------------------------------
"""

from itertools import combinations

N = int(input())
letters = input().split()
K = int(input())

comb = list(combinations(letters, K))

event = sum('a' in c for c in comb)

print(f"{event / len(comb):.3f}")
