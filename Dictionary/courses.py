courses = dict()

command = input()

while True:

    if command == "end":
        break
    else:
        command = command.split(" : ")

    name = command[0]
    student = command[1]

    if name not in courses:
        courses[name] = []
    courses[name].append(student)

    command = input()

for key, value in courses.items():
    print(f"{key}: {len(value)}")
    for student in value:
        print(f"-- {student}")