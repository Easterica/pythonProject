list_of_strings = input().split()

middle = len(list_of_strings) // 2
left_side = list()
right_side = list()

for i in range(0, middle):
    left_side.append(list_of_strings[i])
for i in range(middle + 1, len(list_of_strings)):
    right_side.append(list_of_strings[i])

racer1_time = 0
racer2_time = 0
left_side = list(map(int, left_side))
right_side = list(map(int, right_side))

for time in left_side:
    racer1_time += time
    if time == 0:
        racer1_time *= 0.8
for index in range(-1, -len(right_side) - 1, -1):
    racer2_time += right_side[index]
    if right_side[index] == 0:
        racer2_time *= 0.8

if racer1_time < racer2_time:
    print(f"The winner is left with total time: {racer1_time:.1f}")
else:
    print(f"The winner is right with total time: {racer2_time:.1f}")
