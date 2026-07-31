"""
------------------------------------------------------------
Problem    : The Minion Game
Platform   : HackerRank
Domain     : Python
Category   : Strings
Difficulty : Medium
Language   : Python 3

Description:
Given a string, determine the winner of the Minion Game.
Kevin scores points for substrings that start with vowels,
while Stuart scores points for substrings that start with
consonants. Print the winner and the final score.

Problem Link:
https://www.hackerrank.com/challenges/the-minion-game/problem
------------------------------------------------------------
"""

def minion_game(string):
    vowels = "AEIOU"

    stuart = 0
    kevin = 0
    n = len(string)

    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i

    if stuart > kevin:
        print(f"Stuart {stuart}")
    elif kevin > stuart:
        print(f"Kevin {kevin}")
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
