"""
This program reviews Bubble Sort and Selection Sort 
as learned in CS21, Swarthmore College.
Date: May 6th, 2023.
Author: Duc Dam
"""
def get_lst():
    lst = []
    print("Making a list of int (assuming valid user input)...")
    print("Enter an integer ('q' to quit):")
    while True:
        num = input()
        if num == 'q':
            break
        else:
            num = int(num)
            lst.append(num)
    return lst

def bubble_sort(lst):
    print("\n")
    print("="*50)
    print("Bubble Sorting...")
    newls = lst.copy()
    for i in range(len(newls)):
        print("*"*30)
        print("After %i iteration (outer loop):"%i, newls)
        for j in range(len(newls)-i-1):
        #The highest value bubbles to the end of the list after every outer loop.
        #The next end value of the list is therefore in correct place.
            if newls[j] > newls[j+1]:
                newls[j], newls[j+1] = newls[j+1], newls[j]
            print("After %i iteration (inner loop):"%(j+1), newls)
    return newls

def selection_sort(lst):
    print("\n")
    print("="*50)
    print("Selection Sorting...")
    newls = lst.copy()
    for i in range(len(newls)):
        print("*"*30)
        print("After %i iteration (outer loop):"%i, newls)
        minIndex = i
        for j in range(i+1, len(newls)):
        #The smallest value is selected in each inner loop.
        #It is then placed at the beginning of the list after every outer loop.
            if newls[minIndex] > newls[j]:
                minIndex = j
            print("After %i iteration (inner loop): minIdex = "%(j-i), minIndex)
        newls[i], newls[minIndex] = newls[minIndex], newls[i]
    return newls

def main():
    lst = get_lst()
    print("Original list:", lst)
    print("\nBubble Sort Final Output:", bubble_sort(lst))
    print("\nSelection Sort Final Output:", selection_sort(lst))
main() 