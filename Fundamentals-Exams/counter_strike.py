initial_energy = int(input())
battles_won = 0

while True:
    command = input()

    if command == "End of battle":
        break
    else:
        command = int(command)

    if command <= initial_energy:
        battles_won += 1
        initial_energy -= command
    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy")
        exit()

    if battles_won % 3 == 0:
        initial_energy += battles_won

print(f"Won battles: {battles_won}. Energy left: {initial_energy}")