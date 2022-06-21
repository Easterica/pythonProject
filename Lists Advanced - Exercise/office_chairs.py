rooms_count = int(input())
excess_chairs = 0

for i in range(1, rooms_count + 1):
    command = input().split()
    chairs_count = len(command[0])
    people = int(command[1])

    needed_chairs_in_room = 0
    number_of_room = 0

    if chairs_count == people:
        continue
    elif chairs_count > people:
        excess_chairs += chairs_count - people
    else:
        needed_chairs_in_room += people - chairs_count
        print(f"{needed_chairs_in_room} more chairs needed in room {i}")
if excess_chairs != 0 and needed_chairs_in_room == 0:
    print(f"Game On, {excess_chairs} free chairs left")

