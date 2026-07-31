"""
------------------------------------------------------------
Problem    : Merge the Tools!
Platform   : HackerRank
Domain     : Python
Category   : Strings
Difficulty : Medium
Language   : Python 3

Description:
Split the given string into substrings of length k.
For each substring, remove duplicate characters while
preserving the order of their first occurrence, then
print the resulting string.

Problem Link:
https://www.hackerrank.com/challenges/merge-the-tools/problem
------------------------------------------------------------
"""

def merge_the_tools(string, k):
    
    for i in range(0, len(string), k):

        substring = string[i:i + k]

        distinct_characters = set()
        result = ""

        for char in substring:
            if char not in distinct_characters:
                distinct_characters.add(char)
                result += char

        print(result)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
