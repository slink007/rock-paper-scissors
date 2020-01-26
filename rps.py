# Assignment from Section 9 of Modern Python 3 Bootcamp
# A basic rock, paper, scissors game
# How basic is it?  We ignore the fact that when Player 1 enters a choice
#    Player 2 can see that and totally cheat.
#
# paper > rock
# scissors > paper
# rock > scissors

print("\n...rock...")
print("...paper...")
print("...scissors...")

play1 = input("enter Player 1's choice: ")
play2 = input("enter Player 2's choice: ")
print("SHOOT!")

if play1 != "rock" and play1 != "paper" and play1 !="scissors":
    print("Player 1 gave invalid input")
    exit()
if play2 != "rock" and play2 != "paper" and play2 !="scissors":
    print("Player 2 gave invalid input")
    exit()
        
if play1 == play2:
    print("TIE")
elif play1 == "rock" and play2 == "scissors":
    print("Player 1 wins")
elif play1 == "paper" and play2 == "rock":
    print("Player 1 wins")
elif play1 == "scissors" and play2 == "paper":
    print("Player 1 wins")
else:
    print("Player 2 wins")
