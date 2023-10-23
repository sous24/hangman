## H A N G M A N
import random
word_list = ["Grape", "Pineapple", "Mango", "Blueberry", "Banana"]
random_word = random.choice(word_list)
def check_guess(random_word, guess):
    guess = guess.lower()
    if guess in random_word:
        print("Good guess!", guess, "is in the word.")
    else:
        print("Sorry,", guess, "is not in the word. Try again.")

def ask_for_input():
    while True:
        guess = input("Choose a letter: ")
        if len(guess) == 1 and guess.isalpha():
            check_guess(random_word, guess)
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    return guess

ask_for_input()
    
