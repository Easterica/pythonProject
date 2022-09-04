zoo = {}
command = input()
areas = {}
while True:
    if command == "EndDay":
        break
    else:
        command = command.split(':')

    curr_command = command[0]
    if curr_command == "Add":
        command_info = command[1].strip().split('-')
        animal_name = command_info[0]
        food_quantity = command_info[1]
        area = command_info[2]
        if area not in areas.keys():
            areas[area] = [1, [animal_name]]
        elif animal_name not in areas[area][1]:
            areas[area][0] += int(1)
            areas[area][1].append(animal_name)

        if animal_name not in zoo.keys():
            zoo[animal_name] = [int(food_quantity), area]
        else:
            zoo[animal_name][0] += int(food_quantity)

    elif curr_command == "Feed":
        command_info = command[1].strip().split('-')
        animal_name = command_info[0]
        food_quantity = command_info[1]

        if animal_name in zoo.keys():
            zoo[animal_name][0] -= int(food_quantity)
            if int(zoo[animal_name][0]) <= 0:
                zoo.pop(animal_name)


                print(f"{animal_name} was successfully fed")

    command = input()

print("Animals:")
for animal, info in zoo.items():
    print(f" {animal} -> {info[0]}g")

print("Areas with hungry animals:")
for area, info in areas.items():
    print(f"{area}: {info[0]}")