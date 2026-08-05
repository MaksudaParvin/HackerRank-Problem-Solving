"""
Problem: Game of Two Stacks
Platform: HackerRank
Language: Python
Approach: Greedy + Stack

Description:
Finds the maximum number of elements that can be removed from the
top of two stacks without the running sum exceeding the given limit.
The solution first takes as many elements as possible from the first
stack, then processes the second stack while removing elements from
the first stack when necessary.

Time Complexity: O(n + m)
Space Complexity: O(n)
"""
#!/bin/python3

import math
import os
import random
import re
import sys

def twoStacks(maxSum, a, b):
    stack = []
    current_sum = 0
    count = 0

    for i in a:
        if current_sum + i <= maxSum:
            current_sum += i
            stack.append(i)
            count += 1
        else:
            break

    answer = count

    for j in b:
        current_sum += j
        count += 1

        while current_sum > maxSum and stack:
            removed = stack.pop()
            current_sum -= removed
            count -= 1

        if current_sum <= maxSum:
            answer = max(answer, count)
        else:
            break

    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        maxSum = int(first_multiple_input[2])

        a = list(map(int, input().rstrip().split()))

        b = list(map(int, input().rstrip().split()))

        result = twoStacks(maxSum, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
