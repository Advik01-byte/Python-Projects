from random import randrange # Make sure to import the randrange function from the random module

tries = 0 # Start with 0 tries

def Guess(Guessornot, tries, MaxAndMin_Number, Min_Number = 1, Max_Number = 50): # Create a function to handle the guessing game
  global Random_Number, User_Number, Computer_Number, Greater_or_Smaller, Min, Max # Declare global variables to be used in the function

  if Guessornot.lower() == "y": # If the user wants to guess the computer's number
    Random_Number = MaxAndMin_Number # Set the random number to be guessed by the user
    User_Number = int(input(f"\nChoose a number from {Min_Number} to {Max_Number}: ")) # Get the user's guess
    
    while User_Number < Min_Number or User_Number > Max_Number: # Check if the user's guess is within the valid range
      print(f"You can only choose a number between {Min_Number} and {Max_Number}.") # If not, print an error message
      User_Number = int(input(f"\nChoose a number from {Min_Number} to {Max_Number}: ")) # Get the user's guess
    
    if User_Number < Random_Number: # Check if the user's guess is smaller than the random number
      tries += 1 # Increment the number of tries and print a hint
      print("Your number is smaller than my number")
    elif User_Number > Random_Number: # Check if the user's guess is larger than the random number
      tries += 1 # Increment the number of tries and print a hint
      print("Your number is larger than my number")
    else: # If the user's guess is correct
      tries += 1 # Increment the number of tries and congratulate the user
      print(f"\nCongratulations! You guessed the number {Random_Number} in {tries} tries.\n")
      return # Exit the function
    while User_Number != Random_Number: # Continue the same as above until the user guesses the correct number
      User_Number = int(input(f"\nTry again! Choose a number from {Min_Number} to {Max_Number}: "))
      if User_Number < Min_Number or User_Number > Max_Number: # Check if the user's guess is within the valid range
        print(f"\nPlease enter a number between {Min_Number} and {Max_Number}.\n")
        continue # If not, prompt the user to try again

      tries += 1
      
      if User_Number < Random_Number:
        print("Your number is smaller than my number")
      elif User_Number > Random_Number:
        print("Your number is larger than my number")
      else:
        print(f"\nCongratulations! You guessed the number {Random_Number} in {tries} tries.")
        return # Exit the function
  elif Guessornot.lower() == "n": # If the user does not want to guess the computer's number
    Random_Number = int(input(f"\nChoose a number from {Min_Number} to {Max_Number} for the computer to guess: ")) # Get the number for the computer to guess
    
    while Random_Number < Min_Number or Random_Number > Max_Number: # Check if the user's number is within the valid range
      print(f"\nPlease enter a number between {Min_Number} and {Max_Number}.") # If not, print an error message
      Random_Number = int(input(f"\nChoose a number from {Min_Number} to {Max_Number} for the computer to guess: ")) # If not, prompt the user to try again

    Computer_Number = MaxAndMin_Number # Set the computer's initial guess to the random number

    Min = Min_Number # Set the minimum range for the computer's guesses
    Max = Max_Number # Set the maximum range for the computer's guesses

    print(f"The computer guessed: {Computer_Number}") # Print the computer's initial guess
    Greater_or_Smaller = input("\nPlease enter >, <, or = as per the number the computer guessed (> for greater, and < for smaller in comparision to your number): ") # Get the user's feedback on the computer's guess
    
    if Greater_or_Smaller == ">": # If the computer's guess is greater than the random number
      # Increment the number of tries and adjust the range for the next guess
      tries += 1
      Max = Computer_Number
      Computer_Number = randrange(Min, Max)
    elif Greater_or_Smaller == "<": # If the computer's guess is smaller than the random number
      # Increment the number of tries and adjust the range for the next guess
      tries += 1
      Min = Computer_Number + 1
      Computer_Number = randrange(Min, Max)
    elif Greater_or_Smaller == "=": # If the computer's guess is correct
      # Increment the number of tries and print the result
      tries += 1
      print(f"\nThe computer guessed the number {Random_Number} in {tries} tries.")
      return
    else: # If the user enters an invalid input
      # Print an error message and prompt for valid input
      print("Wrong input entered. Input can only be: >, <, or =")

    while Greater_or_Smaller != "=": # Continue the same as above until the computer guesses the correct number
      print(f"The computer guessed: {Computer_Number}")
      Greater_or_Smaller = input("\nPlease enter >, <, or = as per the number the computer guessed (> for greater, and < for smaller in comparision to your number): ")
      
      if Greater_or_Smaller == ">":
        tries += 1
        Max = Computer_Number
        Computer_Number = randrange(Min, Max)
      elif Greater_or_Smaller == "<":
        tries += 1
        Min = Computer_Number
        Computer_Number = randrange(Min, Max)
      elif Greater_or_Smaller == "=":
        tries += 1
        print(f"\nThe computer guessed the number {Random_Number} in {tries} tries.")
        return
      else:
        print("Wrong input entered. Input can only be: >, <, or =")
  else: # If the user enters an invalid input
    # Print an error message and prompt for valid input
    print("\nWrong input entered. Input can only be: Y or N.")

Game_Mode = input("\nChoose a game mode (Easy, Medium, Hard): ") # Prompt the user to choose a game mode

if Game_Mode.lower() == "easy": # If the user chooses the easy mode
  Guessornot = input("Do you want to guess the computer's number? Type y for yes and n for no: ") # Ask if the user wants to guess the computer's number

  Guess(Guessornot, tries, randrange(1, 51), 1, 50) # Call the Guess function with the appropriate parameters

  print("\nThanks for playing!\n") # Print a thank you message after the game ends
elif Game_Mode.lower() == "medium": # If the user chooses the medium mode
  Guessornot = input("Do you want to guess the computer's number? Type y for yes and n for no: ") # Ask if the user wants to guess the computer's number

  Guess(Guessornot, tries, randrange(1, 101), 1, 100) # Call the Guess function with the appropriate parameters

  print("\nThanks for playing!\n") # Print a thank you message after the game ends
elif Game_Mode.lower() == "hard": # If the user chooses the hard mode
  Guessornot = input("Do you want to guess the computer's number? Type y for yes and n for no: ") # Ask if the user wants to guess the computer's number

  Guess(Guessornot, tries, randrange(1, 501), 1, 500) # Call the Guess function with the appropriate parameters

  print("\nThanks for playing!\n") # Print a thank you message after the game ends
else: # If the user enters an invalid game mode
  print("\nWrong input entered. Input can only be: Easy, Medium, Hard.\n") # Print an error message and prompt for valid input
  print("Please restart the game and choose a valid game mode.\n") # Prompt the user to restart the game with a valid mode
  exit() # Exit the program