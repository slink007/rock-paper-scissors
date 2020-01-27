# Assignment from Section 9 of Modern Python 3 Bootcamp
# A a less basic rock, paper, scissors game
# In this version we will only have one player competing against the
# computer.
#
# paper > rock
# scissors > paper
# rock > scissors

import random

number_wins = 3
player_wins = 0
cpu_wins = 0

print("\n...rock...")
print("...paper...")
print("...scissors...")

while (player_wins < number_wins) and (cpu_wins < number_wins):
    # get the player choices
    player = input("Enter 'q' or 'quit' to stop.\nOtherwise enter 'rock', "\
    "or 'paper' or 'scissors' to play. ")
    player = player.lower()

    # does player want to quit?
    if player == 'q' or player == 'quit':
        break

    cpu = random.randint(0, 2)
    if cpu == 0:
        cpu_choice = "rock"
    elif cpu == 1:
        cpu_choice = "paper"
    else:
        cpu_choice = "scissors"

    print("\nPlayer chose: " + player)
    print("CPU chose: " + cpu_choice)
    print("SHOOT!")

    if player != "rock" and player != "paper" and player !="scissors":
        print("Player gave invalid input")
    elif player == cpu_choice:
        print(f"You both chose {player}. Tie!")
    elif player == "rock" and cpu_choice == "scissors":
        print(f"{player} beats {cpu_choice}.  Player wins this round")
        player_wins += 1
    elif player == "paper" and cpu_choice == "rock":
        print(f"{player} beats {cpu_choice}.  Player wins this round")
        player_wins += 1
    elif player == "scissors" and cpu_choice == "paper":
        print(f"{player} beats {cpu_choice}.  Player wins this round")
        player_wins += 1
    else:
        print(f"{cpu_choice} beats {player}.  CPU wins this round")
        cpu_wins += 1

    # print the scores
    print(f"\nPlayer = {player_wins}\tCPU = {cpu_wins}\n")

# print results
if player_wins > cpu_wins:
    print("Player wins!")
elif player_wins < cpu_wins:
    print("CPU wins  :(")
else:
    print("Draw")
