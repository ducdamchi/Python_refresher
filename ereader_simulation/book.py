"""
Designing the Book class.
Date: April 18, 2023
Author: Duc Dam
"""

class Book(object):
    """
    Creating a Book class
    """
    def __init__(self, title, author, year, file_name):
        self.title = title
        self.author = author
        self.year = int(year)
        self.file = file_name
        self.bookmark = 0
    
    def toString(self):
        book_info = ("%-25s%-20s(%i)"%(self.title, self.author, self.year))
        return book_info

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getFilename(self):
        return self.file

    def getBookmark(self):
        return self.bookmark
    
    def setBookmark(self, page_num):
        self.bookmark = int(page_num)
        return self.bookmark

    def getText(self):
        text = open(self.file,"r")
        content = ""
        for line in text:
            if "#" not in line[0]:
                content += line
        return content


if __name__ == '__main__':
    print("="*50)
    print("Test 1: creating a new book class with book Pride and Prejudice")
    mybook = Book("Pride and Prejudice", "Jane Austin", 1813,
                  "/usr/local/doc/prideandprejudice.txt")

    print("="*50)
    print("Test 2: testing the toString() method:")
    print(mybook.toString())

    print("="*50)
    print("Test 3: test getFilename():")
    print(mybook.getFilename())

    print("="*50)
    print("Test 4: test getAuthor():")
    print(mybook.getAuthor())

    print("="*50)
    print("Test 5: test getTitle():")
    print(mybook.getTitle())

    print("="*50)
    print("Test 6: getting the bookmark and setting the bookmark to 12:")
    print("Bookmark is:", mybook.getBookmark())
    mybook.setBookmark(12)
    print("The updated bookmark is set to:", mybook.getBookmark())

    print("="*50)
    print("Test 7: test getText with first 110 characters:")
    text = mybook.getText()
    print(text[:110])

    print("="*50)
    print("End of testing")
