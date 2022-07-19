schedule = input().split(', ')

while True:
    command = input()

    if command == "course start":
        break
    else:
        command = command.split(":")

    curr_command = command[0]
    lesson_title = command[1]

    if curr_command == "Add":
        if lesson_title not in schedule:
            schedule.append(lesson_title)
    elif curr_command == "Insert":
        index = int(command[2])
        if lesson_title not in schedule:
            schedule.insert(index, lesson_title)
    elif curr_command == "Remove":
        if lesson_title in schedule:
            schedule.remove(lesson_title)
    elif curr_command == "Swap":
        lesson_title2 = command[2]
        if lesson_title in schedule and lesson_title2 in schedule:
            index_of_lesson1 = schedule.index(lesson_title)
            index_of_lesson2 = schedule.index(lesson_title2)

            tmp = lesson_title
            schedule[index_of_lesson1] = lesson_title2
            schedule[index_of_lesson2] = tmp
            if f"{lesson_title2}-Exercise" in schedule:
                tmp = schedule[index_of_lesson1 + 1]
                schedule[index_of_lesson1 + 1] = schedule[index_of_lesson2 + 1]
                schedule[index_of_lesson2 + 1] = tmp
    elif curr_command == "Exercise":
        if lesson_title in schedule and f"{lesson_title}-Exercise" not in schedule:

            lesson_index = schedule.index(lesson_title)
            schedule.insert(lesson_index+1, f"{lesson_title}-Exercise")
        else:
            schedule.append(lesson_title)
            schedule.append(f"{lesson_title}-Exercise")

schedule = list(enumerate(schedule, 1))

for i in range(len(schedule)):
    (index, lesson) = schedule[i]
    print(f"{index}.{lesson}")
