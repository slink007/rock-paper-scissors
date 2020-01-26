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
if play1 == "":
    print("If that's how you're going to act then I'm not playing")
    exit()

play2 = input("enter Player 2's choice: ")
if play2 == "":
    print("If that's how you're going to act then I'm not playing")
    exit()

print("SHOOT!")

if play1 == "rock":
    if play2 == "rock":
        print("TIE")
    elif play2 == "paper":
        print("Player 2 wins")
    elif play2 == "scissors":
        print("Player 1 wins")
    else:
        print("It's called 'rock, paper, scissors' not '" + play2 + \
        ", paper, scissors'")
elif play1 == "paper":
    if play2 == "rock":
        print("Player 1 wins")
    elif play2 == "paper":
        print("TIE")
    elif play2 == "scissors":
        print("Player 2 wins")
    else:
        print("It's called 'rock, paper, scissors' not '" + play2 + \
        ", paper, scissors'")
elif play1 == "scissors":
    if play2 == "rock":
        print("Player 2 wins")
    elif play2 == "paper":
        print("Player 1 wins")
    elif play2 == "scissors":
        print("TIE")
    else:
        print("It's called 'rock, paper, scissors' not '" + play2 + \
        ", paper, scissors'")
else:
    print("It's called 'rock, paper, scissors' not  '" + play1 + \
    ", paper, scissors'")
    exit()