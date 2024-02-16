"""
This program reviews the Recursion concept
as learned in CS 21, Swarthmore College.
Date: 2023, May 7th.
Author: Duc Dam
"""

def main():
    value = mystery(5)
    print("The value is: %d"%value)


def mystery(n):
    if (n>0):
        print(n)
        return n + mystery(n-1)
    else:
        print("*")
        return 0

main()