import math

tournament_count = int(input())
points = int(input())
wins_count = 0
all_points = 0
for i in range(tournament_count):

    place = input()

    if place == "W":
        points += 2000
        all_points += 2000
        wins_count += 1
    elif place == "F":
        points += 1200
        all_points += 1200
    elif place == "SF":
        points += 720
        all_points += 720

avg_points = all_points / tournament_count
percent_won = wins_count / tournament_count * 100

print(f"Final points: {points}")
print(f"Average points: {math.floor(avg_points)}")
print(f"{percent_won:.2f}%")