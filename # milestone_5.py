import random
word_list = ["Grape", "Pineapple", "Mango", "Blueberry", "Banana"]
word = random.choice(word_list)

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.word = word.lower()
        self.word_guessed = ['_'] *  len(self.word)
        self.num_letters = int(len(set(self.word)))
        self.num_lives = num_lives
        self.list_of_guesses = []

        print(f"The chosen word has {len(self.word)} characters")
        print("".join(self.word_guessed))

    def check_guess(self, guess):
        guess = str.lower(guess)
        if guess in self.word:
            print("Good guess!", guess, "is in the word.")
            for i in range(len(self.word)):
                if self.word[i] == guess:
                    self.word_guessed[i] = self.word[i]
            self.num_letters -= 1
            print(f"You have {self.num_lives} lives left.")
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")
    def ask_for_input(self):
        while True:
            guess = input("Choose a letter: ")
            if len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                print("".join(self.word_guessed))
                break

def play_game(word_list):
    num_lives = 5
    game = Hangman(word_list, num_lives)
    while True:
        if game.num_lives == 0:
            print("Game over. You lost!")
        if game.num_letters == 0:
            print("Congrats! you won!")
            break
        if game.word_guessed.count('_') > 0:
            game.ask_for_input()
            
play_game(word_list)


        
        
