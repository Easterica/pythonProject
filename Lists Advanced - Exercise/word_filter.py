list_of_words = input().split()

filtered_list = [word for word in list_of_words if len(word) % 2 == 0]
print("\n".join(filtered_list))

