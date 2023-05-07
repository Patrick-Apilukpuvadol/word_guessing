# need to start coding functions listed in readme document

# importing the data sheet and random function
import data
import random
import re
from colored import fg, bg, attr
import string
from functions import win_game, lose_game, user_input, input_incorrect, guess_wrong

def win_game(mystery_word, partial_answer):
    print(f"{fg(10)}You have won!!! Congratulations!{attr(0)} The Mystery word was: {fg(11)} {mystery_word}{attr(0)}")
    save_name = input('Enter your name. ').title().upper()
    save_score = input('Enter the attempts you have left. ')

    text_file = open("highscores.txt", "a")
    text_file.write("\n" + save_name + ' has won 1 round with ' + save_score + ' attempts remaining' + "\n")
    text_file.close()
    
def lose_game(mystery_word, partial_answer):
    print(f"{fg(1)}You have lost...The Mystery word was: {attr(0)} {fg(11)}{mystery_word}{attr(0)}")


replay = True
while replay:
#Using Nested loop to facilitate replayability in the game
    # list of words available to the program to select when user runs the game (Need to add randomisation)
    # Need to check if only single word options work or 2 words work aswell. Will try
    mystery_words = ["PYTHON", "JAVASCRIPT", "INTEGERS", "STRING", "ENCYCLOPEDIA", "PROGRAMMING", "SOFTWARE"]
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
        c = input("Please Guess a Letter:  ").upper()
        if len(c) == 1 and c.isalpha():
            user_input(c)
        # accepting the user input and converting it into Uppercase
        
            
        else:
            input_incorrect(c)
            continue
            # trying to limit the characters that user can input to 1 letter
            
        if c in mystery_word:
            for i, x in enumerate(mystery_word):
                if x == c:
                    partial_answer = partial_answer[:i] + c + partial_answer[i+1:]
                    
        else:
            guess_wrong(c, wrong_guesses)
            # if c not in wrong_guesses:
            #     wrong_guesses.append(c)
                
        
            # else to make sure that wrong guess attemps are recorded and will update the hangman graphic
        print(data.guesses[len(wrong_guesses)])
        print(f"{fg(10)}Mystery Word: {partial_answer},{attr(0)} {fg(1)}Wrong Guesses: {', '.join(wrong_guesses)}{attr(0)} ")
        # printing the guess attempts and the mystery word
        
    # If function for when the mystery word letters have been guessed correctly it will display victory message
    if (mystery_word == partial_answer):
        win_game(mystery_word, partial_answer)
        
        
    else:
        lose_game(mystery_word, partial_answer)
        
        
    again = input('Would you like to play again? (y/n) ')
    if again == 'n':
        replay = False
        
        
    else:
        if again == 'y':
            replay = True
    # else added for when the hangman graphic has been completed and the user has run out of attempts. Message will pop up telling the user that they have lost and what the mystery word was.
    # again = input('Would you like to play again? (y/n) ')

    # if again == 'n':
    #     replay = False
        
    # else:
    #     if again == 'y':
    #         replay = True