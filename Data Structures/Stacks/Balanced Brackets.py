"""
Problem: Balanced Brackets
Platform: HackerRank
Language: Python
Approach: Stack

Description:
Checks whether a string containing (), {}, and [] brackets is balanced.
Uses a stack to keep track of opening brackets and verifies that each
closing bracket matches the most recent opening bracket.

Time Complexity: O(n)
Space Complexity: O(n)
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def isBalanced(s): 
    stack=[]
    
    for bracket  in s:
        if bracket in '({[':
            stack.append(bracket)
        else:
            if not stack:
                return "NO"
            else:
                remove=stack.pop()
                if remove=="(" and bracket==")":
                    continue
                elif remove=="{" and bracket=="}":
                    continue
                elif remove=="[" and bracket=="]":
                    continue
                else:
                    return "NO"    
                
    if not stack:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
