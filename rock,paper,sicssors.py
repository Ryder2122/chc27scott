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
    elif( 
        (user_choice == "rock" and computer_choice == "scissors"):
        (user_choice == "scissors" and computer_choice == "paper")
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win!")
    else:
        print("You lose!")   
    play_again = input("Do you want to play again? (yes please/nah im chilling): ")
    if play_again != "yes please":
            print("Thanks for playing!")