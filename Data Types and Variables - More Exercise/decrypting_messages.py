key = int(input())
lines = int(input())
new_string = ""

for i in range(lines):
    symbol = input()
    new_string += chr(ord(symbol) + key)
print(new_string)
