#Rock Paper Scissors   
#Exercise 8 (and Solution)
#Make a two-player Rock-Paper-Scissors game. 
# (Hint: Ask for player plays (using input), 
# compare them, print out a message of congratulations 
# to the winner, and ask if the players want to start a new game)

def user_input():
    print("\nWELCOME TO\n--ROCK--- PAPER-- SCISSORS--\n 1.Rock\n2.Paper\n3.Scissors\n")
    player_1 = int(input("Player 1: Enter input:"))
    player_2 = int(input("Player 2: Enter input:"))

    return player_1, player_2

def rsp(player_1,player_2):
  if player_1 ==player_2:
    print("tie")
  elif player_1 ==1:
    if player_2 ==2:
     print("Paper Covers Rock. Paper wins")
    else:
      print("Rock smashes Scisssors. Rock wins")
  elif player_1 ==2:
    if player_2 ==1:
     print("Paper Covers Rock. Paper wins")
    else:
      print("Scissors cuts Paper. Scissors wins")
  elif player_1 ==3:
    if player_2 ==1:
     print("Rock smashes Scisssors. Rock wins")
    else:
      print("Scissors cuts Paper. Scissors wins")
  else:
    print("Invalid input from user")
  return player_1,player_2
    


while True:  
  player_1_choice,player_2_choice = user_input()
  rsp(player_1_choice,player_2_choice)

  play_again = input("Do you want to play another round?\n Y/N\n").strip().upper()
  if play_again not in ('Y'):
   print("Game over...")
   break

