results = dict()
submissions = dict()
command = input()

while True:

    if command == "exam finished":
        break
    else:
        command = command.split("-")

    name = command[0]

    if command[1] != "banned":
        language = command[1]
        score = command[2]
        if name not in results:
            results[name] = score
            if language not in submissions.keys():
                submissions[language] = 1
            else:
                submissions[language] += 1
        else:
            if score > results[name]:
                results[name] = score
            submissions[language] += 1
    else:
        results[name] = 0

    command = input()
print("Results:")
for key, value in results.items():
    if value != 0:
        print(f"{key} | {value}")
print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")
