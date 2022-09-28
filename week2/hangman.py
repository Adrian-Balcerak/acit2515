"""
ACIT2515 Lab

Week 2 -- complete this file!

"""

import random

# The number of turns allowed is a global constant
NB_TURNS = 10

def pick_random_word():
    """Opens the words.txt file, picks and returns a random word from the file"""
    # WRITE YOUR CODE HERE !
    with open('week2/words.txt', 'r') as fp:
        words = fp.read().splitlines()
    return random.choice(words)

def show_letters_in_word(word, letters):
    """
    This function RETURNS A STRING.
    This function scans the word letter by letter.
    First, make sure word is uppercase, and all letters are uppercase.
    If the letter of the word is in the list of letters, keep it.
    Otherwise, replace it with an underscore (_).

    DO NOT USE PRINT!

    Example:
    >>> show_letters_in_word("VANCOUVER", ["A", "V"])
    'V A _ _ _ _ V _ _'
    >>> show_letters_in_word("TIM", ["G", "V"])
    '_ _ _'
    >>> show_letters_in_word("PIZZA", ["A", "I", "P", "Z"])
    'P I Z Z A'
    """
    # WRITE YOUR CODE HERE
    word = word.upper()
    letters = [letter.upper() for letter in letters]
    my_string = ''

    for i in range(len(word)):
        flag = False
        for j in range(len(letters)):
            if (letters[j] == word[i]):
                my_string += letters[j] + ' '
                flag = True
        if flag == False:
            my_string += '_ '
    return my_string[:len(my_string)-1]

def all_letters_found(word, letters):
    """Returns True if all letters in word are in the list 'letters'"""

    #return "_" not in show_letter_in_word(word, letters)
    return set(word).issubset(set(letters))

def main(turns):
    """
    Runs the game. Allows for "turns" loops (attempts).
    At each turn:
    1. Ask the user for a letter
    2. Add the letter to the list of letters already tried by the player
    3. If the letter was already tried, ask again
    4. Use the show_letters_in_word function to display hints about the word
    5. Remove 1 to the number of tries left
    6. Check if the player
        - won (= word has been found)
        - lost (= word has not been found, no tries left)

    Do not forget to pick a random word first :-)

    """
    # WRITE YOUR CODE HERE
    word = pick_random_word()
    already_tried_letters = []
    while turns != 0:
        letter_is_fine = False
        while not letter_is_fine:
            letter = input("Give me a letter! ")
            if letter not in already_tried_letters:
                letter_is_fine = True
                already_tried_letters.append(letter)
        
        print(show_letters_in_word(word, already_tried_letters))
        if all_letters_found(word, already_tried_letters):
            print('You win!')
            break
        turns -= 1
        print(f'{turns} turns remain.')

    print(f'The word was {word}')
if __name__ == "__main__":
    main(NB_TURNS)