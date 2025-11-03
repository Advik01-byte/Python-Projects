import random
from time import sleep

# Tell what the game is about
print('This game is related to cricket')
print('\n')
print('In the original game mode, You have to choose odd or even and then type a number between 1 - 10')
print('If the sum of the computer\'s and the player\'s number is even, then the player who chose even will win the toss, otherwise the other player wins the toss')
print('The player who wins will choose batting or bowling')
print('If you chose batting, then you have to make as many runs as possible without the bowler getting the same number as you (From 1 - 10).' + '\n' + 'Otherwise you have to get the other player out in the same way, and then you\'ll get the chance to do batting')
print('\n')
print('There are other game modes also, you\'ll learn while playing')
'''
Choose a game mode:
Toss
Original
Multiplication
'''
GmMod = input('Choose game mode (Toss / Original / Multiplication) or \'exit\' to quit: ')

if GmMod.lower() == 'toss':
  # TOSS
  # Make player choose odd or even
  OddEven = input('Choose odd or even: ')
  Num = input('Choose number from 1 to 10: ')
  Num = int(Num)
  # Choose random number between 1 - 10 for computer to play next
  Ran = random.randrange(1, 11)
  Runs = 0
  Runs_1 = 1
  # Based on what number player did, find if its sum is even or not
  # If the number is even, then the person who chose even will add the sum to their runs.
  # This will go until a person does not get their chosen type of number (Odd or Even)
  if OddEven.lower() == 'even':
    while ((Num + Ran) % 2) == 0:
      print(Ran)
      if Num > 10:
        print('ERROR. You can only choose the number from 1 to 10.')
        Runs -= Num + Ran
      Runs += Num + Ran
      Runs_1 = Runs + 1
      print('You have ' + str(Runs) + ' runs currently')
      Ran = random.randrange(1, 11)
      Num = input('Choose number from 1 to 10: ')
      Num = int(Num)
    print(Ran)
    print('You are out with ' + str(Runs) + ' runs' + '\n' + 'The computer\'s target is ' + str(Runs_1) + ' runs')
  elif OddEven.lower() == 'odd':
    while ((Num + Ran) % 2) > 0:
      print(Ran)
      if Num > 10:
        print('ERROR. You can only choose the number from 1 to 10.')
        Runs -= Num + Ran
      Runs += Num + Ran
      Runs_1 = Runs + 1
      print('You have ' + str(Runs) + ' runs currently')
      Ran = random.randrange(1, 11)
      Num = input('Choose number from 1 to 10: ')
      Num = int(Num)
    print(Ran)
    print('You are out with ' + str(Runs) + ' runs' + '\n' + 'The computer\'s target is ' + str(Runs_1) + ' runs')
  else:
    print('ERROR. Value can only be "Odd" or "Even"')
  # Then the other person will do the same thing until they are also out like the last person and then their scores will compare
  # Person with higher score will win
  Runs_Comp = 0
  Ran = random.randrange(1, 11)
  Num = input('Choose a number from 1 to 10 to try to get the computer out: ')
  Num = int(Num)
  if OddEven.lower() == 'even':
    while ((Num + Ran) % 2) > 0:
      print(Ran)
      if Num > 10:
        print('ERROR. You can only choose the number from 1 to 10.')
        Runs_Comp -= Num + Ran
      Runs_Comp += Num + Ran
      print('Computer has ' + str(Runs_Comp) + ' runs currently')
      Ran = random.randrange(1, 11)
      Num = input('Choose a number from 1 to 10 to try to get the computer out: ')
      Num = int(Num)
    print(Ran)
    print('Computer is out with ' + str(Runs_Comp) + ' runs' + '\n' + 'Now we have to compare scores')
    sleep(3)
    if Runs > Runs_Comp:
      print('CONGRATULATIONS. You have won!')
    elif Runs < Runs_Comp:
      print('Computer has won')
    else:
      print('It is a tie')
  elif OddEven.lower() == 'odd':
    while ((Num + Ran) % 2) == 0:
      print(Ran)
      if Num > 10:
        print('ERROR. You can only choose the number from 1 to 10.')
        Runs_Comp -= Num + Ran
      Runs_Comp += Num + Ran
      print('Computer has ' + str(Runs_Comp) + ' runs currently')
      Ran = random.randrange(1, 11)
      Num = input('Choose a number from 1 to 10 to try to get the computer out: ')
      Num = int(Num)
    print(Ran)
    print('Computer is out with ' + str(Runs_Comp) + ' runs' + '\n' + 'Now we have to compare scores')
    sleep(3)
    if Runs > Runs_Comp:
      print('CONGRATULATIONS! You have won!')
    elif Runs < Runs_Comp:
      print('Computer has won')
    else:
      print('It is a tie')
elif GmMod.lower() == 'original':
  # ORIGINAL
  # Make player choose odd or even
  OddEven = input('Choose odd or even: ')
  Ran = random.randrange(1, 11)
  # They'll do the toss, and the person who wins will choose batting or bowling
  Num = input('Choose a number from 1 to 10: ')
  Num = int(Num)
  print(Ran)
  Comp_BatOrBowl = ''
  BatOrBowl = ''
  if ((Ran + Num) % 2) == 0 and OddEven.lower() == 'even':
    BatOrBowl = input('Choose batting or bowling: ')
  elif ((Ran + Num) % 2) > 0 and OddEven.lower() == 'odd':
    BatOrBowl = input('Choose batting or bowling: ')
  elif ((Ran + Num) % 2) == 0 and OddEven.lower() != 'even':
    Ran_For_BatBall = random.randrange(1, 3)
    if Ran_For_BatBall == 1:
      Comp_BatOrBowl = 'Batting'
      print('Computer has chosen ' + Comp_BatOrBowl + '.')
    elif Ran_For_BatBall == 2:
      Comp_BatOrBowl = 'Bowling'
      print('Computer has chosen ' + Comp_BatOrBowl + '.')
  elif ((Ran + Num) % 2) > 0 and OddEven.lower() != 'odd':
    Ran_For_BatBall = random.randrange(1, 3)
    if Ran_For_BatBall == 1:
      Comp_BatOrBowl = 'Batting'
      print('Computer has chosen ' + Comp_BatOrBowl + '.')
    elif Ran_For_BatBall == 2:
      Comp_BatOrBowl = 'Bowling'
      print('Computer has chosen ' + Comp_BatOrBowl + '.')

  # The person who chooses batting will try to make as many runs as they can
  # If the bowler's and batsman's number is same, then the batsman is out.
  if Comp_BatOrBowl == 'Batting' or BatOrBowl.lower() == 'bowling' :
    Comp_Runs = 0
    Target = 1
    Ran = random.randrange(1, 11)
    Num = input('Choose a number from 1 to 10 to try to get the computer out: ')
    Num = int(Num)
    while Num != Ran:
      print(Ran)
      if Num > 10:
        print('ERROR. You can only choose the number from 1 to 10.')
        Comp_Runs -= Ran
      Comp_Runs += Ran
      Target = Comp_Runs + 1
      print('Computer has ' + str(Comp_Runs) + ' runs currently')
      Ran = random.randrange(1, 11)
      Num = input('Choose a number from 1 to 10 to try to get the computer out: ')
      Num = int(Num)
    print(Ran)
    print('Computer got out with ' + str(Comp_Runs) + ' runs.' + '\n' + 'Your target is ' + str(Target) + ' runs.')
    # Same will continue for the other person
    Runs = 0
    Ran = random.randrange(1, 11)
    Num = input('Choose a number from 1 to 10: ')
    Num = int(Num)
    while Num != Ran:
      print(Ran)
      if Num > 10:
        print('ERROR. You can only choose the number from 1 to 10.')
        Runs -= Num
      Runs += Num
      print('You have ' + str(Runs) + ' runs currently.')
      Ran = random.randrange(1, 11)
      Num = input('Choose a number from 1 to 10: ')
      Num = int(Num)
    print(Ran)
    print('You are out with ' + str(Runs) + ' runs.' + '\n' + 'Now we have to compare scores.')
    # Runs will compare, one with higher runs wins
    sleep(3)
    if Runs > Comp_Runs:
      print('CONGRATULATIONS! You have won!')
    elif Comp_Runs > Runs:
      print('Computer has won')
    else:
      print('It is a tie')
  elif BatOrBowl.lower() == 'batting' or Comp_BatOrBowl == 'Bowling':
    Runs = 0
    Target = 1
    Ran = random.randrange(1, 11)
    Num = input('Choose a number from 1 to 10: ')
    Num = int(Num)
    while Num != Ran:
      print(Ran)
      if Num > 10:
        print('ERROR. You can only choose the number from 1 to 10.')
        Runs -= Num
      Runs += Num
      Target = Runs + 1
      print('You have ' + str(Runs) + ' runs currently')
      Ran = random.randrange(1, 11)
      Num = input('Choose a number from 1 to 10: ')
      Num = int(Num)
    print(Ran)
    print('You are out with ' + str(Runs) + ' runs.' + '\n' + 'The computer\'s target is ' + str(Target) + ' runs.')
    Comp_Runs = 0
    Ran = random.randrange(1, 11)
    Num = input('Choose a number from 1 to 10 to try to get the computer out: ')
    Num = int(Num)
    while Num != Ran:
      print(Ran)
      if Num > 10:
        print('ERROR. You can only choose the number from 1 to 10.')
        Comp_Runs -= Ran
      Comp_Runs += Ran
      print('Computer has ' + str(Comp_Runs) + ' runs currently.')
      Ran = random.randrange(1, 11)
      Num = input('Choose a number from 1 to 10 to try to get the computer out: ')
      Num = int(Num)
    print(Ran)
    print('Computer is out with ' + str(Comp_Runs) + ' runs.' + '\n' + 'Now we have to compare scores.')
    sleep(3)
    if Runs > Comp_Runs:
      print('CONGRATULATIONS! You have won!')
    elif Comp_Runs > Runs:
      print('Computer has won')
    else:
      print('It is a tie')
elif GmMod.lower() == 'multiplication':
  # MULTIPLICATION
  # Make player choose odd or even
  OddEven = input('Choose odd or even: ')
  Ran = random.randrange(1, 11)
  Num = input('Choose a number from 1 to 10: ')
  Num = int(Num)
  print(Ran)
  Comp_BatOrBowl = ''
  BatOrBowl = ''
  if ((Ran + Num) % 2) == 0 and OddEven.lower() == 'even':
    BatOrBowl = input('Choose batting or bowling: ')
  elif ((Ran + Num) % 2) > 0 and OddEven.lower() == 'odd':
    BatOrBowl = input('Choose batting or bowling: ')
  elif ((Ran + Num) % 2) == 0 and OddEven.lower() != 'even':
    Ran_For_BatBall = random.randrange(1, 3)
    if Ran_For_BatBall == 1:
      Comp_BatOrBowl = 'Batting'
      print('Computer has chosen ' + Comp_BatOrBowl + '.')
    elif Ran_For_BatBall == 2:
      Comp_BatOrBowl = 'Bowling'
      print('Computer has chosen ' + Comp_BatOrBowl + '.')
  elif ((Ran + Num) % 2) > 0 and OddEven.lower() != 'odd':
    Ran_For_BatBall = random.randrange(1, 3)
    if Ran_For_BatBall == 1:
      Comp_BatOrBowl = 'Batting'
      print('Computer has chosen ' + Comp_BatOrBowl + '.')
    elif Ran_For_BatBall == 2:
      Comp_BatOrBowl = 'Bowling'
      print('Computer has chosen ' + Comp_BatOrBowl + '.')
  # Similar to the original game mode, but if the bowler's and batsman's number is same, then the batsman will get the number of runs equal to the square of that number
  # Batsman can get out on 1 less and 1 more than his/her number

  if Comp_BatOrBowl == 'Batting' or BatOrBowl.lower() == 'bowling':
    Comp_Runs = 0
    Target = 1
    Ran = random.randrange(1, 11)
    Num = input('Choose a number from 1 to 10 to try to get the computer out: ')
    Num = int(Num)
    while Num != Ran + 1 and Num != Ran - 1:
      if Num > 10:
        print('ERROR. You can only choose the number from 1 to 10.')
        Comp_Runs -= Ran

      if Num == Ran:
        print(Ran)
        Comp_Runs += Ran ** 2
      else:
        print(Ran)
        Comp_Runs += Ran
        Target = Comp_Runs + 1
        print('Computer has ' + str(Comp_Runs) + ' runs currently')
        Ran = random.randrange(1, 11)
        Num = input('Choose a number from 1 to 10 to try to get the computer out: ')
        Num = int(Num)
    print(Ran)
    print('Computer got out with ' + str(Comp_Runs) + ' runs.' + '\n' + 'Your target is ' + str(Target) + ' runs.')
    # Same will continue for the other person
    Runs = 0
    Ran = random.randrange(1, 11)
    Num = input('Choose a number from 1 to 10: ')
    Num = int(Num)
    while Ran != Num + 1 and Ran != Num - 1:
      if Num > 10:
        print('ERROR. You can only choose the number from 1 to 10.')
        Runs -= Num
      if Num == Ran:
        print(Ran)
        Runs += Num ** 2
      else:
        print(Ran)
        Runs += Num
        print('You have ' + str(Runs) + ' runs currently.')
        Ran = random.randrange(1, 11)
        Num = input('Choose a number from 1 to 10: ')
        Num = int(Num)
    print(Ran)
    print('You are out with ' + str(Runs) + ' runs.' + '\n' + 'Now we have to compare scores.')
    # Runs will compare, one with higher runs wins
    sleep(3)
    if Runs > Comp_Runs:
      print('CONGRATULATIONS! You have won!')
    elif Comp_Runs > Runs:
      print('Computer has won')
    else:
      print('It is a tie')
  elif BatOrBowl.lower() == 'batting' or Comp_BatOrBowl == 'Bowling':
    Runs = 0
    Target = 1
    Ran = random.randrange(1, 11)
    Num = input('Choose a number from 1 to 10: ')
    Num = int(Num)
    while Ran != Num + 1 and Ran != Num - 1:
      if Num > 10:
        print('ERROR. You can only choose the number from 1 to 10.')
        Runs -= Num
      if Num == Ran:
        print(Ran)
        Runs += Num ** 2
      else:
        print(Ran)
        Runs += Num
        Target = Runs + 1
        print('You have ' + str(Runs) + ' runs currently')
        Ran = random.randrange(1, 11)
        Num = input('Choose a number from 1 to 10: ')
        Num = int(Num)
    print(Ran)
    print('You are out with ' + str(Runs) + ' runs.' + '\n' + 'The computer\'s target is ' + str(Target) + ' runs.')
    Comp_Runs = 0
    Ran = random.randrange(1, 11)
    Num = input('Choose a number from 1 to 10 to try to get the computer out: ')
    Num = int(Num)
    while Num != Ran + 1 and Num != Ran - 1:
      if Num > 10:
        print('ERROR. You can only choose the number from 1 to 10.')
        Comp_Runs -= Ran
      if Num == Ran:
        print(Ran)
        Comp_Runs += Ran ** 2
      else:
        print(Ran)
        Comp_Runs += Ran
        print('Computer has ' + str(Comp_Runs) + ' runs currently.')
        Ran = random.randrange(1, 11)
        Num = input('Choose a number from 1 to 10 to try to get the computer out: ')
        Num = int(Num)
    print(Ran)
    print('Computer is out with ' + str(Comp_Runs) + ' runs.' + '\n' + 'Now we have to compare scores.')
    sleep(3)
    if Runs > Comp_Runs:
      print('CONGRATULATIONS! You have won!')
    elif Comp_Runs > Runs:
      print('Computer has won')
    else:
      print('It is a tie')
elif GmMod.lower() == 'exit':
  exit('\nBYE! See you again!\n')
else:
  print('Wrong input entered, try again.')