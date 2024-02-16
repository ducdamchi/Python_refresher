"""
This program enables interaction with the Ereader.
(via completion of the Swindle Class
"""

from swindle import *

def main():
    ereader = Swindle()
    while True:
        pick = getMenuChoice()
        if pick == 1:
            ereader.buy()
        elif pick == 2:
            ereader.showOwned()
        elif pick == 3:
            ereader.read()
        else:
            return

def getMenuChoice():
    """
    Inputs:  None
    Returns: A valid Swindle menu choice
    Purpose: Ensures that a Swindle user selects a valid menu item
    """
    print("-"*50)
    print()
    print("1) Buy/See available books")
    print("2) See owned books")
    print("3) Read a book")
    print("4) Exit")
    print()
    while True:
    #making sure program doesn't crash when non-int is entered.
        try:
            pick = int(input("   ---> "))
            if pick >= 1 and pick <= 4:
                return pick
            else:
                print("Please choose an option from the menu!")
        except ValueError:
             print("Please choose an option from the menu!")


main()
