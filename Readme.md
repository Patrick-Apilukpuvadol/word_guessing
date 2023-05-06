Working on the ideas for the interminal game and the functions to add to the project. Apologies for the lack of commits on this project. i have tried my best to reach the 20 commits but I was juggling this assignment with the Workbook assignment which took me a considerable amount of time. 



Trello Board - Project Task Management

https://trello.com/b/ZgM2Saxc



Game will function basically as hangman where the user will guess the letters until they get the completed word

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