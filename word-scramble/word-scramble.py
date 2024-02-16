"""
Author: Duc Dam
Date: March 21 2023.
"""
import random
import string

def print_introduction():
    print("=======================================================================\
\nWelcome to Word Scramble!\
\nYour goal is to create as many English words as possible from the given letters.\
\nNote: Words must be at least 3 letters long.\
\n=======================================================================")


def player_ready(i):
    while True:
        ready_yet = input("Is player %i ready (yes or no)?: "%(i+1))
        if ready_yet in ["yes","Yes","yes ", "Yes "]:
            break
        else:
            ready_yet = input("Is player %i ready (yes or no)?: "%(i+1))


def generate_letters():
    #importing English alphabet so I don't have to type it out.
    uppercase_alphabet = list(string.ascii_uppercase)
    uppercase_vowels = ['U','E','O','A','I']
    chosen_letters = []
    for i in range(2):
        #choose 2 from vowels list.
        letter = random.choice(uppercase_vowels)
        chosen_letters.append(letter)
    for i in range(4):
        #choose 4 from alphabet list.
        letter = random.choice(uppercase_alphabet)
        chosen_letters.append(letter)
    #shuffle the list to give randomized look.    
    official_letters = random.sample(chosen_letters, 6)
    return official_letters


def read_dictionary(textfile):
    dictionary = open(textfile,"r")
    dictionary_words = []
    for line in dictionary:
        line = line.strip('\n')
        dictionary_words.append(line)
    return dictionary_words


def player_enter_words():
    player_wordlist = []
    print("Enter your words (enter 'q' when ready to quit):")
    while True:
        player_words = input()
        if player_words == 'q':
            print("\n")
            break
        player_wordlist.append(player_words)
    return player_wordlist


def length_check(player_wordlist):
#this function replaces words that have less than 3 letters with "---"
    for i in range(len(player_wordlist)):
        if len(player_wordlist[i]) < 3:
            print ("%s is too short."%player_wordlist[i])
            player_wordlist[i] = "---"


def letter_check(player_wordlist, official_letters):
#this function replaces words that use invalid letters with "---"
    #turning allowed letters into lowercase.
    all_letters_allowed = []
    all_letters_allowed.append(official_letters)
    for i in range(6):
        all_letters_allowed.append(official_letters[i].lower())
    #after this the user-input words could contain both upper and lower cases.
    
    #using nested for loop to find words with invalid letters
    #this for loop goes through each word in word_list
    for word in range(len(player_wordlist)):
        #moves on to next word whenever there is a "-""
        if player_wordlist[word] == "---":
            pass
        else: 
            #this for loop goes through each letter in each word in word_list
            for letter in player_wordlist[word]:
                if (letter in all_letters_allowed) or (letter == "---"):
                    pass
                else:
                    print("%s contains invalid letter(s)."%player_wordlist[word])
                    player_wordlist[word] = "---"
                    break



def dictionary_check(player_wordlist, dictionary_words):
#this function checks if word exists in dictionary.
    for i in range(len(player_wordlist)):
        if player_wordlist[i] == "---":
            pass
        elif player_wordlist[i] not in dictionary_words:
            print("%s is not in the Scramble dictionary."%player_wordlist[i])
            player_wordlist[i] = "---"


def calculate_results(all_player_wordlists):
#this function calculates the score of each player.
    player1_score = 0
    for words in all_player_wordlists[0]:
        if words == "---":
            pass
        else:
            player1_score += 1

    player2_score = 0
    for words in all_player_wordlists[1]:
        if words == "---":
            pass
        else:
            player2_score += 1
    print("=======================================================================\
    \nCalculating results...")
    print("Player 1 found %i words."%player1_score)
    print("Player 2 found %i words."%player2_score)

    if player1_score > player2_score:
        print("Player 1 wins!")
    elif player2_score > player1_score:
        print("Player 2 wins!")
    else:
        print("It's a tie! Maybe a rematch?")

    
def main():
    dictionary_words = read_dictionary("/usr/local/doc/word-scramble-dictionary.txt")
    official_letters = generate_letters()
    all_player_wordlists = []
    for i in range(2):
        print_introduction()
        player_ready(i)
        print(official_letters)
        player_wordlist = player_enter_words()
        length_check(player_wordlist)
        letter_check(player_wordlist, official_letters)
        dictionary_check(player_wordlist, dictionary_words)
        all_player_wordlists.append(player_wordlist)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(all_player_wordlists)
    calculate_results(all_player_wordlists)
main()
