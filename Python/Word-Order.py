"""
------------------------------------------------------------
Problem    : Word Order
Platform   : HackerRank
Domain     : Python
Category   : Collections
Difficulty : Medium
Language   : Python 3

Description:
Given a sequence of words, determine the number of
distinct words and print the occurrence count of each
word in the order of their first appearance.

Problem Link:
https://www.hackerrank.com/challenges/word-order/problem
------------------------------------------------------------
"""

n=int(input())
words = []

for i in range(n):
    words.append(input())

distinct_words=0

words_count={}

for word in words:
    if word in words_count:
        words_count[word] += 1
    else:
        distinct_words+=1
        words_count[word] = 1

print(distinct_words)
for key,value in words_count.items():
    print(value,end=" ")
