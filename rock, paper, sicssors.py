# semester project: rock, paper, sicssors 
import random

actions = ["rock","paper", "sicssors"]

user_choice = input( "enter your chocie (rock, paper, sicssors)")
if user_choice not in actions:
    print("invalid choice.please try agian") 

computer_choice = random.choice(actions) 
print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

if user_choice == computer_choice : 
    print(" It's a tie ")
elif user_choice == "rock":
    if computer_choice == "scissors":
        print("Rock smashes scissors! You win!")
elif:
    print("Paper covers rock! You lose.")
else: user_choice == "paper":
if computer_choice == "rock":
    print("Paper covers rock! You win!")
elif:
print("Scissors cuts paper! You lose.")
else: user_choice == "scissors":
if computer_choice == "paper":
print("Scissors cuts paper! You win!")
elif:
print("Rock smashes scissors! You lose.")
else:
print("Invalid input. Please choose rock, paper, or scissors.")