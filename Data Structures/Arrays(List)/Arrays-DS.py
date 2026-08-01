"""
Problem Name : Arrays - DS
Platform     : HackerRank
Difficulty   : Easy
Topic        : Arrays, List, Reversal
Language     : Python 3

Problem:
Given an array of integers, return the array in reverse order.

Time Complexity : O(n)
Space Complexity: O(n)

Problem Link:
https://www.hackerrank.com/challenges/arrays-ds/
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def reverseArray(a):
    reverse_array=reversed(a)
    return reverse_array

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
