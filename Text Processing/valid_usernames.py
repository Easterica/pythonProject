names = input().split(", ")
for name in names:
    is_valid = True
    if not 3 <= len(name) <= 16:
        is_valid = False
        continue
    for character in name:
        if not (character.isalnum() or character == "-" or character == "_"):
            is_valid = False
            break
    if " " in name:
        is_valid = False
    if is_valid:
        print(name)
