"""
------------------------------------------------------------

Problem     : Equal Stacks
Platform    : HackerRank
Domain      : Data Structures
Category    : Stacks
Difficulty  : Easy
Language    : Python 3

Description:
There are three stacks of cylinders with different heights.
The goal is to make all three stacks equal in height by
removing cylinders only from the top of the stacks.

Return the maximum possible equal height of the three stacks.

Problem Link:
https://www.hackerrank.com/challenges/equal-stacks/problem

------------------------------------------------------------
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def equalStacks(h1, h2, h3):
    height1=sum(h1)
    height2=sum(h2)
    height3=sum(h3)
    
    while not (height1 == height2 == height3): 
        maximum_height=max(height1,height2,height3)
        
        if maximum_height==height1:
            removed=h1.pop(0) 
            height1-=removed
        elif maximum_height==height2:
            removed=h2.pop(0) 
            height2-=removed
        elif maximum_height==height3:
            removed=h3.pop(0) 
            height3-=removed
            
    return height1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
