#### H A N G M A N

import random
word_list = ["Grape", "Pineapple", "Mango", "Blueberry", "Banana"]
random_word = random.choice(word_list)
print(random_word)

# User input
user_guess = input("Choose a letter: ")
if len(user_guess) <= 1 and user_guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input. You chose,", user_guess, "Please choose a letter")
