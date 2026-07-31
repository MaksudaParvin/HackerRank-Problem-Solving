"""
------------------------------------------------------------
Problem    : Piling Up!
Platform   : HackerRank
Domain     : Python
Category   : Collections
Difficulty : Medium
Language   : Python 3

Description:
Given a row of cubes, determine whether it is
possible to build a vertical stack by picking
only the leftmost or rightmost cube at each step,
while ensuring that each cube placed on top is
not larger than the cube below it.

Problem Link:
https://www.hackerrank.com/challenges/piling-up/problem
------------------------------------------------------------
"""

from collections import deque

T = int(input())

for i in range(T):
    n = int(input())
    cubes = deque(map(int, input().split()))

    last = float('inf')

    possible = True

    while cubes:
        if cubes[0] >= cubes[-1]:
            current = cubes.popleft()
        else:
            current = cubes.pop()

        if current > last:
            possible = False
            break

        last = current

    if possible:
        print("Yes")
    else:
        print("No")
