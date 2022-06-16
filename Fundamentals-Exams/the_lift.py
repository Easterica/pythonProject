people = int(input())
lift_state = list(map(int, input().split()))
has_space = False

for i in range(len(lift_state)):
    if lift_state[i] == 0:
        if people >= 4:
            people -= 4
            lift_state[i] += 4
        else:
            lift_state[i] += people
            people -= people
    else:
        wagon_empty_space = 4 - lift_state[i]
        people -= wagon_empty_space
        lift_state[i] += wagon_empty_space
    if lift_state[i] < 4:
        has_space = True

lift_state = " ".join(list(map(str, lift_state)))
if people != 0:
    print(f"There isn't enough space! {people} people in a queue!")
elif has_space:
    print("The lift has empty spots!")
print(lift_state)