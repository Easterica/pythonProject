lines_count = int(input())
plant_dict = {}

for _ in range(lines_count):
    plant = input().split('<->')
    name = plant[0]
    rarity = plant[1]
    plant_dict[name] = [rarity, []]

command = input()

while True:

    if command == "Exhibition":
        break
    else:
        command = command.split(':')

    if command[0] == "Rate":
        info = command[1].strip().split(' - ')
        name = info[0]
        rating = info[1]
        plant_dict[name][1].append(rating)
    elif command[0] == "Update":
        info = command[1].strip().split(' - ')
        name = info[0]
        rarity = info[1]
        plant_dict[name][0] = rarity
    elif command[0] == "Reset":
        info = command[1].strip().split(' - ')
        name = info[0]
        plant_dict[name][1] = []
    command = input()

print("Plants for the exhibition:")
for key, value in plant_dict.items():
    avg_rating = 0.00
    if len(value[1]) != 0:
        avg_rating = sum(list(map(int, value[1]))) / len(value[1])
    print(f"- {key}; Rarity: {value[0]}; Rating: {avg_rating:.2f}")
