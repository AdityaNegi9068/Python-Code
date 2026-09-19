import random
# The User will choose between Rock, Paper, or Scissors
choices = ["rock", "paper", "scissors"]
player = input("Choose Rock, Paper, or Scissors: ").lower()
computer = random.choice(choices)

if player not in choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
elif player == computer:
    print(f"It's a tie! Both chose {player}.")
elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
    print(f"You win! {player} beats {computer}.")
else:
    print(f"Computer wins! {computer} beats {player}.")