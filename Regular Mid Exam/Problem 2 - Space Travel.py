list_of_commands = input().split("||")
initial_fuel = int(input())
initial_ammo = int(input())

for command in list_of_commands:
    command = command.split()

    curr_command = command[0]


    if curr_command == "Travel":
        value = int(command[1])
        if value <= initial_fuel:
            initial_fuel -= value
            print(f"The spaceship travelled {value} light-years.")
        else:
            print("Mission failed.")
            exit()
    elif curr_command == "Enemy":
        value = int(command[1])
        if initial_ammo >= value:
            initial_ammo -= value
            print(f"An enemy with {value} armour is defeated.")
        elif initial_ammo < value:
            if initial_fuel >= value * 2:
                initial_fuel -= value * 2
                print(f"An enemy with {value} armour is outmaneuvered.")
            else:
                print("Mission failed.")
                exit()
    elif curr_command == "Repair":
        value = int(command[1])
        initial_fuel += value
        initial_ammo += value * 2
        print(f"Ammunitions added: {value * 2}.")
        print(f"Fuel added: {value}.")
    elif curr_command == "Titan":
        print("You have reached Titan, all passengers are safe.")
        exit()