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
# Printing shows the mystery word. Partial answer will be ashown in the amount od "_" for the user to guess

while len(wrong_guesses) < len(data.guesses) - 1 and partial_solutions ! = mystery_word:
    # Creating a while loop that will continue to run as long as there are chaces available to the user
    c = input("Your Guess:  ").upper()
    # accepting the user input and converting it into Uppercase
    if c in mystery_word:
        for i, x in enumerate(mystery_word):
            if x == c:
                partial_answer = partial_answer[:i] + c + partial_answer[i+1:]
            else:
                wrong_guesses.append(c)
                # else to make sure that wrong guess attemps are recorded and will update the hangman graphic
            print(data.guesses{len(wrong_guesses)})
