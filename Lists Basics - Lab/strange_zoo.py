tail = input()
body = input()
head = input()

animal = [tail, body, head]
animal[0], animal[2] = animal[-1], animal[-3]
print(animal)