list_of_input = input().split()
counter = 0
first_letter_value = []
new_word = []
sequence = []

for word in list_of_input:
    first_letter_value.clear()
    new_word.clear()
    for i in range(len(word)):
        if word[i].isdigit():
            first_letter_value.append(word[i])
        elif word[i].isalpha():
            index = i
            break
        else:
            continue
    tmp = word[index]
    second_letter = word[-1]
    last_letter = tmp
    first_letter = chr(int("".join(first_letter_value)))
    new_word.append(first_letter)
    new_word.append(second_letter)
    for k in range(index + 1, len(word)):
        new_word.append(word[k])
    new_word[-1] = last_letter
    sequence.append("".join(new_word))

print(" ".join(sequence))


