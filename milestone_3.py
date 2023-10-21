## H A N G M A N
import random
word_list = ["Grape", "Pineapple", "Mango", "Blueberry", "Banana"]
random_word = random.choice(word_list)

def ask_for_input():
    while True:
        guess = input("Choose a letter: ")
        guess = guess
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    return guess

guess = ask_for_input()
    
def check_guess(random_word, guess):
    if guess in random_word:
        print("Good guess!", guess, "is in the word.")
    else:
        print("Sorry,", guess, "is not in the word. Try again.")

check_guess(random_word, guess)

