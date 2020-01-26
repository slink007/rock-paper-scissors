# Assignment from Section 9 of Modern Python 3 Bootcamp
# A a less basic rock, paper, scissors game
# In this version we will only have one player competing against the
# computer.
#
# paper > rock
# scissors > paper
# rock > scissors

import random

print("\n...rock...")
print("...paper...")
print("...scissors...")

player = input("enter your choice: ")
player = player.lower()
cpu = random.randint(0, 2)
# we haven't covered dictionaries yet so doing this with if-else
if cpu == 0:
    cpu_choice = "rock"
elif cpu == 1:
    cpu_choice = "paper"
else:
    cpu_choice = "scissors"

print("CPU chose: " + cpu_choice)
print("SHOOT!")

if player != "rock" and player != "paper" and player !="scissors":
    print("Player gave invalid input")
    exit()
        
if player == cpu_choice:
    print("TIE")
elif player == "rock" and cpu_choice == "scissors":
    print("Player 1 wins")
elif player == "paper" and cpu_choice == "rock":
    print("Player 1 wins")
elif player == "scissors" and cpu_choice == "paper":
    print("Player 1 wins")
else:
    print("CPU wins")
