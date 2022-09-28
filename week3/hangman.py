import random

class SecretWord:
    def __init__(self, word = None):
        if word == None:
            with open('words.txt', 'r') as words:
                self.word = random.choice(words.read().splitlines())
        else:
            self.word = word

    def show_letters(self, letters):
        word = self.word.upper()
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
        
    def check_letters(self, letters):
        letters = [letter.upper() for letter in letters]
        for i in self.word.upper():
            if i in letters:
                continue
            else:
                return False
        return True

    def check(self, word):
        if self.word.upper() == word.upper():
            return True
        return False

class Game:
    def __init__(self, turns = 10):
        self.secret_word = SecretWord()
        self.letters = []
        self.turns = turns

    def play_one_round(self):
        print(f'{self.turns} turns remaining.')
        print(self.secret_word.show_letters(self.letters))
        self.turns -= 1
        input_verified = False
        while input_verified == False:
            user_input = input("Enter an untried letter or try to guess the word: ")
            if len(user_input) > 1:
                input_verified = True
                if self.secret_word.check(user_input) == True:
                    return True
            elif len(user_input) > 0:
                if user_input not in self.letters:
                    input_verified = True
                    self.letters.append(user_input)
        if self.secret_word.check_letters(self.letters) == True:
            return True
        return False
        
    def play(self):
        while self.turns > 0:
            win = self.play_one_round()
            if win == True:
                break

        if win == True:
            print(f'You won the game, the word was {self.secret_word.word}. You had {self.turns} turns remaining.')
        else: 
            print(f'You lost, the word was {self.secret_word.word}.')
                


if __name__ == '__main__':
    my_game = Game(10)  # for 10 turns 
    my_game.play() 