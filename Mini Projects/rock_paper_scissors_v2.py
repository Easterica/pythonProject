import random

print("Welcome to the game \"Rock, Paper, Scissors\"")
print("Please select game mode")
print("A)Best of 1 | B)Best of 3 | C)Best of 5.")
answer = input("A, B or C?\n").lower()

max_game_counter = 0
wins_counter = 0
draws_counter = 0
loses_counter = 0
game_counter = 0


computer_options = ["rock", "paper", "scissors"]
computer_choice = computer_options[random.randint(0, 2)]

if answer == "a":
    max_game_counter = 1
elif answer == "b":
    max_game_counter = 3
elif answer == "c":
    max_game_counter = 5

for games in range(max_game_counter):
    player_choice = input("Pick your fighter: Rock | Paper | Scissors\n").lower()

    while player_choice not in computer_options:
        print("Please select one of the following options: Rock, Paper, Scissors")
        player_choice = input().lower()

    is_draw = False
    is_won = False
    is_lost = False
    if player_choice == computer_choice:
        game_counter += 1
        draws_counter += 1
        is_draw = True
    else:
        if player_choice == "rock" and computer_choice == "scissors":
            game_counter += 1
            wins_counter += 1
            is_won = True
        elif player_choice == "scissors" and computer_choice == "paper":
            game_counter += 1
            wins_counter += 1
            is_won = True
        elif player_choice == "paper" and computer_choice == "rock":
            game_counter += 1
            wins_counter += 1
            is_won = True

        else:
            game_counter += 1
            loses_counter += 1
            is_lost = True

    print(f"Your choice is: {player_choice}.")
    print(f"Computer's choice is: {computer_choice}.")

    if is_won:
        print("Congratulations! You won!")
    elif is_lost:
        print("Sorry, you lost!")
    else:
        print("The result is draw!")
print(f"Your score: Wins: {wins_counter}. Losses: {loses_counter}. Draws: {draws_counter}.")











