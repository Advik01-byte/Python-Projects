from random import randrange as rdn # Importing the random number generator

wins = 0; losses = 0; ties = 0 # Initializing scores

User_Move = input("\nChoose (Rock, Paper, Scissors or e to exit): ") # User input for the game
Random_Move = rdn(1, 4) # Generating a random move for the computer

# Mapping random number to game moves
if Random_Move == 1:
  Random_Move = "rock"
elif Random_Move == 2:
  Random_Move = "paper"
else:
  Random_Move = "scissors"

if User_Move.lower() == "rock": # Checking if the user chose rock
  # Determining the outcome based on the random move
  if Random_Move == "rock":
    print("It's a tie! You both chose Rock.")
    ties += 1
  elif Random_Move == "paper":
    print("You lose! Paper covers Rock.")
    losses += 1
  else:
    print("You win! Rock crushes Scissors.")
    wins += 1
elif User_Move.lower() == "paper": # Checking if the user chose paper
  # Determining the outcome based on the random move
  if Random_Move == "rock":
    print("You win! Paper covers Rock.")
    wins += 1
  elif Random_Move == "paper":
    print("It's a tie! You both chose Paper.")
    ties += 1
  else:
    print("You lose! Scissors cut Paper.")
    losses += 1
elif User_Move.lower() == "scissors": # Checking if the user chose scissors
  # Determining the outcome based on the random move
  if Random_Move == "rock":
    print("You lose! Rock crushes Scissors.")
    losses += 1
  elif Random_Move == "paper":
    print("You win! Scissors cut Paper.")
    wins += 1
  else:
    print("It's a tie! You both chose Scissors.")
    ties += 1
elif User_Move.lower() == "e": # Checking if the user wants to exit
  # Displaying the final score and exiting the game
  print(f"\nYour final score: Wins: {wins}, Losses: {losses}, Ties: {ties}")
  print("\nExiting the game. Goodbye!\n")
  exit()
else: # Handling invalid input
  # Prompting the user to enter a valid move
  print("\nInvalid move. Please choose Rock, Paper, or Scissors.\n")

while User_Move.lower() != "e": # Continue the game the same as above until the user chooses to exit
  User_Move = input("Choose (Rock, Paper, Scissors or e to exit): ")
  Random_Move = rdn(1, 4)

  if Random_Move == 1:
    Random_Move = "rock"
  elif Random_Move == 2:
    Random_Move = "paper"
  else:
    Random_Move = "scissors"

  if User_Move.lower() == "rock":
    
    if Random_Move == "rock":
      print("It's a tie! You both chose Rock.")
      ties += 1
    elif Random_Move == "paper":
      print("You lose! Paper covers Rock.")
      losses += 1
    else:
      print("You win! Rock crushes Scissors.")
      wins += 1
  elif User_Move.lower() == "paper":
    if Random_Move == "rock":
      print("You win! Paper covers Rock.")
      wins += 1
    elif Random_Move == "paper":
      print("It's a tie! You both chose Paper.")
      ties += 1
    else:
      print("You lose! Scissors cut Paper.")
      losses += 1
  elif User_Move.lower() == "scissors":
    if Random_Move == "rock":
      print("You lose! Rock crushes Scissors.")
      losses += 1
    elif Random_Move == "paper":
      print("You win! Scissors cut Paper.")
      wins += 1
    else:
      print("It's a tie! You both chose Scissors.")
      ties += 1
  elif User_Move.lower() == "e":
    print(f"\nYour final score: Wins: {wins}, Losses: {losses}, Ties: {ties}")
    print("\nExiting the game. Goodbye!\n")
    exit()
  else:
    print("\nInvalid move. Please choose Rock, Paper, or Scissors.\n")
    continue