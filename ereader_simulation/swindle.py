"""
Designing the Swindle class.
Date: April 18, 2023
Author: Duc Dam
"""

from book import *

class Swindle(object):
    """
    This Class creates multiple methods that are easy to call while designing the E-reader.
    For example, the method buy(), read(), or showOwned(), etc.
    It also contains multiple helper methods that deals with presenting the text, keeping track
    of bookmarks, or making sure that the user gives a valid input.
    """
    def __init__(self):
        """
        The constructor for the Swindle class.
        """
        print("\nSince this is the first time you used it, ")
        print("let's customize your Swindle...\n")
        name = input("Please enter you name: ")
        self.owner = name
        self.ownedBooks = []
        self.availableBooks = []
        self.pageLength = 20
        fp = open("bookdb.txt", "r")
        for line in fp:
            # each line is: title,author,year,filename
            data = line.strip().split(",")
            book = Book(data[0],data[1],int(data[2]),data[3])
            self.availableBooks.append(book)

        fp.close()
        print("\nWelcome to %s's Swindle v1.0!\n" % self.owner)

    ################################################################
    # INSERT ADDITIONAL METHOD HERE
    def showOwned(self):
        """This method displays a list of books owned by user in a nice row format
        and display numbers at the beginning of the row that user could choose from.
        It doesn't take any argument and doesn't return an output.
        """
        for i in range(len(self.ownedBooks)):
            print("%-5s"%(i+1) + self.ownedBooks[i].toString())


    def showAvailable(self):
        """This method displays a list of books that are available for buying in a nice row format
        and display numbers at the beginning of the row that user could choose from.
        It doesn't take any argument and doesn't return an output.
        """
        for i in range(len(self.availableBooks)):
            print("%-5s"%(i+1) + self.availableBooks[i].toString())


    def getOwner(self):
        """This method simply return the name of the owner, which the user entered initially.
        Input: none. Output: a string
        """
        return self.owner

        
    def buy(self):
        """This method controls how user could buy books from a list of existing books.
        It notifies the user if all the books have been bought.
        If not, it asks for which book to buy, remove it from the availableBooks list
        and append it to the ownedBooks list.
        It doesn't take any argument and doesn't return an output.
        """

        if len(self.availableBooks) == 0:
            print("You've purchased all available books!")
            pass

        else:
            self.showAvailable()
            #making sure program doesn't crash when user input a non-int.
            while True:
                try:
                    choice = int(input("Which book would you like to buy? (0 to skip): "))
                    break
                except ValueError:
                    print("Please enter an integer.")

            if choice in range(len(self.availableBooks)+1):
                if choice != 0:
                    bought = self.availableBooks.pop(choice-1)
                    self.ownedBooks.append(bought)
                else:
                    pass
            else:
                print("Please enter a valid integer from the options below.")
                self.buy()



    def read(self):
        """This method controls how user could read books from a list of owned books.
        It notifies the user if there is no books owned.
        Otherwise, it asks for which book to read from, then presents the text
        in a nice format written by displayText().
        It doesn't take any argument and doesn't return an output.
        """

        if len(self.ownedBooks) == 0:
            print("You don't own any books to read!")
            pass

        else:
            self.showOwned()
            #making sure program doesn't crash when user input a non-int.
            while True:
                try:
                    choice = int(input("Which book would you like to read? (0 to skip): "))
                    break
                except ValueError:
                    print("Please enter an integer.")

            if choice in range(len(self.ownedBooks)+1):
                if choice != 0:
                    self.displayText(self.ownedBooks[choice-1])
                else:
                    pass
            else:
                print("Please enter a valid integer from the options below.")
                self.read()



    #################################################################
    # Default Methods
    
    def displayText(self, book):
        """
        Purpose: Allow the user to read the book one page at a time
        Inputs:  A Book object
        Returns: Current page number
        """
        text = book.getText()
        lines = text.split("\n")
        currentLine = book.getBookmark() * self.pageLength
        while currentLine < len(lines):
            self.displayPage(lines, currentLine)
            prompt = "n (next); p (previous); q (quit): "
            letter = self.getLetter(prompt, ['n', 'p', 'q'])
            if letter == "n":
                print()
                currentLine += self.pageLength
            elif letter == "p":
                currentLine = max(0, currentLine-self.pageLength)
            else:
                return currentLine//self.pageLength
        print("\nYou finished the book!\n")
        currentLine = 0
        return currentLine

    def displayPage(self, lines, startLine):
        """
        Purpose: Displays one page of the book at at a time
        Input:  A str: lines, containing all of
                the text in the book, and
                an int: of the current line within the book
        Returns: None
        """
        endLine = min(startLine + self.pageLength, len(lines))
        print("="*84)
        for i in range(startLine, endLine):
            print("| %-80s |" %(lines[i]))
        print("="*84)
        print()
        pageNum = startLine//self.pageLength
        totalPages = len(lines)//self.pageLength
        print("Showing page %d out of %d\n" % (pageNum, totalPages))

    def getLetter(self, prompt, validList):
        """
        Input:   A string prompt, and list of valid letters
        Returns: A valid choice made by the user
        Purpose: To ensure correct responses to menu requests
        """
        while True:
            letter = input(prompt)
            if len(letter) > 1 or letter not in validList:
                print("invalid input, try again")
            else:
                return letter

if __name__ == '__main__':
    print("="*50)
    print("Test 1:Testing the Swindle class")
    myswindle = Swindle()

    print("="*50)
    print("Test 2:Testing showAvailable()")
    myswindle.showAvailable()

    print("="*50)
    print("Test 3:Testing showOwned()")
    myswindle.showOwned()
    
    #TODO: Write additional tests below

    print("="*50)
    print("Testing buy() function.")
    myswindle.buy()

    print("="*50)
    print("Test 3:Testing showOwned()")
    myswindle.showOwned()

    print("="*50)
    print("Testing read() function.")
    myswindle.read()
