import random

# Stores the configuration of the board. 
board = []
 
# Creates a 5 x 5 board.
for x in range(0,5):
  board.append(["O"] * 5)

# Method prints each row of the board. 
def print_Board(board):
  for row in board:
    print (" ".join(row))

# Opening statment and prints board.
print ("Let's play Battleship!\n")
print_Board(board)
print("\n")
 
# Sets row coordinate location of ship.
def random_Row(board):
  return random.randint(0,len(board)-1)

# Sets column coordinate location of ship.
def random_Col(board):
  return random.randint(0,len(board[0])-1)
 
# Variables store locations of ship.
ship_Row = random_Row(board)
ship_Col = random_Col(board)

# Sets the maximum amount of guesses a player can have until game is over.
guesses = 18

for turn in range(guesses):
	guess_Row = int(input("\nGuess Row:\t"))
	guess_Col = int(input("Guess Col:\t"))

	# If the player inputs coordinates ship was located in, he wins.
	if guess_Row == ship_Row and guess_Col == ship_Col:
	  print ("Congratulations! You sunk my battleship!")
	  # For-loop ends.
	  break
	else:
	  # If the player doesn't guess within 5x5 constraint, error message appears.
	  if (guess_Row < 0 or guess_Row > 4) or (guess_Col < 0 or guess_Col > 4):
	    print ("\nOops, that's not even in the ocean.")
	  # If the player guesses an earlier position inputted, warning message appears.
	  elif(board[guess_Row][guess_Col] == "X"):
	    print ("\nYou guessed that one already.")
	    # Returns a guess to compensate for an accidental move.
	    guesses += 1
	  # If the player guesses incorrectly, a "X" appears.
	  else:
	  	print ("\nYou missed my battleship!")
	  	board[guess_Row][guess_Col] = "X"
	  	# If player runs out of guesses, the game is over.
	  	if turn == (guesses-1):
	  		print ("\nGame Over")
	  		quit()
	  # Tells player what turn they are on.
	  print ("This is your", (turn+1), "-eth guess.\n")
	  # Prints out current state of the board.
	  print_Board(board)
