import random

def game():
    print("Welcome to the Stone, Paper,Scissors Game.")
    print("Enter choice from: Stone/Paper/Scissor:")
    user=input("Enter your choice: ").strip().lower()

    choices=['stone','paper','scissors']
    computer=random.choice(choices)
    print(f"Computer choice: {computer} ")

    if user==computer:
        print("Game tied!")
    elif user == "stone" and computer == "scissors":
        print("You win!")
    elif user == "paper" and computer == "stone":
        print("You win!")
    elif user == "scissors" and computer == "paper":
        print("You win!")
    elif user in choices:
        print("Computer wins!")
    else:
        print("Invalid!.\n Please enter valid choice from: stone, paper, scissors.")
    

game()