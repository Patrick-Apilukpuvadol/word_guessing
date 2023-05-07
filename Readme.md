

Working on the ideas for the interminal game and the functions to add to the project. Apologies for the lack of commits on this project. i have tried my best to reach the 20 commits but I was juggling this assignment with the Workbook assignment and a fulltime job which took me a considerable amount of time to sort. 

# Youtube

https://youtu.be/mOn9qXO5vYU

# GitHub

git@github.com:Patrick-Apilukpuvadol/word_guessing.git

# Trello Board - Project Task Management

https://trello.com/invite/b/ZgM2Saxc/ATTI9e9f4c855a6f3e70b87c8ee38a22443e9E0C8464/project-tasks

https://trello.com/b/ZgM2Saxc/project-tasks

# Introduction

Game will be a Word guessing game (like Hangman) where the user will guess the letters until they get the completed word or they run out of attempts

With the features the in terminal program will have the following features

# Feature that receives user input

```python
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

def input_incorrect(c):
    print(f"{bg(196)}Please type in 1 letter at a time{attr(0)}")
    #Function to prompt user to input another guess within the program parameters
```

In this feature I used the following code to take the user input and ensure that it is within the format that the program will accept. 

For this case the input needed to be a Letter and only 1 Letter at a time. 

Since all the mystery words were in caps I made sure that the user's input will be automatically converted to uppercase

I also added if/else statement to make sure that the input was only 1 character and it was a letter from the alphabet. The Else portion was for the situation that the user inputs something invalid like a number or 2 letters by accident, the program will prompt the user to enter a single letter. 

# Feature that Selects random choice of word from list

```python
mystery_words = ["PYTHON", "JAVASCRIPT", "INTEGERS", "STRING", "ENCYCLOPEDIA", "PROGRAMMING", "SOFTWARE"]
    # adding random function so program selects word randomly when user plays game
    mystery_word = random.choice(mystery_words)
    wrong_guesses = []

    partial_answer = "_" * len(mystery_word)
    # Needed to assign function that will generate word as partially answered when user guesses correct letters

    print(data.guesses[len(wrong_guesses)])
    print(f"Word: {partial_answer}")
    # Printing shows the mystery word. Partial answer will be ashown in the amount od "_" for the user to guess
```

For this feature I imported the random module to utilise the random.choice function. This was for the list that I have entered some words that will be the mystery words in the game. 

To make sure that the mystery word will stay a mystery word I assigned an "_" with the function len to make sure that the mystery word selected will be only underscores numbering to the same amount of letters of the mystery word. 

# Feature that will keep track of user correct and incorrect guesses

```python  
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

def guess_wrong(c, wrong_guesses):
    if c not in wrong_guesses:
        wrong_guesses.append(c)
```
# Example
Attempts left 3
+--,
|  o
| /|
|
|
Mystery Word: S_F_____, Wrong Guesses: D, G, H, J
Please Guess a Letter:  k

In the game I needed the response to the user's input to have clear feedback. I added some if/else statements that will allow the input from the user to either be correct or incorrect. If it is correct the user's input will update the partial_answer adding the correctly guessed letters to the mystery word while also placing them in the correct positions in correspondence to the mystery word. 

Else its incorrect where the function guess_wrong will add the incorrect guess to wrong_guesses. If the incorrectly guessed input is already part of the list, the program will prompt to enter another input. 

# Feature to restart game whether the user wins or loses

```python
    again = input('Would you like to play again? (y/n) ')
    if again == 'n':
        replay = False
        
        
    else:
        if again == 'y':
            replay = True
```

Added this feature to have seemless replayability to the program. At the end of the program (Whether they win or lose) the user will be prompted if they would like to play again 

If/Else statement used so that the program will break program if user inputs "n" or program will restart with new random mystery_word if user inputs "y"

# Score Recording of wins and how many attempts left
```python
    if (mystery_word == partial_answer):
        win_game(mystery_word, partial_answer)
        
        
    else:
        lose_game(mystery_word, partial_answer)

def win_game(mystery_word, partial_answer):
    print(f"{fg(10)}You have won!!! Congratulations!{attr(0)} The Mystery word was: {fg(11)} {mystery_word}{attr(0)}")
    save_name = input('Enter your name. ').title().upper()
    save_score = input('Enter the attempts you have left. ')

    text_file = open("highscores.txt", "a")
    text_file.write("\n" + save_name + ' has won 1 round with ' + save_score + ' attempts remaining' + "\n")
    text_file.close()

def lose_game(mystery_word, partial_answer):
    print(f"{fg(1)}You have lost...The Mystery word was: {attr(0)} {fg(11)}{mystery_word}{attr(0)}")
```

For this Feature I wanted to add score keeping function that will prompt the user to enter their name and attempts left if they have won the round. 

Once they have completed entering their details the data will be stored in the highscores.txt file. 


# In-terminal graphics to make the game more responsive

```python
Attempts left 0
+--,
|  o
| /|\
| / \
|

""".strip().split("\n\n")
```

I added some graphics in the terminal by utilising a separate data python file. 

Within this file I list all the stages of the hangman that indicates the attempts they have left.

I used the strip().split(\n\n") method to ensure that the each of the strings will be interpreted as intended.

# Notes of progress

29/04/23

- Function where program takes user input and verifies if it matches with any letters in the word in the guess. Need to make sure that the letters coinside with the positioning relative to rest of the word. 

- Function to keep track of how many guesses the user has left to be indicated. Want to try add interminal graphics like hang man to make the game more resposive to the user

- Function that keeps a record of the correct and incorrect letter guesses. Correct letter guesses will appear in the mystery word and in the correct positioning in relation to the word. Incorrect guesses must appear on the side list. Will add function that will stop the user from entering duplicate letter guesses so it doesn't waste the user's turns

- Function that will keep the users score of correctly guessed words as a high score

- Function that the program will randomly select from a list of words provided and will display the amount of letters in underscores " _ "

02/05/2023

- Still triying to figure out the requirements text document and how to auto generate it. 
- Imported the Random function into the main game and implemented into program so game will choose random word from listed options. 
- At the moment only have number of guesses for user list down as a number. Want to implement graphics like hangman where it will show each portion of the hangman as the user guesses the incorrect letter. 

03/05/2023

- Completed graphical out to indicate the guesses left for the user 
- explained the partial_answer value and how it will assist the user in understanding what was guessed correctly
- Created Print actions that will indicate to the user the following 
    - Print the Graphic of Hangman for guesses left
    - Print the partial_solution for user to see what was guessed correctly 
    - Print the wrong_guesses for the user

04/05/23 - 05/05/2023

- Completed a rough idea of how the game will end and how the solutions will be printed out. 
- completed the print functions for the mystery word and the hangman grapic indicating the guesses left. 

6/05/23
- completed some additional testing and still need to fix visual output

07/05/2023
- Added some indication of attempts left to improve user visibility of how many chances they have left
- Added and fixed some colour importat issues in the code
- Working on adding some replayability to the game

- Added some replayability in the game by using a Nested loop within the progam so that the user can choose to either play or end the program

- Added additional record keeping feature to keep track of users that have won a round of the game and how many attempts that they have left. 

- Created some limitations of user input to ensure that user can use only letters in the game to prevent program errors so it is handled gracefully

- Added requirements.txt document to the run executable file so that it updates with the modules used in the program. 

- completed tests and run as expected 

07/05/23

- Added some functions to the program and defining the, 
- created an additional functions page to import functions to reduce clutter in the main program. 
- removed some test functions from the main program code to free up space. 
- completed the readme file and amended some instructions to improve user experience
- completed the presentation of project

