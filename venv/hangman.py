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

while len(wrong_guesses)
