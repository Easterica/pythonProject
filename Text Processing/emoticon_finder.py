input_line = input().split()
emoji_list = list()

for word in input_line:
    if word.startswith(":"):
        emoji = word[0] + word[1]
        emoji_list.append(emoji)

print("\n".join(emoji_list))