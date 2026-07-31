"""
------------------------------------------------------------
Problem    : No Idea!
Platform   : HackerRank
Domain     : Python
Category   : Sets
Difficulty : Medium
Language   : Python 3

Description:
Given an array and two sets A and B, calculate the
final happiness score. Increase the score by 1 for
each element found in set A and decrease it by 1 for
each element found in set B.

Problem Link:
https://www.hackerrank.com/challenges/no-idea/problem
------------------------------------------------------------
"""

n, m = map(int, input().split())
a=list(map(int, input().split()))
A=set(map(int, input().split()))
B=set(map(int, input().split()))
    
total_happiness=0   
for i in a:
    if i in A:
        total_happiness+=1
    elif i in B: 
        total_happiness-=1
    else:
        total_happiness=total_happiness

print(total_happiness)
