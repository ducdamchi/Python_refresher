"""
This is the implementation of sorting algorithms on data of US demographics.

Author: Duc Dam
Date: April 4, 2023
"""
from county_demographics import *

def read_record():
   """This function reads the County Records and stores data a list of CountyRecord objects.
   Input: none
   Ouput: list of CountyRecord objects.
   """
   recordFile = open("/usr/local/doc/county_data.csv","r")
   header_line = recordFile.readline()
   county_records = []
   for line in recordFile:
      record = CountyRecord(line)
      county_records.append(record)
   return county_records

def display_result(lst):
   """This function displays any list of CountyRecord objects in a table format.
   Input: list of CountyRecord objects
   Output: none
   Side effect: print table.
   """
   print("=============================================================================================")
   print("| %30s | %6s |%8s| %8s| %8s | %8s | %8s|" % ( "County", "State", \
 "Ed-HS", "H-Own%", "# House", "Pop-2020", "Pop. PSQM" ) )
   print("----------------------------------------------------------------------------------------------")
   for i in range(len(lst)):
      print("| %30s | %6s |%8s| %8s| %8s | %8s | %8s|" % ( lst[i].get_county(), lst[i].get_state(), \
 lst[i].get_education("HighSchool"), lst[i].get_home_ownership(), lst[i].get_num_households(), \
 lst[i].get_population(2020), lst[i].get_population_square_mile() ))

def get_search():
   """This function prompts the user for a search option (0-5) until a valid choice is entered.
   Input: none
   Output: an integer between 0-5
   """
   print("\nPlease select one of the following choices:\n \
   1. Filter records by state name\n \
   2. Filter records by total population\n \
   3. Sort by state name\n \
   4. Sort by total population\n \
   5. Reset list to all records\n \
   0. Quit\n")
   choice_invalid = True
   while choice_invalid:
      selection = input("Enter selection (0-5): ")
      if selection in ['0','1','2','3','4','5']:
         choice_invalid = False
      else:
         print("Invalid selection.")
   return int(selection)

def filter_state(records):
   """This function filters a list of CountyRecord objects.
   It uses bubble sorting in conjunction with a user-input string.
   Input: list of CountyRecord objects
   Output: a new list of CountyRecord objects
   Additional function: display search result.
   """
   state_name = input("State name (or prefix)?: ")
   state_name = state_name.upper()   
   state_list = []

   for index in range(len(records)):
      if (records[index].get_state()).startswith(state_name):
         state_list.append(records[index])

   if len(state_list) == 0:
      print("There are no exact matches.")
   else:
      display_result(state_list)

   return state_list

def filter_population(records):
   """This function filters a list of CountyRecord objects by 2020 population.
   It uses selection sorting in conjunction with two user-input integers
   Input: list of CountyRecord objects
   Output: a new list of CountyRecord objects
   Additional function: a while loop that makes sure user enter a valid population number.
   Display search result.
   """
   while True:
      try:
         pop_min = int(input("Enter the minimum population: "))
         pop_max = int(input("Enter the maximun population: "))
         break
      except ValueError:
         print("Invalid population (must be an integer).")


   population_list = []
   for index in range(len(records)):
      if records[index].get_population(2020) >= pop_min and records[index].get_population(2020) <= pop_max:
         population_list.append(records[index])


   if len(population_list) == 0: 
      print("There are no exact matches.")
   else:
      display_result(population_list)

   return population_list

def sort_state(records):
   """This function sorts a list of CountyRecord objects by state name in alphabetical order.
   It directly modifies the list.
   Input: list of CountyRecord objects
   Output: none
   Additional function: display search result.
   """
   records_length = len(records)
   for j in range (0, records_length - 1):
      for i in range (0, records_length - j - 1):
         if records[i].get_state() > records[i+1].get_state():
            (records[i], records[i+1]) = (records[i+1], records[i])
   
   display_result(records)

def sort_population(records):
   """This function sorts a list of CountyRecord objects by 2020 population in increasing oder.
   It directly modifies the list.
   Input: list of CountyRecord objects
   Output: none
   Additional function: display search result.
   """
   records_length = len(records)
   for i in range(records_length):
      minIndex = i
      for j in range(i + 1, records_length):
         if records[minIndex].get_population(2020) > records[j].get_population(2020):
            minIndex = j
      (records[i], records[minIndex]) = (records[minIndex], records[i])

   display_result(records)

def reset_records():
   """This function resets the list of CountyRecord objects.
   Input: none
   Output: the original list of CountyRecord objects when read from file.
   """
   records_original = read_record()
   records = records_original.copy()
   return records

def loop_search(search_type, records):
   """This function keeps asking user to enter a search option using a while loop.
   It builds on every search and stops when the user enter '0'
   Input: user-enter integer (0-5), list of orginal CountyRecord objects.
   Output: none
   """
   not_quit = True
   while not_quit:
      if search_type == 0:
         not_quit = False
         print("Goodbye!")
         break
      elif search_type == 1:
         records = filter_state(records)
      elif search_type == 2:
         records = filter_population(records)   
      elif search_type == 3:
         sort_state(records)   
      elif search_type == 4:
         sort_population(records)     
      elif search_type == 5:
         records = reset_records()

      search_type = get_search()
         
def main():
   records = read_record()
   search_type = get_search()
   loop_search(search_type, records)
main()

