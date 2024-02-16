"""
This is a practice on writing recursive functions in Python.
Author: Duc Dam 
Date: 10th April, 2023
"""
def iterative_odd_sum(n):
    """
    This function computes the sum of all odd integers up to 'n'
    using while and for loops.
    Input: integer 'n'
    Output: an integer, the calculated sum.
    """
    odd_nums = []
    sum = 0

    # case for 0 as a special even number
    if n == 0:
        sum == 0


    #case for an even number greater than 0
    elif n != 0 and n % 2 == 0 :
        n = n-1
        odd_nums.append(n)
        #making a list of all odd numbers up to n, excluding n
        while n > 1:
            n = n-2
            odd_nums.append(n)
        for i in range(len(odd_nums)):
            sum += odd_nums[i]

            
    #case for an odd number
    else:
    #making a list of all odd numbers up to n
        odd_nums.append(n)
        while n > 1:
            n = n-2
            odd_nums.append(n)
        print("List of all odd numbers is: ", odd_nums)
        for i in range(len(odd_nums)):
            sum += odd_nums[i]
     
    return sum

def recursive_odd_sum(n):
    """
    This function computes the sum of all odd integers up to 'n'
    using only recursive functions.
    Input: integer 'n'
    Output: an integer, the calculated sum.
    """
    if n < 1:
        return 0
    else:
        if n % 2 == 0:
            n = n - 1
            sum = recursive_odd_sum(n-2) + n
        else:
            sum = recursive_odd_sum(n-2) + n
        return sum

def iterative_sum_of_positive(lst):
    """
    This function computes the sum of all positive integers up to 'n'
    using while and for loops.
    Input: integer 'n'
    Output: an integer, the calculated sum.
    """
    sum = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            sum += lst[i]
    return sum

def recursive_sum_of_postitive(lst):
    """
    This function computes the sum of all odd integers up to 'n'
    using only recursive functions.
    Input: integer 'n'
    Output: an integer, the calculated sum.
    """
    if len(lst) == 0:
        return 0
    else:
        new_lst = lst[1:]
        if lst[0] >= 0:
            sum = lst[0] + recursive_sum_of_postitive(new_lst)
        elif lst[0] < 0:
            sum = recursive_sum_of_postitive(new_lst)
        return sum

def get_num():
    """
    This function gets a list of number from users and turn them into integers.
    Input: none
    Output: a list of integers
    """
    lst = []
    number = 0
    print("Enter your list of integers ('z' to stop):")
    while number != 'z':
        number = input()
        lst.append(number)
    lst = lst[:-1]
    print("Your original list is: ", lst)

    for i in range(len(lst)):
        lst[i] = int(lst[i])
    return lst

def main():


    print("\n-------------------- Testing Odd Sum functions now --------------------")
    number = int(input("Enter a number: "))
    odd_sum_I = iterative_odd_sum(number)
    odd_sum_R = recursive_odd_sum(number)
    print("The sum of all odd numbers up to %i is:" %number)
    print("  %i, computed iteratively." %odd_sum_I)
    print("  %i, computed recursively." %odd_sum_R)
    print("================== Odd Sum functions test completed ==================\n")


    print("\n-------------------- Testing Positive Sum functions now --------------------")
    lst = get_num()
    pos_sum_I = iterative_sum_of_positive(lst)
    pos_sum_R = recursive_sum_of_postitive(lst)
    print("The sum of all positive numbers in the list is: ")
    print("  %d, computed iteratively."%pos_sum_I)
    print("  %d, computed recursively."%pos_sum_R)
    print("================== Positive Sum functions test completed ==================\n")


main()
