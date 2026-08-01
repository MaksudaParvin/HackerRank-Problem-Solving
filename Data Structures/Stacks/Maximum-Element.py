"""
------------------------------------------------------------
Problem    : Maximum Element
Platform   : HackerRank
Domain     : Data Structures
Category   : Stacks
Difficulty : Easy
Language   : Python 3

Description:
Implement a stack that supports the following operations:
1 x : Push element x onto the stack.
2   : Remove the element on top of the stack.
3   : Print the maximum element currently in the stack.

The solution uses an auxiliary stack to retrieve the
maximum element in O(1) time.

Problem Link:
https://www.hackerrank.com/challenges/maximum-element/problem
------------------------------------------------------------
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def getMax(operations):
    stack = []
    maximum = []
    result = []

    for operation in operations:

        value = operation.split()

        if value[0] == "1":
            number = int(value[1])
            stack.append(number)

            if not maximum:
                maximum.append(number)

            elif number >= maximum[-1]:
                maximum.append(number)

        elif value[0] == "2":
            if stack[-1] == maximum[-1]:
                maximum.pop()
            stack.pop()

        elif value[0] == "3":
            result.append(maximum[-1])

    return result 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
