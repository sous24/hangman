
import random
import numpy as np
word_list = ["Grape", "Pineapple", "Mango", "Blueberry", "Banana"]
random_word = random.choice(word_list)

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = random_word
        self.word_guessed = ['_'] *  len(self.word)
        self.num_letters = int(len(np.unique(list(self.word))))
        self.num_lives = num_lives
        self.list_of_guesses = []
    def check_guess(self, guess):
        self.guess = guess.lower()
        if guess in self.word:
            print("Good guess!", guess, "is in the word.")
            for i in range(len(self.word)):
                if self.word_guessed == guess:
                    self.word_guessed[i] = self.word[i]
            self.num_letters -= 1
        else:
            print("Sorry, {guess} is not in the word.")
            self.num_lives -= 1
            print("You have {num_lives} lives left.")
    def ask_for_input(self):
        while True:
            self.guess = input("Choose a letter: ")
        if len(guess) != 1:
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)
game = Hangman(word_list)
game.ask_for_input()