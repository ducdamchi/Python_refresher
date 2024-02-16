"""
Author: Duc Dam 
Date: 10th April, 2023
"""

def recursive_disemvowel(phrase):
    """This function removes all vowels from a given string\
    using only recursive functions.
    Input: a string
    Output: a modified string.
    """
    if len(phrase) == 0:
        return ""
    else:
        new_str = phrase[1:]
        if phrase[0] in "AEIOUaeiou":
            phrase = recursive_disemvowel(new_str)
        else:
            phrase = phrase[0] + recursive_disemvowel(new_str)
        return phrase

def main():
    phrase = input("Enter a string: ")
    new_str = recursive_disemvowel(phrase)
    print('"%s" becomes "%s" when disemvowelled.'%(phrase, new_str))
main()
