def characters_in_range(char1, char2):
    list_of_chars = list()

    for char in range(ord(char1) + 1, ord(char2)):
        list_of_chars.append(chr(char))

    return " ".join(list_of_chars)


char1 = input()
char2 = input()
print(characters_in_range(char1, char2))

