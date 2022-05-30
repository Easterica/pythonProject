num_of_lines = int(input())
capacity = 255
liters_in_tank = 0
for i in range(num_of_lines):
    liters_of_water = int(input())

    if capacity - liters_of_water < 0:
        print("Insufficient capacity!")
        continue
    capacity -= liters_of_water
    liters_in_tank += liters_of_water
print(liters_in_tank)