list1 = input().split(', ')
list2 = input().split(', ')
list3 = list()

for string1 in list1:
    for string2 in list2:
        if string1 in string2:
            if string1 in list3:
                continue
            else:
                list3.append(string1)

print(list3)