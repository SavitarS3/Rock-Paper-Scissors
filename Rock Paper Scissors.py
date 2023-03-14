import random

# Keeps track of number of wins and tries for loop.
numberOfWins = 0
numberOfTries = 0

# While the user has less than 10 wins: 
while numberOfWins < 10:

  # User chosen move
  move = input("Choose Rock, Paper or Scissors: ")

  # List of possible moves to check whether user moves exist.
  possibleMoves = ["rock", "paper", "scissors"]

  # If the user did not input the  correct move, ask for a move again. f the user did not in 
  while (move.lower() in possibleMoves) == False:
    move = input("Invalid Move, Choose Rock, Paper or Scissors: ")

  # AI choosing randomly between the possible moves.
  enemyMove = random.choice(possibleMoves)

  # List of possible wins with the first index of each sublist being the player.
  wins = [["rock", "scissors"], ["paper", "rock"], ["scissors", "paper"]]

  # Current gamestate
  gameState = [move, enemyMove]

  result = None

  # If the gamestate is a win for the player, set result to win, if the 
  # gamestate is a draw, set result to tied.
  if gameState in wins:
      result = "Win"
      
  elif move == enemyMove:
      result = "Tied"

  # If the result is a win, print a win message with the moves and 
  # increase tries and wins by 1.
  if result == "Win": 
    print("You won with " + move + " against the AI's " + enemyMove + "!")
    numberOfWins += 1
    numberOfTries += 1

  # If the result is a tie, print a tie message and increase tries by 1.
  elif result == "Tied":
    print("You tied with " + move + "!")
    numberOfTries += 1

  # Else, print a loss message and increase tries by 1.
  else: 
    print("You lost with " + move + " against the AI's " + enemyMove + "!")
    numberOfTries += 1
  print("Number of Wins: ", numberOfWins)

# Final print message telling user they won 10 times in the number of tries it 
# took them.
print("You won 10 times in " + str(numberOfTries) + " tries!")