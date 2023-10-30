'''
Simple hangman game.
'''
import random
word_list = ["Grape", "Pineapple", "Mango", "Blueberry", "Banana"]

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_guess(guess)
        Checks if the letter is in the word.
    ask_for_input()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        
        self.word_list = word_list
        self.word = random.choice(word_list).lower()
        self.word_guessed = ['_'] *  len(self.word)
        self.num_letters = int(len(set(self.word)))
        self.num_lives = num_lives
        self.list_of_guesses = []

        print(f"The chosen word has {len(self.word)} characters")
        print("".join(self.word_guessed))


    def check_guess(self, guess) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # Make sure both words are in lowercase
        guess = str.lower(guess)
        word_lower = str.lower(self.word)

        if len(guess) == 1 and guess.isalpha():
            if guess in self.word:
                print("Good guess!", guess, "is in the word.")

                # Iterating through each position in the word to check for guess
                for i in range(len(self.word)):
                    if self.word[i] == guess:
                        # Placing guess in the place it was found
                        self.word_guessed[i] = self.word[i]
                # Decrementing number of lives
                self.num_letters -= 1
                print(f"You have {self.num_lives} lives left.")
            else:
                # If guess is incorrect, decrease number of lives
                self.num_lives -= 1
                print(f"Sorry, {guess} is not in the word.")
                print(f"You have {self.num_lives} lives left.")
        else:
            print("Invalid input. Please, enter a single alphabetical character.")

    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            # Ask user for input 
            guess = input("Choose a letter: ")
            # Check for invalid input
            if len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            # If guess is valid and hasn't been guessed before
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                # Reveal current state
                print("".join(self.word_guessed))
                # Exit loop allowing player to continue
                break

# Define a function to play the game
def play_game(word_list):
    # Set the initial number of lives to 5
    num_lives = 5
    # Create an instance of the game with the provided word list and lives
    game = Hangman(word_list, num_lives)
    # Start an infinite loop for playing the game
    while True:
        # Check if the player has run out of lives
        if game.num_lives == 0:
            print("Game over. You lost!")
            break
        # Check if the player has successfully guessed all the letters in the word
        if game.num_letters == 0:
            print("Congrats! you won!")
            break
        # Check if there are still underscores (_) in the guessed word
        if game.word_guessed.count('_') > 0:
            game.ask_for_input()

play_game(word_list)

if __name__ == '__main__':
    word_list = ["Grape", "Pineapple", "Mango", "Blueberry", "Banana"]
    play_game(word_list)
# %%