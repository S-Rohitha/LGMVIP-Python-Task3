import random

def play_rps():
    # Get user's choice
    user_choice = input("Choose rock, paper, or scissors: ")

    # Generate computer's choice
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif user_choice == "rock" and computer_choice == "scissors":
        result = "You win!"
    elif user_choice == "paper" and computer_choice == "rock":
        result = "You win!"
    elif user_choice == "scissors" and computer_choice == "paper":
        result = "You win!"
    else:
        result = "Computer wins!"

    # Display the result
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    print(result)

    # Ask the user if they want to play again
    play_again = input("Play again? (y/n): ")
    if play_again == "y":
        play_rps()
    else:
        print("Thanks for playing!")

play_rps()