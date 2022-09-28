from operator import truediv
import random

class SecretWord():
    def __init__(self, word = None):
        if word == None:
            with open("words.txt","r", encoding='utf8') as words:
                word_list = words.readlines()
                selected_word = random.choice(word_list)
                self.word = selected_word.strip().upper()
        else:
            self.word = word.upper()
    
    def show_letters(self, letters):
        upper_list = []
        for letter in letters:
            upper_list.append(letter.upper())
    
        new_string =""
        self.word = self.word.upper()
        for letter in self.word:
            if letter in upper_list:
                new_string += f"{letter} "
            else:
                new_string +="_ "
        return new_string.strip()
    
    def check_letters(self, letters):
        result = self.show_letters(letters)
        if "_" not in result:
            return True
        return False

    def check(self, check_string):
        if check_string.upper() == self.word:
            return True

        return False

class Game():

    def __init__(self, turns = 10):
        self.turns = turns
        self.user_tried_letters = []
        self.current_game = SecretWord()

    def play_one_round(self):
        user_letter = input("Choose your letter!: ")
        self.turns = self.turns - 1
        while user_letter in self.user_tried_letters or user_letter == '': 
            user_letter = input("The letter is unavailable, try again: ")
        self.user_tried_letters.append(user_letter.upper())
        print(self.current_game.show_letters(self.user_tried_letters))
        if self.current_game.check_letters(self.user_tried_letters):
            return True
        elif self.current_game.check(user_letter):
            return True
        else:
            return False

    def play(self):
        while self.turns > 0:
            if self.play_one_round():
                print("Congratulations You Won!")
                break
            elif self.turns == 0:
                print("Sorry, You lost")
                break