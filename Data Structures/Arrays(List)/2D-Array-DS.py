"""
------------------------------------------------------------
Problem    : 2D Array - DS
Platform   : HackerRank
Domain     : Data Structures
Category   : Arrays
Difficulty : Easy
Language   : Python 3

Description:
Given a 6×6 two-dimensional array, calculate the
maximum hourglass sum. An hourglass consists of
7 elements arranged in the following pattern:

a b c
  d
e f g

Problem Link:
https://www.hackerrank.com/challenges/2d-array/problem
------------------------------------------------------------
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def hourglassSum(arr):
    maximum=float('-inf')
    
    for i in range(4):
        for j in range(4):
            top = arr[i][j]+arr[i][j+1]+arr[i][j+2]
            middle= arr[i+1][j+1]
            bottom=arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            hourglasssum=top+middle+bottom
            if hourglasssum>maximum:
                maximum=hourglasssum
    
    return maximum
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
