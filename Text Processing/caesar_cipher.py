input_line = input()
encrypted_line = []
result = ""

for character in input_line:
    new_char = ord(character) + 3
    encrypted_line.append(new_char)

for num in encrypted_line:
    result += chr(num)

print(result)