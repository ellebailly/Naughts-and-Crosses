# Naughts-and-Crosses
A single-player naughts and crosses game played against the computer

DATE PROGRAMMED: 12/11/23

LANGUAGE: Python 

FUNCTIONALITY: 

• Naughts plays first in every game

• The player is able to select if they want to play as 'X' or 'O', with the computer taking the game piece the player doesn't select

• User input validation is included in this step and the player will be prompted to select either 1 or 2 until a valid input is detected

• The play order is determined based on what game piece the player selects

• The player is prompted to select a grid space to place their game piece (1 through 9) 

• User input validation is included in this step and the player will be prompted to re-input a number within the range until a valid input is detected

• If the player selects a square that is already occupied by either a computer or player game piece, the player is again prompted to make another selection until a blank square is selected

• The computer plays its game pieces by randomly generating a coordinate in the grid and has no intelligence or strategy programmed into it on how a game is won

• If a grid square is already occupied by either a player or computer game piece, it will continue to randomly generate grid coordinates until an empty grid square set of coordinates is generated and the game piece can be successfully placed

• The game board is updated after the computer and player each make a valid turn

• The program will detect when a game has been won, and display which game piece was the winner (‘X’ or ‘O’) 

IMPROVEMENTS:

• No message for tie condition

• No error handling for if player inputs anything other than a number when prompted for an input 
