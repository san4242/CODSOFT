import random

def play_game():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("Computer wins!")
        else:
            print("You win!")
    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("Computer wins!")
        else:
            print("You win!")
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")

def main():
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Well played!")
            break

if __name__ == "__main__":
    main()
