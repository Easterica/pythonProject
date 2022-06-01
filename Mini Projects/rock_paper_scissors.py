import random

game_counter = 0

computer_options = ["rock", "paper", "scissors"]
computer_choice = computer_options[random.randint(0,2)]

print("Welcome to the game \"Rock, Paper, Scissors\"")
print("Please select one of the three options and write it down.")
print("Rock, Paper, Scissors?")

my_choice = input().lower()

while my_choice not in computer_options:
    print("Please select one of the following options: Rock, Paper, Scissors")
    

    if my_choice == "rock" and computer_choice == "scissors":
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("You won!")
    elif my_choice == "rock" and computer_choice == "paper":
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("You lost!")
    elif my_choice == "rock" and computer_choice == "rock":
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("Draw!")
    elif my_choice == "paper" and computer_choice == "paper":
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("Draw!")
    elif my_choice == "paper" and computer_choice == "rock":
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("You won!")
    elif my_choice == "paper" and computer_choice == "scissors":
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("You lost!")