input_line = input().split()
sum_of_chars = 0

string1 = input_line[0]
string2 = input_line[1]

if len(string1) > len(string2):
    count = len(string2)
    for i in range(0, count):
        sum_of_chars += (ord(string1[i]) * ord(string2[i]))
    for k in range(count, len(string1)):
        sum_of_chars += ord(string1[k])
elif len(string2) > len(string1):
    count = len(string1)
    for i in range(0, count):
        sum_of_chars += (ord(string1[i]) * ord(string2[i]))
    for k in range(count, len(string2)):
        sum_of_chars += ord(string2[k])
else:
    for i in range(0, len(string1)):
        sum_of_chars += ord(string1[i]) * ord(string2[i])

print(sum_of_chars)