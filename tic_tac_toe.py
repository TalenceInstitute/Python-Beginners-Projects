# Define the game grid
grid = [[" "," "," "],[" "," "," "],[" "," "," "]]

def display_grid(grid):
  # Print the current game grid
  for row in grid:
    print(row)

def get_move(grid, player):
  # Ask the user for their move and update the grid
  while True:
    move = input(f"{player}, enter your move (row column): ")
    row, col = move.split()
    row, col = int(row), int(col)
    if grid[row][col] == " ":
      grid[row][col] = player
      break
    else:
      print("Invalid move. Try again.")

def check_win(grid):
  # Check if there are three of the same symbols in a row (horizontally, vertically, or diagonally)
  for row in range(3):
    if grid[row][0] == grid[row][1] == grid[row][2] and grid[row][0] != " ":
      return True
  for col in range(3):
    if grid[0][col] == grid[1][col] == grid[2][col] and grid[0][col] != " ":
      return True
  if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != " ":
    return True
  if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != " ":
    return True
  # Check if the grid is filled with no winner
  for row in grid:
    if " " in row:
      return False
  return None

# Ask the user which symbol they want to play as
player = input("Do you want to be X or O? ")

# Determine who goes first
import random
if random.randint(0, 1) == 0:
  computer = "O"
else:
  computer = "X"
if player == "X":
  other = "O"
else:
  other = "X"

# Start the game
while True:
  # Display the grid
  display_grid(grid)

  # User's turn
  get_move(grid, player)

  # Check if the user won
  result = check_win(grid)
  if result == True:
    display_grid(grid)
    print("You win!")
    break
  elif result == None:
    display_grid(grid)
    print("It's a draw!")
    break

  # Computer's turn
  while True:
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    if grid[row][col] == " ":
      grid[row][col] = computer
      break

  # Check if the computer won
  result = check_win(grid)
  if result == True:
    display_grid(grid)
    print("The computer wins!")
    break
  elif result == None:
    display_grid(grid)
    print("It's a draw!")
    break
