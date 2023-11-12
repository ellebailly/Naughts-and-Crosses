# Naughts and crosses
# Programmed by Elle Bailly on 12th November 2023

import random

# Display the game rules upon launching the game
def OpeningText():
    print("~ Elle's Naughts and Crosses Game ~")

    print(""" 
      ~ Rules ~ 
      1. Select if you want to play as naughts or crosses - naughts plays first 
      2. Select where in the grid you would like to place your game piece by entering the position (1-9)
      3. Match 3 in a row to win! """)

    print("""
            -------------
            | 1 | 2 | 3 |
            -------------
            | 4 | 5 | 6 |
            -------------
            | 7 | 8 | 9 |
            -------------""")
    print(" ")

# User input and input validation
def UserInput():
  print("Select 'naughts' or 'crosses':")
  print("1 - Naughts (O)")
  print("2 - Crosses (X)")
  print("")
    
  selection = int(input())
  print("")
    
  while selection > 2 or selection < 1:
    print("Invalid input! Select '1' or '2' ")
    selection = int(input())

  if selection == 1:
    print("You have selected 'Naughts' ")
    print("You will play first")
    print("")
    
  else:
    print("You have selected 'Crosses' ")
    print("The computer will play first")
    print("")
  
  return selection

# Defining game grid as a blank array
grid = [[" ", " "," "],[" "," ", " "],[" "," "," "]]

# Displaying the game grid to the user
def ShowGrid(grid):
  print("-------------")
  print("| " + grid[0][0] + " | " + grid[0][1] + " | " + grid[0][2] + " |")
  print("-------------")
  print("| " + grid[1][0] + " | " + grid[1][1] + " | " + grid[1][2] + " |")
  print("-------------")
  print("| " + grid[2][0] + " | " + grid[2][1] + " | " + grid[2][2] + " |")
  print("-------------")

# Initiates gameplay based on player selected turn order
def Gameplay(playerOrder):
  # FOR loop to iterate through player and computer turns until grid is full
  for ii in range(0,9):
    if ii%2 == 0 and playerOrder == 1:
      playerText = "O"
      compText = "X"
      PlayerGameplay(playerText)
      ComputerGameplay(compText)
    
    elif ii%2 != 0 and playerOrder == 2:
      playerText = "X"
      compText = "O"
      ComputerGameplay(compText)
      PlayerGameplay(playerText)
 

# User input for their turn      
def PlayerGameplay(playerText):
  print(" ")
  print("It's your turn!")
  print(" ")

  square = int(input("Choose a square (1 - 9): "))

  # Square input validation
  while square > 9 or square < 1:
    print("Invalid input! Choose a square between 1 and 9 ")
    square = int(input())
    print(" ")
 
  # Convert user input to grid coordinates
  if square == 1 :
    row = 0
    col = 0
  elif square == 2 :
    row = 0
    col = 1
  elif square == 3 :
    row = 0
    col = 2
  elif square == 4 :
    row = 1
    col = 0
  elif square == 5 :
    row = 1
    col = 1
  elif square == 6 :
    row = 1
    col = 2
  elif square == 7 :
    row = 2
    col = 0
  elif square == 8 :
    row = 2
    col = 1
  elif square == 9 :
    row = 2
    col = 2

  # User input validation if chosen square is already occupied
  while grid[row][col] != " " :
    if grid[row][col] == "X" or grid[row][col] == "O":
      print("Square already occupied! Choose another one: ")
      square = int(input())
      if square == 1 :
        row = 0
        col = 0
      elif square == 2 :
        row = 0
        col = 1
      elif square == 3 :
        row = 0
        col = 2
      elif square == 4 :
        row = 1
        col = 0
      elif square == 5 :
        row = 1
        col = 1
      elif square == 6 :
        row = 1
        col = 2
      elif square == 7 :
        row = 2
        col = 0
      elif square == 8 :
        row = 2
        col = 1
      elif square == 9 :
        row = 2
        col = 2

  grid[row][col] = playerText
   
  ShowGrid(grid)
  CheckWinner(grid) 

def ComputerGameplay(compText):
  print(" ")
  print("It's the computers turn!")
  print(" ")

  row = random.randint(0,2)
  col = random.randint(0,2)
  
  # Checks computer selection against grid for squares that aren't empty / have a game piece in them 
  while grid[row][col] != " " :
    if grid[row][col] == "X" or grid[row][col] == "O":
      row = random.randint(0,2)
      col = random.randint(0,2)
  
  grid[row][col] = compText
      
  ShowGrid(grid)
  CheckWinner(grid) 

# Checks for a winning combination
def CheckWinner(grid) :
  win = False
  # Checking rows
  if grid[0][0] == "X" and grid[0][1] == "X" and grid[0][2] == "X" :
    print("Crosses wins!")
    win = True
    exit()
  elif grid[0][0] == "O" and grid[0][1] == "O" and grid[0][2] == "O" :
    print("Naughts wins!")
    win = True
    exit()
  
  if grid[1][0] == "X" and grid[1][1] == "X" and grid[1][2] == "X" :
    print("Crosses wins!")
    win = True
    exit()
  elif grid[1][0] == "O" and grid[1][1] == "O" and grid[1][2] == "O" :
    print("Naughts wins!")
    win = True
    exit() 
  
  if grid[2][0] == "X" and grid[2][1] == "X" and grid[2][2] == "X" :
    print("Crosses wins!")
    win = True
    exit()
  elif grid[2][0] == "O" and grid[2][1] == "O" and grid[2][2] == "O" :
    print("Naughts wins!")
    win = True
    exit()

  # Checking columns
  if grid[0][0] == "X" and grid[1][0] == "X" and grid[2][0] == "X" :
    print("Crosses wins!")
    win = True
    exit()
  elif grid[0][0] == "O" and grid[1][0] == "O" and grid[2][0] == "O" :
    print("Naughts wins!")
    win = True
    exit()
  
  if grid[0][1] == "X" and grid[1][1] == "X" and grid[2][1] == "X" :
    print("Crosses wins!")
    win = True
    exit()
  elif grid[0][1] == "O" and grid[1][1] == "O" and grid[2][1] == "O" :
    print("Naughts wins!")
    win = True
    exit() 
  
  if grid[0][2] == "X" and grid[1][2] == "X" and grid[2][2] == "X" :
    print("Crosses wins!")
    win = True
    exit()
  elif grid[0][2] == "O" and grid[1][2] == "O" and grid[2][2] == "O" :
    print("Naughts wins!")
    win = True
    exit()

  # Checking diagonals
  if grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X" :
    print("Crosses wins!")
    win = True
    exit()
  elif grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O" :
    print("Naughts wins!")
    win = True
    exit()
  
  if grid[0][2] == "X" and grid[1][1] == "X" and grid[2][0] == "X" :
    print("Crosses wins!")
    win = True
    exit()
  elif grid[0][2] == "O" and grid[1][1] == "O" and grid[2][0] == "O" :
    print("Naughts wins!")
    win = True
    exit()
  
# Main program
OpeningText()
userSelection = UserInput()
Gameplay(userSelection)




