print("\n\n\tWELCOME TO THE GAME OF ROCK-PAPAER-SCISORS")
print("\nPlease input: Rock, Paper, or Scissors")
p1 = input ("\n\nPlayer 1: ")
p2 = input ("Player 2: ")


if p1 == "Rock" :
    if p2 == "Paper":
        print("\nPlayer 2 wins!")
    elif p2 == "Scissors":
        print("\nPlayer 1 wins!")
    elif p1 == p2:
        print("\nIt's a tie!") 
    else:
        print("\nThere is an error in the input.")

elif p1 == "Paper" :
    if p2 == "Rock":
        print("\nPlayer 1 wins!")
    elif p2 == "Scissors":
        print("\nPlayer 2 wins!")
    elif p1 == p2:
        print("\nIt's a tie!")
    else:
        print("\nThere is an error in the input.")       

elif p1 == "Scissors" :
    if p2 == "Paper":
        print("\nPlayer 1 wins!")
    elif p2 == "Rock":
        print("\nPlayer 2 wins!")
    elif p1 == p2:
        print("\nIt's a tie!")
    else:
        print("\nThere is an error in the input.")   
   
else:
    print("\nThere is an error in the input.")   