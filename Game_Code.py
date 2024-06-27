from getpass import getpass as input
print("\033[31mE P I C    🪨  📄 ✂️    B A T T L E \033[0m")
print()         #heading done

counter = 1
player1_score = 0
player2_score = 0         #parameters done

while True:
  print("\033[35mRound", counter, "\033[0m")   #mention round no.
  #player 1 moves
  move1 = input("Select your move player 1 (R, P or S):")
  if move1 != 'R' and move1 != 'P' and move1 != 'S':
    print("\033[31mInvalid move player 1 😕")
    exit()
  else:
    print()
    #player 2 moves
    move2 = input("Select your move player 2 (R, P or S):")
    if move2 != 'R' and move2 != 'P' and move2 != 'S':
      print("\033[31mInvalid move player 2 😕")
      exit()
    else:
      print()
      
      #game logic
      if move1 == 'R':
        if move2 == 'R':
          print("It's a tie! 😱")
        elif move2 == 'P':
          print("Player 2 wins! 😎")
          player2_score += 1
        elif move2 == 'S':
          print("Player 1 wins! 😎")
          player1_score += 1
  
      elif move1 == 'P':
        if move2 == 'R':
          print("Player 1 wins! 😎")
          player1_score += 1
        elif move2 == 'P':
          print("It's a tie! 😱")
        elif move2 == 'S':
          print("Player 2 wins! 😎")
          player2_score += 1
  
      elif move1 == 'S':
        if move2 == 'R':
          print("Player 2 wins! 😎")
          player2_score += 1
        elif move2 == 'P':
          print("Player 1 wins! 😎")
          player2_score += 1
        elif move2 == 'S':
          print("It's a tie! 😱")
  print()
  
  counter += 1                 #counting rounds (max 3)
  if counter == 4:
    break
  else:
    continue

#declaring winner
if player1_score > player2_score:
  print("\033[32mPlayer 1 wins with", player1_score, "victories!")
elif player2_score > player1_score:
  print("\033[32mPlayer 2 wins with", player2_score, "victories!")
else:
  print("\033[32mThe match is a tie!")
