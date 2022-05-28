num_of_chars = int(input())
result = 0

for i in range(num_of_chars):
    char = input()
    result += ord(char)

print(f"The sum equals: {result}")
