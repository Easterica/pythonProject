zoo = {}
areas = {}

while True:
    command = input()

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

                print("%s was successfully fed", animal_name)

print("Animals:")
for animal, info in zoo.items():
    print(" %s -> %dg", animal, info[0])

print("Areas with hungry animals:")

areas = dict()

for animal_info in zoo.values():
    if animal_info[1] in areas.keys():
        areas.values[0] += 1
    else:
        areas[animal_info[1]] = 1

for area, info in areas.items():
    print("%s: %d", area, info)

# Add: Adam-4500-ByTheCreek
# Add: Maya-7600-WaterfallArea
# Add: Maya-1230-WaterfallArea
# Feed: Jamie-2000
# EndDay