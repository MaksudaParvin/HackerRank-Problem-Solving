"""
------------------------------------------------------------
Problem    : Time Delta
Platform   : HackerRank
Domain     : Python
Category   : Date and Time
Difficulty : Medium
Language   : Python 3

Description:
Given two timestamps with different time zones,
calculate and return the absolute difference
between them in seconds.

Problem Link:
https://www.hackerrank.com/challenges/python-time-delta/problem
------------------------------------------------------------
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"

    d1 = datetime.strptime(t1, format)
    d2 = datetime.strptime(t2, format)

    diff = abs((d1 - d2).total_seconds())

    return str(int(diff))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
