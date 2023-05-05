# need to start coding functions listed in readme document

# importing the data sheet and random function
import data
import random
from colored import fg, bg, attr

# list of words available to the program to select when user runs the game (Need to add randomisation)
# Need to check if only single word options work or 2 words work aswell. Will try
mystery_words = ["PYTHON", "JAVASCRIPT", "INTEGERS", "CODER ACADEMY", "ENCYCLOPEDIA"]
# adding random function so program selects word randomly when user plays game
mystery_word = random.choice(mystery_words)


wrong_guesses = []

partial_answer = "_" * len(mystery_word)
# Needed to assign function that will generate word as partially answered when user guesses correct letters

print(data.guesses[len(wrong_guesses)])
print(f"Word: {partial_answer}")
# Printing shows the mystery word. Partial answer will be ashown in the amount od "_" for the user to guess

while len(wrong_guesses) < len(data.guesses) - 1 and partial_answer != mystery_word:
    # Creating a while loop that will continue to run as long as there are chaces available to the user
    c = input("Your Guess:  ").upper()
    # accepting the user input and converting it into Uppercase
    if c in mystery_word:
        for i, x in enumerate(mystery_word):
            if x == c:
                partial_answer = partial_answer[:i] + c + partial_answer[i+1:]
    else:
        if c not in wrong_guesses:
            wrong_guesses.append(c)
        # else to make sure that wrong guess attemps are recorded and will update the hangman graphic
    print(data.guesses[len(wrong_guesses)])
    print(f"Mystery Word: {partial_answer}, Wrong Guesses: {', '.join(wrong_guesses)} ")
    # printing the guess attempts and the mystery word
    
# If function for when the mystery word letters have been guessed correctly it will display victory message
if mystery_word == partial_answer:
    print(f"{fg(10)}You have won!!! Congratulations!{attr(0)} The Mystery word was: {fg(11)} {mystery_word}{attr(0)}")
        
else:
    print(f"{fg(1)}You have lost...The Mystery word was: {attr(0)} {fg(11)}{mystery_word}{attr(0)}")
# else added for when the hangman graphic has been completed and the user has run out of attempts. Message will pop up telling the user that they have lost and what the mystery word was.