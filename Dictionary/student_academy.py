students = dict()

count = int(input())

for _ in range(0, count):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = [grade]
    else:
        students[name].append(grade)

for name, grade in students.items():
    if sum(grade) / len(grade) >= 4.50:
        print(f"{name} -> {(sum(grade) / len(grade)):.2f}")

