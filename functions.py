import data
import random
import re
from colored import fg, bg, attr
import string

def win_game(mystery_word, partial_answer):
    print(f"{fg(10)}You have won!!! Congratulations!{attr(0)} The Mystery word was: {fg(11)} {mystery_word}{attr(0)}")
    save_name = input('Enter your name. ').title().upper()
    save_score = input('Enter the attempts you have left. ')

    text_file = open("highscores.txt", "a")
    text_file.write("\n" + save_name + ' has won 1 round with ' + save_score + ' attempts remaining' + "\n")
    text_file.close()
    
def lose_game(mystery_word, partial_answer):
    print(f"{fg(1)}You have lost...The Mystery word was: {attr(0)} {fg(11)}{mystery_word}{attr(0)}")
        
def user_input(c):
    print(c)
    #printing user input
    
def input_incorrect(c):
    print(f"{bg(196)}Please type in 1 letter at a time{attr(0)}")
    #Function to prompt user to input another guess within the program parameters
    
def guess_right(c, mystery_word, partial_answer, i, x):
    i = int
    x = str
    for i, x in enumerate(mystery_word):
        if x == c:
            partial_answer = partial_answer[:i] + c + partial_answer[i+1:]
            #Function that will check guess is right and add to partial answer
                
def guess_wrong(c, wrong_guesses):
    if c not in wrong_guesses:
        wrong_guesses.append(c)