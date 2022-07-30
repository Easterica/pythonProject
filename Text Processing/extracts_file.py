input_line = input().split("\\")

file_name = input_line[-1].split('.')

print(f"File name: {file_name[0]}")
print(f"File extension: {file_name[1]}")
