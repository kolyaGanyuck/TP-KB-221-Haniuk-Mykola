import random

def rock_paper_scissors_game():
    options = ["rock", "paper", "scissors"]
    
    player_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(options)
    
    print(f"You chose {player_choice}")
    print(f"The computer chose {computer_choice}")
    
    if player_choice not in options:
        print("Invalid choice. Please try again.")
    elif player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper") or (player_choice == "paper" and computer_choice == "rock"):
        print("You win!")
    else:
        print("The computer wins!")

rock_paper_scissors_game()