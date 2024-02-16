"""
This is the TDD for CS21 Lab 09
Author: Duc Dam
Date: April 4, 2023
"""
from county_demographics import *

def read_record():
    """This function reads the County Records and stores data a list of CountyRecord objects.
    Input: none
    Ouput: list of CountyRecord objects.
    """
    return [1,2,3]

def display_result(lst):
    """This function displays any list of CountyRecord objects in a table format.
    Input: list of CountyRecord objects
    Output: none
    Side effect: print table.
    """

def get_search():
    """This function prompts the user for a search option (0-5) until a valid choice is entered.
    Input: none
    Output: an integer between 0-5
    """
    return 0

def filter_state(records):
    """This function filters a list of CountyRecord objects.
    It uses bubble sorting in conjunction with a user-input string.
    Input: list of CountyRecord objects
    Output: a new list of CountyRecord objects
    Additional function: display search result.
    """
    return [1,2,3]

def filter_population(records):
    """This function filters a list of CountyRecord objects by 2020 population.
    It uses selection sorting in conjunction with two user-input integers
    Input: list of CountyRecord objects
    Output: a new list of CountyRecord objects
    Additional function: a while loop that makes sure user enter a valid population number.
    Display search result.
    """
    return [1,2,3]

def sort_state(records):
    """This function sorts a list of CountyRecord objects by state name in alphabetical order.
    It directly modifies the list.
    Input: list of CountyRecord objects
    Output: none
    Additional function: display search result.
    """
 
def sort_population(records):
    """This function sorts a list of CountyRecord objects by 2020 population in increasing oder.
    It directly modifies the list.
    Input: list of CountyRecord objects
    Output: none
    Additional function: display search result.
    """

def reset_records():
    """This function resets the list of CountyRecord objects.
    Input: none
    Output: the original list of CountyRecord objects when read from file.
    """
    return [1,2,3] 


def loop_search(search_type, records):
    """This function keeps asking user to enter a search option using a while loop.
    It builds on every search and stops when the user enter '0'
    Input: user-enter integer (0-5), list of orginal CountyRecord objects.
    """
         

def main():
   records = read_record()
   search_type = get_search()
   loop_search(search_type, records)
main()