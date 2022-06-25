people_waiting = int(input())
current_state_of_lift = list(map(int, input().split()))

for i in range(len(current_state_of_lift)):
    if current_state_of_lift[i] == 0:
        if people_waiting >= 4:
            people_waiting -= 4
            current_state_of_lift[i] = 4
        else:
            current_state_of_lift[i] += people_waiting
            people_waiting -= people_waiting
    elif current_state_of_lift[i] != 0 and people_waiting != 0:
        empty_space = 4 - current_state_of_lift[i]
        people_waiting -= empty_space
        current_state_of_lift[i] += empty_space
    if sum(current_state_of_lift) == len(current_state_of_lift) * 4 and people_waiting > 0:
        print(f"There isn't enough space! {people_waiting} people in a queue!")
        print(" ".join(list(map(str, current_state_of_lift))))


