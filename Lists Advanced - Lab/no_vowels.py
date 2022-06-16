input_line = input()
vowels = ['a', 'o', 'u', 'e', 'i']

reformed_list = [x for x in input_line if x not in vowels]
print("".join(reformed_list))