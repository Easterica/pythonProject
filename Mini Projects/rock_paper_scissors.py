import random

game_counter = 0

print("Welcome to the game \"Rock, Paper, Scissors\"")
print("Please select one of the three options and write it down.")
print("Rock, Paper, Scissors?")

my_choice = input().lower()

computer_options = ["rock", "paper", "scissors"]
computer_choice = computer_options[random.randint(0, 2)]

while my_choice not in computer_options:
    print("Please select one of the following options: Rock, Paper, Scissors")
    my_choice = input().lower()
while my_choice in computer_options:
    if game_counter != 0:
        print("Please select one of the following options: Rock, Paper, Scissors")
        my_choice = input().lower()

    if my_choice == "rock" and computer_choice == "scissors":
        game_counter += 1
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("You won!")
        print("Do you want to play again?")
        answer = input("Yes or No\n").lower()
        if answer == "yes":
            continue
        else:
            break

    elif my_choice == "rock" and computer_choice == "paper":
        game_counter += 1
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("You lost!")
        print("Do you want to play again?")
        answer = input("Yes or No\n").lower()
        if answer == "yes":
            continue
        else:
            break

    elif my_choice == "rock" and computer_choice == "rock":
        game_counter += 1
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("Draw!")
        print("Do you want to play again?")
        answer = input("Yes or No\n").lower()
        if answer == "yes":
            continue
        else:
            break

    elif my_choice == "paper" and computer_choice == "paper":
        game_counter += 1
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("Draw!")
        print("Do you want to play again?")
        answer = input("Yes or No\n").lower()
        if answer == "yes":
            continue
        else:
            break

    elif my_choice == "paper" and computer_choice == "rock":
        game_counter += 1
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("You won!")
        print("Do you want to play again?\n")
        answer = input("Yes or No\n").lower()
        if answer == "yes":
            continue
        else:
            break

    elif my_choice == "paper" and computer_choice == "scissors":
        game_counter += 1
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("You lost!")
        print("Do you want to play again?")
        answer = input("Yes or No\n").lower()
        if answer == "yes":
            continue
        else:
            break

    elif my_choice == "scissors" and computer_choice == "scissors":
        game_counter += 1
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("Draw!")
        print("Do you want to play again?")
        answer = input("Yes or No\n").lower()
        if answer == "yes":
            continue
        else:
            break

    elif my_choice == "scissors" and computer_choice == "paper":
        game_counter += 1
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("You won!")
        print("Do you want to play again?")
        answer = input("Yes or No\n").lower()
        if answer == "yes":
            continue
        else:
            break

    elif my_choice == "scissors" and computer_choice == "rock":
        game_counter += 1
        print(f"Your choice is: {my_choice}")
        print(f"Computer's choice is: {computer_choice}")
        print("You lost!")
        print("Do you want to play again?")
        answer = input("Yes or No\n").lower()
        if answer == "yes":
            continue
        else:
            break
    else:
        print("Please select one of the following options: Rock, Paper, Scissors")
        my_choice = input().lower()



