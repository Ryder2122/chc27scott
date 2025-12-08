# semester project: rock, paper, sicssors 
import random
choices = ["rock", "paper", "scissors"]

while True:

    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()


    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")



    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}, Computer chose: {computer_choice}\n")


    if user_choice == computer_choice:
        print("It's a tie!") 
    elif (user_choice == "rock" and computer_choice == "scissors"):
     (user_choice == "scissors" and computer_choice == "paper")
    (user_choice == "paper" and computer_choice == "rock")
    print("You win!")
print("You lose!")   

play_again = input("Do you want to play again? (yes please/nah im chilling): ")
if play_again != "yes please":
                print("Thanks for playing!")


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
        
print("Paper covers rock! You lose.")   
user_choice == "paper"
if computer_choice == "rock":
                print("Paper covers rock! You lose!")
        
print("Scissors cuts paper! You lose.")
user_choice == "scissors"
if computer_choice == "paper":
            print("Scissors cuts paper! You win!")