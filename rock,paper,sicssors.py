# semester project: rock, paper, sicssors 
import random

while True:
    choices = ("rock, paper, sicssors") 
    print("Welcome to Rock-Paper-Scissors with Money!")
    print("Starting balance: ${10000}")
    win_reward = 500
    loss_penalty = 100
   
    player_choice = input("\nChoose rock, paper, or scissors (or 'quit' to stop): ").lower()
            
    if player_choice == "quit":
                
            
        if player_choice not in choices:
            print("Invalid choice. Try again.")
            
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
                
    if player_choice == computer_choice:
                    print("It's a tie! No money gained or lost.")
                
    (player_choice == "rock" and computer_choice == "scissors") 
    (player_choice == "paper" and computer_choice == "rock")
    (player_choice == "scissors" and computer_choice == "paper")
                
    
    print(f"You win! +${win_reward} Balance: ${balance}")
    balance += win_reward

    print(f"You lose! -${loss_penalty} Balance: ${balance}")
    balance -= loss_penalty            
    
    
    
    if balance <= 0:
                    print("You're out of money! Game over.")
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    if user_choice == "quit":
                print(f"Game over! Final balance: ${balance}")
            

    if user_choice not in choices:
                    print("Invalid choice. Please choose rock, paper, or scissors.")

    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}, Computer chose: {computer_choice}\n")

    if user_choice == computer_choice:
                    print("It's a tie!") 
    (user_choice == "scissors" and computer_choice == "paper")
    (user_choice == "paper" and computer_choice == "rock")

    play_again = input("Do you want to play again?(yes please/nahhh):")
    if play_again != "yes please":
                            print("Thanks for playing!") 

                            