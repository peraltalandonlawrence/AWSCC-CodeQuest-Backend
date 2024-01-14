print("\n\n\tWELCOME TO THE GAME OF ROCK-PAPER-SCISSORS")
print("\nPlease input: rock, paper, or scissors")
p1 = input ("\n\nPlayer 1: ").lower()

import random
pick = ["rock", "paper", "scissors"]
p2 = random.choice(pick).lower()
print("Player 2:",p2)


if p1 == "rock" :
    if p2 == "paper":
        print("\nPlayer 2 wins!")
    elif p2 == "scissors":
        print("\nPlayer 1 wins!")
    elif p1 == p2:
        print("\nIt's a tie!") 
    else:
        print("\nThere is an error in the input.")

elif p1 == "paper" :
    if p2 == "rock":
        print("\nPlayer 1 wins!")
    elif p2 == "scissors":
        print("\nPlayer 2 wins!")
    elif p1 == p2:
        print("\nIt's a tie!")
    else:
        print("\nThere is an error in the input.")       

elif p1 == "scissors" :
    if p2 == "paper":
        print("\nPlayer 1 wins!")
    elif p2 == "rock":
        print("\nPlayer 2 wins!")
    elif p1 == p2:
        print("\nIt's a tie!")
    else:
        print("\nThere is an error in the input.")   
   
else:
    print("\nThere is an error in the input.")   