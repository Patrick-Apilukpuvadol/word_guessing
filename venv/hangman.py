# need to start coding functions listed in readme document

# importing the data sheet and random function
import data
import random

# list of words available to the program to select when user runs the game (Need to add randomisation)
# Need to check if only single word options work or 2 words work aswell. Will try
mystery_words = ["PYTHON", "JAVASCRIPT", "INTEGERS", "CODER ACADEMY", "ENCYCLOPEDIA"]
# adding random function so program selects word randomly when user plays game
mystery_word = random.choice(mystery_words)


wrong_guesses = []

partial_answer = "_" * len(wrong_guesses)
# Needed to assign function that will generate word as partially answered when user guesses correct letters

print(data.guesses[len(wrong_guesses)])
print(f"Word: {partial_answer}")
# Print actions to make sure that the user is aware of what was guessed correctly and if they can surmise what the word is

while len(wrong_guesses) < len(data.guesses) - 1 and partial_solutions ! = mystery_word:
    c = input("Your Guess:  ").upper()
    # accepting the user input
    if c in mystery_word:
        
